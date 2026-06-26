---
nav_exclude: true
---

# STATUS — 新潟大学 編入試験対策

## Now
- **学習サイト風テーマへ全面移行 完成 (2026-06-26)** — 公開サイトの「見にくい」を解消
  - テーマ: minima → just-the-docs (remote_theme@v0.12.0)。左サイドバー＋全文検索
  - ナビ整理: 学習者向けページのみ title 付与＝サイドバー表示。内部レポート
    25＋06_progress 5 は nav_exclude で非表示（巨大ナビ爆発を解消）
  - 数式: 単一 `$…$`→`$$…$$` 正規化(34ファイル/1166) + 数式内 `|`→`\vert` 退避
    (13ファイル/76) + MathJax 3.2.2。kramdown は `\(…\)`/`\[…\]` 出力（実機確認で確定）
  - カラーアウト: `::: type`→`<div class="callout…" markdown="1">` (18ファイル/142)
    ＋ custom.scss で配色(📘公式/✍例題/⚠注意/💡試験のコツ)
  - 自動化スクリプト: scripts/{inject_titles,hide_internal_nav,normalize_math,
    convert_callouts}.py（全て冪等・dry-run付き・ruff clean）
- **適応型 LMS 層 完成 (2026-06-21)** — 17 ファイル追加（進捗追跡・ルーブリック等）
- 全教材 + Notion エクスポート 完了 (2026-06-19) — 36 Notion ページ

## Next
1. LMS 活用開始 — student-onboarding.md から diagnostic-checklist.md を実施
2. 試験直前: Notion ページで弱点トピックを重点復習
3. 予測問題 (predicted-2026.md) を本番形式で通し解き
4. 物理ドリル追加 (P01,P03,P04,P05,P06 は未作成 — 時間があれば)
5. PDF パイプライン (`make math`) — basictex sudo 解決後に実行可能

## Blockers
- なし

## Key Decisions
- 試験科目: 数学・物理 (必須) + C言語 (人間支援プログラムのみ)
- 教材言語: 高校生レベルの日本語（専門用語はその場で定義）
- Tier 1 ★ 優先: 線形代数・積分・ODE・ニュートン則・力の分解
- 著作権: raw/ PDFはgit管理外。文字起こしのみコミット
- git 管理済み + private remote pending (2026-06-21 push 予定)

## Notion Structure (36 pages)
```
新潟大学 編入試験対策 2026 (root)
├── 📊 出題傾向分析
│   ├── 数学 Tier表
│   └── 物理 Tier表
├── 📐 数学
│   ├── 過去問: R8-1, R8-2, R7, R6機, R6人 (5)
│   ├── 教科書: M01-M07 (7)
│   ├── ドリル: M02, M05 (2)
│   └── 予測問題 2026 (1)
├── ⚡ 物理
│   ├── 過去問: R8, R7, R6機 (3)
│   ├── 教科書: P01-P07 (7)
│   ├── ドリル: P02 (1)
│   └── 予測問題 2026 (1)
└── 💻 プログラミング (C言語)
    ├── 出題傾向分析 (1)
    ├── 過去問参照: R8, R7, R6 (3)
    ├── 教科書: C01-C04 (4)
    └── 予測問題 2026 (1)
```

## Last Verified
- 2026-06-26: just-the-docs 移行 Phase 1+2 完了・push 済 (main @ 0c80b83 ＋STATUS更新)
  - GitHub Pages ビルド success (run 28218157137)
  - 主要URL 全 200 (STUDENT_HOME/L04/L4ドリル/模擬A/M01/P01)
  - ナビ内部レポート = 0、`:::` 漏れ = 0、数式 `\(…\)`/`\[…\]` 描画 (MathJax 3.2.2)
  - M02 行列・絶対値・行列式が正しく描画、4種カラーアウトが色付きボックス化
  - ブラウザ実機確認 (Chrome DevTools): サイドバー整理・検索動作・C言語経路遷移
- 2026-06-21: 適応型 LMS 層 17 ファイル完成 + commit + push (michaeltakao/niigata-exam-prep)
- 2026-06-19: 36 Notion ページ作成完了 (notion-create-pages MCP)
- Root: https://app.notion.com/p/384fee4dad31818cba33d27d6d0dd986
