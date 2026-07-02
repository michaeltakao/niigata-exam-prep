# M03: 線形代数

---

## 1. 行列の基本演算

### 行列の演算

**加法:** $(A + B)_{ij} = A_{ij} + B_{ij}$（同じサイズのみ）

**積:** $(AB)_{ij} = \sum_k A_{ik} B_{kj}$（$A$ の列数 = $B$ の行数）

$$\begin{pmatrix}a & b\\c & d\end{pmatrix}\begin{pmatrix}e & f\\g & h\end{pmatrix} = \begin{pmatrix}ae+bg & af+bh\\ce+dg & cf+dh\end{pmatrix}$$

**注意:** 一般に $AB \neq BA$（可換でない）

### 転置行列

$(A^T)_{ij} = A_{ji}$

$(AB)^T = B^T A^T$

### 特殊行列

| 名称 | 性質 |
|------|------|
| 単位行列 $I$ | $AI = IA = A$ |
| 零行列 $O$ | 全要素が0 |
| 対角行列 | 対角以外が0 |
| 対称行列 | $A^T = A$ |
| 直交行列 | $A^T A = I$（$A^T = A^{-1}$） |

---

## 2. 行列式（Determinant）

### 2×2 行列

$$\det\begin{pmatrix}a & b\\c & d\end{pmatrix} = ad - bc$$

### 3×3 行列（サラスの法則）

$$\det\begin{pmatrix}a & b & c\\d & e & f\\g & h & i\end{pmatrix} = aei + bfg + cdh - ceg - bdi - afh$$

### 行列式の性質

- $\det(AB) = \det(A)\det(B)$
- $\det(A^T) = \det(A)$
- $\det(cA) = c^n \det(A)$（$n$ = 行列のサイズ）
- 2行（列）を入れ替えると $\det$ の符号が反転
- 2行（列）が比例 → $\det = 0$
- $\det(A) \neq 0 \Leftrightarrow A$ は正則（逆行列が存在）

### 余因子展開（cofactor expansion）

第 $i$ 行での展開:

$$\det(A) = \sum_{j=1}^n A_{ij} C_{ij}$$

$C_{ij} = (-1)^{i+j} M_{ij}$（余因子）、$M_{ij}$ は $(i,j)$ 小行列式

---

## 3. 逆行列

$AB = BA = I$ となる $B = A^{-1}$（逆行列）

### 2×2 行列の逆行列

$$\begin{pmatrix}a & b\\c & d\end{pmatrix}^{-1} = \frac{1}{ad-bc}\begin{pmatrix}d & -b\\-c & a\end{pmatrix}$$

（$ad - bc \neq 0$ のとき）

### 掃き出し法（ガウス・ジョルダン法）

$[A | I]$ を行基本変形で $[I | A^{-1}]$ に変換する。

**例:** $A = \begin{pmatrix}2 & 1\\1 & 1\end{pmatrix}$ の逆行列

$$\begin{pmatrix}2 & 1 & | & 1 & 0\\1 & 1 & | & 0 & 1\end{pmatrix} \to \begin{pmatrix}1 & 0 & | & 1 & -1\\0 & 1 & | & -1 & 2\end{pmatrix}$$

$A^{-1} = \begin{pmatrix}1 & -1\\-1 & 2\end{pmatrix}$（確認: $AA^{-1} = I$）

---

## 4. 連立一次方程式（Systems of Linear Equations）

$A\mathbf{x} = \mathbf{b}$

### 解の存在条件

- $\det(A) \neq 0$ → 唯一解 $\mathbf{x} = A^{-1}\mathbf{b}$
- $\det(A) = 0$ → 解なし or 無数の解

### クラメルの公式

$n$ 元連立方程式 $A\mathbf{x} = \mathbf{b}$ の解:

$$x_i = \frac{\det(A_i)}{\det(A)}$$

（$A_i$: $A$ の第 $i$ 列を $\mathbf{b}$ で置き換えた行列）

### 掃き出し法（ガウスの消去法）

**例:**
$$\begin{cases}x + 2y = 5\\3x + y = 10\end{cases}$$

$$\begin{pmatrix}1 & 2 & 5\\3 & 1 & 10\end{pmatrix} \to \begin{pmatrix}1 & 2 & 5\\0 & -5 & -5\end{pmatrix} \to \begin{pmatrix}1 & 0 & 3\\0 & 1 & 1\end{pmatrix}$$

解: $x = 3, y = 1$

---

## 5. 固有値・固有ベクトル（Eigenvalues & Eigenvectors）

### 定義

$A\mathbf{v} = \lambda\mathbf{v}$（$\mathbf{v} \neq \mathbf{0}$）

- $\lambda$: 固有値（eigenvalue）
- $\mathbf{v}$: 固有ベクトル（eigenvector）

### 特性方程式

$$\det(A - \lambda I) = 0$$

**例:** $A = \begin{pmatrix}3 & 1\\1 & 3\end{pmatrix}$

$$\det\begin{pmatrix}3-\lambda & 1\\1 & 3-\lambda\end{pmatrix} = (3-\lambda)^2 - 1 = \lambda^2 - 6\lambda + 8 = (\lambda-2)(\lambda-4) = 0$$

固有値: $\lambda_1 = 2, \lambda_2 = 4$

**固有ベクトルの計算（$\lambda_1 = 2$）:**

$$\begin{pmatrix}1 & 1\\1 & 1\end{pmatrix}\mathbf{v} = \mathbf{0} \Rightarrow v_1 + v_2 = 0 \Rightarrow \mathbf{v}_1 = c\begin{pmatrix}1\\-1\end{pmatrix}$$

**固有ベクトル（$\lambda_2 = 4$）:**

$$\begin{pmatrix}-1 & 1\\1 & -1\end{pmatrix}\mathbf{v} = \mathbf{0} \Rightarrow \mathbf{v}_2 = c\begin{pmatrix}1\\1\end{pmatrix}$$

### 対角化

$A$ を $P^{-1}AP = D$（対角行列）に変換:

- $P$: 固有ベクトルを列に並べた行列
- $D$: 対角に固有値を並べた行列

$$A^n = P D^n P^{-1}$$（行列の冪乗に便利）

### 固有値の性質

- $\text{tr}(A) = \sum \lambda_i$（トレース = 固有値の和）
- $\det(A) = \prod \lambda_i$（固有値の積）
- 対称行列の固有値はすべて実数
- 異なる固有値に対応する固有ベクトルは線形独立

---

## 6. 試験頻出パターン

### パターン 1: 行列式の計算

**問:** $\det\begin{pmatrix}2 & -1 & 3\\0 & 4 & -2\\1 & 0 & 1\end{pmatrix}$ を求めよ。

**解:** 第1列で余因子展開:

$$= 2\det\begin{pmatrix}4 & -2\\0 & 1\end{pmatrix} - 0 + 1\det\begin{pmatrix}-1 & 3\\4 & -2\end{pmatrix}$$

$$= 2(4 - 0) + 1(2 - 12) = 8 - 10 = -2$$

---

### パターン 2: 固有値・固有ベクトル

**問:** $A = \begin{pmatrix}4 & -2\\1 & 1\end{pmatrix}$ の固有値と固有ベクトルを求めよ。

**解:**
$$\det(A - \lambda I) = (4-\lambda)(1-\lambda) + 2 = \lambda^2 - 5\lambda + 6 = (\lambda-2)(\lambda-3) = 0$$

$\lambda = 2$: $(A-2I)\mathbf{v} = 0 \Rightarrow \begin{pmatrix}2 & -2\\1 & -1\end{pmatrix}\mathbf{v} = 0 \Rightarrow \mathbf{v} = c\begin{pmatrix}1\\1\end{pmatrix}$

$\lambda = 3$: $(A-3I)\mathbf{v} = 0 \Rightarrow \begin{pmatrix}1 & -2\\1 & -2\end{pmatrix}\mathbf{v} = 0 \Rightarrow \mathbf{v} = c\begin{pmatrix}2\\1\end{pmatrix}$

---

### パターン 3: 対角化と行列の冪乗

**問:** 上記 $A$ について $A^{10}$ を求めよ。

**解:** $P = \begin{pmatrix}1 & 2\\1 & 1\end{pmatrix}$, $D = \begin{pmatrix}2 & 0\\0 & 3\end{pmatrix}$

$$P^{-1} = \frac{1}{-1}\begin{pmatrix}1 & -2\\-1 & 1\end{pmatrix} = \begin{pmatrix}-1 & 2\\1 & -1\end{pmatrix}$$

$$A^{10} = PD^{10}P^{-1} = \begin{pmatrix}1 & 2\\1 & 1\end{pmatrix}\begin{pmatrix}2^{10} & 0\\0 & 3^{10}\end{pmatrix}\begin{pmatrix}-1 & 2\\1 & -1\end{pmatrix}$$

---

_← 前: M02 | → 次: M04 微分方程式_
