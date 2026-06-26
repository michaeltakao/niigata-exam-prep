---
title: "L07 関数 — コードを部品に分ける"
---

# L07 関数 — コードを部品に分ける

---

## 1. コンセプト概要

**関数（function）** とは、名前のついた「処理のまとまり」です。  
同じ処理を何度も書かずに、名前を呼ぶだけで実行できます。

C言語のプログラムは必ず `main()` という関数から始まります。  
あなたはすでに関数を使っています — `printf()` も `scanf()` も「関数」です。

---

## 2. なぜ必要か

次の問題を考えてください:

```c
// 関数を使わない場合 — 同じコードが3回登場する
int a = 3, b = 5;
int sum1 = a + b;
printf("合計: %d\n", sum1);

int c = 10, d = 20;
int sum2 = c + d;
printf("合計: %d\n", sum2);

int e = 7, f = 2;
int sum3 = e + f;
printf("合計: %d\n", sum3);
```

同じ「足し算して表示する」処理が3回書かれています。  
バグがあったとき、3か所全部直さないといけません。

**関数を使うと:**

```c
void print_sum(int x, int y) {
    printf("合計: %d\n", x + y);
}

int main() {
    print_sum(3, 5);   // 1行で済む
    print_sum(10, 20);
    print_sum(7, 2);
    return 0;
}
```

一か所直すだけで全部直ります。これが関数の力です。

---

## 3. 現実世界のアナロジー

**関数 ≒ 家電製品のボタン**

電子レンジの「あたため」ボタンを押すと:
- 内部で「温度センサー確認 → ヒーター起動 → タイマー設定 → ...」が実行される
- あなたはその中身を知らなくてもボタン1つで使える

関数も同じです:
- `printf("%d\n", 42)` を呼ぶとき、内部実装を知らなくていい
- 「何を渡すか（引数）」と「何が返ってくるか（戻り値）」だけわかればいい

**別のアナロジー: レシピカード**

- 「から揚げの作り方」というカードを1枚書く（= 関数定義）
- 「から揚げを作って」と呼ぶだけで毎回使える（= 関数呼び出し）
- 材料（引数）を変えると結果（戻り値）が変わる

---

## 4. 構文説明

### 関数の解剖図

```
  ┌── 戻り値の型 ─┐  ┌── 関数名 ──┐  ┌──── 引数リスト ────┐
     int           add    (int a, int b)
  {
      int result = a + b;    ← ローカル変数（この関数内だけ有効）
      return result;         ← 戻り値（呼び出し元に返す値）
  }
```

### 4種類の関数パターン

**パターン1: 引数あり、戻り値あり（最も一般的）**
```c
int add(int a, int b) {
    return a + b;
}
// 使い方:
int result = add(3, 4);   // result = 7
```

**パターン2: 引数あり、戻り値なし（void）**
```c
void print_hello(char name[]) {
    printf("こんにちは、%s！\n", name);
}
// 使い方:
print_hello("田中");   // 戻り値を受け取らない
```

**パターン3: 引数なし、戻り値あり**
```c
int get_fixed_value(void) {
    return 42;
}
// 使い方:
int v = get_fixed_value();
```

**パターン4: 引数なし、戻り値なし**
```c
void greet(void) {
    printf("Hello!\n");
}
// 使い方:
greet();
```

### プロトタイプ宣言（前方宣言）

関数を `main()` の後に定義する場合、先に「こういう関数が存在する」と宣言が必要です:

```c
#include <stdio.h>

int add(int a, int b);   // ← プロトタイプ宣言（セミコロンで終わる）

int main() {
    int result = add(3, 4);
    printf("%d\n", result);
    return 0;
}

int add(int a, int b) {   // ← 実際の定義
    return a + b;
}
```

---

## 5. ステップ実行トレース

次のプログラムを1行ずつ追います:

```c
#include <stdio.h>

int add(int a, int b) {
    int result = a + b;
    return result;
}

int max(int x, int y) {
    if (x > y) return x;
    return y;
}

int main() {
    int p = add(3, 4);
    int q = add(10, p);
    int m = max(p, q);
    printf("p=%d q=%d m=%d\n", p, q, m);
    return 0;
}
```

**コールスタック（呼び出し順）トレース:**

```
ステップ1: main() が起動
  main の変数: p=?, q=?, m=?（まだ未定義）

ステップ2: add(3, 4) を呼び出す
  ┌─────────────────────────────┐
  │ add が起動                  │
  │   a = 3, b = 4（引数コピー）│
  │   result = 3 + 4 = 7        │
  │   return 7                  │
  └─────────────────────────────┘
  → add から戻る、main に 7 が返る
  main: p = 7

ステップ3: add(10, 7) を呼び出す
  ┌─────────────────────────────┐
  │ add が起動                  │
  │   a = 10, b = 7（p の値）   │
  │   result = 10 + 7 = 17      │
  │   return 17                 │
  └─────────────────────────────┘
  → main に 17 が返る
  main: q = 17

ステップ4: max(7, 17) を呼び出す
  ┌─────────────────────────────┐
  │ max が起動                  │
  │   x = 7, y = 17             │
  │   7 > 17 は偽 → return y   │
  │   return 17                 │
  └─────────────────────────────┘
  → main に 17 が返る
  main: m = 17

ステップ5: printf
  出力: p=7 q=17 m=17
```

**変数トレース表:**

| ステップ | 関数 | a/x | b/y | result | main:p | main:q | main:m |
|---|---|---|---|---|---|---|---|
| 初期 | main | — | — | — | ? | ? | ? |
| add(3,4) | add | 3 | 4 | 7 | — | — | — |
| 戻り | main | — | — | — | 7 | ? | ? |
| add(10,7) | add | 10 | 7 | 17 | — | — | — |
| 戻り | main | — | — | — | 7 | 17 | ? |
| max(7,17) | max | 7 | 17 | — | — | — | — |
| 戻り | main | — | — | — | 7 | 17 | 17 |

**出力:** `p=7 q=17 m=17`

---

## 6. 視覚的メモリ図

### スコープの可視化（ローカル変数の寿命）

```
時間の流れ →→→→→→→→→→→→→→→→→→→→→→→→→→

main() が実行中:
  ┌────────────────────────────────────────────┐
  │ main のメモリ: p, q, m                      │
  │                                            │
  │    add(3,4) が呼ばれた間だけ存在:           │
  │    ┌─────────────────────────┐             │
  │    │ add のメモリ: a, b, result│            │
  │    │ ← add が return すると消える →         │
  │    └─────────────────────────┘             │
  │                                            │
  └────────────────────────────────────────────┘
```

**重要:** `add()` の中の変数 `a`, `b`, `result` は `add()` が終わったら消えます。  
`main()` から `result` にアクセスしようとするのは誤りです。

### 値渡し（pass by value）の図解

```c
int double_it(int n) {
    n = n * 2;    // n は引数のコピー
    return n;
}

int main() {
    int x = 5;
    int result = double_it(x);
    // x はまだ 5！（n が変わっても x は変わらない）
}
```

```
main のメモリ:          double_it のメモリ:
┌────────┐              ┌───────────────┐
│ x = 5  │ → コピー →  │ n = 5         │
└────────┘              │ n = 10 (変更) │
   変わらない！          └───────────────┘
                             ↓ return 10
```

---

## 7. よくある間違い

### 間違い1: int関数で return を忘れる

```c
// ❌ 間違い
int add(int a, int b) {
    int result = a + b;
    // return を書き忘れた！
}

// ✅ 正しい
int add(int a, int b) {
    int result = a + b;
    return result;
}
```

`void` 関数は return なしでOKですが、`int` 関数は必ず `return 値;` が必要です。

### 間違い2: 引数を変えても呼び出し元は変わらない

```c
// ❌ こうなると思っている
void add_ten(int x) {
    x = x + 10;   // x を変えても main の変数は変わらない！
}

int main() {
    int a = 5;
    add_ten(a);
    printf("%d\n", a);   // 5 が出力される（15 にはならない）
}
```

引数は「コピー」が渡されます。元の変数を変えたい場合はポインタが必要（L08参照）。

### 間違い3: ローカル変数の住所を返す

```c
// ❌ 危険！
int* bad_function(void) {
    int x = 42;
    return &x;   // x は関数終了後に消える → ダングリングポインタ
}
```

関数が終わると、その関数のローカル変数は消えます。アドレスを返しても、そのメモリはもう無効です。

### 間違い4: 関数を定義前に使う（プロトタイプなし）

```c
// ❌ エラー
int main() {
    int r = add(3, 4);   // add がまだ定義されていない!
}

int add(int a, int b) { return a + b; }
```

```c
// ✅ 正しい（プロトタイプを先に書く）
int add(int a, int b);   // プロトタイプ

int main() {
    int r = add(3, 4);   // OK
}

int add(int a, int b) { return a + b; }
```

### 間違い5: 再帰で基底ケースを忘れる

```c
// ❌ 無限再帰（スタックオーバーフロー）
int factorial(int n) {
    return n * factorial(n - 1);   // 止まらない！
}

// ✅ 基底ケースが必要
int factorial(int n) {
    if (n <= 1) return 1;           // 基底ケース
    return n * factorial(n - 1);
}
```

---

## 8. ミニクイズ

**Q1.** 次の関数の戻り値の型は何ですか?

```c
void say_hi(void) { printf("Hi!\n"); }
```

<details><summary>答え</summary>

`void` — 戻り値なし。`int r = say_hi();` とは書けません。
</details>

---

**Q2.** 次のプログラムの出力は?

```c
int f(int x) { x = x + 1; return x; }
int main() {
    int a = 5;
    int b = f(a);
    printf("%d %d\n", a, b);
}
```

<details><summary>答え</summary>

`5 6` — `a` は変わらない（値渡し）。`f()` の中で `x` が 6 になるが、`a` は 5 のまま。`b` には return された 6 が入る。
</details>

---

**Q3.** プロトタイプ宣言の正しい書き方は?

<details><summary>答え</summary>

関数定義の先頭だけをコピーして **セミコロン** をつける:
```c
int add(int a, int b);   // ← セミコロン必須
```
</details>

---

**Q4.** `void` 関数の中に `return;`（値なし）と書くことはできますか?

<details><summary>答え</summary>

できます。`return;` と書くと、その時点で関数を終了して呼び出し元に戻ります。
```c
void check(int x) {
    if (x < 0) return;   // 負なら即座に終了
    printf("%d\n", x);
}
```
</details>

---

**Q5.** 次の関数 `triple(4)` の戻り値は?

```c
int triple(int n) { return n * 3; }
```

<details><summary>答え</summary>

`12` — `4 * 3 = 12`
</details>

---

## 9. 例題

### 例題1: 階乗を求める関数（factorial）

```c
#include <stdio.h>

int factorial(int n) {
    if (n <= 1) return 1;        // 基底ケース: 0! = 1! = 1
    return n * factorial(n - 1); // 再帰ステップ
}

int main() {
    printf("4! = %d\n", factorial(4));  // 24
    printf("5! = %d\n", factorial(5));  // 120
    return 0;
}
```

**factorial(4) のトレース:**

```
factorial(4)
  → 4 * factorial(3)
         → 3 * factorial(2)
                → 2 * factorial(1)
                       → return 1
                  → 2 * 1 = 2
           → 3 * 2 = 6
    → 4 * 6 = 24
```

### 例題2: 素数判定関数

```c
#include <stdio.h>

int is_prime(int n) {
    if (n < 2) return 0;         // 2未満は素数でない
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) return 0; // 割り切れたら素数でない
    }
    return 1;                    // 割り切れなかった = 素数
}

int main() {
    for (int i = 2; i <= 20; i++) {
        if (is_prime(i)) printf("%d ", i);
    }
    printf("\n");
    // 出力: 2 3 5 7 11 13 17 19
    return 0;
}
```

**設計ポイント:** `i * i <= n` の条件は「√n まで調べれば十分」という数学的根拠から。

### 例題3: 配列の平均を求める関数

```c
#include <stdio.h>

double average(int arr[], int n) {
    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += arr[i];
    }
    return (double)sum / n;   // int/int にならないようキャスト
}

int main() {
    int data[] = {10, 20, 30, 40, 50};
    double avg = average(data, 5);
    printf("平均: %.1f\n", avg);  // 平均: 30.0
    return 0;
}
```

**注意:** 配列は「先頭アドレスのコピー」が渡されます（実質的な参照渡し）。  
関数内で `arr[i]` を変更すると、呼び出し元の配列も変わります（値渡しの例外的動作）。

---

## 10. 新潟大学試験との関連

**出題頻度:** Tier 1 ★★★ — R7, R8 で確認

**出題パターン:**

| パターン | 具体例 |
|---|---|
| 関数の出力を答えよ | `int f(int n) {...}` を与えて `f(5)` の結果を問う |
| 空欄を埋めよ | 関数の `return` 文や引数部分を空欄にする |
| 関数を実装せよ | 「配列の最大値を返す `max_val()` 関数を書け」 |
| 再帰のトレース | `factorial(4)` の呼び出し過程を示せ（L11で詳述） |

**試験直前チェックリスト:**
- [ ] 戻り値の型と `return` 文が一致しているか確認できる
- [ ] void関数と int関数の使い分けがわかる
- [ ] 値渡しで呼び出し元が変わらないことを説明できる
- [ ] 配列が実質的に参照渡しになることを知っている
- [ ] 再帰の基底ケースを書くことができる

**典型的な試験問題（練習）:**

```c
// Q: この関数は何をするか説明し、f(6) の値を答えよ。
int f(int n) {
    if (n == 0) return 0;
    return n + f(n - 1);
}
```

答え: `f(n) = 0 + 1 + 2 + ... + n`（1からnまでの和）。`f(6) = 21`。
