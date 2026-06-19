---
title: M03 固有値・固有ベクトル・対角化
---

# M03 固有値・固有ベクトル・対角化

## 1. 直感的説明

行列 $A$ に対して「方向が変わらず、大きさだけが $\lambda$ 倍になるベクトル $\mathbf{v}$」が
固有ベクトル、$\lambda$ が固有値です。

$$A\mathbf{v} = \lambda\mathbf{v} \quad (\mathbf{v}\neq\mathbf{0})$$

---

## 2. 固有値の求め方

### 特性方程式

::: formula
$$\det(A - \lambda I) = 0$$

この方程式を解いて固有値 $\lambda_1, \lambda_2, \ldots$ を求める。
:::

### 手順

1. $A-\lambda I$ を作る（対角成分から $\lambda$ を引く）
2. 行列式を計算（$\lambda$ の多項式になる）
3. 因数分解して $\lambda$ を求める

### 例題

::: example
$$A=\begin{pmatrix}3&1\\0&2\end{pmatrix}$$

$\det(A-\lambda I)=\begin{vmatrix}3-\lambda&1\\0&2-\lambda\end{vmatrix}=(3-\lambda)(2-\lambda)-0=(3-\lambda)(2-\lambda)$

$=0 \Rightarrow \lambda_1=2, \lambda_2=3$

**ポイント**: 上三角行列の固有値は対角成分そのもの！
:::

---

## 3. 固有ベクトルの求め方

固有値 $\lambda_i$ が定まったら:

::: formula
$(A-\lambda_i I)\mathbf{v} = \mathbf{0}$ の非自明解を求める

→ 行基本変形（行簡約）で解く
:::

### 例題 (続き)

::: example
$\lambda_1=2$ のとき:

$$A-2I=\begin{pmatrix}1&1\\0&0\end{pmatrix}\Rightarrow v_1+v_2=0\Rightarrow \mathbf{v}_1=t\begin{pmatrix}1\\-1\end{pmatrix}$$

$\lambda_2=3$ のとき:

$$A-3I=\begin{pmatrix}0&1\\0&-1\end{pmatrix}\Rightarrow v_2=0\Rightarrow \mathbf{v}_2=t\begin{pmatrix}1\\0\end{pmatrix}$$
:::

---

## 4. 対角化

### 対角化可能の条件

- $n\times n$ 行列が **$n$ 個の線形独立な固有ベクトル** を持つとき対角化可能
- 異なる固有値に対応する固有ベクトルは常に線形独立
- 重複固有値でも固有空間の次元が重複度と一致すれば対角化可能

### 対角化の手順

::: formula
1. 固有値 $\lambda_1,\ldots,\lambda_n$ を求める
2. 各固有値の固有ベクトル $\mathbf{v}_1,\ldots,\mathbf{v}_n$ を求める
3. $P = [\mathbf{v}_1\;\mathbf{v}_2\;\cdots\;\mathbf{v}_n]$ (固有ベクトルを列に並べる)
4. $D = \operatorname{diag}(\lambda_1,\ldots,\lambda_n)$
5. $A = PDP^{-1}$
:::

### 例題 — 対角化

::: example
$$A=\begin{pmatrix}2&1\\1&2\end{pmatrix}$$

**Step 1**: 特性方程式 $\det(A-\lambda I)=(2-\lambda)^2-1=\lambda^2-4\lambda+3=(\lambda-1)(\lambda-3)=0$

$\lambda_1=1, \lambda_2=3$

**Step 2**: 
- $\lambda_1=1$: $(A-I)\mathbf{v}=\begin{pmatrix}1&1\\1&1\end{pmatrix}\mathbf{v}=0 \Rightarrow \mathbf{v}_1=(1,-1)^T$
- $\lambda_2=3$: $(A-3I)\mathbf{v}=\begin{pmatrix}-1&1\\1&-1\end{pmatrix}\mathbf{v}=0 \Rightarrow \mathbf{v}_2=(1,1)^T$

**Step 3-5**:
$$P=\begin{pmatrix}1&1\\-1&1\end{pmatrix},\quad D=\begin{pmatrix}1&0\\0&3\end{pmatrix}$$

$$P^{-1}=\frac{1}{2}\begin{pmatrix}1&-1\\1&1\end{pmatrix}$$

確認: $PDP^{-1}=\begin{pmatrix}1&1\\-1&1\end{pmatrix}\begin{pmatrix}1&0\\0&3\end{pmatrix}\frac{1}{2}\begin{pmatrix}1&-1\\1&1\end{pmatrix}=A$ ✓
:::

---

## 5. よくある間違い

::: warning
- **固有ベクトルは「方向」が重要**: スカラー倍の違いは無視してよい（どれを代表として書いてもよい）
- **$P$ の列の順序と $D$ の対角成分の対応**: $P$ の第$k$列が $\lambda_k$ の固有ベクトルでなければならない
- **対角化不可能な場合**: 固有値が重複し、かつ固有空間の次元が足りない場合（例: $\begin{pmatrix}1&1\\0&1\end{pmatrix}$）
:::

---

## 6. 新潟大学での出題パターン

::: examtip
- **R8-2 問題I**: $A^n$ を対角化で求める（固有値・対角化・$A^n$ の流れ）
- **R8-2 問題II**: 固有値→固有ベクトル→対角化可能性判定→$B=PDP^{-1}$
- **頻出パターン**: 2×2 行列の完全な対角化手順（特性方程式→固有ベクトル→P・D作成）
:::
