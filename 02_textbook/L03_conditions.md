# L03 条件分岐 — 「もし〜なら」の実装

> **対象レベル:** L02 完了済み（演算子・式を理解している）  
> **所要時間:** 90〜120分  
> **到達目標:** if/else if/else と switch/case を正しく書いてトレースできる

---

## 1. コンセプト概要

**条件分岐（conditional branching）** とは、ある条件が成立するかどうかによって、実行するコードを切り替える仕組みです。現実世界では「もし雨なら傘を持つ、そうでなければ持たない」というように、状況に応じて行動が変わります。プログラムでも同じように「もし点数が90点以上なら優、70〜89なら良、…」という処理が必要です。C言語では **`if`文** と **`switch`文** という2つの主要な条件分岐構文が用意されています。この2つの使い分けと、よくある落とし穴（`break` 忘れなど）が試験で頻出です。

---

## 2. なぜ必要か

条件分岐がなければ、プログラムは常に同じ結果しか返せません。

- ログインシステム: 「パスワードが正しければログイン許可、違えばエラー」
- 成績計算: 「点数に応じて A/B/C/D を割り当てる」
- ゲーム: 「HPが0以下になったらゲームオーバー」

条件分岐はプログラムに「判断能力」を与える根本的な仕組みです。ループと組み合わせることで、複雑なアルゴリズムが構築できます。

---

## 3. 現実世界のアナロジー

**自動販売機のアナロジー**

```
if (投入金額 >= 商品の値段) {
    商品を出す;
    おつりを返す;
} else {
    「金額が足りません」と表示する;
}
```

switch 文は「チャンネル選択リモコン」に似ています：

```
switch (チャンネル番号) {
    case 1: NHKを映す; break;
    case 2: 民放Aを映す; break;
    case 3: 民放Bを映す; break;
    default: 「放送なし」と表示; break;
}
```

どのチャンネルを押したかによって動作が決まり、決まった動作が終わると（`break`）次には進まない。`break` を忘れると次のチャンネルの動作も実行されてしまいます（フォールスルー）。

---

## 4. 構文説明

### 4.1 if 文の基本形

```
if (条件式) {
    ↑──────┘
    条件式が真(1)のときだけ実行
    真・偽は L02 で学んだ比較演算子の結果
}
```

```c
int x = 10;
if (x > 5) {
    printf("x は 5 より大きい\n");  // 実行される
}
// x > 5 が偽(0)なら {} の中はスキップ
```

### 4.2 if-else

```
if (条件式) {
    // 条件が真のとき
} else {
    // 条件が偽のとき
}
```

```c
int score = 65;
if (score >= 60) {
    printf("合格\n");   // score=65 なので実行
} else {
    printf("不合格\n"); // スキップ
}
```

### 4.3 else if チェーン

```c
int score = 75;

if (score >= 90) {
    printf("優\n");        // 条件1: 90以上
} else if (score >= 70) {
    printf("良\n");        // 条件2: 70以上（かつ90未満）← 実行される
} else if (score >= 60) {
    printf("可\n");        // 条件3: 60以上（かつ70未満）
} else {
    printf("不可\n");      // どれにも当てはまらない
}
```

**重要:** else if は **上から順に評価** し、最初に真になったブロックだけを実行して残りはスキップします。

### 4.4 switch 文

```
switch (整数式) {
    case 値1:
        処理1;
        break;      ← 必須！なければ次の case に落ちる
    case 値2:
        処理2;
        break;
    default:        ← どの case にも一致しないとき
        処理デフォルト;
        break;
}
```

```c
int day = 3;
switch (day) {
    case 1: printf("月曜\n"); break;
    case 2: printf("火曜\n"); break;
    case 3: printf("水曜\n"); break;  // ← 実行される
    case 4: printf("木曜\n"); break;
    case 5: printf("金曜\n"); break;
    default: printf("週末\n"); break;
}
```

### 4.5 フォールスルー（break なし）

```c
int x = 2;
switch (x) {
    case 1: printf("one\n");   // break なし！
    case 2: printf("two\n");   // x==2 なのでここから実行 → 出力: two
    case 3: printf("three\n"); // break なし → ここも実行される！
    default: printf("other\n"); // これも実行される！
}
// 出力: two / three / other
```

意図的なフォールスルーは複数の case を同じ処理にまとめるときに使います：

```c
switch (month) {
    case 1: case 3: case 5: case 7:
    case 8: case 10: case 12:
        printf("31日\n"); break;
    case 4: case 6: case 9: case 11:
        printf("30日\n"); break;
    case 2:
        printf("28日または29日\n"); break;
}
```

### 4.6 ASCII フローチャート

**if-else のフロー:**
```
        ┌──────────────┐
        │   条件式を    │
        │    評価する   │
        └──────┬───────┘
               │
        ┌──────┴──────┐
        │  真(1)?      │
        └──┬───────┬──┘
          Yes      No
           │        │
     ┌─────┴──┐  ┌──┴─────┐
     │ if ブロ│  │ else ブ │
     │   ック │  │  ロック │
     └─────┬──┘  └──┬─────┘
           └────┬────┘
                │
          （次の処理へ）
```

**switch のフロー:**
```
        ┌──────────────┐
        │  switch 式   │
        │    を評価    │
        └──────┬───────┘
               │
    ┌──────────┼──────────┐
  case1?     case2?     default
    │           │           │
  処理1       処理2       デフォルト処理
  break       break       break
    │           │           │
    └──────────┼──────────┘
               │
          （次の処理へ）
```

---

## 5. ステップ実行トレース

```c
#include <stdio.h>
int main() {
    int score = 75;
    
    if (score >= 90) {
        printf("優\n");
    } else if (score >= 70) {
        printf("良\n");
    } else if (score >= 60) {
        printf("可\n");
    } else {
        printf("不可\n");
    }
    
    switch (score / 10) {
        case 9:  printf("9\n"); break;
        case 8:  printf("8\n"); break;
        case 7:  printf("7\n"); break;
        default: printf("other\n");
    }
    return 0;
}
```

**if-else チェーンのトレース（score = 75）:**

| ステップ | 評価 | 結果 | 動作 |
|---|---|---|---|
| 1 | `score >= 90` → `75 >= 90` | **偽(0)** | このブロックをスキップ |
| 2 | `score >= 70` → `75 >= 70` | **真(1)** | `printf("良\n")` を実行 |
| — | 残りの else if / else | スキップ | 最初の真でチェーン終了 |

**switch のトレース（score / 10 = 75 / 10 = 7）:**

| ステップ | 評価 | 結果 |
|---|---|---|
| — | `score / 10` = **7** | switch の式 = 7 |
| 1 | `case 9:` → 7 == 9? | 偽 → スキップ |
| 2 | `case 8:` → 7 == 8? | 偽 → スキップ |
| 3 | `case 7:` → 7 == 7? | **真** → `printf("7\n")` + `break` で脱出 |

**最終出力:**
```
良
7
```

---

## 6. 視覚的メモリ図

`else if` チェーンの評価の流れ（score = 75 の場合）：

```
score = 75
    │
    ▼
[score >= 90?]  → 75 >= 90 → FALSE ─→ skip
    │
    ▼ (elseへ)
[score >= 70?]  → 75 >= 70 → TRUE  ─→ 「良」を出力
    │
    × (以降はスキップ)
[score >= 60?]  → 評価されない
[else]          → 実行されない
```

switch の内部イメージ：
```
switch の式の値 = 7
                  │
    ┌─────────────┼──────────────────┐
    │             │                  │
  case 9        case 8            case 7
  7==9? No      7==8? No          7==7? YES!
  スキップ      スキップ          printf("7\n")
                                  break → 脱出
```

---

## 7. よくある間違い

### 間違い1: `=` と `==` の混同（最重要！）

```c
int x = 5;
// ❌ 間違い: 代入になってしまう
if (x = 3) {        // x に 3 が代入され、条件が 3（真）になる
    printf("equal"); // 常に実行される
}

// ✅ 正しい: 比較は == を使う
if (x == 3) {
    printf("equal");
}
```

**見分け方:** `=` は「代入」（左辺に右辺を入れる）、`==` は「比較」（等しいかチェック）。

---

### 間違い2: switch で break を忘れる（フォールスルー）

```c
int n = 2;
// ❌ break なし → フォールスルー発生
switch (n) {
    case 1: printf("one\n");
    case 2: printf("two\n");   // ここから実行
    case 3: printf("three\n"); // break なし → 続けて実行！
}
// 出力: two / three（意図と異なる！）

// ✅ 正しい: 各 case に break を入れる
switch (n) {
    case 1: printf("one\n");   break;
    case 2: printf("two\n");   break;  // ← ここで脱出
    case 3: printf("three\n"); break;
}
// 出力: two
```

---

### 間違い3: 境界値の `>=` vs `>` のミス

```c
// ❌ 間違い: 90点の人が「優」に入らない
if (score > 90) {    // 91点以上が優（90点は良に落ちる）
    printf("優\n");
} else if (score > 70) {
    printf("良\n");
}

// ✅ 正しい: 90点も「優」に含める
if (score >= 90) {   // 90点以上が優
    printf("優\n");
} else if (score >= 70) {
    printf("良\n");
}
```

**問題設定をよく読む。** 「90点以上」なら `>= 90`、「90点より多い」なら `> 90`。

---

### 間違い4: 複数行の if 本体に {} を忘れる

```c
int x = 5;
// ❌ 間違い: インデントで複数行に見えるが、else は最初の printf だけに対応
if (x > 3)
    printf("大きい\n");
    printf("x = %d\n", x);   // ← これは常に実行される（if の外！）

// ✅ 正しい: 複数行には必ず {} を使う
if (x > 3) {
    printf("大きい\n");
    printf("x = %d\n", x);
}
```

**習慣:** 条件分岐の本体は **常に `{}` で囲む**（1行でも）。

---

### 間違い5: ぶら下がり else（dangling else）

```c
int x = 5, y = 3;
// ❌ インデントは if(x>0) に属するように見えるが、
//    コンパイラは else を直近の if(y>0) に紐付ける
if (x > 0)
    if (y > 0)
        printf("both positive\n");
else
    printf("x not positive\n");  // 実際は y<=0 のとき実行される

// ✅ 正しい: {} で意図を明確にする
if (x > 0) {
    if (y > 0) {
        printf("both positive\n");
    }
} else {
    printf("x not positive\n");
}
```

---

## 8. ミニクイズ

**Q1.** 次のコードの出力は何ですか？（score = 85）
```c
if (score >= 90) printf("A\n");
else if (score >= 80) printf("B\n");
else if (score >= 70) printf("C\n");
else printf("D\n");
```

**Q2.** 次のコードは何を出力しますか？
```c
int n = 2;
switch (n) {
    case 1: printf("one\n");
    case 2: printf("two\n");
    case 3: printf("three\n"); break;
    default: printf("other\n");
}
```

**Q3.** `if (x = 5)` と `if (x == 5)` の違いを説明してください。

**Q4.** score = 70 のとき、次のコードは何を出力しますか？
```c
if (score > 70) printf("良\n");
else printf("可\n");
```

**Q5.** switch 文で使える式として正しいものはどれですか？
- (a) `switch (3.14)`
- (b) `switch (x + 1)`
- (c) `switch ("hello")`
- (d) `switch (x > 0)`

---

## 9. 例題（ワーク済み）

### 例題1: 成績判定プログラム

**問題:** 0〜100の点数を入力し、90以上「優」、70〜89「良」、60〜69「可」、それ未満「不可」と表示せよ。

```c
#include <stdio.h>
int main() {
    int score;
    printf("点数を入力: ");
    scanf("%d", &score);
    
    if (score >= 90) {
        printf("優\n");
    } else if (score >= 70) {
        printf("良\n");
    } else if (score >= 60) {
        printf("可\n");
    } else {
        printf("不可\n");
    }
    return 0;
}
```

**実行例:**
```
点数を入力: 75
良
```

**ポイント:** `else if` は上から評価されるので、`score >= 70` の時点で `score >= 90` は偽と確定済み。重複チェック不要。

---

### 例題2: switch を使った曜日表示

**問題:** 1〜7の整数を入力し、対応する曜日（月〜日）を表示せよ。

```c
#include <stdio.h>
int main() {
    int day;
    scanf("%d", &day);
    
    switch (day) {
        case 1: printf("月曜日\n"); break;
        case 2: printf("火曜日\n"); break;
        case 3: printf("水曜日\n"); break;
        case 4: printf("木曜日\n"); break;
        case 5: printf("金曜日\n"); break;
        case 6: printf("土曜日\n"); break;
        case 7: printf("日曜日\n"); break;
        default: printf("無効な入力\n"); break;
    }
    return 0;
}
```

**ポイント:** switch は整数値との完全一致で分岐。各 case に `break` 必須。

---

### 例題3: 三項演算子

**問題:** 2つの整数のうち大きい方を表示せよ。

```c
#include <stdio.h>
int main() {
    int a, b;
    scanf("%d %d", &a, &b);
    
    // 三項演算子: 条件 ? 真の値 : 偽の値
    int max = (a > b) ? a : b;
    printf("大きい方: %d\n", max);
    
    // if-else で書き換えると同じ意味:
    // if (a > b) { max = a; } else { max = b; }
    
    return 0;
}
```

**実行例（入力: 7 3）:**
```
大きい方: 7
```

---

## 10. 新潟大学試験との関連

**出題頻度: Tier 1 ★（毎年登場）**

条件分岐は単独でも出題されますが、ループ・配列と組み合わせた問題に組み込まれることが多いです。

### 典型的な出題パターン

**パターン A: 空欄補充（最頻出）**

```c
void classify(int score) {
    if (score _____ 90) {         // (A) を埋めよ
        printf("A\n");
    } else if (score _____ 70) {  // (B) を埋めよ
        printf("B\n");
    } else {
        printf("C\n");
    }
}
```

→ (A) `>=`、(B) `>=`。`>` と `>=` の違いに注意。

**パターン B: フォールスルー問題**

```c
int x = 2;
switch (x) {
    case 1: printf("1 ");
    case 2: printf("2 ");
    case 3: printf("3 ");
    default: printf("d ");
}
```

→ 出力: `2 3 d`（break がないため case 2 以降すべて実行）。
試験では「このコードの出力を答えよ」という形で出題。

**パターン C: バグ修正**

```c
// バグがあります。修正してください。
if (score = 60) {    // バグ: = → ==
    printf("60点\n");
}
```

### 試験対策チェックリスト

- [ ] if / else if / else の評価順序を説明できる
- [ ] switch の fall-through を正確にトレースできる
- [ ] `=` と `==` を絶対に混同しない
- [ ] 境界値（`>=` vs `>`）の違いを正確に読み取れる
- [ ] {} 省略時のスコープを正しく理解している

---

## ミニクイズ 解答

**A1.** `B`（score=85 → 90未満なので最初の条件は偽、80以上なので2番目が真）

**A2.** 
```
two
three
```
（`case 2` でマッチ → break なし → `case 3` も実行 → break で脱出 → `default` はスキップ）

**A3.** `if (x = 5)` は **代入**（x に 5 を代入し、条件が 5 = 真になり常に実行）。`if (x == 5)` は **比較**（x が 5 と等しいときだけ実行）。

**A4.** `可`（`score > 70` → `70 > 70` → **偽**。`else` の「可」が実行される）

**A5.** `(b) switch (x + 1)` と `(d) switch (x > 0)`
- (a) 浮動小数点数は switch に使えない
- (c) 文字列は switch に使えない
- (b) 整数式はOK
- (d) 比較式の結果（0 または 1）は整数なのでOK（ただし実用的でない）
