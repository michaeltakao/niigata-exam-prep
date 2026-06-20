---
title: C04 ポインタ・構造体
---

# C04 ポインタ・構造体

## 1. ポインタの基本概念

**ポインタ** = 変数のメモリアドレスを格納する変数。

::: formula
```c
int a = 5;
int *p = &a;    // p は a のアドレスを持つ

*p              // アドレス p が指す値 (間接参照) → 5
&a              // a のアドレス (番地)
```

| 演算子 | 意味 |
|---|---|
| `&変数` | 変数のアドレスを得る |
| `*ポインタ` | ポインタが指す先の値 (デリファレンス) |
:::

::: example
```c
int a = 10;
int *p = &a;

printf("%d\n", a);    // 10  (変数の値)
printf("%p\n", p);    // アドレス (例: 0x7fff5f...)
printf("%d\n", *p);   // 10  (ポインタ経由で同じ値)

*p = 20;              // ポインタ経由で書き換え
printf("%d\n", a);    // 20  (a も変わる)
```
:::

---

## 2. ポインタと配列

::: formula
配列名は先頭要素へのポインタと等価:

```c
int a[] = {1, 2, 3, 4, 5};
int *p = a;       // p = &a[0] と同じ

a[i]   ≡  *(a + i)   ≡  *(p + i)   ≡  p[i]
```
:::

::: example
```c
int a[] = {10, 20, 30};
int *p = a;

printf("%d\n", *p);       // 10
printf("%d\n", *(p+1));   // 20
printf("%d\n", p[2]);     // 30

p++;                      // p が a[1] を指すようになる
printf("%d\n", *p);       // 20
```
:::

::: warning
`a++` は**不可** (配列名はポインタ定数)。`p++` は可 (ポインタ変数)。
:::

---

## 3. ポインタを引数に渡す (値の交換)

::: example
```c
void swap(int *x, int *y) {
    int tmp = *x;
    *x = *y;
    *y = tmp;
}

int main() {
    int a = 3, b = 7;
    swap(&a, &b);
    printf("a=%d, b=%d\n", a, b);   // a=7, b=3
    return 0;
}
```
:::

---

## 4. 構造体

関連する変数をまとめる。

::: formula
```c
struct 構造体名 {
    型 メンバ1;
    型 メンバ2;
};
struct 構造体名 変数名;

// typedef で型名を簡略化
typedef struct {
    型 メンバ1;
    型 メンバ2;
} 型名;
型名 変数名;
```
:::

::: example
```c
typedef struct {
    char name[20];
    int  age;
    double score;
} Student;

int main() {
    Student s = {"Taro", 20, 85.5};
    printf("%s: %d歳, %.1f点\n", s.name, s.age, s.score);
    return 0;
}
```
:::

### 構造体のポインタ → `->` 演算子

```c
Student s = {"Hanako", 21, 92.0};
Student *p = &s;

printf("%s\n", p->name);    // Hanako  ((*p).name と同じ)
p->age = 22;
```

---

## 5. 動的メモリ確保 (参考)

```c
#include <stdlib.h>

int *a = (int*)malloc(n * sizeof(int));   // n 個の int を確保
if (a == NULL) { /* エラー処理 */ }
// ... 使用 ...
free(a);    // 必ず解放
```

---

## 6. 新潟大学での出題パターン

::: examtip
- `*p`、`&a`、`p++` の意味を問う穴埋め
- ポインタを使った `swap` 関数の実装
- 配列とポインタ演算の出力結果トレース
- 構造体のメンバアクセス (`s.age` vs `p->age`)
:::

::: example
**出力結果を書け:**

```c
int a[] = {3, 1, 4, 1, 5};
int *p = a + 2;
printf("%d %d %d\n", *p, *(p-1), *(p+1));
```

**答え:** `4 1 1`
:::
