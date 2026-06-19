# STATUS — 新潟大学 編入試験対策

## Now
- Scaffold 完成（2026-06-19）
- `other-universities.md` + `formula-first.md` 作成済み
- **次アクション**: 過去問PDF を `00_exam-analysis/raw/` に配置 → Phase 1 開始

## Next
1. Phase 1: 過去問文字起こし → `Q_YYYY_NNN.md` × N問 + `analysis.md` 頻出表
2. Phase 2: `dependency-graph.md`（前提知識チェーン）
3. Phase 3: `roadmap.md`（4週間スケジュール、%込み）
4. Phase 4: 教科書 Tier 1 レベルから順次作成
5. Phase 5: ドリル問題

## Blockers
- 過去問PDF 未受領（Phase 1 はPDF待ち）

## Key Decisions
- 試験言語: C89/C99（両方対応）
- 教材言語: 高校生レベルの日本語（専門用語は必ずその場で定義）
- ドリル数: Tier 1 トピックのみ 30問/レベル（10×easy/medium/hard）
- 著作権: raw/ PDFはgit管理外。文字起こしのみコミット
- `predicted-2026.md`: Phase 1 完了後に作成

## Last Verified
- 2026-06-19: `git init` + scaffold + 初期ファイル作成
