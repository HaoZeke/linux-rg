#!/usr/bin/env python3
"""Finish leftover 7.1.8 rebase hunks in an already-applied linux-rg tree."""
from __future__ import annotations

import sys
from pathlib import Path


def replace_once(path: Path, old: str, new: str, label: str) -> None:
    text = path.read_text()
    if new in text and old not in text:
        print(f"ok already: {label}")
        return
    if old not in text:
        raise SystemExit(f"missing anchor: {label} in {path}")
    path.write_text(text.replace(old, new, 1))
    print(f"fixed: {label}")


def main() -> None:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".")

    replace_once(
        root / "kernel/fork.c",
        """#ifdef CONFIG_SCHED_BORE
			list_add_tail_rcu(&p->sibling, &p->real_parent->children);
#else /* !CONFIG_SCHED_BORE */
#ifdef CONFIG_SCHED_BORE
			list_add_tail_rcu(&p->sibling, &p->real_parent->children);
#else /* !CONFIG_SCHED_BORE */
			list_add_tail(&p->sibling, &p->real_parent->children);
#endif /* CONFIG_SCHED_BORE */
#endif /* CONFIG_SCHED_BORE */
""",
        """#ifdef CONFIG_SCHED_BORE
			list_add_tail_rcu(&p->sibling, &p->real_parent->children);
#else /* !CONFIG_SCHED_BORE */
			list_add_tail(&p->sibling, &p->real_parent->children);
#endif /* CONFIG_SCHED_BORE */
""",
        "fork.c sibling rcu",
    )

    replace_once(
        root / "kernel/sched/ext.c",
        """	ret = sysfs_create_group(&scx_kset->kobj, &scx_global_attr_group);
	if (ret < 0) {
		pr_err("sched_ext: Failed to add global attributes\\n");
		return ret;
	}

	return 0;
}
""",
        """	ret = sysfs_create_group(&scx_kset->kobj, &scx_global_attr_group);
	if (ret < 0) {
		pr_err("sched_ext: Failed to add global attributes\\n");
		return ret;
	}

#ifdef CONFIG_SCHED_ASA
	ret = asa_init(scx_kset);
	if (ret) {
		pr_err("sched_ext: Failed to initialize ASA router (%d)\\n", ret);
		return ret;
	}
#endif

	return 0;
}
""",
        "ext.c asa_init",
    )

    replace_once(
        root / "kernel/sched/fair.c",
        "\tunsigned int group_asym_packing;\t/* Tasks should be moved to preferred CPU */\n"
        "\tunsigned int group_smt_balance;\t\t/* Task on busy SMT be moved */\n"
        "\tunsigned long group_misfit_task_load;\t/* A CPU has a task too big for its capacity */\n",
        "\tunsigned int group_asym_packing;\t/* Tasks should be moved to preferred CPU */\n"
        "\tunsigned int group_smt_balance;\t\t/* Task on busy SMT be moved */\n"
        "\tunsigned int group_llc_balance;\t\t/* Tasks should be moved to preferred LLC */\n"
        "\tunsigned long group_misfit_task_load;\t/* A CPU has a task too big for its capacity */\n",
        "fair.c group_llc_balance field",
    )
    replace_once(
        root / "kernel/sched/fair.c",
        """#ifdef CONFIG_NUMA_BALANCING
	unsigned int nr_numa_running;
	unsigned int nr_preferred_running;
#endif
};
""",
        """#ifdef CONFIG_NUMA_BALANCING
	unsigned int nr_numa_running;
	unsigned int nr_preferred_running;
#endif
#ifdef CONFIG_SCHED_CACHE
	unsigned int nr_pref_dst_llc;
#endif
};
""",
        "fair.c nr_pref_dst_llc",
    )

    replace_once(
        root / "kernel/sched/topology.c",
        "\t\t\tif (IS_ENABLED(CONFIG_NUMA) && sd->parent)\n"
        "\t\t\t\tadjust_numa_imbalance(sd);\n",
        "\t\t\tif (IS_ENABLED(CONFIG_NUMA) && sd->parent) {\n"
        "\t\t\t\tunsigned int nr_llcs =\n"
        "\t\t\t\t\tsd->parent->span_weight / sd->span_weight;\n"
        "\n"
        "\t\t\t\tif (nr_llcs > 1)\n"
        "\t\t\t\t\thas_multi_llcs = true;\n"
        "\t\t\t\tadjust_numa_imbalance(sd);\n"
        "\t\t\t}\n",
        "topology.c has_multi_llcs",
    )

    replace_once(
        root / "mm/vmalloc.c",
        "\tfor (i = 0; i < vm->nr_pages; i++) {\n"
        "\t\tstruct page *page = vm->pages[i];\n"
        "\n"
        "\t\tBUG_ON(!page);\n"
        "\t\t/*\n"
        "\t\t * High-order allocs for huge vmallocs are split, so\n"
        "\t\t * can be freed as an array of order-0 allocations\n"
        "\t\t */\n"
        "\t\tif (!(vm->flags & VM_MAP_PUT_PAGES))\n"
        "\t\t\tmod_lruvec_page_state(page, NR_VMALLOC, -1);\n"
        "\t\t__free_page(page);\n"
        "\t\tcond_resched();\n"
        "\t}\n"
        "\tkvfree(vm->pages);\n"
        "\tkfree(vm);\n",
        "\tif (vm->nr_pages) {\n"
        "\t\tunsigned long i;\n"
        "\n"
        "\t\tfor (i = 0; i < vm->nr_pages; i++) {\n"
        "\t\t\tBUG_ON(!vm->pages[i]);\n"
        "\t\t\tif (!(vm->flags & VM_MAP_PUT_PAGES))\n"
        "\t\t\t\tmod_lruvec_page_state(vm->pages[i], NR_VMALLOC, -1);\n"
        "\t\t}\n"
        "\t\tfree_pages_bulk(vm->pages, vm->nr_pages);\n"
        "\t}\n"
        "\tkvfree(vm->pages);\n"
        "\tkfree(vm);\n",
        "vmalloc.c free_pages_bulk",
    )

    replace_once(
        root / "mm/vmscan.c",
        "static int get_type_to_scan(struct lruvec *lruvec, int swappiness)\n"
        "{\n"
        "\tstruct ctrl_pos sp, pv = {};\n"
        "\n"
        "\tif (swappiness <= MIN_SWAPPINESS + 1)\n"
        "\t\treturn LRU_GEN_FILE;\n",
        "static int get_type_to_scan(struct lruvec *lruvec, struct scan_control *sc,\n"
        "\t\t\t    int swappiness)\n"
        "{\n"
        "\tstruct ctrl_pos sp, pv = {};\n"
        "\n"
        "\tif (swappiness == MIN_SWAPPINESS)\n"
        "\t\treturn LRU_GEN_FILE;\n"
        "\n"
        "\tif (sc->clean_below_min || sc->clean_below_low)\n"
        "\t\treturn LRU_GEN_ANON;\n"
        "\n"
        "\tif (sc->anon_below_min)\n"
        "\t\treturn LRU_GEN_FILE;\n"
        "\n"
        "\tif (swappiness == MIN_SWAPPINESS + 1)\n"
        "\t\treturn LRU_GEN_FILE;\n",
        "vmscan get_type_to_scan",
    )

    replace_once(
        root / "mm/vmscan.c",
        "\tstruct lru_gen_mm_walk *walk;\n"
        "\tbool skip_retry = false;\n"
        "\tstruct lru_gen_folio *lrugen = &lruvec->lrugen;\n"
        "\tstruct mem_cgroup *memcg = lruvec_memcg(lruvec);\n"
        "\tstruct pglist_data *pgdat = lruvec_pgdat(lruvec);\n"
        "\n"
        "\tlruvec_lock_irq(lruvec);\n"
        "\n"
        "\tscanned = isolate_folios(nr_to_scan, lruvec, sc, swappiness, &type, &list);\n",
        "\tstruct lru_gen_mm_walk *walk;\n"
        "\tint scanned, reclaimed;\n"
        "\tint isolated = 0, type, type_scanned = 0;\n"
        "\tbool skip_retry = false;\n"
        "\tstruct lru_gen_folio *lrugen = &lruvec->lrugen;\n"
        "\tstruct mem_cgroup *memcg = lruvec_memcg(lruvec);\n"
        "\tstruct pglist_data *pgdat = lruvec_pgdat(lruvec);\n"
        "\n"
        "\tlruvec_lock_irq(lruvec);\n"
        "\n"
        "\tscanned = isolate_folios(nr_to_scan, lruvec, sc, swappiness,\n"
        "\t\t\t\t &list, &isolated, &type, &type_scanned);\n",
        "vmscan isolate_folios call",
    )

    replace_once(
        root / "kernel/sched/fair.c",
        "\tif (!p->se.sched_delayed)\n"
        "\t\tutil_est_dequeue(&rq->cfs, p);\n"
        "\n"
        "\tif (dequeue_entities(rq, &p->se, flags) < 0)\n"
        "\t\treturn false;\n",
        "\tif (!p->se.sched_delayed)\n"
        "\t\tutil_est_dequeue(&rq->cfs, p);\n"
        "\n"
        "#ifdef CONFIG_SCHED_BORE\n"
        "\tif ((flags & DEQUEUE_SLEEP) && entity_is_task(&p->se)) {\n"
        "\t\tstruct cfs_rq *cfs_rq = cfs_rq_of(&p->se);\n"
        "\n"
        "\t\tif (cfs_rq->curr == &p->se)\n"
        "\t\t\tupdate_curr(cfs_rq);\n"
        "\t\trestart_burst_bore(p);\n"
        "\t}\n"
        "#endif /* CONFIG_SCHED_BORE */\n"
        "\n"
        "\tif (dequeue_entities(rq, &p->se, flags) < 0)\n"
        "\t\treturn false;\n",
        "fair.c restart_burst_bore",
    )
    replace_once(
        root / "kernel/sched/fair.c",
        "\t\tplace_entity(cfs_rq, se, 0);\n"
        "\t\tif (se != cfs_rq->curr)\n"
        "\t\t\t__enqueue_entity(cfs_rq, se);\n"
        "\t\tcfs_rq->nr_queued++;\n"
        "\t}\n"
        "\n"
        "\tupdate_load_avg(cfs_rq, se, 0);\n"
        "\tclear_delayed(se);\n",
        "\t\tplace_entity(cfs_rq, se, flags);\n"
        "\t\tif (se != cfs_rq->curr)\n"
        "\t\t\t__enqueue_entity(cfs_rq, se);\n"
        "\t\tcfs_rq->nr_queued++;\n"
        "\t}\n"
        "\n"
        "\tupdate_load_avg(cfs_rq, se, 0);\n"
        "\tclear_delayed(se);\n",
        "fair.c requeue place_entity flags",
    )

    replace_once(
        root / "net/ipv4/tcp_bbr.c",
        "\t.min_tso_segs\t= bbr_min_tso_segs,\n",
        "\t.tso_segs\t= bbr_tso_segs,\n",
        "tcp_bbr.c tso_segs op",
    )
    replace_once(
        root / "net/ipv4/tcp_bbr.c",
        "BTF_ID_FLAGS(func, bbr_min_tso_segs)\n",
        "BTF_ID_FLAGS(func, bbr_tso_segs)\n",
        "tcp_bbr.c tso_segs btf",
    )

    removed = 0
    for rej in root.rglob("*.rej"):
        rej.unlink()
        removed += 1
    origs = 0
    for orig in root.rglob("*.orig"):
        orig.unlink()
        origs += 1
    print(f"removed {removed} .rej files, {origs} .orig files")


if __name__ == "__main__":
    main()
