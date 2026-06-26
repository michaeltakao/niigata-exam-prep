---
title: "L6 関数・再帰 — 類題ドリル (30問)"
---

# L6 関数・再帰 — 類題ドリル (30問)

> 関数定義・引数・戻り値・スコープ・再帰（階乗・フィボナッチ・GCD）

---

## ★ Easy（公式代入・基本トレース）

### E1. 単純な関数呼び出し

```c
int add(int a, int b) {
    return a + b;
}
int main() {
    printf("%d\n", add(3, 7));
    printf("%d\n", add(10, -4));
    return 0;
}
```

出力を答えよ。

💡 **Hint**: `return a + b`が戻り値を決める。

✅ **Solution**:
```
10
6
```

📝 **Explanation**: `add(3,7)`は`3+7=10`を返す。`add(10,-4)`は`10+(-4)=6`を返す。関数は`return`の値をそのまま式中で使える。

---

### E2. 戻り値を変数に格納

```c
int square(int n) {
    return n * n;
}
int main() {
    int x = square(5);
    int y = square(x);
    printf("%d %d\n", x, y);
    return 0;
}
```

出力を答えよ。

💡 **Hint**: `y = square(x) = square(25)`。

✅ **Solution**: `25 625`

📝 **Explanation**: `square(5)=25`、`square(25)=625`。関数の戻り値は変数に格納して再利用できる。`y=square(square(5))`のように入れ子にすることも可能。

---

### E3. 関数内での計算

```c
double circle_area(double r) {
    return 3.14159 * r * r;
}
int main() {
    printf("%.2f\n", circle_area(5.0));
    return 0;
}
```

出力を答えよ。

💡 **Hint**: π×r² = 3.14159 × 25

✅ **Solution**: `78.54`

📝 **Explanation**: `3.14159 × 5.0 × 5.0 = 78.53975`、`%.2f`で小数2桁に丸めて`78.54`。double型で精度が保たれる。

---

### E4. 複数の関数呼び出しの連鎖

```c
int double_val(int n) { return n * 2; }
int add_one(int n) { return n + 1; }
int main() {
    int x = 5;
    x = double_val(x);
    x = add_one(x);
    x = double_val(x);
    printf("%d\n", x);
    return 0;
}
```

出力を答えよ。

💡 **Hint**: 5→10→11→22 と順に変換される。

✅ **Solution**: `22`

📝 **Explanation**: `double_val(5)=10`、`add_one(10)=11`、`double_val(11)=22`。関数を順に適用する合成の考え方。各ステップで`x`が書き換わる。

---

### E5. void関数の副作用

```c
void print_stars(int n) {
    for (int i = 0; i < n; i++) {
        printf("*");
    }
    printf("\n");
}
int main() {
    print_stars(3);
    print_stars(5);
    return 0;
}
```

出力を答えよ。

💡 **Hint**: void関数は戻り値なし。副作用（printfの実行）のみが目的。

✅ **Solution**:
```
***
*****
```

📝 **Explanation**: `void`関数は`return`値を持たず、処理の実行自体が目的。`print_stars(3)`は`*`を3個出力後に改行する。

---

### E6. ローカル変数 vs グローバル変数 (1)

```c
int x = 10;

void func() {
    printf("%d\n", x);
}
int main() {
    int x = 20;
    func();
    printf("%d\n", x);
    return 0;
}
```

出力を答えよ。

💡 **Hint**: `func()`内では`x`はグローバル変数を参照する。

✅ **Solution**:
```
10
20
```

📝 **Explanation**: `func()`内にローカル`x`はないので、グローバル`x=10`を参照する。`main()`内のローカル`x=20`はmainスコープのみで有効。関数スコープはコードブロック`{}`で定まる。

---

### E7. ローカル変数のシャドーイング

```c
int g = 100;
int main() {
    printf("%d\n", g);
    int g = 200;
    printf("%d\n", g);
    return 0;
}
```

出力を答えよ。

💡 **Hint**: ローカル変数`g`が宣言された後は、内側スコープの`g`が優先される。

✅ **Solution**:
```
100
200
```

📝 **Explanation**: 1行目のprintfはローカル`g`が未宣言なのでグローバル`g=100`。`int g=200`の宣言後は内側スコープの`g=200`が優先（シャドーイング）。試験ではスコープの優先順位が頻出。

---

### E8. void関数とprintfの副作用

```c
void greet(char name[]) {
    printf("Hello, %s!\n", name);
}
int main() {
    greet("Alice");
    greet("Bob");
    return 0;
}
```

出力を答えよ。

💡 **Hint**: 関数を2回呼び出すと2行出力される。

✅ **Solution**:
```
Hello, Alice!
Hello, Bob!
```

📝 **Explanation**: 文字列を引数として渡すとき、配列の先頭アドレスが渡される。"Alice", "Bob"はリテラル文字列。`%s`で文字列を表示する。

---

### E9. 複数引数と計算

```c
int max3(int a, int b, int c) {
    int m = a;
    if (b > m) m = b;
    if (c > m) m = c;
    return m;
}
int main() {
    printf("%d\n", max3(5, 3, 8));
    printf("%d\n", max3(7, 7, 2));
    return 0;
}
```

出力を答えよ。

💡 **Hint**: 3つの引数の最大値を返す。

✅ **Solution**:
```
8
7
```

📝 **Explanation**: `max3(5,3,8)`: m=5→8（8>5）→8（8≤8... 修正: c=8>m=5→m=8、最終m=8。`max3(7,7,2)`: m=7、b=7不変、c=2不変、m=7。同値の場合は先に入れた値が残る。

---

### E10. returnなしの関数の動作

```c
int missing_return(int n) {
    if (n > 0) return n * 2;
    // n <= 0 の場合: return なし
}
int main() {
    printf("%d\n", missing_return(5));
    printf("%d\n", missing_return(-1));
    return 0;
}
```

(1) `missing_return(5)`の出力を答えよ。
(2) `missing_return(-1)`はどうなるか？

💡 **Hint**: returnのない経路は未定義動作。

✅ **Solution**:
(1) `10`
(2) 未定義動作（garbage valueが返る可能性が高い）

📝 **Explanation**: `n>0`の場合は`n*2=10`を正常に返す。`n=-1`の場合はreturnに到達しないため、戻り値は不定（スタック上の残留データが返ることが多い）。コンパイラ警告が出る。本番では必ず全パスにreturnを書くこと。

---

## ★★ Medium（変形・穴埋め・再帰トレース）

### M1. 関数シグネチャの補完 (1)

次のmain関数の呼び出しに対応する関数シグネチャと実装を書け。

```c
// 関数定義（ここを書け）

int main() {
    printf("%.2f\n", average(10, 20, 30));
    return 0;
}
```

期待出力: `20.00`

💡 **Hint**: 3つのintを受け取り、doubleを返す。

✅ **Solution**:
```c
double average(int a, int b, int c) {
    return (double)(a + b + c) / 3;
}
```

📝 **Explanation**: 3引数の平均を返す。`(a+b+c)/3`だと整数除算で`20`になるが、`(double)(...)/3`でdoubleに変換。関数の引数型・戻り値型はmain側の使い方から逆算できる。

---

### M2. 関数シグネチャの補完 (2)

```c
// 関数定義（ここを書け）

int main() {
    int a[] = {3, 1, 4, 1, 5, 9};
    printf("%d\n", sum_array(a, 6));
    return 0;
}
```

期待出力: `23`

💡 **Hint**: 配列とサイズを受け取りintを返す。

✅ **Solution**:
```c
int sum_array(int a[], int n) {
    int sum = 0;
    for (int i = 0; i < n; i++) sum += a[i];
    return sum;
}
```

📝 **Explanation**: 配列引数は`int a[]`または`int *a`で受け取る。サイズ`n`も必ず渡す（配列から要素数は取得できないため）。3+1+4+1+5+9=23。

---

### M3. 関数シグネチャの補完 (3)

```c
// 関数定義（ここを書け）

int main() {
    printf("%s\n", is_even(4) ? "even" : "odd");
    printf("%s\n", is_even(7) ? "even" : "odd");
    return 0;
}
```

💡 **Hint**: intを受け取り、偶数かどうかをint（0/1）で返す。

✅ **Solution**:
```c
int is_even(int n) {
    return n % 2 == 0;
}
```

出力:
```
even
odd
```

📝 **Explanation**: `n % 2 == 0`は偶数のとき1（true）、奇数のとき0（false）。三項演算子`? :`で条件分岐。C言語にbool型はなく、int（0=偽、非0=真）で代用する。

---

### M4. factorial の再帰トレース

```c
int factorial(int n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}
```

`factorial(4)`の呼び出しツリーを書き、戻り値を答えよ。

💡 **Hint**: 再帰の底（n=1）から戻り値が折り返してくる。

✅ **Solution**:
```
factorial(4)
  → 4 * factorial(3)
       → 3 * factorial(2)
            → 2 * factorial(1)
                 → return 1
            → return 2 * 1 = 2
       → return 3 * 2 = 6
  → return 4 * 6 = 24
```

**答え: 24**

📝 **Explanation**: 再帰の基底条件は`n <= 1 → 1`。それ以外は`n * factorial(n-1)`。呼び出しスタックが深くなり、基底条件で折り返して乗算していく。4! = 4×3×2×1 = 24。

---

### M5. factorial の実装穴埋め

```c
int factorial(int n) {
    if ((A)) return (B);
    return (C) * factorial((D));
}
```

空欄を埋めよ。

💡 **Hint**: 基底条件と再帰呼び出しのパターンを考える。

✅ **Solution**: `(A) n <= 1`, `(B) 1`, `(C) n`, `(D) n - 1`

📝 **Explanation**: 再帰関数には必ず「基底条件（終了条件）」と「再帰呼び出し（問題を小さくする）」の2つが必要。基底条件がないと無限再帰になる。

---

### M6. Fibonacci の再帰トレース (1)

```c
int fib(int n) {
    if (n <= 1) return 1;
    return fib(n-1) + fib(n-2);
}
```

`fib(5)`の値を答え、`fib(0)〜fib(5)`の列を示せ。

💡 **Hint**: fib(0)=1, fib(1)=1 から順に計算する。

✅ **Solution**:
```
fib(0)=1, fib(1)=1, fib(2)=2, fib(3)=3, fib(4)=5, fib(5)=8
```

**答え: 8**

📝 **Explanation**: この定義では`fib(n) = fib(n-1) + fib(n-2)`, `fib(0)=fib(1)=1`（一般的なフィボナッチ数列より1つずれている）。`fib(5) = fib(4)+fib(3) = 5+3 = 8`。試験ではどの定義を使うかを確認すること。

---

### M7. Fibonacci の実装穴埋め

```c
int fib(int n) {
    if (n (A)) return 1;
    return fib(n-(B)) + fib(n-(C));
}
```

空欄を埋め、`fib(6)`の値を答えよ。

💡 **Hint**: `n <= 1`が基底条件。

✅ **Solution**: `(A) <= 1`, `(B) 1`, `(C) 2`

`fib(6) = fib(5)+fib(4) = 8+5 = 13`

📝 **Explanation**: フィボナッチ再帰は指数的に関数呼び出しが増えるため計算量O(2^n)と非常に非効率。実用上はメモ化や反復実装を使う。試験ではトレースの正確さが問われる。

---

### M8. GCD の再帰トレース

```c
int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}
```

`gcd(48, 18)`のトレースを示し、答えを求めよ。

💡 **Hint**: ユークリッドの互除法：a % b が 0 になるまで繰り返す。

✅ **Solution**:
```
gcd(48, 18)
  → gcd(18, 48%18=12)
  → gcd(12, 18%12=6)
  → gcd(6,  12%6=0)
  → b==0, return 6
```

**答え: 6**

📝 **Explanation**: ユークリッドの互除法はGCD計算の最も効率的なアルゴリズムでO(log(min(a,b)))。`gcd(a,b) = gcd(b, a mod b)`という恒等式に基づく。48=2×18+12、18=1×12+6、12=2×6+0。

---

### M9. 配列を関数で変更

```c
void negate_all(int a[], int n) {
    for (int i = 0; i < n; i++) {
        a[i] = (A);
    }
}
int main() {
    int a[] = {1, -2, 3, -4, 5};
    negate_all(a, 5);
    for (int i = 0; i < 5; i++) printf("%d ", a[i]);
    return 0;
}
```

空欄を埋め、出力を答えよ。

💡 **Hint**: 各要素の符号を反転する。

✅ **Solution**: `(A) -a[i]`

出力: `-1 2 -3 4 -5 `

📝 **Explanation**: `-a[i]`で符号反転。正数は負数に、負数は正数になる。配列の参照渡しにより、関数内の変更がmainに反映される。

---

### M10. 値渡しと配列渡しの違い

```c
void try_change_int(int x) {
    x = 999;
}
void change_array(int a[], int n) {
    a[0] = 999;
}
int main() {
    int x = 1;
    int a[] = {1, 2, 3};
    try_change_int(x);
    change_array(a, 3);
    printf("%d\n", x);
    printf("%d\n", a[0]);
    return 0;
}
```

出力を答えよ。その理由を説明せよ。

💡 **Hint**: intはコピーが渡され、配列はアドレスが渡される。

✅ **Solution**:
```
1
999
```

📝 **Explanation**: `try_change_int(x)`ではxのコピーが渡されるので元のxは変わらない。`change_array(a,3)`では配列の先頭アドレスが渡されるため、`a[0]=999`は元の配列を直接書き換える。C言語の「配列は参照渡し相当」という特性。

---

## ★★★ Hard — 入試形式

### H1. 再帰トレース＋穴埋め ← R8類題

```c
int mystery(int n) {
    if (n == 0) return 0;
    return mystery(n / 10) + n % 10;
}
```

(1) `mystery(123)`の戻り値を答えよ（トレースを示せ）。
(2) この関数は何を計算しているか答えよ。
(3) 空欄を埋めて同じ動作をする反復版を完成させよ。
```c
int mystery_iter(int n) {
    int sum = 0;
    while ((A)) {
        sum += (B);
        n = (C);
    }
    return sum;
}
```

💡 **Hint**: `n % 10`は1の位、`n / 10`で1桁削る。

✅ **Solution**:
(1)
```
mystery(123)
  → mystery(12) + 3
       → mystery(1) + 2
            → mystery(0) + 1
                 → return 0
            → return 0 + 1 = 1
       → return 1 + 2 = 3
  → return 3 + 3 = 6
```
**答え: 6**

(2) **各桁の合計（digit sum）を計算する。**

(3) `(A) n != 0`, `(B) n % 10`, `(C) n / 10`

📝 **Explanation**: `n%10`で下位桁を取り出し、`n/10`でその桁を削る。再帰版と反復版は同じロジック。再帰の「基底条件→積み上げ」と反復の「ループ条件→集計」が対応する。

---

### H2. 関数の実装 ← R7類題

次の仕様通りの関数を実装せよ。

**仕様**: `is_prime(n)` — `n`が素数なら1、そうでなければ0を返す。

```c
int is_prime(int n) {
    // ここを実装
}
int main() {
    int primes[] = {2, 3, 5, 7, 11, 13};
    for (int i = 0; i < 6; i++) printf("%d ", is_prime(primes[i]));
    printf("\n");
    printf("%d %d %d\n", is_prime(1), is_prime(4), is_prime(9));
}
```

期待出力:
```
1 1 1 1 1 1 
0 0 0
```

💡 **Hint**: 2からsqrt(n)までで割り切れるかチェックする。n<2は素数でない。

✅ **Solution**:
```c
int is_prime(int n) {
    if (n < 2) return 0;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) return 0;
    }
    return 1;
}
```

📝 **Explanation**: `n < 2`はすべて非素数。`i * i <= n`（つまり`i <= sqrt(n)`）まで確認すれば十分（それ以上の因子は対称に既チェック済み）。割り切れれば0を即返す。これはO(√n)の効率的な実装。

---

### H3. 相互再帰のトレース

```c
int is_even(int n);
int is_odd(int n);

int is_even(int n) {
    if (n == 0) return 1;
    return is_odd(n - 1);
}
int is_odd(int n) {
    if (n == 0) return 0;
    return is_even(n - 1);
}
```

(1) `is_even(4)`の値を答えよ（全トレース）。
(2) `is_odd(3)`の値を答えよ。
(3) この実装の問題点は何か？

💡 **Hint**: 2つの関数が互いに呼び合う「相互再帰」。`n`が0になるまで1ずつ減る。

✅ **Solution**:
(1)
```
is_even(4) → is_odd(3) → is_even(2) → is_odd(1) → is_even(0) → 1
```
**答え: 1（偶数）**

(2)
```
is_odd(3) → is_even(2) → is_odd(1) → is_even(0) → 1
```
**答え: 1（奇数）**

(3) 問題点: **再帰の深さがnに比例するため、nが大きいとスタックオーバーフローする。** `n%2==0`の直接比較の方が効率的でO(1)。

📝 **Explanation**: 相互再帰は理論的には正しいが実用上非効率。`is_even(100000)`は10万回の関数呼び出しを行う。試験ではトレース能力と問題点の指摘が求められる。

---

### H4. ハノイの塔（n=3）

```c
void hanoi(int n, char from, char to, char via) {
    if (n == 1) {
        printf("Move disk 1 from %c to %c\n", from, to);
        return;
    }
    hanoi(n-1, from, via, to);
    printf("Move disk %d from %c to %c\n", n, from, to);
    hanoi(n-1, via, to, from);
}
int main() {
    hanoi(3, 'A', 'C', 'B');
    return 0;
}
```

出力を答えよ（全7行）。

💡 **Hint**: n枚を「fromからtoへ、viaを経由して」移す。1枚の場合は直接移す。

✅ **Solution**:
```
Move disk 1 from A to C
Move disk 2 from A to B
Move disk 1 from C to B
Move disk 3 from A to C
Move disk 1 from B to A
Move disk 2 from B to C
Move disk 1 from A to C
```

📝 **Explanation**: n=3のハノイの塔は2³-1=7手。`hanoi(n-1, from, via, to)`でn-1枚をviaへ移動、次に最大ディスクをtoへ、最後に`hanoi(n-1, via, to, from)`でn-1枚をtoへ移す。再帰の典型的な応用。

---

### H5. 再帰による桁和

各桁の数字を加算し続けて1桁になるまで繰り返す関数を実装せよ。

```c
int digit_root(int n) {
    // ここを実装
}
int main() {
    printf("%d\n", digit_root(493));   // 4+9+3=16 → 1+6=7
    printf("%d\n", digit_root(9999));  // 9+9+9+9=36 → 3+6=9
    printf("%d\n", digit_root(0));
}
```

💡 **Hint**: digit_sumを求めてから、1桁ならそれを返し、複数桁なら再帰する。

✅ **Solution**:
```c
int digit_sum(int n) {
    if (n == 0) return 0;
    return n % 10 + digit_sum(n / 10);
}
int digit_root(int n) {
    int s = digit_sum(n);
    if (s < 10) return s;
    return digit_root(s);
}
```

出力: `7`, `9`, `0`

📝 **Explanation**: `digit_sum`で桁和を計算し、10未満なら終了、そうでなければ`digit_root`を再帰呼び出し。493→16→7。実際、digit_root(n) = n==0 ? 0 : 1+(n-1)%9 という直接公式があるが、再帰実装の方が理解しやすい。

---

### H6. 冪乗の実装（pow不使用）

整数の冪乗を計算する関数を実装せよ（反復版と再帰版の両方）。

```c
long power_iter(int base, int exp) {
    // 反復版
}
long power_rec(int base, int exp) {
    // 再帰版
}
int main() {
    printf("%ld\n", power_iter(2, 10));
    printf("%ld\n", power_rec(3, 5));
}
```

💡 **Hint**: `exp`が0なら1、そうでなければ`base^(exp-1) * base`。

✅ **Solution**:
```c
long power_iter(int base, int exp) {
    long result = 1;
    for (int i = 0; i < exp; i++) result *= base;
    return result;
}
long power_rec(int base, int exp) {
    if (exp == 0) return 1;
    return base * power_rec(base, exp - 1);
}
```

出力: `1024`, `243`

📝 **Explanation**: 反復版：1から始めexpの回数だけbaseを掛ける。再帰版：exp=0が基底条件（b^0=1）、それ以外はbase×b^(exp-1)。2^10=1024、3^5=243。高速化（O(log n)）には二分冪乗法を使う。

---

### H7. スコープの罠

```c
int x = 1;
void f() {
    int x = 2;
    printf("f: x=%d\n", x);
    x = 3;
}
int g() {
    printf("g: x=%d\n", x);
    return x;
}
int main() {
    f();
    printf("main after f: x=%d\n", x);
    int r = g();
    printf("r=%d\n", r);
    return 0;
}
```

出力を答えよ。

💡 **Hint**: `f()`内の`x`はローカル。`g()`内の`x`はグローバル。

✅ **Solution**:
```
f: x=2
main after f: x=1
g: x=1
r=1
```

📝 **Explanation**: `f()`内の`x=2`はローカル変数で、グローバル`x=1`と別物。`f()`内で`x=3`と書いてもグローバルは不変。`g()`はローカル`x`を宣言していないのでグローバル`x=1`を参照する。スコープを混同した典型的な落とし穴。

---

### H8. 関数ポインタの基礎

```c
int double_it(int n) { return n * 2; }
int square_it(int n) { return n * n; }

int apply(int (*f)(int), int x) {
    return (*f)(x);
}
int main() {
    printf("%d\n", apply(double_it, 5));
    printf("%d\n", apply(square_it, 4));
    int (*ptr)(int) = double_it;
    printf("%d\n", ptr(7));
    return 0;
}
```

出力を答えよ。

💡 **Hint**: `(*f)(x)`は関数ポインタ`f`を通じて関数を呼び出す。

✅ **Solution**:
```
10
16
14
```

📝 **Explanation**: `apply(double_it, 5)`はdouble_itを関数ポインタとして渡し、`(*f)(5)=10`を返す。`apply(square_it, 4)=16`。`ptr(7)`は`double_it(7)=14`。関数ポインタは高階関数（コールバック）に使う。

---

### H9. 再帰バイナリサーチ

```c
int bin_search(int a[], int left, int right, int key) {
    if (left > right) return -1;
    int mid = (left + right) / 2;
    if (a[mid] == key) return mid;
    if (a[mid] < key) return bin_search(a, mid+1, right, key);
    return bin_search(a, left, mid-1, key);
}
int main() {
    int a[] = {1, 3, 5, 7, 9, 11, 13};
    printf("%d\n", bin_search(a, 0, 6, 7));
    printf("%d\n", bin_search(a, 0, 6, 6));
}
```

(1) `bin_search(a, 0, 6, 7)`のトレースを示し、答えを求めよ。
(2) `bin_search(a, 0, 6, 6)`の答えを求めよ。

💡 **Hint**: 中央要素と比較して半分に絞る。

✅ **Solution**:
(1)
```
left=0, right=6, mid=3, a[3]=7 == 7 → return 3
```
**答え: 3**

(2)
```
left=0, right=6, mid=3, a[3]=7 > 6 → bin_search(a, 0, 2, 6)
left=0, right=2, mid=1, a[1]=3 < 6 → bin_search(a, 2, 2, 6)
left=2, right=2, mid=2, a[2]=5 < 6 → bin_search(a, 3, 2, 6)
left=3 > right=2 → return -1
```
**答え: -1**

📝 **Explanation**: 二分探索はO(log n)で配列を検索する。毎回探索範囲を半分に絞る。ソート済み配列にのみ適用可能。7はインデックス3に存在し、6は存在しないので-1。

---

### H10. 再帰による整数配列処理

```c
int sum_rec(int a[], int n) {
    if (n == 0) return 0;
    return a[0] + sum_rec(a+1, n-1);
}
int max_rec(int a[], int n) {
    if (n == 1) return a[0];
    int rest_max = max_rec(a+1, n-1);
    return a[0] > rest_max ? a[0] : rest_max;
}
int main() {
    int a[] = {3, 1, 4, 1, 5, 9, 2, 6};
    int n = 8;
    printf("sum=%d\n", sum_rec(a, n));
    printf("max=%d\n", max_rec(a, n));
    return 0;
}
```

(1) 出力を答えよ。
(2) `a+1`というポインタ演算が何を意味するか説明せよ。
(3) `sum_rec`の反復版を書け。

💡 **Hint**: `a+1`はa[1]を先頭とする配列へのポインタ。

✅ **Solution**:
(1)
```
sum=31
max=9
```
3+1+4+1+5+9+2+6=31、最大値=9

(2) `a+1`は配列の先頭アドレスを1つ進めたポインタ。つまり`a[1]`から始まる配列として渡せる。`n-1`でサイズも1減らすことで部分配列を再帰的に処理する。

(3)
```c
int sum_iter(int a[], int n) {
    int s = 0;
    for (int i = 0; i < n; i++) s += a[i];
    return s;
}
```

📝 **Explanation**: `sum_rec(a, n) = a[0] + sum_rec(a+1, n-1)`は「先頭要素＋残りの和」の分解。ポインタ算術`a+1`でサブ配列を渡す慣用句。基底条件`n==0`で0を返す。max_recは三項演算子で2値の大きい方を選ぶ。
