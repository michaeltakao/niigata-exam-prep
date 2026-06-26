---
title: C03 関数・スコープ・再帰
---

# C03 関数・スコープ・再帰

## 1. 関数の定義

<div class="callout callout-formula" markdown="1">

```c
戻り値型 関数名(引数型 引数名, ...) {
    処理;
    return 戻り値;
}
```

- `void` は戻り値なし
- 引数がなければ `()` または `(void)` と書く

</div>

<div class="callout callout-example" markdown="1">

```c
// 2数の最大値を返す関数
int max(int a, int b) {
    if (a > b) return a;
    return b;
}

int main() {
    printf("%d\n", max(3, 7));   // 7
    return 0;
}
```

</div>

---

## 2. 値渡しと参照渡し (ポインタ渡し)

C言語の関数引数はデフォルトで**値渡し** (コピー)。  
関数内で変更しても呼び出し元の変数は変わらない。

<div class="callout callout-formula" markdown="1">

```c
// 値渡し — 呼び出し元は変わらない
void add1(int x) { x++; }

// ポインタ渡し — 呼び出し元が変わる
void add1_ptr(int *x) { (*x)++; }
```

</div>

<div class="callout callout-example" markdown="1">

```c
int a = 5;
add1(a);          // a はまだ 5
add1_ptr(&a);     // a は 6 になる
printf("%d\n", a);   // 6
```

</div>

---

## 3. スコープ (変数の有効範囲)

<div class="callout callout-formula" markdown="1">

| スコープ | 宣言場所 | 有効範囲 |
|---|---|---|
| **ローカル変数** | 関数・ブロック内 | 宣言したブロック内のみ |
| **グローバル変数** | 全関数の外 | プログラム全体 |

</div>

<div class="callout callout-warning" markdown="1">

- 同名のローカル変数がグローバル変数を隠す (シャドーイング)
- グローバル変数の多用は副作用を生む → 必要最小限に

</div>

---

## 4. 再帰関数 (最重要)

関数が自分自身を呼び出す。必ず**基底ケース** (終了条件) が必要。

<div class="callout callout-formula" markdown="1">

**階乗 $$n! = n \times (n-1)!$$, $$0! = 1$$**

```c
int factorial(int n) {
    if (n <= 0) return 1;      // 基底ケース
    return n * factorial(n-1); // 再帰呼び出し
}
```

**フィボナッチ数列 $$F(n) = F(n-1) + F(n-2)$$, $$F(0)=0$$, $$F(1)=1$$**

```c
int fib(int n) {
    if (n <= 0) return 0;
    if (n == 1) return 1;
    return fib(n-1) + fib(n-2);
}
```

</div>

<div class="callout callout-example" markdown="1">

```c
// factorial(5) の呼び出し展開
// factorial(5) = 5 * factorial(4)
//              = 5 * 4 * factorial(3)
//              = 5 * 4 * 3 * factorial(2)
//              = 5 * 4 * 3 * 2 * factorial(1)
//              = 5 * 4 * 3 * 2 * 1 * factorial(0)
//              = 5 * 4 * 3 * 2 * 1 * 1 = 120
```

</div>

<div class="callout callout-warning" markdown="1">

- 基底ケースがないと**無限再帰**でスタックオーバーフロー
- `fib(n)` のナイーブ再帰は計算量 $$O(2^n)$$ — 大きな `n` では遅い

</div>

---

## 5. 関数プロトタイプ宣言

`main` より後に関数を定義する場合、前方宣言が必要。

```c
int max(int a, int b);  // プロトタイプ宣言

int main() {
    printf("%d\n", max(3, 7));
    return 0;
}

int max(int a, int b) {  // 実装
    return (a > b) ? a : b;
}
```

---

## 6. 新潟大学での出題パターン

<div class="callout callout-examtip" markdown="1">

- 再帰関数の実行結果トレース (特に階乗・フィボナッチ)
- `factorial(n)` の実行回数を答えさせる
- 値渡しとポインタ渡しの違いを穴埋めで問う
- 関数を定義して「○○を実装せよ」 (GCD, 配列の最大値など)

</div>

<div class="callout callout-example" markdown="1">

**出力結果を書け:**

```c
int f(int n) {
    if (n == 0) return 0;
    return f(n-1) + n;
}
int main() {
    printf("%d\n", f(5));
    return 0;
}
```

**答え:** `15` (1+2+3+4+5)

</div>
