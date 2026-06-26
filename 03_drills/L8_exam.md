---
title: "L8 入試形式 総合問題 — 類題ドリル (30問)"
---

# L8 入試形式 総合問題 — 類題ドリル (30問)

> 実際の新潟大学入試スタイルに合わせた統合問題
> 各Hardは「実際の大問1つ」に相当する規模

---

## ★ Easy（単一トピック・ウォームアップ）

### E1. ループトレース

```c
int x = 1;
for (int i = 0; i < 4; i++) {
    x = x * 2 + i;
}
printf("%d\n", x);
```

出力を答えよ。

💡 **Hint**: iが0,1,2,3と変化する。変数表を書くこと。

✅ **Solution**:

| i | x（更新前） | x = x*2+i |
|---|---|---|
| 0 | 1 | 2 |
| 1 | 2 | 5 |
| 2 | 5 | 12 |
| 3 | 12 | 27 |

出力: `27`

📝 **Explanation**: ループトレース問題では必ず変数表を作る。各反復でiとxの値を丁寧に追う。x=1→2→5→12→27。

---

### E2. 配列トレース

```c
int a[] = {2, 4, 6, 8, 10};
int s = 0;
for (int i = 0; i < 5; i += 2) {
    s += a[i];
}
printf("%d\n", s);
```

出力を答えよ。

💡 **Hint**: `i += 2`で偶数インデックスのみアクセスする。

✅ **Solution**: `i=0,2,4`の要素: a[0]=2, a[2]=6, a[4]=10。合計=18。

出力: `18`

📝 **Explanation**: `i += 2`はi=0,2,4と2ずつ増える（3回実行）。インデックスの飛び方を正確に読む。i=3でのアクセスはない。

---

### E3. 関数トレース

```c
int f(int n) {
    if (n <= 0) return 0;
    return f(n - 2) + 1;
}
printf("%d\n", f(6));
printf("%d\n", f(5));
```

出力を答えよ。

💡 **Hint**: 再帰ごとにnが2減る。n<=0で0を返す。

✅ **Solution**:
```
f(6) = f(4)+1 = f(2)+2 = f(0)+3 = 0+3 = 3
f(5) = f(3)+1 = f(1)+2 = f(-1)+3 = 0+3 = 3
```

出力:
```
3
3
```

📝 **Explanation**: f(n)はn/2（切り捨て）を返す（偶数の場合）。この関数は「nを0になるまで2ずつ減らした回数」を数える。

---

### E4. ポインタトレース

```c
int a[] = {5, 10, 15, 20};
int *p = a + 1;
printf("%d\n", *p);
printf("%d\n", *(p + 1));
printf("%d\n", p[-1]);
```

出力を答えよ。

💡 **Hint**: p=a[1]を起点に計算する。

✅ **Solution**:
```
10
15
5
```

📝 **Explanation**: p=&a[1]=10。*(p+1)=a[2]=15。p[-1]=*(p-1)=a[0]=5。ポインタ算術はa[]の範囲内なら有効。

---

### E5. 文字列トレース

```c
#include <string.h>
char s[] = "Niigata";
printf("%zu\n", strlen(s));
printf("%c\n", s[strlen(s) - 1]);
s[0] = 'n';
printf("%s\n", s);
```

出力を答えよ。

💡 **Hint**: "Niigata"は7文字。末尾はインデックス6。

✅ **Solution**:
```
7
a
niigata
```

📝 **Explanation**: strlen("Niigata")=7。s[6]='a'が末尾文字。s[0]を'n'（小文字）に変えると"niigata"に変わる。

---

### E6. 穴埋め（ループで偶数のみ表示）

```c
for (int i = 1; i <= 10; i++) {
    if (i (A) 2 (B) 0) {
        printf("%d ", i);
    }
}
```

出力が`2 4 6 8 10`になるよう空欄を埋めよ。

💡 **Hint**: 偶数判定は`%`（剰余）を使う。

✅ **Solution**: `(A) %`, `(B) ==`

📝 **Explanation**: `i % 2 == 0`が偶数判定の標準パターン。剰余が0なら2で割り切れる（偶数）。

---

### E7. 穴埋め（最大値）

```c
int a[] = {7, 2, 9, 4, 6};
int max = (A);
for (int i = 1; i < 5; i++) {
    if (a[i] > max) max = (B);
}
printf("%d\n", max);
```

空欄を埋め、出力を答えよ。

💡 **Hint**: 最初の要素を初期最大値として使う慣例。

✅ **Solution**: `(A) a[0]`, `(B) a[i]`

出力: `9`

📝 **Explanation**: `max=a[0]=7`から始め、a[1]=2（小），a[2]=9（大→max=9），a[3]=4（小），a[4]=6（小）。最終max=9。

---

### E8. 穴埋め（関数呼び出し）

```c
int multiply(int x, int y) {
    return (A);
}
int main() {
    int result = multiply(6, (B));
    printf("%d\n", result);  // 42を出力したい
}
```

空欄を埋めよ。

💡 **Hint**: 6 × ? = 42。

✅ **Solution**: `(A) x * y`, `(B) 7`

📝 **Explanation**: `multiply(6, 7) = 6*7 = 42`。関数の実装`x*y`と引数の値`7`を両方埋める。

---

### E9. 出力が正しいか判定 (1)

「次のコードが`1 2 3 4 5`を出力する」という主張は正しいか？

```c
for (int i = 5; i >= 1; i--) {
    printf("%d ", i);
}
```

💡 **Hint**: ループの開始値と条件を確認する。

✅ **Solution**: **誤り**。実際の出力は`5 4 3 2 1 `（逆順）。

📝 **Explanation**: `i=5`から始まり`i--`で減少する。条件`i>=1`は1になるまで継続。昇順にしたければ`i=1; i<=5; i++`にすべき。ループの方向を常に確認する。

---

### E10. 出力が正しいか判定 (2)

「次のコードが`strcmp("abc","abc")`で1を返す」という主張は正しいか？

```c
#include <string.h>
int r = strcmp("abc", "abc");
if (r == 1) printf("equal\n");
```

💡 **Hint**: `strcmp`が返す値は「0」（等しい場合）。

✅ **Solution**: **誤り**。`strcmp("abc","abc")`は`0`を返す。等しい場合は0、第1引数が辞書順で小さければ負、大きければ正。1を返すとは限らない（処理系依存）。

正しい書き方: `if (r == 0) printf("equal\n");`

📝 **Explanation**: strcmp仕様の典型的な誤解。「等しければ0」は絶対に覚える。「等しければ1」と誤解している受験者が多い。

---

## ★★ Medium（複数トピック・2〜3パート）

### M1. ループ＋条件（2パート）

```c
int count = 0;
for (int i = 1; i <= 20; i++) {
    if (i % 3 == 0 && i % 5 == 0) count++;
    else if (i % 3 == 0) count += 2;
}
printf("%d\n", count);
```

**(A)** 出力を答えよ。

**(B)** 変数`count`を使わず、15の倍数の個数だけを数えるよう修正せよ。

💡 **Hint**: 1〜20で3の倍数かつ5の倍数（=15の倍数）は15のみ。

✅ **Solution**:
**(A)** 3の倍数: {3,6,9,12,15,18}=6個、ただし15は「かつ5の倍数」なのでcount+=1（else ifに入らない）。
- i=3: else if → count=2
- i=6: else if → count=4
- i=9: else if → count=6
- i=12: else if → count=8
- i=15: if → count=9
- i=18: else if → count=11

出力: `11`

**(B)**
```c
int cnt15 = 0;
for (int i = 1; i <= 20; i++) {
    if (i % 15 == 0) cnt15++;
}
printf("%d\n", cnt15);  // 1
```

📝 **Explanation**: 複合条件の評価順を丁寧に追う。`&&`の方がelse ifより優先評価されるため15はcountに1を加えるのみ。修正版は`i%15==0`で直接15の倍数を検出。

---

### M2. 配列＋関数（2パート）

```c
int contains(int a[], int n, int val) {
    for (int i = 0; i < n; i++)
        if (a[i] == val) return 1;
    return 0;
}
int main() {
    int a[] = {1, 3, 5, 7, 9};
    printf("%d\n", contains(a, 5, 5));
    printf("%d\n", contains(a, 5, 4));
}
```

**(A)** 出力を答えよ。

**(B)** `contains`を使って配列aとbの共通要素を全て表示する関数を書け。

💡 **Hint**: B部分は2重ループかcontainsを使ってbの各要素がaに含まれるか確認する。

✅ **Solution**:
**(A)**
```
1
0
```

**(B)**
```c
void common(int a[], int na, int b[], int nb) {
    for (int i = 0; i < nb; i++) {
        if (contains(a, na, b[i])) {
            printf("%d ", b[i]);
        }
    }
    printf("\n");
}
```

📝 **Explanation**: `contains`は値の存在確認のためのユーティリティ関数。`common`はbの各要素についてaに含まれるかチェックする。O(na×nb)の実装。

---

### M3. 文字列＋ループ（2パート）

**(A)** 出力を答えよ。

```c
char s[] = "Hello World";
int vowels = 0;
for (int i = 0; s[i] != '\0'; i++) {
    char c = s[i];
    if (c=='a'||c=='e'||c=='i'||c=='o'||c=='u'||
        c=='A'||c=='E'||c=='I'||c=='O'||c=='U')
        vowels++;
}
printf("%d\n", vowels);
```

**(B)** 同じ文字列のアルファベット文字だけをカウントする`count_alpha`関数を実装せよ。

💡 **Hint**: アルファベット判定は`(c>='a'&&c<='z')||(c>='A'&&c<='Z')`。

✅ **Solution**:
**(A)** "Hello World"の母音: e, o, o = 3。出力: `3`

**(B)**
```c
int count_alpha(char s[]) {
    int count = 0;
    for (int i = 0; s[i] != '\0'; i++) {
        char c = s[i];
        if ((c>='a'&&c<='z')||(c>='A'&&c<='Z')) count++;
    }
    return count;
}
// count_alpha("Hello World") = 10 (スペース除く)
```

📝 **Explanation**: "Hello World"の母音はe(1),o(4),o(7)の3文字。スペースは母音でも子音でもない。アルファベット判定ではctype.hの`isalpha(c)`を使うことも多いが、比較演算子で自作することも可能。

---

### M4. トレース＋穴埋め＋実装（3パート）

```c
int mystery(int n) {
    int result = 0;
    while (n > 0) {
        result += n % 2;
        n /= 2;
    }
    return result;
}
```

**(A)** `mystery(13)`の値を答えよ（トレース必須）。
**(B)** この関数は何を計算しているか。
**(C)** 空欄を埋め、同じことをする再帰版を書け。

```c
int mystery_rec(int n) {
    if (n == 0) return (X);
    return (Y) + mystery_rec((Z));
}
```

💡 **Hint**: `n % 2`は2進数の1の位。`n / 2`は右シフト。

✅ **Solution**:
**(A)** トレース:

| n | n%2 | result | n/=2 |
|---|---|---|---|
| 13 | 1 | 1 | 6 |
| 6 | 0 | 1 | 3 |
| 3 | 1 | 2 | 1 |
| 1 | 1 | 3 | 0 |

**答え: 3**

**(B)** 整数nの **2進表現における1のビット数（popcount）** を計算する。

13 = 1101₂ → 1が3個

**(C)** `(X) 0`, `(Y) n % 2`, `(Z) n / 2`

📝 **Explanation**: `n%2`で最下位ビット取得、`n/2`で右シフト。13=1101₂に1が3個。再帰版は「最下位ビット + 残りのpopcount」という分解。

---

### M5. 穴埋め＋出力＋バグ修正（3パート）

```c
// バブルソートの実装
void sort(int a[], int n) {
    for (int i = 0; i < n-1; i++) {
        for (int j = 0; j < n-1-i; j++) {
            if (a[j] > a[j+1]) {
                int tmp = a[j];
                a[j] = a[j+1];
                a[j+1] = (A);
            }
        }
    }
}
```

**(A)** 空欄を埋めよ。

**(B)** `a[]={4,2,7,1,5}`を渡した後の配列を答えよ。

**(C)** 降順ソートに変えるにはどこを変更すればよいか。

💡 **Hint**: (A)はtmpを使う。(C)は比較演算子を変える。

✅ **Solution**:
**(A)** `tmp`

**(B)** `{1, 2, 4, 5, 7}`

**(C)** `a[j] > a[j+1]`を`a[j] < a[j+1]`に変更する。

📝 **Explanation**: tmpを使ったスワップの(A)はtmpのみ。昇順`>`を降順`<`に変えると大きい要素が先頭に向かって動く。

---

### M6. 再帰＋穴埋め＋トレース（3パート）

```c
int power(int base, int exp) {
    if ((A)) return 1;
    if (exp % 2 == 0) {
        int half = power(base, (B));
        return half * half;
    }
    return base * power(base, (C));
}
```

**(A)** 空欄を埋めよ。
**(B)** `power(2, 8)`の呼び出し回数を数えよ（効率的な版）。
**(C)** `power(3, 5)`の値を答えよ。

💡 **Hint**: 偶数乗は`(base^(exp/2))^2`で半分の計算量になる。

✅ **Solution**:
**(A)** `(A) exp == 0`, `(B) exp/2`, `(C) exp-1`

**(B)** `power(2,8)→power(2,4)→power(2,2)→power(2,1)→power(2,0)` = 5回呼び出し。

**(C)** `power(3,5) = 3*power(3,4) = 3*(power(3,2))^2 = 3*(3*3)^2 = 3*81 = 243`

📝 **Explanation**: 二分冪乗法（fast exponentiation）はO(log n)。通常のexp-1再帰はO(n)。evenの場合のhalf*halfがポイント。

---

### M7. バグ修正（配列操作）

以下のコードにはバグが3つある。全て見つけて修正せよ。

```c
#include <stdio.h>
void print_array(int a, int n) {     // Bug 1
    for (int i = 1; i <= n; i++) {   // Bug 2
        printf("%d ", a[i]);
    }
}
int main() {
    int a[5] = {10, 20, 30, 40, 50};
    print_array(a, 5);
    printf("\n");
    printf("last: %d\n", a[5]);      // Bug 3
    return 0;
}
```

💡 **Hint**: 配列引数の型、ループの開始インデックス、配列の範囲外アクセスを確認。

✅ **Solution**:

| バグ | 問題箇所 | 修正 |
|---|---|---|
| Bug 1 | `int a` | `int a[]`（または`int *a`） |
| Bug 2 | `int i = 1; i <= n` | `int i = 0; i < n` |
| Bug 3 | `a[5]` | `a[4]`（サイズ5の配列の最大インデックスは4） |

修正後の出力: `10 20 30 40 50 \nlast: 50`

📝 **Explanation**: Bug1は配列を配列として渡していない型エラー。Bug2は1から始めるとa[0]を飛ばし、<=nで境界外にアクセスする。Bug3はサイズ5の配列a[]の有効インデックスは0〜4。

---

### M8. バグ修正（再帰の終了条件）

```c
int sum_to(int n) {
    return n + sum_to(n - 1);  // バグあり
}
int main() {
    printf("%d\n", sum_to(5));
}
```

**(A)** バグを修正せよ。
**(B)** 修正後の`sum_to(5)`の値を答えよ。

💡 **Hint**: 再帰には基底条件が必要。

✅ **Solution**:
**(A)**
```c
int sum_to(int n) {
    if (n <= 0) return 0;  // 追加
    return n + sum_to(n - 1);
}
```

**(B)** `sum_to(5) = 5+4+3+2+1+0 = 15`

📝 **Explanation**: 基底条件なしの再帰は無限に呼び出しが続きスタックオーバーフローで強制終了する。`n <= 0`の場合に0を返すことで正しく動作する。1+2+...+5 = n(n+1)/2 = 15。

---

### M9. バグ修正（ポインタ）

```c
void increment(int n) {   // バグあり
    n++;
}
int main() {
    int x = 10;
    increment(x);
    printf("%d\n", x);  // 11を期待しているが...
}
```

**(A)** 実際の出力を答えよ。
**(B)** `x`が11になるよう修正せよ。

💡 **Hint**: 整数は値渡しなので関数内の変更は元の変数に反映されない。

✅ **Solution**:
**(A)** 出力: `10`（xは変化しない）

**(B)**
```c
void increment(int *n) {
    (*n)++;
}
int main() {
    int x = 10;
    increment(&x);
    printf("%d\n", x);  // 11
}
```

📝 **Explanation**: intの値渡しでは`n++`はコピーを増やすだけ。`int *n`にして`&x`を渡すことでxを直接変更できる。`(*n)++`は`*n`を先に評価してからインクリメント。`*n++`は`*(n++)`となりポインタ自体を進めてしまう（罠）。

---

### M10. バグ修正（文字列）

```c
#include <stdio.h>
#include <string.h>

int main() {
    char s1[10] = "hello";
    char s2[10] = "world";
    
    // 文字列の結合を試みる
    s1 = s1 + s2;           // Bug A
    
    // 長さ確認
    int len = sizeof(s1);   // Bug B
    printf("len=%d\n", len);
    
    // 比較
    if (s1 == s2) {          // Bug C
        printf("equal\n");
    }
    return 0;
}
```

3つのバグを修正せよ。

💡 **Hint**: C言語では文字列は配列。+=演算子は文字列に使えない。

✅ **Solution**:
- **Bug A**: `s1 = s1 + s2` → `strcat(s1, s2)`
- **Bug B**: `sizeof(s1)` → `strlen(s1)`（sizeofは配列サイズ10を返す）
- **Bug C**: `s1 == s2` → `strcmp(s1, s2) == 0`

📝 **Explanation**: C言語で文字列操作には`string.h`の関数を使う。`s1+s2`はアドレス算術、`s1==s2`はアドレス比較、`sizeof`は型サイズ。`strcat`, `strlen`, `strcmp`が正しい文字列操作関数。

---

## ★★★ Hard — 入試規模の完全問題

### H1. ← R8模倣: ループ＋配列の総合問題

**次のプログラムについて以下の問いに答えよ。**

```c
#include <stdio.h>
int main() {
    int a[] = {3, 1, 4, 1, 5, 9, 2, 6};
    int n = 8;
    
    // Part A
    int sum = 0, max = a[0];
    for (int i = 0; i < n; i++) {
        sum += a[i];
        if (a[i] > max) max = a[i];
    }
    printf("sum=%d, max=%d\n", sum, max);
    
    // Part B
    int cnt = 0;
    for (int i = 0; i < n; i++) {
        if (a[i] % 2 == 1) cnt++;
    }
    printf("odd count=%d\n", cnt);
    
    // Part C — 穴埋め: 逆順に表示
    for (int i = (A); i (B) 0; i--) {
        printf("%d ", a[i]);
    }
    printf("\n");
    return 0;
}
```

**(1)** Part Aの出力を答えよ。
**(2)** Part Bの出力を答えよ。
**(3)** Part Cの空欄を埋めよ。
**(4)** 配列aを昇順に並べ替えるコードを追記せよ（バブルソート）。

💡 **Hint**: (1)要素を全部足し最大値を追う。(3)末尾インデックスから0まで。

✅ **Solution**:

**(1)** 3+1+4+1+5+9+2+6=31、max=9。出力: `sum=31, max=9`

**(2)** 奇数: 3,1,1,5,9 = 5個。出力: `odd count=5`

**(3)** `(A) n-1`, `(B) >=`

逆順出力: `6 2 9 5 1 4 1 3 `

**(4)**
```c
for (int i = 0; i < n-1; i++)
    for (int j = 0; j < n-1-i; j++)
        if (a[j] > a[j+1]) {
            int t=a[j]; a[j]=a[j+1]; a[j+1]=t;
        }
// 結果: {1,1,2,3,4,5,6,9}
```

📝 **Explanation**: 試験の大問は「トレース→穴埋め→実装」の3段構成が多い。(1)(2)でプログラムの動作理解、(3)で文法、(4)で実装力を問う。バブルソートはTier 1 ★の必須アルゴリズム。

---

### H2. ← R7模倣: 関数＋再帰の総合問題

**次のプログラムについて以下の問いに答えよ。**

```c
#include <stdio.h>

int f(int n) {
    if (n <= 0) return 0;
    if (n == 1) return 1;
    return f(n-1) + f(n-2);
}

int g(int a[], int n) {
    if (n == 0) return 0;
    return a[n-1] + g(a, n-1);
}
```

**(1)** `f(5)`の値を答え、呼び出しツリーの概略を示せ。
**(2)** `f(n)`は何を計算しているか。
**(3)** 次の空欄を埋めてf(n)の反復版を完成させよ。
```c
int f_iter(int n) {
    if (n <= 0) return 0;
    if (n == 1) return 1;
    int prev2 = 0, prev1 = 1, curr;
    for (int i = 2; i <= n; i++) {
        curr = (A);
        prev2 = (B);
        prev1 = (C);
    }
    return curr;
}
```
**(4)** `a[]={5,3,8,2,7}`, n=5として`g(a,5)`の値を答えよ。
**(5)** `g`関数が持つバグを一つ指摘せよ（n=0の時に注意）。

💡 **Hint**: f=フィボナッチ、g=配列の再帰的合計。

✅ **Solution**:

**(1)** f(5)=f(4)+f(3)=5+3=8。呼び出しツリー（主要ノードのみ）:
```
f(5) → f(4)+f(3)
f(4) → f(3)+f(2)
f(3) → f(2)+f(1)=2+1=3
f(2) → f(1)+f(0)=1+0=1
```
**答え: 8**

**(2)** フィボナッチ数列（f(0)=0, f(1)=1から始まる版）。

**(3)** `(A) prev1 + prev2`, `(B) prev1`, `(C) curr`

**(4)** g(a,5) = a[4]+g(a,4) = 7+(a[3]+g(a,3)) = 7+2+(a[2]+g(a,2)) = 7+2+8+(a[1]+g(a,1)) = 7+2+8+3+(a[0]+g(a,0)) = 7+2+8+3+5+0 = **25**

**(5)** n=0の時に返り値が0（`return 0`）なのは正しい。バグはない... 実際はバグなし。代わりに**n<0の場合の処理がない**（n=-1で無限再帰）ことを指摘できる。

📝 **Explanation**: 再帰の反復変換では「前の2値を保持しながら更新」するパターンが重要。curr=prev1+prev2、更新時はprev2←prev1←curr。O(n)かつO(1)空間で実装できる。

---

### H3. ← R6模倣: 文字列＋ポインタの総合問題

**次のプログラムについて以下の問いに答えよ。**

```c
#include <stdio.h>
#include <string.h>

void reverse(char *s) {
    char *left = s;
    char *right = s + strlen(s) - 1;
    while (left < right) {
        char tmp = *left;
        *left++ = *right;
        *right-- = tmp;
    }
}

int count_char(const char *s, char c) {
    int count = 0;
    while (*s) {
        if (*s == c) count++;
        s++;
    }
    return count;
}
```

**(1)** `reverse("hello")`を呼び出した後の文字列を答えよ（引数は`char s[]`として宣言したとする）。
**(2)** `*left++ = *right`の`++`は`left`と`*left`どちらに作用するか。
**(3)** `count_char("mississippi", 's')`の値を答えよ。
**(4)** `count_char`をポインタではなく配列インデックスで書き直せ。

💡 **Hint**: (2)後置++はデリファレンスの後に作用する。

✅ **Solution**:

**(1)** `"olleh"`

**(2)** `*left++ = *right`は `(*left) = *right; left++;` と等価。つまり`left`（ポインタ自体）に後置インクリメントが作用する（`*left`の値に作用するのではない）。

**(3)** "mississippi"の's': m-i-**s**-**s**-i-**s**-**s**-i-p-p-i → 4個。出力: `4`

**(4)**
```c
int count_char_idx(const char s[], char c) {
    int count = 0;
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] == c) count++;
    }
    return count;
}
```

📝 **Explanation**: `*left++ = *right`は後置++の優先順位の理解が鍵。先に`*left`に`*right`を代入してから`left`を進める。`*++left`だと先に進めてから代入する（別の動作）。mississippiの's'は4箇所。

---

### H4. ソート＋探索の複合問題

次の仕様に従ってプログラムを実装せよ。

**仕様**:
1. ユーザーが入力した5個の整数を配列に格納（`scanf`使用）
2. バブルソートで昇順に並べ替える
3. 並べ替え後の配列を表示する
4. 二分探索でキー値を探し、見つかればインデックス、見つからなければ-1を表示

```c
#include <stdio.h>

void bubble_sort(int a[], int n) { /* 実装せよ */ }
int binary_search(int a[], int n, int key) { /* 実装せよ */ }

int main() {
    int a[5], key;
    // 入力・ソート・表示・探索を実装せよ
}
```

💡 **Hint**: 二分探索はソート済み配列にのみ使える。midを計算してleft/rightを更新する。

✅ **Solution**:
```c
#include <stdio.h>

void bubble_sort(int a[], int n) {
    for (int i = 0; i < n-1; i++)
        for (int j = 0; j < n-1-i; j++)
            if (a[j] > a[j+1]) {
                int t=a[j]; a[j]=a[j+1]; a[j+1]=t;
            }
}

int binary_search(int a[], int n, int key) {
    int left = 0, right = n-1;
    while (left <= right) {
        int mid = (left + right) / 2;
        if (a[mid] == key) return mid;
        if (a[mid] < key) left = mid + 1;
        else right = mid - 1;
    }
    return -1;
}

int main() {
    int a[5], key;
    printf("5つの整数を入力: ");
    for (int i = 0; i < 5; i++) scanf("%d", &a[i]);
    bubble_sort(a, 5);
    printf("ソート後: ");
    for (int i = 0; i < 5; i++) printf("%d ", a[i]);
    printf("\n探索するキー: ");
    scanf("%d", &key);
    int idx = binary_search(a, 5, key);
    if (idx >= 0) printf("index=%d\n", idx);
    else printf("not found\n");
    return 0;
}
```

📝 **Explanation**: バブルソートO(n²)後に二分探索O(log n)を使う。二分探索はソート後にのみ適用可能。`(left+right)/2`のオーバーフローを防ぐには`left+(right-left)/2`がより堅牢。

---

### H5. 構造体＋関数（ミニデータベース）

```c
#include <stdio.h>
#define MAX 5

typedef struct {
    char name[20];
    int score;
} Student;

// (1) 最高スコアの学生を返す関数を実装せよ
Student find_best(Student db[], int n) {
    // 実装せよ
}

// (2) スコアが閾値以上の学生数を返す関数を実装せよ
int count_above(Student db[], int n, int threshold) {
    // 実装せよ
}

int main() {
    Student db[MAX] = {
        {"Alice", 85}, {"Bob", 72}, {"Carol", 91},
        {"Dave", 68}, {"Eve", 88}
    };
    Student best = find_best(db, MAX);
    printf("Best: %s (%d)\n", best.name, best.score);
    printf("Above 80: %d\n", count_above(db, MAX, 80));
    return 0;
}
```

**(1)(2)** を実装し、出力を答えよ。

💡 **Hint**: 構造体の最大値探索はintと同じロジック。比較するフィールドを指定するだけ。

✅ **Solution**:
```c
Student find_best(Student db[], int n) {
    Student best = db[0];
    for (int i = 1; i < n; i++) {
        if (db[i].score > best.score) best = db[i];
    }
    return best;
}

int count_above(Student db[], int n, int threshold) {
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (db[i].score >= threshold) count++;
    }
    return count;
}
```

出力:
```
Best: Carol (91)
Above 80: 3
```

📝 **Explanation**: 構造体は`db[i].score`でフィールドアクセス。`find_best`は最大スコアの構造体を返す。`count_above`は閾値以上の学生（Alice85, Carol91, Eve88）=3人。構造体の値渡しではコピーが発生する点に注意。

---

### H6. GCD＋LCM の実装と検証

**(1)** GCDをユークリッド互除法で実装せよ（再帰版）。
**(2)** LCMをGCDを使って実装せよ。
**(3)** 以下の全てについてGCDとLCMを計算し答えよ:
   - (48, 18)
   - (100, 75)
   - (13, 7)

```c
int gcd(int a, int b) { /* 実装せよ */ }
int lcm(int a, int b) { /* 実装せよ */ }
int main() {
    printf("gcd(48,18)=%d, lcm=%d\n", gcd(48,18), lcm(48,18));
    printf("gcd(100,75)=%d, lcm=%d\n", gcd(100,75), lcm(100,75));
    printf("gcd(13,7)=%d, lcm=%d\n", gcd(13,7), lcm(13,7));
}
```

💡 **Hint**: LCM(a,b) = a × b / GCD(a,b)。整数オーバーフロー対策でa/gcd*bの順で計算する。

✅ **Solution**:
```c
int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}
int lcm(int a, int b) {
    return a / gcd(a, b) * b;  // a/gcd先でオーバーフロー防止
}
```

**(3)**:
```
gcd(48,18)=6,  lcm=144
gcd(100,75)=25, lcm=300
gcd(13,7)=1,   lcm=91
```

出力:
```
gcd(48,18)=6, lcm=144
gcd(100,75)=25, lcm=300
gcd(13,7)=1, lcm=91
```

📝 **Explanation**: LCM=a×b/GCDだが`a*b`が先にオーバーフローする可能性があるため`(a/gcd)*b`と書く。互いに素（gcd=1）の場合はLCM=a×b。GCDは古代ギリシャ起源のアルゴリズム（紀元前300年頃）で最速のGCDアルゴリズム。

---

### H7. 行列操作（行和と列最大値）

```c
#define ROWS 3
#define COLS 4

void row_sums(int a[ROWS][COLS], int sums[ROWS]) {
    // 各行の和をsums[]に格納する実装せよ
}

void col_maxes(int a[ROWS][COLS], int maxes[COLS]) {
    // 各列の最大値をmaxes[]に格納する実装せよ
}

int main() {
    int a[ROWS][COLS] = {
        {1, 5, 3, 2},
        {4, 2, 8, 1},
        {3, 7, 2, 6}
    };
    int sums[ROWS], maxes[COLS];
    row_sums(a, sums);
    col_maxes(a, maxes);
    printf("Row sums: ");
    for (int i = 0; i < ROWS; i++) printf("%d ", sums[i]);
    printf("\nCol maxes: ");
    for (int j = 0; j < COLS; j++) printf("%d ", maxes[j]);
    printf("\n");
}
```

実装し、出力を答えよ。

💡 **Hint**: 行和は各行の全列を合計。列最大値は各列の全行を比較。

✅ **Solution**:
```c
void row_sums(int a[ROWS][COLS], int sums[ROWS]) {
    for (int i = 0; i < ROWS; i++) {
        sums[i] = 0;
        for (int j = 0; j < COLS; j++) sums[i] += a[i][j];
    }
}

void col_maxes(int a[ROWS][COLS], int maxes[COLS]) {
    for (int j = 0; j < COLS; j++) {
        maxes[j] = a[0][j];
        for (int i = 1; i < ROWS; i++)
            if (a[i][j] > maxes[j]) maxes[j] = a[i][j];
    }
}
```

出力:
```
Row sums: 11 15 18 
Col maxes: 4 7 8 6 
```

行0: 1+5+3+2=11、行1: 4+2+8+1=15、行2: 3+7+2+6=18。列0: max(1,4,3)=4、列1: max(5,2,7)=7、列2: max(3,8,2)=8、列3: max(2,1,6)=6。

📝 **Explanation**: 行走査はi外側・j内側、列走査はj外側・i内側。ループの入れ子の方向を変えるだけで行/列の処理が切り替わる。

---

### H8. 回文チェック（再帰＋非再帰）

**(1)** 再帰版`is_palindrome_rec`を実装せよ。
**(2)** 非再帰版`is_palindrome_iter`を実装せよ。
**(3)** 次の文字列について両方で判定せよ: "racecar", "hello", "aabaa", ""

```c
int is_palindrome_rec(char s[], int left, int right) { /* 実装 */ }
int is_palindrome_iter(char s[]) { /* 実装 */ }
int main() {
    char *tests[] = {"racecar", "hello", "aabaa", ""};
    for (int i = 0; i < 4; i++) {
        int n = strlen(tests[i]);
        printf("%s: rec=%d, iter=%d\n", tests[i],
               is_palindrome_rec(tests[i], 0, n-1),
               is_palindrome_iter(tests[i]));
    }
}
```

💡 **Hint**: 再帰: left==rightまたはleft>rightが基底条件。

✅ **Solution**:
```c
#include <string.h>
int is_palindrome_rec(char s[], int left, int right) {
    if (left >= right) return 1;  // 基底条件
    if (s[left] != s[right]) return 0;
    return is_palindrome_rec(s, left+1, right-1);
}

int is_palindrome_iter(char s[]) {
    int left = 0, right = strlen(s) - 1;
    while (left < right) {
        if (s[left] != s[right]) return 0;
        left++; right--;
    }
    return 1;
}
```

**(3)** 出力:
```
racecar: rec=1, iter=1
hello: rec=0, iter=0
aabaa: rec=1, iter=1
: rec=1, iter=1
```

📝 **Explanation**: 空文字列は`left=0, right=-1`で`left>=right`が即成立して1を返す（空文字列は回文）。再帰版は「両端一致→内側を再帰」の分解。反復版は2ポインタで内側に収束。

---

### H9. 文字列トークナイザ

文字列をデリミタ（区切り文字）で分割してトークン数を数え、各トークンを表示する関数を実装せよ。

```c
int tokenize(char s[], char delim, char tokens[][50], int max_tokens) {
    // sをdelimで分割し、tokens[][]に格納
    // 返り値はトークン数
}
int main() {
    char s[] = "apple,banana,cherry,date";
    char tokens[10][50];
    int n = tokenize(s, ',', tokens, 10);
    printf("count=%d\n", n);
    for (int i = 0; i < n; i++) printf("[%s]\n", tokens[i]);
}
```

期待出力:
```
count=4
[apple]
[banana]
[cherry]
[date]
```

💡 **Hint**: 文字を1つずつ読み、delimでなければtokens[cnt]に追加。delimに当たったらnull終端してcntを増やす。

✅ **Solution**:
```c
#include <string.h>
int tokenize(char s[], char delim, char tokens[][50], int max_tokens) {
    int cnt = 0, ti = 0;
    tokens[0][0] = '\0';
    for (int i = 0; s[i] != '\0' && cnt < max_tokens; i++) {
        if (s[i] == delim) {
            tokens[cnt][ti] = '\0';
            cnt++;
            ti = 0;
            if (cnt < max_tokens) tokens[cnt][0] = '\0';
        } else {
            tokens[cnt][ti++] = s[i];
        }
    }
    if (ti > 0 || cnt == 0) {
        tokens[cnt][ti] = '\0';
        cnt++;
    }
    return cnt;
}
```

📝 **Explanation**: 文字走査でdelimを検出したら現在のトークンをnull終端してカウンタを増やす。最後のトークンはdelimなしで終わるため、ループ後にnull終端とカウントを追加する。`strtok`（標準ライブラリ）は同様の機能を提供するが、試験では手実装が問われることが多い。

---

### H10. 仕様からの完全実装

**次の仕様に従ったCプログラムを一から実装せよ。**

**仕様**:
- `int`型の配列（サイズ定数`N=6`）に以下の初期値を持つ: `{64, 34, 25, 12, 22, 11}`
- バブルソートで昇順にソートする
- ソート後の配列を表示する（形式: `Sorted: 11 12 22 25 34 64`）
- 配列の合計、平均（小数1桁）、最大値、最小値を表示する
- 配列が回文配列かどうかを判定して表示する（`Palindrome: yes/no`）

```
期待出力:
Sorted: 11 12 22 25 34 64 
Sum=168, Avg=28.0, Max=64, Min=11
Palindrome: no
```

💡 **Hint**: 全ての要素操作（ソート・統計・回文）を関数として実装すると整理しやすい。

✅ **Solution**:
```c
#include <stdio.h>
#define N 6

void bubble_sort(int a[], int n) {
    for (int i = 0; i < n-1; i++)
        for (int j = 0; j < n-1-i; j++)
            if (a[j] > a[j+1]) {
                int t=a[j]; a[j]=a[j+1]; a[j+1]=t;
            }
}

int is_palindrome_arr(int a[], int n) {
    for (int i = 0; i < n/2; i++)
        if (a[i] != a[n-1-i]) return 0;
    return 1;
}

int main() {
    int a[N] = {64, 34, 25, 12, 22, 11};
    bubble_sort(a, N);
    
    printf("Sorted: ");
    for (int i = 0; i < N; i++) printf("%d ", a[i]);
    printf("\n");
    
    int sum = 0, max = a[0], min = a[0];
    for (int i = 0; i < N; i++) {
        sum += a[i];
        if (a[i] > max) max = a[i];
        if (a[i] < min) min = a[i];
    }
    printf("Sum=%d, Avg=%.1f, Max=%d, Min=%d\n",
           sum, (double)sum/N, max, min);
    
    printf("Palindrome: %s\n",
           is_palindrome_arr(a, N) ? "yes" : "no");
    return 0;
}
```

出力:
```
Sorted: 11 12 22 25 34 64 
Sum=168, Avg=28.0, Max=64, Min=11
Palindrome: no
```

📝 **Explanation**: 仕様から実装する問題は「機能を関数に分割→main で呼ぶ」構造が採点しやすい。ソート後の最小値はa[0]、最大値はa[N-1]だが、ソート前を想定して毎回比較する汎用ロジックを書く方が堅牢。`(double)sum/N`の型変換を忘れずに。回文配列：{11,12,22,25,34,64}は左右対称でないのでno。
