# 過去問 → 必要知識 対応表

---

## 使い方

「自分が解けなかった過去問」を探して、必要な教科書レベル → ドリルへ移動して補強。

---

## C言語 過去問対応表（R6〜R8）

| 年度 | 問 | トピッククラスタ | 必要レベル | ドリルファイル | 模擬試験 |
|---|---|---|---|---|---|
| R8 | 問1 | ループ + 出力トレース | L4 | `03_drills/L4_loops.md` H1 | mock-exam-A 大問I |
| R8 | 問2 | 配列 + バブルソート | L5 | `03_drills/L5_arrays.md` H1 | mock-exam-A 大問II |
| R8 | 問3 | 再帰関数トレース | L6 | `03_drills/L6_functions.md` H1 | mock-exam-B 大問I |
| R7 | 問1 | 制御構造 + 出力 | L3/L4 | `03_drills/L3_conditions.md` H1 | mock-exam-C 大問I |
| R7 | 問2 | 関数 + 引数渡し | L6 | `03_drills/L6_functions.md` M9 | mock-exam-B 大問III |
| R7 | 問3 | 行列式（3×3） fill-blank | L5 | `03_drills/L5_arrays.md` H7 | mock-exam-C 大問II |
| R6 | 問1 | 文字列操作 + ポインタ | L7 | `03_drills/L7_pointers.md` H2 | mock-exam-B 大問II |
| R6 | 問2 | 配列ソート + 探索 | L5/L8 | `03_drills/L8_exam.md` H4 | mock-exam-A 大問II |
| R6 | 問3 | 再帰（フィボナッチ） | L6 | `03_drills/L6_functions.md` M6 | mock-exam-B 大問I |

---

## トピック別ドリル索引

| トピック | Tier | 最初のドリル | 対応レベル |
|---|---|---|---|
| 変数・型・printf | 1★ | L1 E1 | L1 |
| 整数除算の罠 | 1★ | L1 E8 | L1 |
| 演算子優先順位 | 1 | L2 M1 | L2 |
| if/else トレース | 1★ | L3 E1 | L3 |
| switch fall-through | 1 | L3 E8 | L3 |
| for ループトレース | 1★ | L4 E1 | L4 |
| ネストループ | 1★ | L4 M4 | L4 |
| バブルソート | 1★ | L4 H6, L5 H1 | L4/L5 |
| 配列アクセス | 1★ | L5 E1 | L5 |
| 文字列 strlen/strcpy | 1 | L5 M4 | L5 |
| 関数定義・呼び出し | 1★ | L6 E1 | L6 |
| 再帰（階乗） | 1 | L6 M4 | L6 |
| 再帰（フィボナッチ） | 1 | L6 M6 | L6 |
| GCD ユークリッド | 1 | L6 M8 | L6 |
| ポインタ基礎 | 1 | L7 E1 | L7 |
| ポインタ演算 | 1 | L7 E6 | L7 |
| swap 関数（ポインタ） | 1 | L7 M4 | L7 |
| 文字列逆順 | 1 | L7 H4 | L7 |
| 総合試験形式 | — | L8 H1 | L8 |

---

## 弱点 → 補強パス（diagnostic-checklist.md と連携）

| 弱点 | 判定方法 | 補強ドリル |
|---|---|---|
| ループが書けない | L4 Medium 正答率 < 50% | L4 E1〜E10 再実施 |
| 再帰が追えない | L6 M4〜M7 で詰まる | L6 E1〜E5 → M4 再実施 |
| ポインタが混乱 | L7 Easy で間違える | L7 E1〜E5 → メモリ図を紙に書く |
| バブルソートが書けない | L5 H1 で詰まる | L4 H6 → L5 M1〜M3 → H1 |
| 試験形式に慣れない | mock-exam-A < 50点 | L8 M1〜M5 → mock-exam-A 再挑戦 |
