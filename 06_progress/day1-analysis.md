# Day 1 Pre-Session Analysis — 2026-06-22

> **⚠️ ASSUMPTION** — All mastery estimates, score predictions, and weakness rankings below
> derive from the Day 0 diagnostic baseline (2026-06-22: 1/100, L02=25%, all other topics 0%).
> This is a **predictive document** written before Day 1 occurs.
> After Day 1 (2026-06-23), fill in section 6 ("Actual Day 1 Results") with real session data.

---

## 1. Baseline State (Day 0 — 2026-06-22)

| Field | Value | Source |
|---|---|---|
| Diagnostic score | 1 / 100 | score-tracking.md |
| L01 変数・型 mastery | 0% | score-tracking.md |
| L02 演算子・式 mastery | 25% (operator tracing pre-known) | score-tracking.md |
| L03–L07 mastery | 0% each | score-tracking.md |

---

## 2. 予測習熟度（Day 1 終了後）

**Day 1 scope (coach.py — authoritative):** L01 変数・型・printf/scanf + L02 演算子・式
Drill target: L1 Q1–5 + L2 Q1–3

| トピック | ベースライン | Day 1 終了後 予測 | 根拠 |
|---|---|---|---|
| L01 変数・型 | 0% | 40–60% | 初回教科書 + Easy ドリル5問（0%からの初期学習効果） |
| L02 演算子・式 | 25% | 50–65% | 演算子トレース既知（+25% ヘッドスタート）+ Easy 3問 |
| L03–L07 | 0% each | 0% each | Day 1 では学習しない |

*Epistemic label: Assumption — typical first-exposure improvement rate on Easy drills from zero
baseline, adjusted for the pre-existing L02 knowledge.*

---

## 3. 予測試験スコア（Day 1 終了時点）

**Formula (score-prediction.md §1 tier weights — approximated):**

> `predicted ≈ (Tier1_avg × 0.6) + (Tier2_avg × 0.4)`
>
> Tier 1 = L04, L05, L06, L07（高配点 — 合計 80点推定）
> Tier 2 = L01, L02, L03, L08（基礎 / 低配点 — 合計 35点推定）

**Day 1 終了後の推定:**
- Tier 1 平均: 0%（L04–L07 未学習）
- Tier 2 平均: ~13%（L01≈50%, L02≈58%, L03=0%, L08=0% → 4トピック平均≈27%; Day 1で学習するのは2/4なので実効カバレッジ≈13%）

**予測スコア: 0–6 / 100**

> これは正常かつ期待値通りです。スコアへの有意な貢献は **Day 3+** から始まります
> （L04 ネストループ, Priority 9.0 学習開始後）。
> Day 1 の目標はスコア向上ではなく L01/L02 の基盤構築です。

*Epistemic label: Assumption — formula uses approximate tier weights; actual exam scoring is non-public.*

---

## 4. 上位3弱点予測（Day 1 後）

exam-priority-ranking.md の Priority スコアと 0% ベースラインから算出。

| 順位 | トピック | Priority | ベースライン | リスク要因 |
|---|---|---|---|---|
| 1 | **L04 ネストループ・トレース** | 9.0 | 0% | 4日間（Days 3–6）割り当て; 最初の高インパクトトピック |
| 2 | **L06 再帰関数トレース (fib/fact)** | 11.0 | 0% | 最高 Priority; 高度概念; Days 10–11 の2日のみ |
| 3 | **L05 バブルソート穴埋め** | 9.0 | 0% | Days 7–9; L04 が前提条件 |

*Epistemic label: Assumption — all three are at 0% baseline with no prior exposure.*

---

## 5. Day 2 分岐条件

Day 1 終了後に `make coach` を実行すると正確なアドバイスが表示される。
以下は事前に計算した分岐テーブル:

| 条件 | Day 2 の行動 |
|---|---|
| L01 ≥60% AND L02 ≥60% | 予定通り Day 2 へ進む: L03 条件分岐（L3 Q1–5） |
| L01 <60%（Weak） | Day 2 午前に L01 補強30分 → その後 L03 へ |
| L02 <60%（Weak） | L2 演算子ドリルを20分追加 → L03 へ |
| 自信度 ≤2 (Day 1 終了後) | フラストレーション検出フラグ — `coach.py` が Easy のみ処方 |

*コーチ検出ロジック: 同一トピックで2セッション連続 confidence ≤2 → フラストレーション検出
(scripts/coach.py:197–208)*

---

## 6. Actual Day 1 Results [FILL AFTER SESSION]

```
## Actual Day 1 Results — 2026-06-23

- Date: 2026-06-23
- Topics studied: [L01 / L02 / both]
- Duration: [N] min (predicted: 75 min)
- L1 drill score: [N]/5  (Q1–Q5)
- L2 drill score: [N]/3  (Q1–Q3)
- Overall drill performance: [N]/8 → [%]
- Confidence: [1–5]
- Weak problems: [list problem numbers, or "none"]
- L01 mastery estimate: [Weak / Developing / Strong]
- L02 mastery estimate: [Weak / Developing / Strong]
- Patterns detected: [none / frustration / stagnation / overload]
- Notes:
```

---

## 7. スコア予測更新スケジュール

| Day | イベント | 更新対象 |
|---|---|---|
| 1 | 初回ドリルスコア | セクション 6 を記入 |
| 6 | L04 習熟確認 | Tier 1 推定値を修正 |
| 9 | L05 習熟確認 | Tier 1 推定値を修正 |
| 11 | L06 習熟確認 | Mock 前の最終予測 |
| 12 | Mock A 実スコア | 全予測を実績値に置換 |
