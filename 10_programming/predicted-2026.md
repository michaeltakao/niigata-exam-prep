---
title: C言語 予測問題 2026
date: 2026-06-19
---

# C言語 予測問題 2026

Tier 1 ★ トピックを中心に2026年度出題を予測した。

---

## 予測問題 1 — 出力結果を答えよ (ループ)

```c
#include <stdio.h>
int main() {
    int s = 0;
    for (int i = 1; i <= 5; i++) {
        if (i % 2 == 1) s += i;
    }
    printf("%d\n", s);
    return 0;
}
```

<details>
<summary>✅ 解答を見る</summary>

奇数の和: 1 + 3 + 5 = **9**
</details>

---

## 予測問題 2 — 穴埋め (バブルソート)

次のプログラムは配列を昇順ソートする。`(A)`, `(B)`, `(C)` を埋めよ。

```c
void bubble_sort(int a[], int n) {
    for (int i = 0; i < n-1; i++) {
        for (int j = 0; j < (A); j++) {
            if (a[j] (B) a[j+1]) {
                int tmp = a[j];
                a[j]   = (C);
                a[j+1] = tmp;
            }
        }
    }
}
```

<details>
<summary>✅ 解答を見る</summary>

**(A)** `n-1-i`  
**(B)** `>`  
**(C)** `a[j+1]`
</details>

---

## 予測問題 3 — 関数実装 (最大公約数)

ユークリッドの互除法で GCD を求める関数を実装せよ。

```c
int gcd(int a, int b) {
    // ここを実装
}
```

<details>
<summary>✅ 解答を見る</summary>

```c
int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}
```

例: `gcd(12, 8)` → `gcd(8, 4)` → `gcd(4, 0)` → `4`
</details>

---

## 予測問題 4 — 再帰関数のトレース

次の関数 `f(4)` の戻り値を答えよ。

```c
int f(int n) {
    if (n <= 1) return 1;
    return f(n-1) + f(n-2);
}
```

<details>
<summary>✅ 解答を見る</summary>

フィボナッチ数列: `f(0)=1, f(1)=1, f(2)=2, f(3)=3, f(4)=5`

**答え: 5**
</details>

---

## 予測問題 5 — ポインタと配列

```c
int a[] = {10, 20, 30, 40, 50};
int *p = a + 1;
printf("%d %d %d\n", *p, *(p+2), p[-1]);
```

出力結果を答えよ。

<details>
<summary>✅ 解答を見る</summary>

- `*p` = `a[1]` = **20**
- `*(p+2)` = `a[3]` = **40**
- `p[-1]` = `*(p-1)` = `a[0]` = **10**

**答え: `20 40 10`**
</details>

---

## 予測問題 6 — 文字列処理

文字列 `s` を逆順にする関数を実装せよ。

```c
#include <string.h>
void reverse(char s[]) {
    // ここを実装
}
```

<details>
<summary>✅ 解答を見る</summary>

**方法A — インデックス版（基本）:**

```c
void reverse(char s[]) {
    int n = strlen(s);
    for (int i = 0; i < n / 2; i++) {
        char tmp = s[i];
        s[i]     = s[n - 1 - i];
        s[n-1-i] = tmp;
    }
}
```

**方法B — ポインタ版（応用）:**

```c
void reverse_ptr(char *s) {
    char *left  = s;
    char *right = s + strlen(s) - 1;
    while (left < right) {
        char tmp = *left;
        *left++  = *right;
        *right-- = tmp;
    }
}
```

**トレース例**: `"hello"` の場合  
→ `h↔o`, `e↔l`, `l` は中央なのでスキップ  
→ `"olleh"`

**ポイント**: `left < right` の条件が重要。`<=` にすると中央文字が2回スワップされて元に戻ってしまう。
</details>
