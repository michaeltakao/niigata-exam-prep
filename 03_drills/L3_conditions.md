---
title: L3 条件分岐 ドリル
level: L3
topics: [if/else, switch/case, nested conditions, boundary conditions, debug]
---

# L3 条件分岐 ドリル

---

## ★ Easy（直接トレース）

### E1. 基本 if-else

**問題:** 次のプログラムの出力を書け（x=7）。

```c
#include <stdio.h>
int main() {
    int x = 7;
    if (x > 5) {
        printf("big\n");
    } else {
        printf("small\n");
    }
    return 0;
}
```

💡 **ヒント:** 7 > 5 は真か偽か。

✅ **解答:** `big`

📝 **解説:** `7 > 5` は真なので if ブロックの `printf("big\n")` が実行される。else ブロックはスキップされる。

---

### E2. else if 分岐

**問題:** 次のプログラムの出力を書け（score=75）。

```c
#include <stdio.h>
int main() {
    int score = 75;
    if (score >= 90) {
        printf("A\n");
    } else if (score >= 70) {
        printf("B\n");
    } else if (score >= 50) {
        printf("C\n");
    } else {
        printf("F\n");
    }
    return 0;
}
```

💡 **ヒント:** 上から順に条件を評価し、最初に真になった分岐だけ実行される。

✅ **解答:** `B`

📝 **解説:** `75>=90` は偽 → スキップ。`75>=70` は真 → `"B"` を出力してブロック終了。残りの else if と else は評価されない。

---

### E3. 境界値の確認

**問題:** 次のプログラムで、x=70 と x=69 のときの出力をそれぞれ書け。

```c
if (x >= 70) printf("pass\n");
else         printf("fail\n");
```

💡 **ヒント:** `>=` は「以上」なので等しい場合も含む。

✅ **解答:** x=70 → `pass`, x=69 → `fail`

📝 **解説:** `70>=70` は真（等しいので「以上」に含まれる）。`69>=70` は偽。境界値（70）での挙動に注意。`>` と `>=` の違いは試験で問われやすい。

---

### E4. ネスト if

**問題:** 次のプログラムの出力を書け（x=5, y=3）。

```c
#include <stdio.h>
int main() {
    int x = 5, y = 3;
    if (x > 0) {
        if (y > 0) {
            printf("both positive\n");
        } else {
            printf("x positive only\n");
        }
    } else {
        printf("x not positive\n");
    }
    return 0;
}
```

💡 **ヒント:** 外側の if が真なら内側の if を評価する。

✅ **解答:** `both positive`

📝 **解説:** `x=5>0` 真 → 内側へ進む。`y=3>0` 真 → `"both positive"` を出力。両方の条件が真のときだけ最内側のブロックが実行される。

---

### E5. ネスト if（片方偽）

**問題:** 次のプログラムを x=5, y=-1 で実行したときの出力を書け。

```c
if (x > 0) {
    if (y > 0) printf("A\n");
    else       printf("B\n");
} else {
    printf("C\n");
}
```

💡 **ヒント:** 外側が真、内側が偽。どちらの else が対応するか。

✅ **解答:** `B`

📝 **解説:** `x=5>0` 真 → 外側 if に入る。`y=-1>0` 偽 → 内側 else の `"B"` を実行。`else` は最も近い `if` に対応する（ぶら下がり else）。

---

### E6. switch 基本

**問題:** 次のプログラムの出力を書け（day=3）。

```c
#include <stdio.h>
int main() {
    int day = 3;
    switch (day) {
        case 1: printf("Mon\n"); break;
        case 2: printf("Tue\n"); break;
        case 3: printf("Wed\n"); break;
        case 4: printf("Thu\n"); break;
        default: printf("Other\n");
    }
    return 0;
}
```

💡 **ヒント:** switch は day の値に一致する case にジャンプする。

✅ **解答:** `Wed`

📝 **解説:** `day=3` なので `case 3:` にジャンプし `"Wed"` を出力。`break` により switch ブロックを抜ける。一致しない case は実行されない。

---

### E7. switch と default

**問題:** 次のプログラムの出力を書け（x=7）。

```c
switch (x) {
    case 1: printf("one\n"); break;
    case 2: printf("two\n"); break;
    default: printf("other: %d\n", x);
}
```

💡 **ヒント:** どの case にも一致しないときは default が実行される。

✅ **解答:** `other: 7`

📝 **解説:** x=7 はどの case にも一致しないので `default:` が実行される。`default` に `break` がなくても case がないので switch の最後に達して終了する。

---

### E8. switch フォールスルー

**問題:** 次のプログラムの出力を書け（n=2）。

```c
switch (n) {
    case 1:
    case 2:
        printf("one or two\n");
        break;
    case 3:
        printf("three\n");
        break;
}
```

💡 **ヒント:** case 1: に `break` がないので、n=1 でも case 2: のコードが実行される。

✅ **解答:** `one or two`

📝 **解説:** `n=2` → `case 2:` にジャンプ → `"one or two"` を出力 → `break` で終了。`case 1:` は `break` がないので n=1 でも `case 2:` のコードにフォールスルー（fall-through）する。これは「1 か 2 のとき同じ処理」を書く慣用パターン。

---

### E9. if-else if チェーン

**問題:** 次のプログラムを n=0, n=1, n=2, n=3 それぞれで実行したときの出力を書け。

```c
if      (n == 1) printf("one\n");
else if (n == 2) printf("two\n");
else if (n == 3) printf("three\n");
else             printf("other\n");
```

💡 **ヒント:** 上から順に評価し、最初に一致したものだけ実行。

✅ **解答:**
- n=0 → `other`
- n=1 → `one`
- n=2 → `two`
- n=3 → `three`

📝 **解説:** n=0 は n==1, n==2, n==3 いずれも偽 → else の `"other"`。n=1〜3 は対応する case が真になり該当文字列を出力。

---

### E10. 条件の複合

**問題:** 次のプログラムの出力を書け（a=3, b=7）。

```c
#include <stdio.h>
int main() {
    int a = 3, b = 7;
    if (a > 0 && b > 0) {
        if (a + b > 8) printf("large sum\n");
        else           printf("small sum\n");
    } else {
        printf("non-positive\n");
    }
    return 0;
}
```

💡 **ヒント:** まず外側の条件を評価し、次に内側。

✅ **解答:** `large sum`

📝 **解説:** `3>0&&7>0=1` → 内側へ。`3+7=10>8=1` → `"large sum"`。a=3, b=5 なら `3+5=8>8` は偽（8>8 ではない）→ `"small sum"`。

---

## ★★ Medium（穴埋め・デバッグ）

### M1. 条件の穴埋め（1）

**問題:** 次のコードが「n が偶数なら `even`、奇数なら `odd`」を出力するよう空欄を埋めよ。

```c
if ((A)) {
    printf("even\n");
} else {
    printf("odd\n");
}
```

💡 **ヒント:** 偶数の定義は 2 で割り切れること。

✅ **解答:** `(A) = n % 2 == 0`

📝 **解説:** `n % 2` は n を 2 で割った余り。偶数なら余り 0、奇数なら余り 1。`n % 2 == 0` が偶数の条件。

---

### M2. 条件の穴埋め（2）

**問題:** 次のコードが「閏年かどうか」を判定するよう空欄を埋めよ。
閏年の条件: 4で割り切れる AND (100で割り切れない OR 400で割り切れる)

```c
if ((A) && (!(B) || (C))) {
    printf("leap year\n");
}
```

💡 **ヒント:** 各条件は `year % n == 0` の形。

✅ **解答:** `(A) = year % 4 == 0`, `(B) = year % 100 == 0`, `(C) = year % 400 == 0`

📝 **解説:** 閏年ルール: 4の倍数、ただし100の倍数は除く、ただし400の倍数は含む。例: 2000年 → 400の倍数 → 閏年。1900年 → 4の倍数かつ100の倍数かつ400の倍数でない → 閏年でない。

---

### M3. 範囲条件の穴埋め

**問題:** 「x が 10 以上 20 以下」を正しく判定する条件を書け。以下の5つのうち正しいものを選び、なぜ間違いかを説明せよ。

```
(a) 10 <= x <= 20
(b) x >= 10 && x <= 20
(c) x >= 10 || x <= 20
(d) 10 <= x && x <= 20
(e) !(x < 10 || x > 20)
```

💡 **ヒント:** (a) は C言語では意図した動作にならない。

✅ **解答:** 正しいのは **(b), (d), (e)** の3つ。

📝 **解説:**  
(a) `10<=x` が 0 or 1 になり、`1<=20` 常に真 → 常に true（バグ）。  
(b) ✓ x が10以上かつ20以下。  
(c) ✗ OR なのでほぼ常に真（x<10 でも x<=20=true になる等）。正確には x∈(-∞,20]∪[10,+∞)=全数。  
(d) ✓ (b) と等価。  
(e) ✓ ド・モルガン: `!(x<10||x>20) = x>=10&&x<=20`。

---

### M4. バグ発見: == vs =

**問題:** 次のコードにバグがある。バグを特定して修正せよ。

```c
int x;
scanf("%d", &x);
if (x = 0) {
    printf("zero\n");
} else {
    printf("non-zero\n");
}
```

💡 **ヒント:** `=` と `==` の違いを確認。

✅ **解答:** `if (x = 0)` → `if (x == 0)` に修正。

📝 **解説:** `x = 0` は「x に 0 を代入する式」で値は 0（偽）。常に else 分岐に入る。意図は「x が 0 かどうか比較する」ので `==` を使う。このバグはコンパイラ警告 `warning: suggest parentheses around assignment` で検出できる。

---

### M5. バグ発見: 境界値

**問題:** 次のコードは「60点以上を合格」にしたいが、バグがある。修正せよ。

```c
if (score > 60) printf("pass\n");
else            printf("fail\n");
```

💡 **ヒント:** score=60 のとき、この条件は？

✅ **解答:** `>` → `>=` に修正: `if (score >= 60)`

📝 **解説:** `score > 60` は「60より大きい」なので、score=60 のとき偽となり `fail` が出力されてしまう。`>=` は「60以上」なので score=60 も合格になる。境界値（60点ぴったり）のテストが重要。

---

### M6. 真偽値テーブル

**問題:** 次の条件 `(x > 0 && y < 0) || (x < 0 && y > 0)` は何を表しているか？ x, y の組み合わせで真偽を確認せよ。

| x  | y  | 結果 |
|----|----|----|
| 5  | -3 | ?  |
| 5  |  3 | ?  |
| -5 | -3 | ?  |
| -5 |  3 | ?  |
| 0  |  3 | ?  |

💡 **ヒント:** この条件は「x と y が異符号」を表している？

✅ **解答:**

| x  | y  | 結果 |
|----|----|----|
| 5  | -3 | 1（真） |
| 5  |  3 | 0（偽） |
| -5 | -3 | 0（偽） |
| -5 |  3 | 1（真） |
| 0  |  3 | 0（偽） |

📝 **解説:** この条件は「x と y が異符号（片方正、片方負）のとき真」。x=0 は正でも負でもないので偽。`x * y < 0` とも書ける（積が負 = 異符号）。ただし overflow に注意。

---

### M7. switch を if に書き換え

**問題:** 次の switch 文を等価な if-else if 文に書き換えよ。

```c
switch (grade) {
    case 'A': points = 4; break;
    case 'B': points = 3; break;
    case 'C': points = 2; break;
    default:  points = 0;
}
```

💡 **ヒント:** 各 case が一つの else if に対応する。

✅ **解答:**
```c
if      (grade == 'A') points = 4;
else if (grade == 'B') points = 3;
else if (grade == 'C') points = 2;
else                   points = 0;
```

📝 **解説:** `case 'A':` は `grade == 'A'` に対応。`default:` は最後の `else` に対応。switch は整数/文字の一致判定に特化しているが、if-else で完全に等価に書ける。

---

### M8. if を switch に書き換え

**問題:** 次の if 文を switch 文に書き換えよ。

```c
if      (n == 1) printf("January");
else if (n == 2) printf("February");
else if (n == 3) printf("March");
else             printf("Unknown");
```

💡 **ヒント:** 各 if (n == k) が `case k:` に対応する。

✅ **解答:**
```c
switch (n) {
    case 1: printf("January");  break;
    case 2: printf("February"); break;
    case 3: printf("March");    break;
    default: printf("Unknown");
}
```

📝 **解説:** 整数の等値比較は switch で書くと読みやすい。`break` を忘れるとフォールスルーが起きるので注意。範囲比較（`n > 5`）は switch では書けないので if を使う。

---

### M9. 条件の順序

**問題:** 次の2つのコードの違いを説明し、入力が `-5` のとき両方の出力を書け。

**コードA:**
```c
if (x > 0)       printf("positive\n");
if (x < 0)       printf("negative\n");
if (x == 0)      printf("zero\n");
```

**コードB:**
```c
if      (x > 0)  printf("positive\n");
else if (x < 0)  printf("negative\n");
else             printf("zero\n");
```

💡 **ヒント:** コードAは3つの独立した if 文、コードBは1つの if-else if チェーン。

✅ **解答:** 両コードとも x=-5 のとき `negative` を出力。しかし挙動は異なる: コードAでは3つの条件を全部評価する（x が変化したら複数行が出力される可能性）。コードBは最初に真の条件だけ実行して残りをスキップ。

📝 **解説:** コードAは「排他的に見えるが実は独立した3条件」。x の値が変化しない限り同じだが、コードBの方が「場合分け」の意図を明確に表現できる。試験では「else if を使った方が正しい」と書けばよい。

---

### M10. フォールスルーの利用

**問題:** 次のプログラムの出力を書け（month=8）。

```c
int days;
switch (month) {
    case 1: case 3: case 5: case 7:
    case 8: case 10: case 12:
        days = 31; break;
    case 4: case 6: case 9: case 11:
        days = 30; break;
    case 2:
        days = 28; break;
}
printf("days = %d\n", days);
```

💡 **ヒント:** 複数の case をまとめるフォールスルーのパターン。

✅ **解答:** `days = 31`

📝 **解説:** month=8 は `case 8:` にジャンプ。直後に `case 10:` や `case 12:` もあるが `break` なし。ただし同一グループの最後の case は `days=31; break;` につながる。これは「複数の値で同じ処理」を表す慣用パターン。

---

## ★★★ Hard（入試形式）

### H1. 境界値の多重判定

**問題:** 次のプログラムの出力を score=60, 70, 79, 80, 100 それぞれで求めよ。

```c
char grade;
if (score < 60)       grade = 'F';
else if (score < 70)  grade = 'D';
else if (score < 80)  grade = 'C';
else if (score < 90)  grade = 'B';
else                  grade = 'A';
printf("%c\n", grade);
```

💡 **ヒント:** 各境界（60, 70, 80, 90）でどちらの分岐に入るか確認。

✅ **解答:**
- 60 → `D`（60<60偽→60<70真）
- 70 → `C`
- 79 → `C`
- 80 → `B`
- 100 → `A`

📝 **解説:** `score < 60` は「60未満」なので score=60 は偽 → 次へ。`score < 70` は「70未満」なので score=60 は真 → `'D'`。境界値（ちょうどの値）では `<` と `<=` のどちらを使うかで結果が変わる。

---

### H2. ネストしたトレース

**問題:** 次のプログラムで (x, y) = (3, 3), (5, 3), (3, 7), (5, 7) それぞれの出力を書け。

```c
if (x > 4) {
    if (y > 5) printf("A\n");
    else       printf("B\n");
} else {
    if (y > 5) printf("C\n");
    else       printf("D\n");
}
```

💡 **ヒント:** 2×2 の場合分け表を作ると整理しやすい。

✅ **解答:**
- (3, 3) → `D`（外偽→内偽）
- (5, 3) → `B`（外真→内偽）
- (3, 7) → `C`（外偽→内真）
- (5, 7) → `A`（外真→内真）

📝 **解説:**
| x>4 | y>5 | 出力 |
|-----|-----|------|
| 偽  | 偽  | D    |
| 真  | 偽  | B    |
| 偽  | 真  | C    |
| 真  | 真  | A    |

ネストした if は表で整理すると見落としを防げる。

---

### H3. switch フォールスルーのトレース

**問題:** 次のプログラムを n=2 で実行したときの出力をすべて書け。

```c
switch (n) {
    case 1:
        printf("one\n");
    case 2:
        printf("two\n");
    case 3:
        printf("three\n");
        break;
    case 4:
        printf("four\n");
}
```

💡 **ヒント:** `break` がない case は次の case にフォールスルーする。

✅ **解答:**
```
two
three
```

📝 **解説:** n=2 → `case 2:` にジャンプ → `"two"` 出力。`break` がないので `case 3:` にフォールスルー → `"three"` 出力。`break` に達して終了。case 1 は実行されない（ジャンプしていないから）。`case 4:` は `case 3:` の `break` で到達しない。

---

### H4. FizzBuzz 実装

**問題:** 1から20まで順に出力するプログラムを書け。
- 3の倍数のとき `Fizz`
- 5の倍数のとき `Buzz`
- 15の倍数のとき `FizzBuzz`
- それ以外はその数

```c
#include <stdio.h>
int main() {
    for (int i = 1; i <= 20; i++) {
        // ここを実装せよ
    }
    return 0;
}
```

💡 **ヒント:** 15の倍数チェックを先に行うこと。

✅ **解答:**
```c
#include <stdio.h>
int main() {
    for (int i = 1; i <= 20; i++) {
        if (i % 15 == 0)      printf("FizzBuzz\n");
        else if (i % 3 == 0)  printf("Fizz\n");
        else if (i % 5 == 0)  printf("Buzz\n");
        else                  printf("%d\n", i);
    }
    return 0;
}
```

📝 **解説:** 15の倍数を先にチェックする。`i % 3 == 0` を先に書くと15も "Fizz" と判定されてしまう（15%3=0）。試験ではこの順序を問われることが多い。

---

### H5. 成績評価システム

**問題:** 次の仕様を満たすプログラムを書け。
- 点数（0〜100）を入力
- 90以上: "Excellent", 70以上: "Good", 50以上: "Pass", それ未満: "Fail"
- 範囲外（0未満または100超）: "Invalid"

```c
#include <stdio.h>
int main() {
    int score;
    scanf("%d", &score);
    // ここを実装
}
```

💡 **ヒント:** 範囲外チェックを最初に行う。

✅ **解答:**
```c
#include <stdio.h>
int main() {
    int score;
    scanf("%d", &score);
    if (score < 0 || score > 100) {
        printf("Invalid\n");
    } else if (score >= 90) {
        printf("Excellent\n");
    } else if (score >= 70) {
        printf("Good\n");
    } else if (score >= 50) {
        printf("Pass\n");
    } else {
        printf("Fail\n");
    }
    return 0;
}
```

📝 **解説:** 入力検証（Invalid チェック）を先に行う設計が堅牢。その後は高い点数から順に判定する（低い点数から判定すると全員が最初の条件に引っかかる）。

---

### H6. 曜日判定プログラム

**問題:** 次の仕様を switch 文を使って実装せよ。
- 1→月, 2→火, 3→水, 4→木, 5→金: "Weekday"
- 6, 7: "Weekend"
- それ以外: "Invalid"

```c
#include <stdio.h>
int main() {
    int day;
    scanf("%d", &day);
    switch (day) {
        // ここを実装
    }
    return 0;
}
```

💡 **ヒント:** 複数の case を同じ処理にまとめるフォールスルーを活用。

✅ **解答:**
```c
#include <stdio.h>
int main() {
    int day;
    scanf("%d", &day);
    switch (day) {
        case 1: case 2: case 3: case 4: case 5:
            printf("Weekday\n");
            break;
        case 6: case 7:
            printf("Weekend\n");
            break;
        default:
            printf("Invalid\n");
    }
    return 0;
}
```

📝 **解説:** 1〜5 はフォールスルーで同じ処理にまとめる。6, 7 も同様。default で範囲外を処理。switch のフォールスルーを意図的に使う典型パターン。

---

### H7. 条件とループの組み合わせ

**問題:** 1から100までの整数のうち、3の倍数かつ5の倍数でないものの個数を数えるプログラムを書け。

```c
#include <stdio.h>
int main() {
    int count = 0;
    for (int i = 1; i <= 100; i++) {
        // ここを実装
    }
    printf("%d\n", count);
    return 0;
}
```

💡 **ヒント:** 「3の倍数かつ5の倍数でない」= `i%3==0 && i%5!=0`。

✅ **解答:**
```c
#include <stdio.h>
int main() {
    int count = 0;
    for (int i = 1; i <= 100; i++) {
        if (i % 3 == 0 && i % 5 != 0) {
            count++;
        }
    }
    printf("%d\n", count);
    return 0;
}
```

出力: `27`

📝 **解説:** 1〜100で3の倍数は33個（3,6,9,...,99）。そのうち15の倍数（3かつ5の倍数）は6個（15,30,45,...,90）。33-6=27個。条件の組み合わせ `&&` と `!=` を正確に使う。

---

### H8. 最大・最小の判定

**問題:** 3つの整数 a, b, c を入力して最大値と最小値を出力するプログラムを書け。

```c
#include <stdio.h>
int main() {
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);
    int max, min;
    // ここを実装
    printf("max=%d min=%d\n", max, min);
    return 0;
}
```

💡 **ヒント:** 最大値: a, b の大きい方と c を比較。最小値も同様。

✅ **解答:**
```c
#include <stdio.h>
int main() {
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);
    int max = (a > b) ? a : b;
    if (c > max) max = c;
    int min = (a < b) ? a : b;
    if (c < min) min = c;
    printf("max=%d min=%d\n", max, min);
    return 0;
}
```

📝 **解説:** まず a と b を比較して仮の max/min を求め、次に c と比較して更新する。三項演算子で2値の比較を簡潔に書いてから、3値目を if で更新するパターン。

---

### H9. 複雑な条件のトレース

**問題:** 次のプログラムを a=4, b=6, c=3 で実行したとき出力をすべて書け。

```c
#include <stdio.h>
int main() {
    int a = 4, b = 6, c = 3;
    
    if (a < b && b < c) printf("ascending\n");
    else if (a > b && b > c) printf("descending\n");
    else printf("other\n");
    
    if (a % 2 == 0 && b % 2 == 0) {
        printf("both even\n");
    } else if (a % 2 != 0 && b % 2 != 0) {
        printf("both odd\n");
    } else {
        printf("mixed\n");
    }
    
    printf("%d\n", (a > c) ? (b - c) : (b + c));
    return 0;
}
```

💡 **ヒント:** 3つの独立した判定を順番に実行する。

✅ **解答:**
```
other
mixed
3
```

📝 **解説:**  
1: `4<6=1` かつ `6<3=0` → 偽 → `4>6=0` → else → `"other"`  
2: `4%2=0` (even), `6%2=0` (even) → both even... 待って `a=4` (even), `b=6` (even) → `"both even"` ✓  

修正: a=4(偶数), b=6(偶数) → 両方偶数 → `"both even"` が正しい出力。

3: `a > c` → `4>3=1` → `b-c = 6-3 = 3`

✅ **修正解答:**
```
other
both even
3
```

---

### H10. ← 入試形式 総合条件判定問題

**問題:** 次のプログラムについて (1)〜(4) に答えよ。

```c
#include <stdio.h>
int main() {
    int x, y;
    scanf("%d %d", &x, &y);
    
    // (1) x, y = 3, 7 のとき出力は？
    if (x + y > 8 && x * y > 15) printf("A\n");
    else if (x + y > 8 || x * y > 15) printf("B\n");
    else printf("C\n");
    
    // (2) x = 12 のとき出力は？
    switch (x % 4) {
        case 0: printf("zero\n"); break;
        case 1: printf("one\n"); break;
        case 2: printf("two\n"); break;
        case 3: printf("three\n"); break;
    }
    
    // (3) x=5, y=3 のとき、関数の戻り値は？
    // int result = (x > y) ? (x - y) : (y - x);
    
    // (4) 次のif文に等価なswitch文を書け
    // if (x==1||x==3||x==5||x==7||x==9) printf("odd\n");
    
    return 0;
}
```

💡 **ヒント:** (1) 各条件を計算してから論理演算。(2) 12 % 4 = ?。

✅ **解答:**

**(1)** x=3, y=7: `x+y=10>8=真`, `x*y=21>15=真` → `A`

**(2)** x=12: `12%4=0` → `"zero"`

**(3)** x=5, y=3: `5>3=真` → `x-y=2`、result=2

**(4)**
```c
switch (x) {
    case 1: case 3: case 5: case 7: case 9:
        printf("odd\n"); break;
}
```

📝 **解説:** (1) 両条件が真なので `&&` も `||` も真 → 最初の `if` に入り `A`。(2) 整数の余りで case を分岐。(3) 三項演算子で絶対差を計算。(4) switch のフォールスルーで複数値を1処理にまとめる。
