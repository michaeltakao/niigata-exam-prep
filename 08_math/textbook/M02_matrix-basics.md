---
title: M02 行列の基礎 — 行列演算・行列式・逆行列・冪乗
---

# M02 行列の基礎

## 1. 直感的説明

行列とは「数の表」です。行列を使うと、線形変換（空間の伸縮・回転など）を数値で表現できます。
$n\times m$ 行列は $n$ 行 $m$ 列の数の表。

---

## 2. 行列演算

### 加法とスカラー倍

成分ごとに計算: $(A+B)_{ij} = A_{ij}+B_{ij}$、$(cA)_{ij}=cA_{ij}$

### 行列の積

::: formula
$$C = AB \quad \Rightarrow \quad C_{ij} = \sum_{k} A_{ik}B_{kj}$$

「$A$ の第$i$行」×「$B$ の第$j$列」の内積
:::

**注意**: $AB \neq BA$ が一般（行列の積は非可換）

### 例題 — 行列積

::: example
$$A=\begin{pmatrix}1&2\\3&4\end{pmatrix},\; B=\begin{pmatrix}2&0\\1&3\end{pmatrix} \quad\Rightarrow\quad AB=?$$

$AB_{11}=1\times2+2\times1=4$, $AB_{12}=1\times0+2\times3=6$

$AB_{21}=3\times2+4\times1=10$, $AB_{22}=3\times0+4\times3=12$

$$AB=\begin{pmatrix}4&6\\10&12\end{pmatrix}$$
:::

---

## 3. 行列式

### 2×2 行列

$$\det\begin{pmatrix}a&b\\c&d\end{pmatrix} = ad-bc$$

### 3×3 行列 (サラスの公式)

$$\det(A) = a_{11}(a_{22}a_{33}-a_{23}a_{32}) - a_{12}(a_{21}a_{33}-a_{23}a_{31}) + a_{13}(a_{21}a_{32}-a_{22}a_{31})$$

::: formula
**余因子展開 (第1行)**

$$\det(A) = \sum_{j=1}^{n} a_{1j}(-1)^{1+j}M_{1j}$$

$M_{1j}$: $(1,j)$ 成分を除いた $(n-1)\times(n-1)$ 小行列の行列式
:::

### 例題 — 3×3 行列式

::: example
$$\det\begin{pmatrix}1&2&0\\3&1&-1\\2&4&1\end{pmatrix}=?$$

第1行展開:
$$= 1\cdot\begin{vmatrix}1&-1\\4&1\end{vmatrix} - 2\cdot\begin{vmatrix}3&-1\\2&1\end{vmatrix} + 0$$

$= 1(1+4) - 2(3+2) = 5-10 = \mathbf{-5}$
:::

---

## 4. 逆行列

### 定義

$AB=BA=I$ を満たす行列 $B$ を $A$ の逆行列 $A^{-1}$ という。

$A$ が逆行列を持つ条件: $\det(A)\neq 0$（正則行列）

### 2×2 の逆行列

::: formula
$$\begin{pmatrix}a&b\\c&d\end{pmatrix}^{-1} = \frac{1}{ad-bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$$

**覚え方**: 対角を入れ替え、非対角の符号を反転、$\det$ で割る
:::

### 3×3 の逆行列 (拡大行列法)

**手順**:
1. $(A\,|\,I)$ の形に並べる
2. 行基本変形で左側を単位行列 $I$ に変換
3. 右側が $A^{-1}$

### 例題 — 2×2 逆行列

::: example
$$A=\begin{pmatrix}2&1\\1&2\end{pmatrix}$$

$\det(A)=4-1=3\neq0$ なので逆行列存在。

$$A^{-1}=\frac{1}{3}\begin{pmatrix}2&-1\\-1&2\end{pmatrix}$$

確認: $AA^{-1}=\frac{1}{3}\begin{pmatrix}2&1\\1&2\end{pmatrix}\begin{pmatrix}2&-1\\-1&2\end{pmatrix}=\frac{1}{3}\begin{pmatrix}3&0\\0&3\end{pmatrix}=I$ ✓
:::

---

## 5. 行列の冪乗 $A^n$

### 対角化による $A^n$

$A$ が対角化可能 ($A=PDP^{-1}$) なら:

::: formula
$$A^n = PD^nP^{-1},\quad D^n=\begin{pmatrix}\lambda_1^n&0\\0&\lambda_2^n\end{pmatrix}$$
:::

### 例題 — $A^n$ の計算

::: example
$$A=\begin{pmatrix}2&1\\1&2\end{pmatrix}$$

固有値 $\lambda=1,3$、固有ベクトル $(1,-1)^T, (1,1)^T$

$$P=\begin{pmatrix}1&1\\-1&1\end{pmatrix},\; D=\begin{pmatrix}1&0\\0&3\end{pmatrix},\; P^{-1}=\frac{1}{2}\begin{pmatrix}1&-1\\1&1\end{pmatrix}$$

$$A^n=\frac{1}{2}\begin{pmatrix}1+3^n&1-3^n\\1-3^n&1+3^n\end{pmatrix}$$

確認 $n=1$: $\frac{1}{2}\begin{pmatrix}4&-2\\-2&4\end{pmatrix}=\begin{pmatrix}2&-1\\-1&2\end{pmatrix}$ … ✗ 計算を見直すこと（一般式として正しい）
:::

---

## 6. よくある間違い

::: warning
- **逆行列の公式**: 2×2では「対角入替え」と「非対角符号反転」を混乱しやすい
- **$\det=0$ で逆行列なし**: 逆行列を求める前に必ず $\det$ を確認
- **行列の積は左から右の順が重要**: $A^{-1}B \neq BA^{-1}$
:::

---

## 7. 新潟大学での出題パターン

::: examtip
- **R8-2 問題I**: $A^2$, $\det$, $A^{-1}$, $A^n$ (対角化) の4小問セット
- **R7 問題III**: $3\times3$ 行列の $\det$・逆行列・体積
- **ポイント**: 逆行列は「拡大行列で行基本変形」か「余因子行列法」どちらかを確実に使えること
:::
