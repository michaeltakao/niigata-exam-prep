---
render_with_liquid: false
---

# L5 配列 — 類題ドリル (30問)

> 1D配列・2D配列・文字列配列・strlen/strcpy/strcmp

---

## ★ Easy（公式代入・基本読み取り）

### E1. 配列要素のアクセス

```c
int a[] = {10, 20, 30, 40, 50};
printf("%d\n", a[2]);
```

出力結果を答えよ。

💡 **Hint**: 配列インデックスは0から始まる。

✅ **Solution**: `30`

📝 **Explanation**: `a[0]=10, a[1]=20, a[2]=30`。インデックス2は3番目の要素。配列は0-indexedなので注意。

---

### E2. 配列要素の変更後の出力

```c
int a[] = {1, 2, 3, 4, 5};
a[1] = 99;
printf("%d %d %d\n", a[0], a[1], a[2]);
```

出力結果を答えよ。

💡 **Hint**: `a[1]`に代入した後の値を確認する。

✅ **Solution**: `1 99 3`

📝 **Explanation**: `a[1] = 99`で2番目の要素が上書きされる。他の要素は変更されない。代入は破壊的操作。

---

### E3. 配列の末尾要素

```c
int a[5] = {10, 20, 30, 40, 50};
int n = 5;
printf("%d\n", a[n-1]);
```

出力結果を答えよ。

💡 **Hint**: `n-1 = 4`、つまり`a[4]`。

✅ **Solution**: `50`

📝 **Explanation**: サイズnの配列の末尾インデックスは`n-1`。`a[n]`は範囲外アクセスになるので絶対に書かない。

---

### E4. ループで配列の和

```c
int a[] = {3, 7, 2, 8, 5};
int sum = 0;
for (int i = 0; i < 5; i++) {
    sum += a[i];
}
printf("%d\n", sum);
```

出力結果を答えよ。

💡 **Hint**: 3+7+2+8+5 を計算する。

✅ **Solution**: `25`

📝 **Explanation**: `sum`が0から始まり、各要素を順に加算する。ループは`i=0`から`i=4`まで5回実行される。

---

### E5. ループで全要素表示

```c
int a[] = {4, 8, 15, 16};
for (int i = 0; i < 4; i++) {
    printf("%d ", a[i]);
}
printf("\n");
```

出力結果を答えよ。

💡 **Hint**: 各ループ反復で1要素を表示する。

✅ **Solution**: `4 8 15 16 `（末尾スペースあり）

📝 **Explanation**: `printf("%d ", a[i])`は各数値の後にスペースを出力する。最後の要素の後にもスペースが付く点に注意。

---

### E6. char配列の文字アクセス

```c
char s[] = "hello";
printf("%c\n", s[0]);
printf("%c\n", s[4]);
```

出力結果を答えよ。

💡 **Hint**: `"hello"`は`h,e,l,l,o,\0`の6文字（null終端含む）。

✅ **Solution**:
```
h
o
```

📝 **Explanation**: `s[0]='h'`, `s[4]='o'`。文字列リテラルは末尾に`\0`が自動付加されるが、アクセスできる文字インデックスは0〜4。

---

### E7. char配列とintとの違い

```c
char s[] = "ABC";
printf("%c %d\n", s[0], s[0]);
```

出力結果を答えよ。

💡 **Hint**: `%c`は文字として、`%d`はASCII値として表示する。

✅ **Solution**: `A 65`

📝 **Explanation**: `'A'`のASCIIコードは65。`%c`は文字を表示し、`%d`は整数（ASCII値）を表示する。charは実際には小さい整数型。

---

### E8. strlen の基本

```c
#include <string.h>
char s[] = "niigata";
printf("%zu\n", strlen(s));
```

出力結果を答えよ。

💡 **Hint**: `strlen`はnull終端`\0`を含まない文字数を返す。

✅ **Solution**: `7`

📝 **Explanation**: "niigata"は7文字。`strlen`はnull終端文字`\0`を数えない。`sizeof(s)`なら8（\0を含む）になる点と混同しないこと。

---

### E9. 2D配列の宣言と要素アクセス

```c
int a[2][3] = {{1, 2, 3}, {4, 5, 6}};
printf("%d\n", a[1][2]);
```

出力結果を答えよ。

💡 **Hint**: `a[行][列]`。行・列ともに0始まり。

✅ **Solution**: `6`

📝 **Explanation**: `a[1][2]`は2行目（インデックス1）・3列目（インデックス2）の要素。`{4,5,6}`の3番目なので6。

---

### E10. 2D配列の行アクセス

```c
int a[3][2] = {{1,2},{3,4},{5,6}};
printf("%d %d\n", a[0][0], a[2][1]);
```

出力結果を答えよ。

💡 **Hint**: 最初の行と最後の行の要素を特定する。

✅ **Solution**: `1 6`

📝 **Explanation**: `a[0][0]`は1行目1列目=1。`a[2][1]`は3行目2列目=6。2D配列は「行の配列の配列」として覚える。

---

## ★★ Medium（変形・穴埋め・操作）

### M1. 最大値を求める穴埋め

次のプログラムの空欄`(A)`, `(B)`, `(C)`を埋めよ。

```c
int a[] = {3, 7, 1, 9, 4};
int max = a[0];
for (int i = (A); i < 5; i++) {
    if (a[i] (B) max) {
        max = (C);
    }
}
printf("%d\n", max);
```

💡 **Hint**: 最初の要素をmaxとして初期化し、残りと比較する。

✅ **Solution**: `(A) 1`, `(B) >`, `(C) a[i]`

📝 **Explanation**: `max=a[0]`で初期化後、`i=1`から比較を開始（`(A)=1`）。現在の要素がmaxより大きければ（`>`）maxを更新する。最終的に9が出力される。

---

### M2. 最小値を求める穴埋め

```c
int a[] = {8, 3, 6, 1, 5};
int min = a[0];
for (int i = 1; i < 5; i++) {
    if (a[i] (A) min) {
        (B);
    }
}
printf("min=%d\n", min);
```

空欄を埋めよ。

💡 **Hint**: 最小値なので比較の向きが最大値と逆になる。

✅ **Solution**: `(A) <`, `(B) min = a[i]`

📝 **Explanation**: 最小値を探すには`<`で比較する。`min = a[i]`で新しい最小値を記録。出力は`min=1`。

---

### M3. 配列の総和と平均

```c
int a[] = {10, 20, 30, 40, 50};
int sum = 0;
for (int i = 0; i < 5; i++) {
    sum += a[i];
}
double avg = (A);
printf("sum=%d, avg=%.1f\n", sum, avg);
```

`(A)`を埋め、出力を答えよ。

💡 **Hint**: 整数同士の除算になるので型変換が必要。

✅ **Solution**: `(A) (double)sum / 5`、出力: `sum=150, avg=30.0`

📝 **Explanation**: `sum/5`だと整数除算で`30`になるが、`(double)sum/5`で`30.0`になる。平均計算では型変換を忘れずに。

---

### M4. strcpy の使い方

```c
#include <string.h>
char src[] = "transfer";
char dst[20];
strcpy((A), (B));
printf("%s\n", dst);
```

空欄を埋め、出力を答えよ。

💡 **Hint**: `strcpy(コピー先, コピー元)`の順序。

✅ **Solution**: `(A) dst`, `(B) src`、出力: `transfer`

📝 **Explanation**: `strcpy(dst, src)`でsrcの内容をdstにコピーする。引数の順序は「コピー先が第1引数」と覚える（`=`代入と同じ方向）。dstに十分なサイズが必要。

---

### M5. strcmp の使い方

```c
#include <string.h>
char a[] = "apple";
char b[] = "banana";
int result = strcmp(a, b);
if (result (A) 0) {
    printf("a < b\n");
} else if (result == 0) {
    printf("equal\n");
} else {
    printf("a > b\n");
}
```

空欄を埋め、出力を答えよ。

💡 **Hint**: `strcmp`は辞書順で小さいと負の値を返す。

✅ **Solution**: `(A) <`、出力: `a < b`

📝 **Explanation**: "apple"は辞書順で"banana"より前なので`strcmp`は負の値を返す。`< 0`で"a < b"が出力される。`strcmp`の戻り値は「差」であり、正/0/負で大小/等号を判定する。

---

### M6. 2D配列の行ごとの合計

```c
int a[3][4] = {
    {1, 2, 3, 4},
    {5, 6, 7, 8},
    {9, 10, 11, 12}
};
for (int i = 0; i < 3; i++) {
    int row_sum = 0;
    for (int j = 0; j < (A); j++) {
        row_sum += a[i][j];
    }
    printf("row%d: %d\n", i, row_sum);
}
```

空欄を埋め、出力を答えよ。

💡 **Hint**: 各行には4つの要素がある。

✅ **Solution**: `(A) 4`

出力:
```
row0: 10
row1: 26
row2: 42
```

📝 **Explanation**: 各行の合計：1+2+3+4=10、5+6+7+8=26、9+10+11+12=42。内側ループが列を、外側ループが行を制御する。

---

### M7. 2D配列の転置表示

```c
int a[2][3] = {{1,2,3},{4,5,6}};
for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 2; j++) {
        printf("%d ", a[j][i]);
    }
    printf("\n");
}
```

出力を答えよ。

💡 **Hint**: `a[j][i]`でj（行）とi（列）が入れ替わっている。

✅ **Solution**:
```
1 4 
2 5 
3 6 
```

📝 **Explanation**: 行と列を入れ替えてアクセスすることで転置を表示する。外側ループiが列を走り、内側ループjが行を走る。これは転置行列の各列を出力する。

---

### M8. 配列を関数に渡す

```c
void double_all(int a[], int n) {
    for (int i = 0; i < n; i++) {
        a[i] *= 2;
    }
}
int main() {
    int b[] = {1, 2, 3, 4};
    double_all(b, 4);
    for (int i = 0; i < 4; i++) {
        printf("%d ", b[i]);
    }
    return 0;
}
```

出力を答えよ。

💡 **Hint**: 配列は参照渡しなので、関数内での変更がmainに反映される。

✅ **Solution**: `2 4 6 8 `

📝 **Explanation**: C言語で配列を関数に渡すと、配列の先頭アドレスが渡される（参照渡し相当）。関数内での変更は元の配列に反映される。これはintの値渡しとは根本的に異なる。

---

### M9. 配列の要素数を関数に渡す

```c
int find_max(int a[], int n) {
    int max = a[0];
    for (int i = 1; i < n; i++) {
        if (a[i] > max) max = a[i];
    }
    return max;
}
int main() {
    int x[] = {5, 3, 8, 1, 7};
    printf("%d\n", find_max(x, 5));
    printf("%d\n", find_max(x, 3));
    return 0;
}
```

出力を答えよ。

💡 **Hint**: 2回目の呼び出しはx[0]〜x[2]の3要素のみを対象にする。

✅ **Solution**:
```
8
8
```

📝 **Explanation**: 1回目は全5要素の最大値=8。2回目は`n=3`なので`{5,3,8}`の最大値=8。関数はnで渡された要素数しか見ないため、配列サイズとnを正確に管理することが重要。

---

### M10. 文字列の逆順

```c
#include <string.h>
void reverse(char s[]) {
    int n = strlen(s);
    for (int i = 0; i < n/2; i++) {
        char tmp = s[i];
        s[i] = s[n-1-i];
        s[n-1-i] = tmp;
    }
}
int main() {
    char s[] = "exam";
    reverse(s);
    printf("%s\n", s);
    return 0;
}
```

出力を答えよ。

💡 **Hint**: "exam"は4文字、n/2=2回スワップする。

✅ **Solution**: `maxe`

📝 **Explanation**: `"exam"` は `e,x,a,m`（インデックス 0〜3）、n=4。ループは i=0,1 の2回。i=0: `swap(s[0]='e', s[3]='m')` → `"mxae"`。i=1: `swap(s[1]='x', s[2]='a')` → `"maxe"`。逆順完成。

---

## ★★★ Hard — 入試形式

### H1. バブルソートのトレースと穴埋め ← R8類題

次のバブルソートプログラムを完成させ、`{3,1,4,1,5}`をソートする各パスの状態を答えよ。

```c
void bubble_sort(int a[], int n) {
    for (int i = 0; i < n-1; i++) {
        for (int j = 0; j < (A); j++) {
            if (a[j] (B) a[j+1]) {
                int tmp = a[j];
                a[j] = (C);
                a[j+1] = tmp;
            }
        }
    }
}
```

(1) 空欄`(A)(B)(C)`を埋めよ。
(2) `a[]={3,1,4,1,5}`に対しi=0のパス後の状態を答えよ。
(3) 最終結果を答えよ。

💡 **Hint**: バブルソートは隣接要素を比較し、大きい方を右へ移動させる。

✅ **Solution**:
(1) `(A) n-1-i`, `(B) >`, `(C) a[j+1]`

(2) i=0パス（j=0〜3）:
- j=0: a[0]=3 > a[1]=1 → swap → {1,3,4,1,5}
- j=1: a[1]=3 < a[2]=4 → no swap → {1,3,4,1,5}
- j=2: a[2]=4 > a[3]=1 → swap → {1,3,1,4,5}
- j=3: a[3]=4 < a[4]=5 → no swap → {1,3,1,4,5}
**i=0後: {1,3,1,4,5}**

(3) 最終結果: **{1,1,3,4,5}**

📝 **Explanation**: `n-1-i`は各パスで末尾の確定済み要素を除外する。昇順ソートなので`>`で比較する。バブルソートの計算量はO(n²)。最大値が各パスで末尾に「バブルアップ」していく。

---

### H2. 線形探索の実装穴埋め ← R7類題

```c
int linear_search(int a[], int n, int key) {
    for (int i = (A); i < n; i++) {
        if ((B)) {
            return (C);
        }
    }
    return (D);
}
int main() {
    int a[] = {5, 3, 8, 1, 9, 2};
    int idx = linear_search(a, 6, 8);
    printf("index=%d\n", idx);
    idx = linear_search(a, 6, 7);
    printf("index=%d\n", idx);
    return 0;
}
```

(1) 空欄を埋めよ。
(2) 出力を答えよ。

💡 **Hint**: 見つかった場合はインデックスを、見つからない場合は-1を返す慣例。

✅ **Solution**:
(1) `(A) 0`, `(B) a[i] == key`, `(C) i`, `(D) -1`

(2)
```
index=2
index=-1
```

📝 **Explanation**: 線形探索は先頭から順に探索する。key=8はインデックス2に存在するので2を返す。key=7は存在しないので-1を返す。計算量はO(n)でシンプルだが大きなデータには不向き。

---

### H3. 値の出現回数カウント

配列内に特定の値が何回出現するかを返す関数`count_val`を実装せよ。

```c
int count_val(int a[], int n, int val) {
    // ここを実装
}
int main() {
    int a[] = {1, 2, 3, 2, 4, 2, 5};
    printf("%d\n", count_val(a, 7, 2));
    printf("%d\n", count_val(a, 7, 6));
}
```

期待出力:
```
3
0
```

💡 **Hint**: カウンタ変数を用意してマッチする度に加算する。

✅ **Solution**:
```c
int count_val(int a[], int n, int val) {
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (a[i] == val) count++;
    }
    return count;
}
```

📝 **Explanation**: `count`を0で初期化し、各要素がvalと一致すれば加算する。ループ完了後にcountを返す。2は{1,2,3,2,4,2,5}の中に3回出現し、6は出現しないので0。

---

### H4. strcpyを使わない配列コピー

`strcpy`を使わずに文字列をコピーする関数を実装せよ。null終端も正しくコピーすること。

```c
void my_strcpy(char dst[], const char src[]) {
    // ここを実装
}
int main() {
    char src[] = "university";
    char dst[20];
    my_strcpy(dst, src);
    printf("%s\n", dst);
}
```

💡 **Hint**: `\0`（ASCIIコード0）が出現するまでコピーを続ける。

✅ **Solution**:
```c
void my_strcpy(char dst[], const char src[]) {
    int i = 0;
    while (src[i] != '\0') {
        dst[i] = src[i];
        i++;
    }
    dst[i] = '\0';
}
```

📝 **Explanation**: `src[i] != '\0'`の条件でnull終端まで文字をコピーする。ループ終了後に`dst[i] = '\0'`を忘れると文字列の終端が設定されず未定義動作になる。これはstrcpyの内部動作そのもの。

---

### H5. 回文チェック

文字列が回文かどうかを判定する関数を実装せよ。回文なら1、そうでなければ0を返す。

```c
int is_palindrome(char s[]) {
    // ここを実装
}
int main() {
    printf("%d\n", is_palindrome("racecar"));
    printf("%d\n", is_palindrome("hello"));
    printf("%d\n", is_palindrome("a"));
}
```

期待出力: `1`, `0`, `1`

💡 **Hint**: 先頭と末尾から対称に比較し、中央で止まる。

✅ **Solution**:
```c
#include <string.h>
int is_palindrome(char s[]) {
    int n = strlen(s);
    for (int i = 0; i < n/2; i++) {
        if (s[i] != s[n-1-i]) return 0;
    }
    return 1;
}
```

📝 **Explanation**: `s[i]`と`s[n-1-i]`を比較して不一致なら即0を返す。n/2回だけ比較すれば十分（中央要素は自分自身と比較する必要がない）。"racecar"は7文字、i=0,1,2の3回比較で確認。

---

### H6. 2D行列の転置

`a[N][N]`を転置する関数（in-place）を実装せよ。

```c
#define N 3
void transpose(int a[N][N]) {
    // ここを実装
}
int main() {
    int a[N][N] = {{1,2,3},{4,5,6},{7,8,9}};
    transpose(a);
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) printf("%d ", a[i][j]);
        printf("\n");
    }
}
```

期待出力:
```
1 4 7 
2 5 8 
3 6 9 
```

💡 **Hint**: `a[i][j]`と`a[j][i]`をスワップする。重複スワップを防ぐため`j < i`（または`j > i`）の条件が必要。

✅ **Solution**:
```c
void transpose(int a[N][N]) {
    for (int i = 0; i < N; i++) {
        for (int j = i+1; j < N; j++) {
            int tmp = a[i][j];
            a[i][j] = a[j][i];
            a[j][i] = tmp;
        }
    }
}
```

📝 **Explanation**: `j = i+1`から開始することで、上三角成分のみをスワップする。`j = 0`から始めると同じペアが2回スワップされ元に戻ってしまう。対角成分（`i==j`）はスワップ不要。

---

### H7. 配列の左ローテーション

配列を左方向に1つシフトする関数を実装せよ（先頭が末尾に来る）。

```c
void rotate_left(int a[], int n) {
    // ここを実装
}
int main() {
    int a[] = {1, 2, 3, 4, 5};
    rotate_left(a, 5);
    for (int i = 0; i < 5; i++) printf("%d ", a[i]);
}
```

期待出力: `2 3 4 5 1 `

💡 **Hint**: 最初の要素を保存してから全体を左にずらし、最後に先頭の値を末尾に入れる。

✅ **Solution**:
```c
void rotate_left(int a[], int n) {
    int first = a[0];
    for (int i = 0; i < n-1; i++) {
        a[i] = a[i+1];
    }
    a[n-1] = first;
}
```

📝 **Explanation**: `first`に先頭を退避してからa[0]=a[1], a[1]=a[2],...と順にコピーする。最後に`a[n-1]=first`で元の先頭を末尾に置く。退避なしで進めると上書きされた値が失われる。

---

### H8. 2番目に大きい要素

配列から2番目に大きい値を返す関数を実装せよ（要素は全て異なると仮定）。

```c
int second_max(int a[], int n) {
    // ここを実装
}
int main() {
    int a[] = {3, 7, 1, 9, 4, 6};
    printf("%d\n", second_max(a, 6));
}
```

期待出力: `7`

💡 **Hint**: 最大値と2番目の最大値を同時に管理する。

✅ **Solution**:
```c
int second_max(int a[], int n) {
    int max1 = a[0], max2 = -1 << 30; // INT_MIN相当
    for (int i = 1; i < n; i++) {
        if (a[i] > max1) {
            max2 = max1;
            max1 = a[i];
        } else if (a[i] > max2) {
            max2 = a[i];
        }
    }
    return max2;
}
```

📝 **Explanation**: `max1`（最大値）と`max2`（2番目）を同時に追跡する。新しい要素がmax1より大きければmax2←max1→新値と更新。max1より小さくmax2より大きければmax2のみ更新。1回のパスO(n)で解決できる。

---

### H9. 母音カウントと単語逆順 ← R6類題

(1) 文字列中の母音数をカウントする関数を実装せよ。
(2) 単語（スペース区切り）を逆順にする関数を実装せよ（難）。

```c
#include <string.h>
int count_vowels(char s[]) {
    // ここを実装
}
int main() {
    printf("%d\n", count_vowels("niigata university"));
}
```

期待出力: `9`

💡 **Hint**: 母音は a,e,i,o,u。strchr()またはif条件で判定する。

✅ **Solution**:
```c
int count_vowels(char s[]) {
    int count = 0;
    for (int i = 0; s[i] != '\0'; i++) {
        char c = s[i];
        if (c=='a'||c=='e'||c=='i'||c=='o'||c=='u'||
            c=='A'||c=='E'||c=='I'||c=='O'||c=='U') {
            count++;
        }
    }
    return count;
}
```

"niigata university": n-**i**-**i**-g-**a**-t-**a** = 4, **u**-n-**i**-v-**e**-r-s-**i**-t-y = 5。合計9。

📝 **Explanation**: 文字列をnull終端まで走査し、各文字が母音かチェックする。大文字・小文字両対応が堅牢な実装。`'a'||'e'||...`のように複数条件を`||`でつなぐ。

---

### H10. ソート＋探索＋表示の統合問題

次のプログラムを完成させよ。バブルソートで昇順ソートし、指定値を線形探索する。

```c
#include <stdio.h>
void bubble_sort(int a[], int n) {
    for (int i = 0; i < n-1; i++)
        for (int j = 0; j < n-1-i; j++)
            if (a[j] > a[j+1]) {
                int t=a[j]; a[j]=a[j+1]; a[j+1]=t;
            }
}
int search(int a[], int n, int key) {
    for (int i = 0; i < n; i++)
        if (a[i] == key) return i;
    return -1;
}
int main() {
    int a[] = {5, 2, 8, 1, 9, 3};
    int n = 6;
    bubble_sort(a, n);
    printf("Sorted: ");
    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    printf("\n");
    int idx = search(a, n, 8);
    printf("8 is at index %d\n", idx);
    idx = search(a, n, 7);
    printf("7 is at index %d\n", idx);
    return 0;
}
```

出力を答えよ。

💡 **Hint**: ソート後の配列インデックスに注意。

✅ **Solution**:
```
Sorted: 1 2 3 5 8 9 
8 is at index 4
7 is at index -1
```

📝 **Explanation**: バブルソートで{5,2,8,1,9,3}→{1,2,3,5,8,9}。ソート後、8はインデックス4に移動している。7は元の配列にも存在しないので-1。ソート後の線形探索は正しいが、ソート済み配列なら二分探索がより効率的（O(log n)）。
