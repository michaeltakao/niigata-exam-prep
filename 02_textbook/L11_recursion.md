---
title: "L11 再帰 — 関数が自分を呼び出す"
---

# L11 再帰 — 関数が自分を呼び出す

> **難易度**: ★★★★☆ | **前提**: L07 関数、L04 ループ | **試験重要度**: Tier 1（R6・R8 出題）

---

## 1. コンセプト概要

**再帰（recursion）**とは、関数が自分自身を呼び出すことです。

```c
int factorial(int n) {
    if (n <= 0) return 1;       // ← 基底ケース（停止条件）
    return n * factorial(n - 1); // ← 再帰呼び出し
}
```

再帰を理解するには2つの要素が必要です:

| 要素 | 役割 | 忘れると |
|---|---|---|
| **基底ケース (base case)** | 再帰を止める条件 | 無限ループ → スタックオーバーフロー |
| **再帰ケース (recursive case)** | 問題を小さくして自分を呼ぶ | 問題が解けない |

---

## 2. なぜ必要か

**繰り返しパターンを持つ問題**は再帰で自然に書けます。たとえば:

- `5! = 5 × 4!` → 階乗は「自分より小さい階乗」で定義できる
- `fib(n) = fib(n-1) + fib(n-2)` → フィボナッチ数列
- `gcd(48, 18) = gcd(18, 48%18) = gcd(18, 12) = ...` → 最大公約数

試験では再帰関数の**コールトレース**（呼び出し過程を追う）が頻繁に出題されます。「`f(5)`の戻り値を求めよ（途中過程も示せ）」という形式です。

---

## 3. 現実世界のアナロジー

### ロシアのマトリョーシカ人形

マトリョーシカは人形の中に人形が入っています。「中に入っている人形を全部数える」タスクを考えます:

```
count(人形) =
    もし中身がなければ: return 1        ← 基底ケース
    それ以外: return 1 + count(中の人形) ← 再帰ケース
```

これが再帰の構造そのものです。

### 鏡の中の鏡

2枚の鏡を向かい合わせると、鏡の中にまた鏡が映り、その中にまた...と無限に続きます。基底ケースのない再帰はこれと同じです — **永遠に終わりません**。

---

## 4. 構文説明

### 階乗: n! = 1 × 2 × 3 × ... × n

数学的定義: `n! = n × (n-1)!`、`0! = 1`

```c
#include <stdio.h>

int factorial(int n) {
    if (n <= 0) return 1;        // 基底ケース: 0! = 1
    return n * factorial(n - 1); // 再帰ケース: n! = n × (n-1)!
}

int main(void) {
    printf("5! = %d\n", factorial(5));  // → 120
    return 0;
}
```

### フィボナッチ数列

数学的定義: `F(n) = F(n-1) + F(n-2)`、`F(0) = 1`、`F(1) = 1`

**注意:** `F(0)=0` と定義する教科書もありますが、新潟大学過去問では `F(0)=1` が使われています。

```c
int fib(int n) {
    if (n <= 1) return 1;              // 基底ケース: F(0)=F(1)=1
    return fib(n - 1) + fib(n - 2);   // 再帰ケース
}
```

### GCD（最大公約数）— ユークリッドの互除法

数学的定義: `gcd(a, 0) = a`、`gcd(a, b) = gcd(b, a % b)`

```c
int gcd(int a, int b) {
    if (b == 0) return a;          // 基底ケース
    return gcd(b, a % b);          // 再帰ケース
}
```

### べき乗関数

```c
int power(int base, int exp) {
    if (exp == 0) return 1;                // base^0 = 1（基底ケース）
    return base * power(base, exp - 1);   // base^n = base × base^(n-1)
}
```

---

## 5. ステップ実行トレース

プログラム:
```c
#include <stdio.h>

int factorial(int n) {
    if (n <= 0) return 1;
    return n * factorial(n - 1);
}

int fib(int n) {
    if (n <= 1) return 1;
    return fib(n - 1) + fib(n - 2);
}

int main(void) {
    printf("4! = %d\n", factorial(4));
    printf("fib(5) = %d\n", fib(5));
    return 0;
}
```

### factorial(4) のコールスタックトレース

| 呼び出し順 | 関数 | n | 条件 | 戻り値 |
|---|---|---|---|---|
| 1 | factorial(4) | 4 | 4>0 → 再帰 | 4 × factorial(3) |
| 2 | factorial(3) | 3 | 3>0 → 再帰 | 3 × factorial(2) |
| 3 | factorial(2) | 2 | 2>0 → 再帰 | 2 × factorial(1) |
| 4 | factorial(1) | 1 | 1>0 → 再帰 | 1 × factorial(0) |
| 5 | factorial(0) | 0 | 0≤0 → 停止 | **1** |
| 4に戻る | factorial(1) | — | — | 1 × 1 = **1** |
| 3に戻る | factorial(2) | — | — | 2 × 1 = **2** |
| 2に戻る | factorial(3) | — | — | 3 × 2 = **6** |
| 1に戻る | factorial(4) | — | — | 4 × 6 = **24** |

**出力: `4! = 24`**

### fib(5) の完全展開ツリー

```
fib(5)
├─ fib(4)
│   ├─ fib(3)
│   │   ├─ fib(2)
│   │   │   ├─ fib(1) → 1
│   │   │   └─ fib(0) → 1
│   │   │   └─ 戻り値: 1+1 = 2
│   │   └─ fib(1) → 1
│   │   └─ 戻り値: 2+1 = 3
│   └─ fib(2)
│       ├─ fib(1) → 1
│       └─ fib(0) → 1
│       └─ 戻り値: 1+1 = 2
│   └─ 戻り値: 3+2 = 5
└─ fib(3)
    ├─ fib(2)
    │   ├─ fib(1) → 1
    │   └─ fib(0) → 1
    │   └─ 戻り値: 1+1 = 2
    └─ fib(1) → 1
    └─ 戻り値: 2+1 = 3
└─ 戻り値: 5+3 = 8

fib(5) = 8
```

**出力: `fib(5) = 8`**

フィボナッチ数列 (F(0)=1 定義):
```
F(0)=1, F(1)=1, F(2)=2, F(3)=3, F(4)=5, F(5)=8, F(6)=13
```

---

## 6. 視覚的メモリ図

### コールスタックの積み上がりと巻き戻し

```
factorial(4) を呼ぶとき、スタックがこう積み上がる:

呼び出し中:                    戻り中:
┌──────────────────┐          ┌──────────────────┐
│ factorial(0)     │ ← top    │ 全て返り終わる    │
│ n=0, return 1    │          └──────────────────┘
├──────────────────┤                    ↑
│ factorial(1)     │          ┌──────────────────┐
│ n=1              │          │ factorial(4)=24  │ 最終結果
├──────────────────┤          └──────────────────┘
│ factorial(2)     │
│ n=2              │
├──────────────────┤
│ factorial(3)     │
│ n=3              │
├──────────────────┤
│ factorial(4)     │ ← bottom
│ n=4              │
└──────────────────┘

各関数は「下の関数が戻ってから」自分の計算を完了できる。
```

### 基底ケースがない場合（スタックオーバーフロー）

```c
// 危険なコード: 基底ケースがない!
int bad_factorial(int n) {
    return n * bad_factorial(n - 1);  // 永遠に呼び続ける
}
```

```
スタックが満杯になる:
┌──────────────────┐
│ bad_factorial(-1000) │
├──────────────────┤
│ bad_factorial(-999)  │
├──────────────────┤
│   ...（無限に続く）  │
├──────────────────┤
│ bad_factorial(4)     │
└──────────────────┘
→ Stack overflow! プログラムがクラッシュする
```

---

## 7. よくある間違い

### ① 基底ケースが抜けている → 無限再帰

```c
// WRONG: 基底ケースなし
int factorial(int n) {
    return n * factorial(n - 1);  // n=0 でも呼ばれ続ける → クラッシュ
}

// RIGHT:
int factorial(int n) {
    if (n <= 0) return 1;          // ← 必ず基底ケースを書く
    return n * factorial(n - 1);
}
```

### ② 階乗の基底ケースで 0 を返す

```c
// WRONG: 0! = 0 は数学的に間違い
int factorial(int n) {
    if (n == 0) return 0;  // 0! は 1 であるべき!
    return n * factorial(n - 1);
}
// factorial(3) = 3 × 2 × 1 × 0 = 0 になってしまう

// RIGHT:
if (n == 0) return 1;  // 0! = 1
```

### ③ フィボナッチの基底ケースの定義ミス

```c
// WRONG: n <= 0 を基底ケースにするとfib(1)が再帰する
int fib(int n) {
    if (n <= 0) return 1;          // n=1 のとき fib(0)+fib(-1) を呼ぶ!
    return fib(n - 1) + fib(n - 2);
}

// RIGHT: n <= 1 で止める
int fib(int n) {
    if (n <= 1) return 1;          // F(0)=1, F(1)=1 どちらも止める
    return fib(n - 1) + fib(n - 2);
}
```

### ④ 再帰の深さが深すぎる

```c
// n=10000 などの大きい数では実行時にスタックオーバーフロー
int factorial(int n) {
    if (n <= 0) return 1;
    return n * factorial(n - 1);  // n=10000だと10000回スタックを積む
}
// 試験では n が小さい値（4〜6程度）なので実際は問題ない
```

### ⑤ 再帰が常にループより速いと思い込む

```c
// フィボナッチの再帰版: fib(40) の計算には膨大な時間がかかる
// （同じ計算を何度も繰り返すため — fib(2)は何回も呼ばれる）

// ループ版の方が圧倒的に速い:
int fib_iter(int n) {
    if (n <= 1) return 1;
    int a = 1, b = 1;
    for (int i = 2; i <= n; i++) {
        int c = a + b;
        a = b;
        b = c;
    }
    return b;
}
```

試験では再帰版のトレースが問われるので、再帰版を理解するのが優先。

---

## 8. ミニクイズ

**Q1.** `factorial(3)` の戻り値はいくつか？

<details><summary>答え</summary>
6。トレース: factorial(3)=3×factorial(2)=3×(2×factorial(1))=3×(2×(1×factorial(0)))=3×2×1×1=6。
</details>

**Q2.** `fib(4)` の戻り値はいくつか？（F(0)=F(1)=1 の定義）

<details><summary>答え</summary>
5。F(0)=1, F(1)=1, F(2)=2, F(3)=3, F(4)=5。
</details>

**Q3.** 次の関数で `gcd(12, 8)` を呼んだとき何が返るか？
```c
int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}
```

<details><summary>答え</summary>
4。トレース: gcd(12,8)→gcd(8,4)→gcd(4,0)→return 4。
</details>

**Q4.** 基底ケースを忘れた再帰関数はどうなるか？

<details><summary>答え</summary>
無限に自分を呼び続け、スタックオーバーフローでプログラムがクラッシュする。
</details>

**Q5.** `power(2, 4)` の戻り値はいくつか？（`power(base, exp) = base × power(base, exp-1)`, `power(x, 0)=1`）

<details><summary>答え</summary>
16。2^4 = 2×2×2×2 = 16。トレース: power(2,4)=2×power(2,3)=2×2×power(2,2)=2×2×2×power(2,1)=2×2×2×2×power(2,0)=2×2×2×2×1=16。
</details>

---

## 9. 例題

### 例題 1: factorial(5) のコールスタックトレース

**問題:** `factorial(5)` の戻り値を求めよ。呼び出し過程を示せ。

```c
#include <stdio.h>

int factorial(int n) {
    if (n <= 0) return 1;
    return n * factorial(n - 1);
}

int main(void) {
    printf("%d\n", factorial(5));
    return 0;
}
```

**トレース（コールスタック）:**

```
factorial(5)
 └─ 5 × factorial(4)
         └─ 4 × factorial(3)
                 └─ 3 × factorial(2)
                         └─ 2 × factorial(1)
                                 └─ 1 × factorial(0)
                                         └─ return 1  ← 基底ケース
                                 return 1×1 = 1
                         return 2×1 = 2
                 return 3×2 = 6
         return 4×6 = 24
 return 5×24 = 120
```

**答え: 120**（出力: `120`）

---

### 例題 2: fib(6) の完全ツリートレース

**問題:** `fib(6)` の戻り値を求めよ。

```c
int fib(int n) {
    if (n <= 1) return 1;
    return fib(n - 1) + fib(n - 2);
}
```

**ツリー展開:**

```
fib(6) = fib(5) + fib(4)
       = 8      + 5
       = 13

補助: F(0)=1, F(1)=1, F(2)=2, F(3)=3, F(4)=5, F(5)=8, F(6)=13
```

**数列の確認:**
```
n:    0  1  2  3  4  5  6
F(n): 1  1  2  3  5  8  13
```

**答え: 13**

---

### 例題 3: GCD(48, 18) をユークリッドの互除法でトレース

**問題:** `gcd(48, 18)` の計算過程を示し、戻り値を求めよ。

```c
#include <stdio.h>

int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}

int main(void) {
    printf("gcd(48,18) = %d\n", gcd(48, 18));
    return 0;
}
```

**トレース:**

| 呼び出し | a | b | a%b | 次の呼び出し |
|---|---|---|---|---|
| gcd(48, 18) | 48 | 18 | 12 | gcd(18, 12) |
| gcd(18, 12) | 18 | 12 | 6  | gcd(12, 6) |
| gcd(12, 6)  | 12 | 6  | 0  | gcd(6, 0) |
| gcd(6, 0)   | 6  | 0  | —  | **return 6** |

**答え: 6**（48 と 18 の最大公約数は 6）

検証: 48 = 6×8、18 = 6×3 ✓

---

## 10. 新潟大学試験との関連

**出題実績:** 再帰関数は **R6・R8 で出題**。「フィボナッチ数列の特定の項の値を求めよ」「関数 f の戻り値を答えよ（途中過程も示せ）」が典型問題です。

**典型的な出題パターン:**

**パターン1: 再帰トレース（最頻出）**
```c
int f(int n) {
    if (n <= 1) return 1;
    return f(n-1) + f(n-2);
}
// 問: f(4) の戻り値を求めよ。呼び出し過程を示せ。
// 答え: 5 (F(0)=1,F(1)=1,F(2)=2,F(3)=3,F(4)=5)
```

**パターン2: 空欄埋め**
```c
int factorial(int n) {
    if (n (A) 0) return (B);   // (A)=<=, (B)=1
    return n * factorial((C)); // (C)=n-1
}
```

**パターン3: 実装問題**
```
GCD を求める再帰関数を実装せよ。
```

**試験対策のポイント:**
- `factorial(4)=24`、`fib(5)=8`、`fib(6)=13` は暗記すること（頻繁に出る）
- コールスタックを**紙に書いて**トレースする練習をすること（頭の中だけでは追えなくなる）
- 基底ケースの条件と戻り値を必ず確認すること（`n <= 0` vs `n <= 1` の違いで答えが変わる）
- F(0)=1 の定義（`n<=1` で return 1）と F(0)=0 の定義（`n==0` で return 0）を混同しないこと
