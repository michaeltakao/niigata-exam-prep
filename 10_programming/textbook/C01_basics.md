---
title: C01 基本構文 — 変数・型・制御構造
---

# C01 基本構文

## 1. データ型と変数宣言

<div class="callout callout-formula" markdown="1">

| 型 | バイト数 | 値の範囲 | 使い方 |
|---|---|---|---|
| `int` | 4 | −2^31 〜 2^31−1 | 整数全般 |
| `double` | 8 | 倍精度浮動小数点 | 実数計算 |
| `char` | 1 | 0〜255 (ASCII) | 文字・小整数 |
| `float` | 4 | 単精度浮動小数点 | メモリ節約時 |

</div>

```c
int a = 10;
double x = 3.14;
char c = 'A';     // シングルクォート
char s[] = "hello"; // 文字列はダブルクォート
```

<div class="callout callout-warning" markdown="1">

- `int / int` は **整数除算**。`3 / 2 = 1`（小数切り捨て）
- `double d = 3 / 2;` でも右辺が整数除算されて `1.0` になる
- `double d = 3.0 / 2;` または `(double)3 / 2` にすること

</div>

---

## 2. printf / scanf

<div class="callout callout-formula" markdown="1">

| 書式指定子 | 型 |
|---|---|
| `%d` | int |
| `%f` | float / double |
| `%lf` | double (scanf では必須) |
| `%c` | char |
| `%s` | 文字列 |

</div>

<div class="callout callout-example" markdown="1">

```c
#include <stdio.h>
int main() {
    int n;
    double x;
    printf("整数と実数を入力: ");
    scanf("%d %lf", &n, &x);           // & を忘れずに
    printf("n=%d, x=%.2f\n", n, x);   // %.2f は小数2桁
    return 0;
}
```

</div>

---

## 3. 制御構造

### if-else

```c
if (x > 0) {
    printf("正");
} else if (x == 0) {
    printf("ゼロ");
} else {
    printf("負");
}
```

### for ループ

<div class="callout callout-formula" markdown="1">

```
for (初期化; 条件; 更新) {
    処理;
}
```

</div>

<div class="callout callout-example" markdown="1">

```c
// 1 から 10 の和
int sum = 0;
for (int i = 1; i <= 10; i++) {
    sum += i;
}
printf("sum = %d\n", sum);   // 55
```

</div>

### while ループ

```c
int n = 1;
while (n <= 5) {
    printf("%d ", n);
    n++;
}
// 出力: 1 2 3 4 5
```

### switch

```c
int x = 2;
switch (x) {
    case 1: printf("one"); break;
    case 2: printf("two"); break;
    default: printf("other");
}
```

<div class="callout callout-warning" markdown="1">

`break` を忘れると次の `case` も実行される（フォールスルー）。意図しない場合は必ず `break` を入れる。

</div>

---

## 4. 演算子まとめ

<div class="callout callout-formula" markdown="1">

| 種類 | 演算子 |
|---|---|
| 算術 | `+  -  *  /  %` |
| 比較 | `==  !=  <  >  <=  >=` |
| 論理 | `&&` (AND)、`||` (OR)、`!` (NOT) |
| 代入 | `=  +=  -=  *=  /=` |
| インクリメント | `++n` (前置)、`n++` (後置) |

</div>

---

## 5. 新潟大学での出題パターン

<div class="callout callout-examtip" markdown="1">

- `printf` の出力結果を手でトレースして書かせる問題
- `for` ループの変数 `i` の値の変化を追う
- `%d` と `%f` の違い、整数除算の落とし穴
- `if` のネスト（条件の読み取り）

</div>

<div class="callout callout-example" markdown="1">

**出力結果を書け:**

```c
for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
        if (i == j) printf("%d ", i);
    }
}
```

**答え:** `0 1 2`

</div>

---

## 6. 変数のスコープ（有効範囲）

スコープとは変数が「どこから見えるか」の範囲。新潟大学では「この変数の値は？」という穴埋め問題で必要になる。

<div class="callout callout-formula" markdown="1">

| 種類 | 宣言場所 | 有効範囲 |
|---|---|---|
| **ローカル変数** | 関数・ブロック内 `{}` | そのブロック内のみ |
| **グローバル変数** | 関数の外 | プログラム全体 |

</div>

```c
#include <stdio.h>

int g = 100;          // グローバル変数

void func() {
    int x = 10;       // ローカル変数 (func 内のみ有効)
    printf("%d %d\n", x, g);   // 10 100
}

int main() {
    int x = 20;       // main のローカル変数 (func の x とは別)
    func();
    printf("%d %d\n", x, g);   // 20 100
    return 0;
}
```

<div class="callout callout-warning" markdown="1">

- ブロック `{}` を出ると、その中で宣言したローカル変数は消える
- 同名の変数が外と内にある場合、**内側が優先**（シャドーイング）
- グローバル変数の多用は避ける（副作用のバグ原因になる）

</div>

<div class="callout callout-example" markdown="1">

**穴埋め問題（スコープ）:**

```c
int a = 5;
int main() {
    int a = 10;
    {
        int a = 20;
        printf("%d\n", a);   // (A)
    }
    printf("%d\n", a);       // (B)
    return 0;
}
```

**(A)** `20`（内側のブロックの `a`）  
**(B)** `10`（main の `a`。内側ブロックの `a` はすでに消えた）

</div>

---

## まとめ

| 節 | 要点 |
|---|---|
| データ型 | `int`・`double`・`char`。整数除算に注意 (`3/2=1`) |
| printf/scanf | 書式指定子 `%d %f %c %s`。scanf は `&` 必須 |
| 制御構造 | `if-else`・`for`・`while`・`switch`。`break` を忘れずに |
| 演算子 | 算術 / 比較 / 論理 / 代入。`%` は剰余 |
| 出題パターン | ループトレース・穴埋め・整数除算の落とし穴 |
| スコープ | ブロック内変数はブロック外から見えない。内側が優先 |

**次のステップ**: C02（配列・文字列）へ進む。配列操作は Tier 1 ★ 最頻出トピック。
