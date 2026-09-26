#!/usr/bin/env python3
"""Reject audit helpers.

  linux-rg-reject-audit.py REJDIR TREE     rejected hunks whose added lines never landed
  linux-rg-reject-audit.py --unique PATCH TREE
      hunks whose before-text (context plus removed lines) does not occur
      exactly once in TREE; a hunk that matches twice can apply, with an
      offset, inside the wrong function.
"""
import re, sys, pathlib


def unique(patch, tree):
    text = pathlib.Path(patch).read_text(errors="replace")
    text = re.split(r"(?m)^-- $", text)[0]
    for blk in re.split(r"(?m)^(?=diff --git |--- a/|--- /dev/null)", text):
        new = re.search(r"(?m)^\+\+\+ b/(\S+)", blk)
        old = re.search(r"(?m)^--- (\S+)", blk)
        if not new or not old or old.group(1) == "/dev/null":
            continue
        path = pathlib.Path(tree) / new.group(1)
        if not path.exists():
            continue
        body = path.read_text(errors="replace")
        for h in re.split(r"(?m)^(?=@@ )", blk)[1:]:
            lines = h.splitlines()
            before = [l[1:] for l in lines[1:] if l[:1] in (" ", "-")]
            if not before:
                continue
            n = body.count("\n".join(before))
            if n != 1:
                name = pathlib.Path(patch).name
                print(f"{'AMBIG' if n else 'NOMATCH'}    x{n} {name} {new.group(1)} {lines[0][:60]}")


if len(sys.argv) == 4 and sys.argv[1] == "--unique":
    unique(sys.argv[2], sys.argv[3])
    raise SystemExit(0)
rejroot, tree = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
for rej in sorted(rejroot.rglob("*.rej")):
    patch = rej.relative_to(rejroot).parts[0]
    target = tree / pathlib.Path(*rej.relative_to(rejroot).parts[1:]).with_suffix("")
    final = target.read_text(errors="replace") if target.exists() else ""
    hunks, cur = [], None
    for line in rej.read_text(errors="replace").splitlines():
        if line.startswith("@@"):
            cur = []; hunks.append((line, cur))
        elif cur is not None and line.startswith("+") and not line.startswith("+++"):
            cur.append(line[1:])
    for hdr, added in hunks:
        sig = [a for a in added if len(a.strip()) > 8]
        if not sig:
            continue
        miss = [a for a in sig if a not in final]
        status = "LANDED" if not miss else ("PARTIAL" if len(miss) < len(sig) else "MISSING")
        print(f"{status:8s} {patch} {target.relative_to(tree)} {hdr[:40]} added={len(sig)} missing={len(miss)}")
        if status != "LANDED":
            for m in miss[:4]:
                print("           -", m.strip()[:100])
