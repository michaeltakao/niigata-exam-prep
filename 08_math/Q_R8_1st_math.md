---
title: 数学 過去問 R8 第1次
---

# 数学 過去問 — 令和8年度 第1次試験

> 出典: 新潟大学工学部 第3年次編入学試験 令和8年度第1次

---

## 問題 I — ベクトル

$\mathbb{R}^3$ のベクトル $\mathbf{a} = (1, 2, -1)$, $\mathbf{b} = (2, -1, 3)$, $\mathbf{c} = (1, 1, 1)$ について答えよ。

**(1)** $\mathbf{a} \cdot \mathbf{b}$ (内積) を求めよ。

**(2)** $\mathbf{a} \times \mathbf{b}$ (外積) を求めよ。

**(3)** $\mathbf{a}, \mathbf{b}, \mathbf{c}$ を 3 辺とする平行六面体の体積を求めよ。

---

## 問題 II — 線形写像

$\mathbb{R}^3$ から $\mathbb{R}^2$ への線形写像 $f$ が

$$
f\!\left(\begin{pmatrix}1\\0\\0\end{pmatrix}\right) = \begin{pmatrix}1\\2\end{pmatrix},\quad
f\!\left(\begin{pmatrix}0\\1\\0\end{pmatrix}\right) = \begin{pmatrix}-1\\1\end{pmatrix},\quad
f\!\left(\begin{pmatrix}0\\0\\1\end{pmatrix}\right) = \begin{pmatrix}2\\0\end{pmatrix}
$$

で定義されている。

**(1)** $f$ の表現行列 $A$ を求めよ。

**(2)** $f$ の像 $\operatorname{Im}(f)$ を求め、その次元を答えよ。

**(3)** $f$ の核 $\ker(f)$ を求め、その次元を答えよ。

---

## 問題 III — 積分

**(1)** 次の定積分を計算せよ。

$$\int_0^{\pi} x \sin x \, dx$$

**(2)** 曲線 $y = x^2$ と直線 $y = x + 2$ で囲まれた図形の面積を求めよ。

**(3)** 次の広義積分を求めよ。

$$\int_0^{+\infty} x e^{-x} \, dx$$

---

## 問題 IV — 極限・微分方程式

**(1)** 次の極限を求めよ。

$$\lim_{x \to 0} \frac{\sin 3x}{x}$$

**(2)** 次の極限を求めよ (ロピタルの定理を使ってよい)。

$$\lim_{x \to 0} \frac{e^x - 1 - x}{x^2}$$

**(3)** 次の微分方程式を解け ($y(0) = 1$)。

$$\frac{dy}{dx} = 2xy$$

---

## 解答方針

### I (1) 内積
$\mathbf{a}\cdot\mathbf{b} = 1\cdot2 + 2\cdot(-1) + (-1)\cdot3 = 2-2-3 = \mathbf{-3}$

### I (2) 外積
$$\mathbf{a}\times\mathbf{b} = \begin{vmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\\1&2&-1\\2&-1&3\end{vmatrix} = \mathbf{i}(6-1)-\mathbf{j}(3+2)+\mathbf{k}(-1-4) = \mathbf{(5,-5,-5)}$$

### I (3) 体積
スカラー三重積 $|\mathbf{a}\cdot(\mathbf{b}\times\mathbf{c})|$ を計算する。

$\mathbf{b}\times\mathbf{c} = \begin{vmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\\2&-1&3\\1&1&1\end{vmatrix} = (-1-3, 3-2, 2+1) = (-4,1,3)$

$\mathbf{a}\cdot(-4,1,3) = -4+2-3 = -5$、体積 $= |-5| = \mathbf{5}$

### II (1) 表現行列
$$A = \begin{pmatrix}1&-1&2\\2&1&0\end{pmatrix}$$

### II (2) Im(f)
$A$ の列空間 = $\operatorname{span}\left\{\begin{pmatrix}1\\2\end{pmatrix},\begin{pmatrix}-1\\1\end{pmatrix}\right\}$。
2列は線形独立（行列式 $1+2=3\neq0$）。$\therefore\operatorname{Im}(f) = \mathbb{R}^2$、$\dim = \mathbf{2}$

### II (3) ker(f)
$A\mathbf{x}=\mathbf{0}$ を解く。行簡約:
$$\begin{pmatrix}1&-1&2\\2&1&0\end{pmatrix}\to\begin{pmatrix}1&-1&2\\0&3&-4\end{pmatrix}\to\begin{pmatrix}1&0&2/3\\0&1&-4/3\end{pmatrix}$$
$x_1=-\frac{2}{3}t,\; x_2=\frac{4}{3}t,\; x_3=t$ $(t\in\mathbb{R})$、$\dim\ker = \mathbf{1}$

### III (1) 部分積分
$\int_0^\pi x\sin x\,dx = [-x\cos x]_0^\pi + \int_0^\pi\cos x\,dx = \pi + [\sin x]_0^\pi = \mathbf{\pi}$

### III (2) 面積
交点: $x^2=x+2\Rightarrow x=-1,2$。面積 $=\int_{-1}^2(x+2-x^2)dx=[\frac{x^2}{2}+2x-\frac{x^3}{3}]_{-1}^2 = \mathbf{\frac{9}{2}}$

### III (3) 広義積分
部分積分: $\int_0^\infty xe^{-x}dx = [-xe^{-x}]_0^\infty+\int_0^\infty e^{-x}dx = 0+[-e^{-x}]_0^\infty = \mathbf{1}$

### IV (1)(2)(3)
- (1) $\lim_{x\to0}\frac{\sin3x}{x}=3\cdot\frac{\sin3x}{3x}\to\mathbf{3}$
- (2) ロピタル2回: $\frac{e^x-1}{2x}\to\frac{e^x}{2}\to\mathbf{\frac{1}{2}}$
- (3) 変数分離: $\frac{dy}{y}=2x\,dx\Rightarrow\ln|y|=x^2+C\Rightarrow y=e^{x^2}$ ($y(0)=1$ より $C=0$)
