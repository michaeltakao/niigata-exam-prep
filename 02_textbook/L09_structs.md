---
title: "L09 構造体 — 複数のデータをまとめる"
---

# L09 構造体 — 複数のデータをまとめる

---

## 1. コンセプト概要

**構造体（struct）** とは、**異なる型のデータをひとつの名前でまとめる**仕組みです。

配列は「同じ型のデータの集まり」でしたが、構造体は「異なる型のデータをセットにする」ものです。

```c
// 配列: 同じ型 (int) だけ
int scores[] = {90, 85, 78};

// 構造体: 異なる型をひとまとめ
struct Student {
    int    id;        // 整数
    char   name[20];  // 文字列
    double gpa;       // 浮動小数点
};
```

---

## 2. なぜ必要か

学生のデータ（ID・名前・GPA）を3人分管理したいとします。

**構造体を使わない場合 — 混乱しやすい:**
```c
int   id1 = 1001,   id2 = 1002,   id3 = 1003;
char  name1[] = "田中", name2[] = "鈴木", name3[] = "佐藤";
double gpa1 = 3.8,  gpa2 = 3.5,  gpa3 = 2.9;
// 3人目のデータを関数に渡すとき: id3, name3, gpa3 を全部渡す必要がある
```

**構造体を使う場合 — 整理される:**
```c
Student students[3];   // 3人分のデータを1つの配列で管理
students[0].id = 1001;
students[0].gpa = 3.8;
// students[0] を渡すだけで1人分全データが渡せる
```

---

## 3. 現実世界のアナロジー

**構造体 ≒ 申込用紙の1行**

| 学籍番号 | 氏名 | GPA |
|---|---|---|
| 1001 | 田中 | 3.8 |
| 1002 | 鈴木 | 3.5 |

1行が1つの `struct Student` です。  
複数行の表 = `struct Student` の配列です。

**別のアナロジー: 住所録の1件**

- 名前・電話番号・メールアドレス・住所 → これらをまとめて「連絡先1件」として扱う
- これが構造体のイメージです

---

## 4. 構文説明

### 構造体の定義

```c
//   キーワード  構造体タグ名
//       ↓         ↓
   struct Student {
       int    id;        // メンバ変数1
       char   name[20];  // メンバ変数2
       double gpa;       // メンバ変数3
   };                    // ← セミコロン必須！
```

### typedef で省略

毎回 `struct Student s;` と書くのは面倒なので `typedef` で省略できます:

```c
typedef struct {
    int    id;
    char   name[20];
    double gpa;
} Student;   // ← これ以降 Student だけで使える

// typedef なし:   struct Student s1;
// typedef あり:   Student s1;        ← すっきり
```

### メンバアクセス: ドット演算子 (`.`)

```c
Student s;
s.id = 1001;              // メンバ id に代入
strcpy(s.name, "田中");   // メンバ name に文字列コピー
s.gpa = 3.8;              // メンバ gpa に代入

printf("%d %s %.1f\n", s.id, s.name, s.gpa);
```

### ポインタ経由のアクセス: アロー演算子 (`->`)

```c
Student s = {1001, "田中", 3.8};
Student *p = &s;

// ポインタ経由のアクセス: p->メンバ  (= (*p).メンバ)
printf("%d\n", p->id);       // 1001
printf("%s\n", p->name);     // 田中
printf("%.1f\n", p->gpa);    // 3.8

// p->id は (*p).id と全く同じ（略記）
```

### 初期化の方法

```c
// 方法1: メンバを個別に代入
Student s1;
s1.id = 1001;
strcpy(s1.name, "田中");
s1.gpa = 3.8;

// 方法2: 宣言時に一括初期化
Student s2 = {1002, "鈴木", 3.5};

// 方法3: 構造体のコピー（全メンバがコピーされる）
Student s3 = s2;   // s2 の全メンバが s3 にコピーされる
```

---

## 5. ステップ実行トレース

```c
#include <stdio.h>
#include <string.h>

typedef struct {
    int    id;
    char   name[20];
    double gpa;
} Student;

int main() {
    Student s1;
    s1.id = 1001;
    strcpy(s1.name, "Tanaka");
    s1.gpa = 3.8;

    Student s2 = {1002, "Suzuki", 3.5};

    printf("ID: %d, Name: %s, GPA: %.1f\n", s1.id, s1.name, s1.gpa);
    printf("ID: %d, Name: %s, GPA: %.1f\n", s2.id, s2.name, s2.gpa);
    return 0;
}
```

**トレース表:**

| ステップ | 操作 | s1.id | s1.name | s1.gpa | s2.id | s2.name | s2.gpa |
|---|---|---|---|---|---|---|---|
| 初期 | — | ? | ? | ? | ? | ? | ? |
| `s1.id = 1001` | s1 設定 | 1001 | ? | ? | — | — | — |
| `strcpy(s1.name, "Tanaka")` | s1 設定 | 1001 | "Tanaka" | ? | — | — | — |
| `s1.gpa = 3.8` | s1 設定 | 1001 | "Tanaka" | 3.8 | — | — | — |
| `s2 = {1002,...}` | s2 初期化 | — | — | — | 1002 | "Suzuki" | 3.5 |
| printf s1 | 出力 | → | → | → | — | — | — |
| printf s2 | 出力 | — | — | — | → | → | → |

**出力:**
```
ID: 1001, Name: Tanaka, GPA: 3.8
ID: 1002, Name: Suzuki, GPA: 3.5
```

---

## 6. 視覚的メモリ図

### 構造体のメモリレイアウト

```
Student s1:
┌───────────────────────────────────────────────────────┐
│  id          name                         gpa         │
│ ┌────────┬──────────────────────────────┬──────────┐  │
│ │  1001  │ T a n a k a \0 . . . . . .  │  3.800   │  │
│ └────────┴──────────────────────────────┴──────────┘  │
│  4 bytes         20 bytes                 8 bytes      │
└───────────────────────────────────────────────────────┘
```

### 配列 vs 構造体の比較

```
配列 (同じ型):          構造体 (異なる型):
int scores[3]:          Student s:
┌────┬────┬────┐       ┌──────┬────────────────┬────────┐
│ 90 │ 85 │ 78 │       │ 1001 │    "Tanaka"     │  3.8   │
└────┴────┴────┘       └──────┴────────────────┴────────┘
  int  int  int          int        char[20]      double
```

### 構造体の配列

```
Student students[3]:
┌──────────────────────────────────────────────────────────┐
│ [0]: id=1001, name="Tanaka", gpa=3.8                     │
├──────────────────────────────────────────────────────────┤
│ [1]: id=1002, name="Suzuki", gpa=3.5                     │
├──────────────────────────────────────────────────────────┤
│ [2]: id=1003, name="Sato",   gpa=2.9                     │
└──────────────────────────────────────────────────────────┘

アクセス方法:
  students[1].gpa  →  3.5   (2番目の学生のGPA)
  students[0].name →  "Tanaka"
```

### ポインタ経由のアクセス

```
Student s = {1001, "Tanaka", 3.8};
Student *p = &s;

  p                     s (メモリ上)
┌──────┐              ┌───────────────────┐
│ &s   │─────────→    │ id:1001 name:... │
└──────┘              │ gpa:3.8          │
                       └───────────────────┘

p->id  = (*p).id = 1001
p->gpa = (*p).gpa = 3.8
```

---

## 7. よくある間違い

### 間違い1: ポインタに `.` を使う（`->` が必要）

```c
Student s = {1001, "田中", 3.8};
Student *p = &s;

// ❌ 間違い
printf("%d\n", p.id);    // エラー: p はポインタなので . は使えない

// ✅ 正しい
printf("%d\n", p->id);   // ポインタには -> を使う
printf("%d\n", (*p).id); // これも等価（括弧が必要！）
```

**覚え方:** 「変数に `.`、ポインタに `→`（矢印）」

### 間違い2: 構造体に `.` を使う場所でポインタ演算子 `->` を使う

```c
Student s = {1001, "田中", 3.8};

// ❌ 間違い（s はポインタではない）
printf("%d\n", s->id);    // エラー: s は構造体変数、ポインタではない

// ✅ 正しい
printf("%d\n", s.id);     // 構造体変数には . を使う
```

### 間違い3: 構造体の配列でのメンバアクセス順序

```c
Student students[3];

// ❌ 間違い（こう書きたくなるが間違い）
students.id[0] = 1001;     // エラー: students に . は使えない
students.name[0] = "田中"; // エラー

// ✅ 正しい
students[0].id = 1001;      // 先に [i] で要素を選び、次に .メンバ
strcpy(students[0].name, "田中");
```

**覚え方:** 「配列の添字 `[i]` が先、`.メンバ` が後」

### 間違い4: 文字列メンバへの代入に `=` を使う

```c
Student s;

// ❌ 間違い（文字列は = で代入できない）
s.name = "田中";   // エラー: 配列への直接代入は不可

// ✅ 正しい（strcpy を使う）
strcpy(s.name, "田中");

// ✅ 宣言時の初期化なら = でOK
Student s2 = {1001, "田中", 3.8};   // これはOK
```

### 間違い5: typedef の位置の混乱

```c
// ❌ 間違い（型名が最後に来ることを忘れる）
typedef Student {
    int id;
};     // エラー: struct キーワードが必要

// ✅ 正しい
typedef struct {
    int id;
} Student;   // ← 型名は } の後

// または
typedef struct Student_tag {
    int id;
} Student;   // タグ名をつける場合（再帰的な構造体で必要）
```

---

## 8. ミニクイズ

**Q1.** 次のコードの出力は?

```c
typedef struct { int x; int y; } Point;
Point p = {3, 7};
printf("%d %d\n", p.x, p.y);
```

<details><summary>答え</summary>
`3 7`
</details>

---

**Q2.** 構造体ポインタ `Student *p` で、メンバ `id` にアクセスする方法を2つ書け。

<details><summary>答え</summary>
`p->id` と `(*p).id` の2通り。`(*p).id` の括弧は必須（優先順位のため）。
</details>

---

**Q3.** `Student s2 = s1;` の操作は何をするか?

<details><summary>答え</summary>
s1 の全メンバ（id, name の配列, gpa）を s2 にコピーする（深いコピー）。ただし、メンバにポインタが含まれる場合はアドレスがコピーされるだけ（シャローコピー）になる点に注意。
</details>

---

**Q4.** 構造体配列の2番目の要素の gpa を読む式は?

```c
Student students[3];
// 2番目（インデックス1）の gpa を読む式:
```

<details><summary>答え</summary>
`students[1].gpa`
</details>

---

**Q5.** `typedef struct { int a; } Foo;` のとき、変数を宣言するのに正しいのはどれ?

(A) `struct Foo f;`  (B) `Foo f;`  (C) `typedef Foo f;`

<details><summary>答え</summary>
(B) `Foo f;` が正しい。typedef があるので `struct` キーワードは不要。(A) は typedef なしの場合に使う書き方。(C) は誤り。
</details>

---

## 9. 例題

### 例題1: 最高GPA学生を探す

```c
#include <stdio.h>
#include <string.h>

typedef struct {
    int    id;
    char   name[20];
    double gpa;
} Student;

int main() {
    Student students[] = {
        {1001, "Tanaka", 3.8},
        {1002, "Suzuki", 3.5},
        {1003, "Sato",   4.0},
        {1004, "Ito",    2.9}
    };
    int n = 4;

    int best = 0;   // 最高GPA学生のインデックス
    for (int i = 1; i < n; i++) {
        if (students[i].gpa > students[best].gpa) {
            best = i;
        }
    }

    printf("最高GPA: %s (%.1f)\n", students[best].name, students[best].gpa);
    // 出力: 最高GPA: Sato (4.0)
    return 0;
}
```

**トレース（ループ部分）:**

| i | students[i].gpa | students[best].gpa | best |
|---|---|---|---|
| 初期 | — | 3.8 (Tanaka) | 0 |
| 1 | 3.5 (Suzuki) | 3.8 > 3.5 → 更新なし | 0 |
| 2 | 4.0 (Sato) | 4.0 > 3.8 → 更新 | 2 |
| 3 | 2.9 (Ito) | 2.9 < 4.0 → 更新なし | 2 |

### 例題2: ポインタで構造体を変更する関数

```c
#include <stdio.h>

typedef struct {
    int id;
    double gpa;
} Student;

void update_gpa(Student *s, double new_gpa) {
    s->gpa = new_gpa;   // ポインタ経由で変更 → 呼び出し元に反映される
}

int main() {
    Student s = {1001, 3.5};
    printf("Before: GPA=%.1f\n", s.gpa);
    update_gpa(&s, 3.9);   // アドレスを渡す
    printf("After:  GPA=%.1f\n", s.gpa);
    // 出力:
    // Before: GPA=3.5
    // After:  GPA=3.9
    return 0;
}
```

**ポイント:** 構造体を「値渡し」するとコピーが作られ、変更が元に反映されません。  
ポインタ渡しにすると、元のデータを直接変更できます。

### 例題3: GPA 順でバブルソート

```c
#include <stdio.h>
#include <string.h>

typedef struct {
    int    id;
    char   name[20];
    double gpa;
} Student;

void sort_by_gpa(Student arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - 1 - i; j++) {
            if (arr[j].gpa > arr[j+1].gpa) {   // GPA 降順
                Student tmp = arr[j];            // 構造体ごとスワップ
                arr[j]     = arr[j+1];
                arr[j+1]   = tmp;
            }
        }
    }
}

int main() {
    Student students[] = {
        {1001, "Tanaka", 3.8},
        {1002, "Suzuki", 3.5},
        {1003, "Sato",   4.0}
    };
    int n = 3;

    sort_by_gpa(students, n);

    for (int i = 0; i < n; i++) {
        printf("%d: %s (%.1f)\n", i+1, students[i].name, students[i].gpa);
    }
    return 0;
}
```

**出力（GPA昇順）:**
```
1: Suzuki (3.5)
2: Tanaka (3.8)
3: Sato (4.0)
```

**ポイント:** `Student tmp = arr[j];` は構造体全体をコピーします。  
配列のバブルソートと同じロジックを、`arr[j]` の代わりに構造体に適用しただけです。

---

## 10. 新潟大学試験との関連

**出題頻度:** Tier 2 — R7 で確認（1/3 年度）

**出題パターン:**

| パターン | 具体例 |
|---|---|
| メンバアクセスの出力 | `s.id` や `p->name` の値を書く |
| 構造体配列の操作 | 「GPAが最も高い学生を探せ」 |
| 構造体を引数にとる関数 | 「`print_student()` を実装せよ」 |
| ソート + 構造体 | 「GPA順にソートして表示せよ」 |

**試験直前チェックリスト:**
- [ ] `typedef struct { ... } Name;` の書き方が書ける
- [ ] `.`（変数）と `->` （ポインタ）を使い分けられる
- [ ] 構造体配列の `arr[i].member` が書ける
- [ ] 文字列メンバに `strcpy()` が必要なことを知っている
- [ ] 構造体を関数に渡す2通り（値渡し vs ポインタ渡し）の違いを説明できる

**試験での優先度:**
構造体はTier 2（頻度 1/3）なので、Tier 1 ★（ループ・配列・関数）を完成させてから着手すること。  
ただし、構造体 + ポインタ（`->`）の組み合わせはポインタの理解を深めるのに非常に有効なので、L08を理解した後に続けて学習することを推奨します。
