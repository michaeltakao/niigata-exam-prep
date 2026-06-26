---
nav_exclude: true
---

# 新潟大学 編入試験対策 教材

> 対象: プログラミング未経験者 → 新潟大学 C言語 編入試験合格
> 期間: 1ヶ月スプリント  
> 言語: C89/C99

---

## ナビゲーション

| ディレクトリ | 内容 | ステータス |
|---|---|---|
| [00_exam-analysis/](00_exam-analysis/) | 過去問分析・頻出表・予測問題 | Phase 1 実施後に充填 |
| [01_roadmap/](01_roadmap/) | 4週間学習スケジュール | Phase 3 実施後 |
| [02_textbook/](02_textbook/) | C言語教科書 (L00–L11) | Phase 4 実施後 |
| [03_drills/](03_drills/) | 練習問題 (各レベル30問) | Phase 5 実施後 |
| [04_question-map/](04_question-map/) | 過去問→必要知識 対応表 | Phase 6 実施後 |
| [05_mock-exams/](05_mock-exams/) | 模擬試験 A/B/C | Phase 9 実施後 |
| [06_progress/](06_progress/) | 学習進捗チェックリスト | 随時更新 |
| [07_technique-guide/](07_technique-guide/) | 解法テクニック集 | **作成済み** |

---

## 最初に読むファイル

1. **[07_technique-guide/formula-first.md](07_technique-guide/formula-first.md)** — 試験問題を解く基本テクニック（今すぐ読める）
2. **[00_exam-analysis/other-universities.md](00_exam-analysis/other-universities.md)** — 他大学の傾向分析（今すぐ読める）
3. 過去問PDFを `00_exam-analysis/raw/` に入れてください → Phase 1 開始

---

## 4週間学習ガイド（暫定）

```
Week 1: 変数・型・条件・ループ (L01–L04)
Week 2: 配列・文字列・関数 (L05–L07)
Week 3: ポインタ・構造体 + 過去問演習 (L08–L09)
Week 4: アルゴリズム・再帰 + 模擬試験 (L10–L11)
```

詳細スケジュールは過去問分析後に `01_roadmap/roadmap.md` へ。

---

## C言語スコープ (試験対象)

- データ型: `int`, `char`, `float`, `double`, 配列, 文字列 (`char[]`)
- 制御フロー: `if`/`else`, `switch`, `for`, `while`, `do-while`
- 関数: 定義・引数（値渡し）・`return`
- ポインタ: `*`, `&`, ポインタ算術, ポインタと配列の関係
- 構造体: `struct`, `typedef`
- 標準I/O: `printf`, `scanf`
- アルゴリズム: 線形探索・二分探索・バブルソート・選択ソート・挿入ソート
- 再帰: 階乗・フィボナッチ

※ 過去問分析後に再スコープ。

---

## コピーライト注意

過去問PDFは大学の著作物です。`raw/` ディレクトリは `.gitignore` に含めています。
文字起こし (`Q_YYYY_NNN.md`) のみをコミットしてください。
