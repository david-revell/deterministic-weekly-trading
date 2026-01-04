# Document Codifiability Assessment

This document records which specification files in this repository are suitable
for deterministic codification, and which are intended to remain as guidance only.

Classification meanings:
- A = Fully codifiable (deterministic, explicit rules or formulas)
- B = Partially codifiable (some deterministic core, but judgement or external data required)
- C = Spec-only (conceptual, exploratory, or explicitly non-final)

## Classification

- etf_buy_avg_realised_profit_v1.md – A – explicit spreadsheet-style formulas
- etf_dividend_strategy_v1.md – B – deterministic thresholds, but depends on external dividend data
- etf_exit_strategy_v1.md – C – conceptual ladder logic without parameterised rules
- etf_getout_highvol_v2.md – C – exploratory, open design space
- etf_health_1_to_5_v1.md – A – complete 16-state matrix and decision tree
- etf_lean_ladder_move_v1.md – C – rationale and example, not an algorithm
- etf_limit_buy_orders_v1.md – B – heuristics and ranges, not fixed formulas
- etf_limit_sell_orders_v1.md – B – monotonic structure without concrete allocation rules
- etf_order_levels_v1.md – B – ranked priorities without numeric selection rules
- etf_performance_comparison_v3.md – A – explicit formulas and baseline definitions
- etf_performance_metrics_v1.md – A – fully formula-driven metrics
- etf_rotation_exit_rules_v1.md – C – marked draft, not agreed
- etf_rotation_v1.md – C – manual workflow, human judgement
- etf_tracker_v1.md – C – manual tracking, no computation
- etf_weekly_pack_v2.md – B – clear intent, underspecified mechanics
- mwrr_cheatsheet_v2.md – A – fully defined NPV / root-solve algorithm

This file is descriptive only.  
Reclassification may occur if specs are refined or formalised.
