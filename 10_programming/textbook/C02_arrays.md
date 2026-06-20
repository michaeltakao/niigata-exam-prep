---
title: C02 配列・文字列
---

# C02 配列・文字列

## 1. 配列の基本

::: formula
```c
型 配列名[要素数];
型 配列名[要素数] = {値1, 値2, ...};
```

- インデックスは **0 始まり**: `a[0]`, `a[1]`, ..., `a[n-1]`
- 配列の範囲外アクセスは未定義動作 (バグの元)
:::

::: example
```c
int a[5] = {10, 20, 30, 40, 50};
printf("%d\n", a[0]);    // 10
printf("%d\n", a[4]);    // 50

// 全要素の和
int sum = 0;
for (int i = 0; i < 5; i++) {
    sum += a[i];
}
printf("sum = %d\n", sum);   // 150
```
:::

---

## 2. バブルソート (最重要)

::: formula
隣り合う要素を比較・交換を繰り返してソートする。  
計算量: $O(n^2)$

```c
for (int i = 0; i < n-1; i++) {
    for (int j = 0; j < n-1-i; j++) {
        if (a[j] > a[j+1]) {       // 降順にしたいなら < に変える
            int tmp = a[j];
            a[j] = a[j+1];
            a[j+1] = tmp;
        }
    }
}
```
:::

::: example
`{5, 3, 1, 4, 2}` を昇順ソート:

パス1後: `{3, 1, 4, 2, 5}`  
パス2後: `{1, 3, 2, 4, 5}`  
...最終: `{1, 2, 3, 4, 5}`
:::

---

## 3. 2次元配列

```c
int m[3][3] = {
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9}
};
printf("%d\n", m[1][2]);    // 6 (2行目、3列目)
```

::: example
**行列の対角成分の和 (トレース):**

```c
int trace = 0;
for (int i = 0; i < 3; i++) {
    trace += m[i][i];
}
// trace = 1 + 5 + 9 = 15
```
:::

---

## 4. 文字列

C言語の文字列は `char` 配列 + 末尾の `\0` (ヌル文字)。

::: formula
```c
char s[] = "hello";    // {'h','e','l','l','o','\0'} として格納
```

| 関数 | 説明 |
|---|---|
| `strlen(s)` | 文字列の長さ (`\0` 除く) |
| `strcpy(dst, src)` | 文字列のコピー |
| `strcat(dst, src)` | 文字列の連結 |
| `strcmp(s1, s2)` | 比較 (等しければ 0) |

**要** `#include <string.h>`
:::

::: example
```c
#include <stdio.h>
#include <string.h>

int main() {
    char s[] = "Hello";
    printf("%zu\n", strlen(s));      // 5
    printf("%c\n", s[0]);            // H
    s[0] = 'h';
    printf("%s\n", s);               // hello
    return 0;
}
```
:::

::: warning
- `s1 == s2` では文字列比較できない (アドレス比較になる)。必ず `strcmp` を使う
- `strcpy(dst, src)` で `dst` のサイズが足りないとバッファオーバーフロー
:::

---

## 5. 新潟大学での出題パターン

::: examtip
- 配列の内容をトレースして「実行結果を書け」
- ソートアルゴリズムの穴埋め (`tmp` の宣言位置、条件式)
- `strlen` の返り値の型 (`size_t`、つまり符号なし整数)
- 文字列と `for` ループを組み合わせた処理
:::

::: example
**出力結果を書け:**

```c
char s[] = "ABCDE";
int n = strlen(s);
for (int i = 0; i < n/2; i++) {
    char tmp = s[i];
    s[i] = s[n-1-i];
    s[n-1-i] = tmp;
}
printf("%s\n", s);
```

**答え:** `EDCBA` (文字列の逆順)
:::
