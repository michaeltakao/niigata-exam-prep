# L06 文字列 — char配列と文字列処理

> **重要度**: Tier 1 ★★ — R6・R7 に出題。逆順・コピー・比較が頻出。

---

## 1. コンセプト概要

C言語に「文字列型」は存在しません。文字列は **`char` の配列** に、末尾に **null文字 `'\0'`** を付けた形で表現します。

```
"hello" という文字列:

インデックス: [0] [1] [2] [3] [4] [5]
内容:          h   e   l   l   o  \0
                                   ↑
                              null文字（文字列の終わりを示す）
```

**null文字 `'\0'`** は数値では `0` と同じ。文字列を扱う関数はこれを「終わり」の目印として使います。

---

## 2. なぜ必要か

文字列処理はあらゆるプログラムの基本です：
- ユーザー名・パスワードの入力
- メッセージの表示・比較
- テキストの検索・置換

C言語では文字列を「char配列」として手動で操作することで、文字列の仕組みをより深く理解できます。この仕組みを知ることが、後のポインタ理解にも直結します。

---

## 3. 現実世界のアナロジー

### 文字列 → 封筒に入れた手紙

```
封筒（配列）:  [ h ][ e ][ l ][ l ][ o ][ \0 ]
               文字  文字  文字  文字  文字  封印マーク

"封印マーク（\0）がある場所が手紙の終わり"
郵便屋さん（printf, strlen 等の関数）はこのマークまで読む
```

### strlen → 文字列の長さを測るメジャー

```
strlen("hello") = 5

[ h ][ e ][ l ][ l ][ o ][ \0 ]
  1    2    3    4    5   ← 終わり（\0 は数えない）
```

### strcmp → 辞書の「どちらが先か」比較

```
strcmp("apple", "banana")
  → 'a' vs 'b': 'a' の ASCII コード (97) < 'b' (98)
  → 負の値を返す（apple が banana より「前」）

strcmp("hello", "hello")
  → 全文字一致
  → 0 を返す（等しい）
```

---

## 4. 構文説明

### 4-1. 文字列の宣言と初期化

```c
// 方法1: 文字列リテラルで初期化（最も一般的）
char s1[] = "hello";         // {'h','e','l','l','o','\0'} 自動的にサイズ6

// 方法2: サイズ指定（十分大きくする）
char s2[20] = "world";       // 残りは'\0'で埋まる

// 方法3: 手動で一文字ずつ設定
char s3[4];
s3[0] = 'h';
s3[1] = 'i';
s3[2] = '!';
s3[3] = '\0';   // ← 忘れずに！

// ポインタ版（注意: 変更不可）
char *s4 = "hello";   // リテラルへのポインタ。s4[0]='H' はNG（未定義動作）
```

### 4-2. 文字列の出力

```c
char s[] = "hello";

printf("%s\n", s);   // hello（文字列全体）
printf("%c\n", s[0]); // h（1文字）
puts(s);             // hello（改行付き）
putchar(s[1]);       // e（1文字、改行なし）
```

### 4-3. 文字列の入力

```c
char name[50];
printf("名前: ");
scanf("%s", name);   // ※ & は不要！（配列名がすでにアドレス）
                     // ※ スペースで区切られる → "hello world" → "hello" のみ
printf("こんにちは、%s\n", name);
```

### 4-4. 主要な文字列関数（`<string.h>` が必要）

```c
#include <string.h>

// strlen: 文字列の長さ（\0 を含まない）
size_t len = strlen("hello");   // 5

// strcpy: 文字列をコピー（コピー先は十分な大きさ必要）
char dst[20];
strcpy(dst, "hello");   // dst = "hello"

// strcmp: 文字列の比較
// 0=等しい, 負=s1<s2, 正=s1>s2
int cmp = strcmp("abc", "abc");   // 0
int cmp2 = strcmp("abc", "abd");  // 負（c<d）

// strcat: 文字列を末尾に追加（dst に十分な容量が必要）
char s[20] = "hello";
strcat(s, " world");   // s = "hello world"

// strncpy: サイズ制限付きコピー（安全版）
strncpy(dst, "hello", sizeof(dst) - 1);
dst[sizeof(dst) - 1] = '\0';   // 終端を保証
```

### 4-5. 文字の手動操作

```c
char s[] = "hello";

// 文字を一文字ずつ処理（\0 まで）
for (int i = 0; s[i] != '\0'; i++) {
    printf("%c", s[i]);   // h e l l o
}

// または while ループで
int i = 0;
while (s[i] != '\0') {
    putchar(s[i]);
    i++;
}
```

---

## 5. ステップ実行トレース

```c
#include <stdio.h>
#include <string.h>
int main() {
    char s1[] = "hello";
    char s2[20];

    printf("長さ: %zu\n", strlen(s1));
    strcpy(s2, s1);
    s2[0] = 'H';
    printf("s1: %s\n", s1);
    printf("s2: %s\n", s2);
    printf("比較: %d\n", strcmp(s1, s2));
    return 0;
}
```

### 行ごとのトレース

**宣言後**:
```
s1: [ h ][ e ][ l ][ l ][ o ][\0 ]
     [0]  [1]  [2]  [3]  [4]  [5]

s2: [?? ][ ?? ][ ?? ]...（未初期化）
```

**`strlen(s1)` → 5** を出力:
```
h→e→l→l→o→\0 で止まる → 5文字
出力: 長さ: 5
```

**`strcpy(s2, s1)` 後**:
```
s2: [ h ][ e ][ l ][ l ][ o ][\0 ][ ?? ][ ?? ]...
     [0]  [1]  [2]  [3]  [4]  [5]
     ← s1と同じ内容がコピーされた
```

**`s2[0] = 'H'` 後**:
```
s1: [ h ][ e ][ l ][ l ][ o ][\0 ]   （変更なし）
s2: [ H ][ e ][ l ][ l ][ o ][\0 ]   （s2[0]だけ変わった）
     ↑ 'H' に変更
```

**`printf("s1: %s", s1)` → `s1: hello`**

**`printf("s2: %s", s2)` → `s2: Hello`**

**`strcmp(s1, s2)`**:
```
比較: s1="hello", s2="Hello"
s1[0]='h'(104) vs s2[0]='H'(72)
104 > 72 → s1 > s2 → 正の値（例: 32）を返す
出力: 比較: 32
```

**最終出力**:
```
長さ: 5
s1: hello
s2: Hello
比較: 32
```

---

## 6. 視覚的メモリ図

### "hello" のメモリ配置

```
char s[] = "hello";

アドレス  内容  インデックス  意味
 0x100:  'h'    s[0]        'h' (ASCII 104)
 0x101:  'e'    s[1]        'e' (ASCII 101)
 0x102:  'l'    s[2]        'l' (ASCII 108)
 0x103:  'l'    s[3]        'l' (ASCII 108)
 0x104:  'o'    s[4]        'o' (ASCII 111)
 0x105:  '\0'   s[5]        終端文字 (数値 0)
```

### strlen の動作イメージ

```
strlen("hello"):

start → [ h ]→[ e ]→[ l ]→[ l ]→[ o ]→[ \0 ] STOP
カウント:  1     2     3     4     5     終了

戻り値: 5
```

### strcpy の動作イメージ

```
strcpy(dst, src):

src: [ h ][ e ][ l ][ l ][ o ][ \0 ]
      ↓    ↓    ↓    ↓    ↓    ↓
dst: [ h ][ e ][ l ][ l ][ o ][ \0 ][ ?  ][ ?  ]...
     （\0 もコピーされることが重要）
```

---

## 7. よくある間違い

### 間違い1: null 終端文字 `\0` を忘れる

```c
// ❌ 間違い: \0 がないので文字列の終わりが不明
char s[5];
s[0] = 'h'; s[1] = 'i'; s[2] = '!';
// s[3] は未初期化 → printf("%s", s) は予測不能な動作

// ✅ 正解: 必ず \0 を付ける
char s[5];
s[0] = 'h'; s[1] = 'i'; s[2] = '!'; s[3] = '\0';
```

### 間違い2: `==` で文字列を比較する

```c
char s[] = "hello";

// ❌ 間違い: これはアドレスの比較であり、内容の比較ではない
if (s == "hello") {   // 常に false（異なるメモリ領域）
    printf("同じ\n");
}

// ✅ 正解: strcmp を使う
if (strcmp(s, "hello") == 0) {
    printf("同じ\n");
}
```

### 間違い3: strcpy の宛先が小さすぎる（バッファオーバーフロー）

```c
// ❌ 間違い: dst が小さすぎて overflow
char dst[3];
strcpy(dst, "hello");   // 危険！dst に6バイト必要なのに3バイトしかない

// ✅ 正解: 宛先は十分に大きくする
char dst[20];
strcpy(dst, "hello");   // OK
```

### 間違い4: strlen の戻り値の型ミス

```c
// ❌ 間違い: strlen は size_t（符号なし整数）を返す
// strlen("") - 1 は size_t の 0 - 1 = 非常に大きな正の数になる！
int len = strlen(s);    // 技術的にはOKだが...
if (strlen(s) - 1 >= 0) {   // 常に true（符号なし同士の比較）
    // 空文字列でも実行されてしまう
}

// ✅ 正解: int にキャストするか、0との比較で回避
int len = (int)strlen(s);
if (len > 0) { ... }
```

### 間違い5: 文字列リテラルを変更しようとする

```c
// ❌ 間違い: ポインタが指す文字列リテラルは変更不可
char *s = "hello";
s[0] = 'H';   // 未定義動作（クラッシュする可能性がある）

// ✅ 正解: char 配列を使う
char s[] = "hello";
s[0] = 'H';   // OK → "Hello"
```

---

## 8. ミニクイズ

**Q1.** `strlen("programming")` の戻り値を答えよ。
<details><summary>答え</summary>
`11`（p-r-o-g-r-a-m-m-i-n-g の11文字。'\0'は数えない）
</details>

**Q2.** 次のコードで出力される文字は何か。
```c
char s[] = "exam";
printf("%c\n", s[2]);
```
<details><summary>答え</summary>
`a`（インデックス: s[0]='e', s[1]='x', s[2]='a', s[3]='m'）
</details>

**Q3.** 空欄を埋めよ。2つの文字列が等しいかどうか判定するコード：
```c
char a[] = "hello";
char b[] = "hello";
if ((A) == 0) {
    printf("等しい\n");
}
```
<details><summary>答え</summary>
`(A)` = `strcmp(a, b)`
</details>

**Q4.** 次のコードの出力を答えよ。
```c
char s[] = "hello";
int count = 0;
for (int i = 0; s[i] != '\0'; i++) {
    count++;
}
printf("%d\n", count);
```
<details><summary>答え</summary>
`5`（strlen と同じ動作。h,e,l,l,o の5文字を数える）
</details>

**Q5.** `strcpy(dst, src)` を使う際に `dst` の大きさはどう決めるべきか。
<details><summary>答え</summary>
`strlen(src) + 1` 以上の大きさが必要。`+1` は null 終端文字 `'\0'` のため。
</details>

---

## 9. 例題

### 例題1: 母音の個数をカウント

```c
#include <stdio.h>
#include <string.h>
int main() {
    char s[] = "programming";
    int count = 0;

    for (int i = 0; s[i] != '\0'; i++) {
        char c = s[i];
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
            count++;
        }
    }
    printf("母音の数: %d\n", count);   // 3 (o,a,i)
    return 0;
}
```

---

### 例題2: 文字列を大文字に変換

```c
#include <stdio.h>
int main() {
    char s[] = "hello, world!";

    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] >= 'a' && s[i] <= 'z') {
            s[i] = s[i] - 'a' + 'A';   // 小文字を大文字に
            // 例: 'h'(104) - 'a'(97) + 'A'(65) = 72 = 'H'
        }
    }
    printf("%s\n", s);   // HELLO, WORLD!
    return 0;
}
```

**仕組み**:
```
'a'のASCIIコード = 97
'A'のASCIIコード = 65
差 = 32

'h'(104) - 32 = 72 = 'H'
's'(115) - 32 = 83 = 'S'
```

---

### 例題3: 文字列の回文チェック

```c
#include <stdio.h>
#include <string.h>
int main() {
    char s[] = "racecar";
    int n = (int)strlen(s);
    int is_palindrome = 1;   // 1=true

    for (int i = 0; i < n / 2; i++) {
        if (s[i] != s[n - 1 - i]) {
            is_palindrome = 0;   // 一致しない文字があれば false
            break;
        }
    }

    if (is_palindrome) {
        printf("\"%s\" は回文です\n", s);
    } else {
        printf("\"%s\" は回文ではありません\n", s);
    }
    return 0;
}
```

**比較の様子** (`"racecar"`, n=7):
```
i=0: s[0]='r' vs s[6]='r' → 一致 ✓
i=1: s[1]='a' vs s[5]='a' → 一致 ✓
i=2: s[2]='c' vs s[4]='c' → 一致 ✓
i=3: n/2=3 なのでここでループ終了（中央文字は比較不要）
→ 回文！
```

---

## 10. 新潟大学試験との関連

> **文字列処理は R6、R7 に出題。逆順・コピー・比較がよく出る。**

**R6 出題パターン**: 文字列をポインタで操作するプログラムの出力と実装。
**R7 出題パターン**: 文字列関数（strlen、strcpy、strcmp）の使い方。

**試験で問われやすいパターン**:
1. `strlen` の結果（\0 を含まない長さ）
2. `strcmp` の戻り値（0=等しい、負/正=大小関係）
3. 文字列の逆順（インデックス版・ポインタ版）
4. 文字の ASCII コードを使った大文字/小文字変換
5. 文字列中の特定文字をカウント

**次のステップ**: 文字列とポインタは密接に関連している。`L08_pointers.md` でポインタを学ぶと、`char *s = "hello"` や `char *p = s; while (*p != '\0') { p++; }` といったポインタを使った文字列操作が理解できるようになる。

**対策**: `03_drills/L5_arrays.md` の M4〜M5（文字列関数）と H9（文字列処理）を解くこと。
