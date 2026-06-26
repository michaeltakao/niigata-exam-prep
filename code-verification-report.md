---
nav_exclude: true
---

# C言語コードスニペット検証レポート

**検証日時**: 2026-06-20 21:24:19
**検証対象**: 03_drills/, 05_mock-exams/
**使用コンパイラ**: gcc -Wall -Wextra -std=c11

## サマリー

| 区分 | 件数 |
|---|---|
| 全スニペット数 | 542 |
| コンパイル成功 (クリーン) | 298 |
| 警告あり | 54 |
| エラー（修復前） | 0 |
| 自動修復成功 | 0 |
| 修復不可能 | 0 |
| 意図的バグ（スキップ） | 64 |
| 穴埋め問題（スキップ） | 122 |
| 非Cコンテンツ・スキップ | 1 |
| フラグメント（ラップ後成功） | 140 |

## エラー詳細

### 自動修復済み

*なし*

### 修復不可能（要手動確認）

*なし — 全エラー解消済み* ✅

### 警告一覧

| ファイル | スニペット# | 警告内容 |
|---|---|---|
| 03_drills/L1_variables.md | #13 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmpkl8_yb71.c:4:20: warning: variable 'x' is uninit` |
| 03_drills/L2_expressions.md | #6 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmp3gkwbfzo.c:4:9: warning: unused variable 'x' [-W` |
| 03_drills/L2_expressions.md | #6 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmp3gkwbfzo.c:5:9: warning: unused variable 'y' [-W` |
| 03_drills/L2_expressions.md | #7 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmpok73eaxy.c:4:11: warning: using the result of an` |
| 03_drills/L2_expressions.md | #11 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmpmv0_t354.c:4:14: warning: multiple unsequenced m` |
| 03_drills/L2_expressions.md | #18 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmpe6gbx35y.c:4:9: warning: unused variable 'result` |
| 03_drills/L3_conditions.md | #15 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmp1pfu6ymo.c:5:9: warning: variable 'points' set b` |
| 03_drills/L3_conditions.md | #16 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmp5a9ejpp0.c:5:9: warning: variable 'points' set b` |
| 03_drills/L5_arrays.md | #34 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmp96qmhj_a.c:4:32: warning: shifting a negative si` |
| 03_drills/L6_functions.md | #23 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmpbx8wt7je.c:2:25: warning: parameter 'x' set but ` |
| 03_drills/L6_functions.md | #23 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmpbx8wt7je.c:5:32: warning: unused parameter 'n' [` |
| 03_drills/L6_functions.md | #32 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmprx1lhsr3.c:3:21: warning: unused parameter 'base` |
| 03_drills/L6_functions.md | #32 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmprx1lhsr3.c:3:31: warning: unused parameter 'exp'` |
| 03_drills/L7_pointers.md | #9 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmp0ogflls6.c:9:20: warning: format specifies type ` |
| 03_drills/L7_pointers.md | #18 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmp1yrwl7f6.c:7:21: warning: format specifies type ` |
| 03_drills/L7_pointers.md | #20 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmpoahhcc_i.c:4:13: warning: address of stack memor` |
| 03_drills/L7_pointers.md | #23 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmp9o0y_uv4.c:5:10: warning: unused variable 'p' [-` |
| 03_drills/L7_pointers.md | #23 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmp9o0y_uv4.c:6:10: warning: unused variable 'q' [-` |
| 03_drills/L7_pointers.md | #30 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmpwvfzdb4b.c:7:10: warning: unused variable 'p' [-` |
| 03_drills/L7_pointers.md | #33 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmp3ep5yd15.c:7:13: warning: address of stack memor` |
| 03_drills/L8_exam.md | #5 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmpxrjxrsgt.c:4:9: warning: unused variable 'n' [-W` |
| 03_drills/L8_exam.md | #15 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmp31wpd3wa.c:4:9: warning: unused variable 'a' [-W` |
| 03_drills/L8_exam.md | #33 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmp4rssbtpw.c:3:22: warning: unused parameter 'a' [` |
| 03_drills/L8_exam.md | #33 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmp4rssbtpw.c:3:31: warning: unused parameter 'n' [` |
| 03_drills/L8_exam.md | #37 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmp34ey3doz.c:2:13: warning: unused parameter 'a' [` |
| 03_drills/L8_exam.md | #37 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmp34ey3doz.c:2:20: warning: unused parameter 'b' [` |
| 03_drills/L8_exam.md | #39 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmphjlarbjh.c:5:19: warning: unused parameter 'a' [` |
| 03_drills/L8_exam.md | #39 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmphjlarbjh.c:5:38: warning: unused parameter 'sums` |
| 03_drills/L8_exam.md | #41 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmpmsvadhka.c:3:28: warning: unused parameter 's' [` |
| 03_drills/L8_exam.md | #41 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmpmsvadhka.c:3:37: warning: unused parameter 'left` |
| 03_drills/L8_exam.md | #43 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmpumpd7i39.c:2:19: warning: unused parameter 's' [` |
| 03_drills/L8_exam.md | #43 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmpumpd7i39.c:2:29: warning: unused parameter 'deli` |
| 05_mock-exams/mock-exam-A.md | #4 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmphdwzzmul.c:4:9: warning: unused variable 'n' [-W` |
| 05_mock-exams/mock-exam-A.md | #4 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmphdwzzmul.c:5:9: warning: unused variable 'sum' [` |
| 05_mock-exams/mock-exam-A.md | #11 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmpj_9lezih.c:6:9: warning: variable 'sum' set but ` |
| 05_mock-exams/mock-exam-B.md | #16 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmph754k2xq.c:4:9: warning: unused variable 'n' [-W` |
| 05_mock-exams/mock-exam-B.md | #16 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmph754k2xq.c:5:12: warning: unused variable 'resul` |
| 02_textbook/L01_variables-types.md | #1 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmpopobgk2i.c:4:9: warning: unused variable 'apples` |
| 02_textbook/L01_variables-types.md | #1 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmpopobgk2i.c:5:12: warning: unused variable 'price` |
| 02_textbook/L01_variables-types.md | #2 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmpdxbxyi4n.c:4:9: warning: variable 'apples' set b` |
| 02_textbook/L01_variables-types.md | #2 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmpdxbxyi4n.c:5:9: warning: variable 'grade' set bu` |
| 02_textbook/L01_variables-types.md | #3 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmp6h68e5mn.c:4:12: warning: unused variable 'apple` |
| 02_textbook/L01_variables-types.md | #3 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmp6h68e5mn.c:5:12: warning: unused variable 'price` |
| 02_textbook/L01_variables-types.md | #12 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmpiwo2ufg9.c:5:17: warning: format specifies type ` |
| 02_textbook/L01_variables-types.md | #12 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmpiwo2ufg9.c:5:17: warning: variable 'n' is uninit` |
| 02_textbook/L05_arrays.md | #1 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmp2e2wetzu.c:4:9: warning: unused variable 'score0` |
| 02_textbook/L05_arrays.md | #1 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmp2e2wetzu.c:5:9: warning: unused variable 'score1` |
| 02_textbook/L05_arrays.md | #3 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmp0fpjhwea.c:4:9: warning: unused variable 'a' [-W` |
| 02_textbook/L05_arrays.md | #3 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmp0fpjhwea.c:5:12: warning: unused variable 'b' [-` |
| 02_textbook/L05_arrays.md | #4 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmpupg4iy_e.c:5:9: warning: unused variable 'a' [-W` |
| 02_textbook/L05_arrays.md | #4 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmpupg4iy_e.c:8:9: warning: unused variable 'b' [-W` |
| 02_textbook/L05_arrays.md | #6 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmpk54jz4eq.c:5:9: warning: unused variable 'n' [-W` |
| 02_textbook/L05_arrays.md | #8 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmpoo3erppt.c:4:9: warning: unused variable 'matrix` |
| 02_textbook/L05_arrays.md | #15 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmpce3rr4m5.c:4:9: warning: unused variable 'a' [-W` |
| 02_textbook/L05_arrays.md | #18 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmpiszuqry3.c:4:9: warning: unused variable 'm' [-W` |
| 02_textbook/L06_strings.md | #1 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmplkix70ul.c:4:9: warning: unused variable 'i' [-W` |
| 02_textbook/L06_strings.md | #1 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmplkix70ul.c:6:10: warning: unused variable 's1' [` |
| 02_textbook/L06_strings.md | #4 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmpax4812l0.c:7:12: warning: unused variable 'len' ` |
| 02_textbook/L06_strings.md | #4 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmpax4812l0.c:15:9: warning: unused variable 'cmp' ` |
| 02_textbook/L07_functions.md | #3 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmpn505ggl1.c:8:9: warning: unused variable 'result` |
| 02_textbook/L07_functions.md | #5 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmp_3q68rnx.c:8:9: warning: unused variable 'v' [-W` |
| 02_textbook/L07_functions.md | #9 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmpy6m7lje5.c:8:9: warning: unused variable 'result` |
| 02_textbook/L07_functions.md | #18 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmpkuzl97q3.c:4:9: warning: unused variable 'a' [-W` |
| 02_textbook/L07_functions.md | #18 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmpkuzl97q3.c:5:9: warning: unused variable 'b' [-W` |
| 02_textbook/L08_pointers.md | #3 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmpy7cb7oxv.c:4:10: warning: unused variable 'p' [-` |
| 02_textbook/L08_pointers.md | #8 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmp9xjhn14x.c:5:10: warning: unused variable 'p' [-` |
| 02_textbook/L09_structs.md | #1 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmplz8ld4ac.c:12:9: warning: unused variable 'score` |
| 02_textbook/L09_structs.md | #1 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmplz8ld4ac.c:10:3: warning: unused typedef 'Studen` |
| 02_textbook/L09_structs.md | #2 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmpcrm06uc0.c:4:11: warning: unused variable 'id1' ` |
| 02_textbook/L09_structs.md | #2 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmpcrm06uc0.c:4:25: warning: unused variable 'id2' ` |
| 02_textbook/L09_structs.md | #4 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmpqbf39ivt.c:10:3: warning: unused typedef 'Studen` |
| 02_textbook/L09_structs.md | #5 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmp__i3fin0.c:8:7: warning: unused typedef 'Student` |
| 02_textbook/L09_structs.md | #7 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmp5tz_c1nx.c:11:37: warning: missing field 'score'` |
| 02_textbook/L09_structs.md | #8 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmpkmbl7isf.c:19:38: warning: missing field 'score'` |
| 02_textbook/L09_structs.md | #8 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmpkmbl7isf.c:22:13: warning: unused variable 's3' ` |
| 02_textbook/L09_structs.md | #16 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmpu3x59s0d.c:11:13: warning: unused variable 'stud` |
| 02_textbook/L10_algorithms.md | #7 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmpt52ey1lo.c:4:9: warning: unused variable 'a' [-W` |
| 02_textbook/L11_recursion.md | #7 | `/var/folders/pz/9bgt14gd58q0dnhjvypyk3cc0000gn/T/tmpdnwikvnr.c:4:26: warning: all paths through this` |

## ファイル別結果

| ファイル | 合計 | OK | REPAIRED | WARNING | ERROR | INTENTIONAL | FILL_BLANK | SKIP |
|---|---|---|---|---|---|---|---|---|
| 03_drills/L1_variables.md | 31 | 24 | 0 | 1 | 0 | 0 | 6 | 0 |
| 03_drills/L2_expressions.md | 23 | 9 | 0 | 4 | 0 | 1 | 9 | 0 |
| 03_drills/L3_conditions.md | 37 | 25 | 0 | 2 | 0 | 2 | 8 | 0 |
| 03_drills/L4_loops.md | 35 | 25 | 0 | 0 | 0 | 3 | 7 | 0 |
| 03_drills/L5_arrays.md | 37 | 21 | 0 | 1 | 0 | 0 | 15 | 0 |
| 03_drills/L6_functions.md | 38 | 23 | 0 | 2 | 0 | 0 | 13 | 0 |
| 03_drills/L7_pointers.md | 35 | 18 | 0 | 6 | 0 | 0 | 11 | 0 |
| 03_drills/L8_exam.md | 45 | 22 | 0 | 7 | 0 | 5 | 11 | 0 |
| 05_mock-exams/mock-exam-A.md | 17 | 8 | 0 | 2 | 0 | 0 | 7 | 0 |
| 05_mock-exams/mock-exam-B.md | 19 | 9 | 0 | 1 | 0 | 1 | 8 | 0 |
| 05_mock-exams/mock-exam-C.md | 15 | 7 | 0 | 0 | 0 | 2 | 5 | 1 |
| 02_textbook/L01_variables-types.md | 17 | 7 | 0 | 4 | 0 | 5 | 1 | 0 |
| 02_textbook/L02_operators-expressions.md | 17 | 12 | 0 | 0 | 0 | 4 | 1 | 0 |
| 02_textbook/L03_conditions.md | 21 | 13 | 0 | 0 | 0 | 6 | 2 | 0 |
| 02_textbook/L04_loops.md | 22 | 16 | 0 | 0 | 0 | 5 | 1 | 0 |
| 02_textbook/L05_arrays.md | 22 | 9 | 0 | 7 | 0 | 5 | 1 | 0 |
| 02_textbook/L06_strings.md | 17 | 8 | 0 | 2 | 0 | 4 | 3 | 0 |
| 02_textbook/L07_functions.md | 24 | 12 | 0 | 4 | 0 | 6 | 2 | 0 |
| 02_textbook/L08_pointers.md | 20 | 9 | 0 | 2 | 0 | 5 | 4 | 0 |
| 02_textbook/L09_structs.md | 19 | 7 | 0 | 7 | 0 | 5 | 0 | 0 |
| 02_textbook/L10_algorithms.md | 13 | 7 | 0 | 1 | 0 | 4 | 1 | 0 |
| 02_textbook/L11_recursion.md | 18 | 7 | 0 | 1 | 0 | 1 | 9 | 0 |