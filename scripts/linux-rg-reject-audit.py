#!/usr/bin/env python3
"""For every rejected hunk, report whether its added lines landed in the final tree."""
import sys, pathlib
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
