---
title: 数学 過去問 R8 第2次
---

# 数学 過去問 — 令和8年度 第2次試験

> 出典: 新潟大学工学部 第3年次編入学試験 令和8年度第2次

---

## 問題 I — 行列演算

$$A = \begin{pmatrix}2&1\\1&2\end{pmatrix}$$

**(1)** $$A^2$$ を計算せよ。

**(2)** $$A$$ の行列式 $$\det(A)$$ と逆行列 $$A^{-1}$$ を求めよ。

**(3)** $$A^n$$ を $$n$$ の式で表せ（対角化を用いよ）。

---

## 問題 II — 固有値と対角化

$$B = \begin{pmatrix}3&1\\0&2\end{pmatrix}$$

**(1)** $$B$$ の固有値をすべて求めよ。

**(2)** 各固有値に対応する固有ベクトルを求めよ。

**(3)** $$B$$ は対角化可能か。可能なら $$B = PDP^{-1}$$ の形に書け。

---

## 問題 III — 広義積分

**(1)** 次の広義積分を求めよ。

$$\int_1^{+\infty} \frac{1}{x^2} \, dx$$

**(2)** 次の広義積分を求めよ。

$$\int_0^1 \frac{1}{\sqrt{x}} \, dx$$

**(3)** 次の積分が収束するか発散するかを判定し、収束する場合は値を求めよ。

$$\int_0^{+\infty} \frac{1}{1+x^2} \, dx$$

---

## 解答方針

### I (1)
$$A^2 = \begin{pmatrix}2&1\\1&2\end{pmatrix}^2 = \begin{pmatrix}5&4\\4&5\end{pmatrix}$$

### I (2)
$$\det(A)=4-1=3$$、$$A^{-1}=\frac{1}{3}\begin{pmatrix}2&-1\\-1&2\end{pmatrix}$$

### I (3) 対角化による $$A^n$$
固有値: $$\det(A-\lambda I)=(2-\lambda)^2-1=0 \Rightarrow \lambda=1,3$$

- $$\lambda=1$$: 固有ベクトル $$(1,-1)^T$$
- $$\lambda=3$$: 固有ベクトル $$(1,1)^T$$

$$P=\begin{pmatrix}1&1\\-1&1\end{pmatrix},\quad D=\begin{pmatrix}1&0\\0&3\end{pmatrix}$$

$$A^n = PD^nP^{-1} = \frac{1}{2}\begin{pmatrix}1+3^n & 1-3^n\\1-3^n & 1+3^n\end{pmatrix}$$

### II (1) 固有値
$$\det(B-\lambda I)=(3-\lambda)(2-\lambda)=0 \Rightarrow \lambda=2,3$$（上三角行列なので対角成分が固有値）

### II (2) 固有ベクトル
- $$\lambda=2$$: $$(B-2I)\mathbf{v}=\begin{pmatrix}1&1\\0&0\end{pmatrix}\mathbf{v}=0 \Rightarrow \mathbf{v}=(1,-1)^T$$
- $$\lambda=3$$: $$(B-3I)\mathbf{v}=\begin{pmatrix}0&1\\0&-1\end{pmatrix}\mathbf{v}=0 \Rightarrow \mathbf{v}=(1,0)^T$$

### II (3) 対角化
固有値が異なる2つ → **対角化可能**。

$$P=\begin{pmatrix}1&1\\-1&0\end{pmatrix},\quad D=\begin{pmatrix}2&0\\0&3\end{pmatrix}$$

$$B=PDP^{-1},\quad P^{-1}=\begin{pmatrix}0&-1\\1&1\end{pmatrix}$$

### III (1)
$$\int_1^\infty x^{-2}dx=\left[-x^{-1}\right]_1^\infty=0-(-1)=\mathbf{1}$$

### III (2)
$$\int_0^1 x^{-1/2}dx=\left[2x^{1/2}\right]_0^1=2-0=\mathbf{2}$$

### III (3)
$$\int_0^\infty\frac{dx}{1+x^2}=\left[\arctan x\right]_0^\infty=\frac{\pi}{2}-0=\mathbf{\frac{\pi}{2}}$$（収束）
