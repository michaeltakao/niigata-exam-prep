---
title: 数学 予測問題 2026年度
date: 2026-06-19
---

# 数学 予測問題 — 2026年度 (R8)

**予測根拠**: R6機械・R7・R8-1・R8-2 の4年分の出題パターン分析

---

## 予測問題 1 ★★★ (積分 — 毎年必出)

**[I](1)** 次の定積分を求めよ。

$$\int_0^{\pi/2} x^2\cos x\,dx$$

**(2)** 曲線 $y=\sqrt{x}$ と直線 $y=\frac{x}{2}$ で囲まれた図形の面積を求めよ。

**(3)** 次の広義積分が収束するか判定し、収束する場合は値を求めよ。

$$\int_1^\infty \frac{\ln x}{x^2}\,dx$$

**予測根拠**: 積分は4/4年出題。部分積分+面積+広義積分の3小問セットが定番。

---

**解答**:

(1) 部分積分2回: $u=x^2$, $dv=\cos x\,dx$

$= [x^2\sin x]_0^{\pi/2}-\int_0^{\pi/2}2x\sin x\,dx$

$= \frac{\pi^2}{4}-2\int_0^{\pi/2}x\sin x\,dx$

$\int_0^{\pi/2}x\sin x\,dx = [-x\cos x]_0^{\pi/2}+\int_0^{\pi/2}\cos x\,dx=0+1=1$

$$=\frac{\pi^2}{4}-2=\frac{\pi^2-8}{4}$$

(2) 交点: $\sqrt{x}=\frac{x}{2} \Rightarrow x=4$。$[0,4]$ で $\sqrt{x}\ge\frac{x}{2}$

$$S=\int_0^4\left(\sqrt{x}-\frac{x}{2}\right)dx=\left[\frac{2x^{3/2}}{3}-\frac{x^2}{4}\right]_0^4=\frac{16}{3}-4=\frac{4}{3}$$

(3) 部分積分: $u=\ln x$, $dv=\frac{dx}{x^2}$

$$=\left[-\frac{\ln x}{x}\right]_1^\infty+\int_1^\infty\frac{1}{x^2}dx=0+\left[-\frac{1}{x}\right]_1^\infty=1$$

---

## 予測問題 2 ★★★ (線形代数 — 毎年必出)

**[II]** 

$$A=\begin{pmatrix}4&2\\1&3\end{pmatrix}$$

**(1)** $\det(A)$ と $A^{-1}$ を求めよ。

**(2)** $A$ の固有値・固有ベクトルを求め、対角化せよ。

**(3)** $A^n$ を求めよ。

**予測根拠**: 線形代数は3/4年出題。R8-2は行列冪乗・対角化の複合問題。

---

**解答**:

(1) $\det(A)=12-2=10$; $A^{-1}=\frac{1}{10}\begin{pmatrix}3&-2\\-1&4\end{pmatrix}$

(2) 特性方程式: $(4-\lambda)(3-\lambda)-2=\lambda^2-7\lambda+10=(\lambda-2)(\lambda-5)=0$

$\lambda_1=2$: $(A-2I)\mathbf{v}=\begin{pmatrix}2&2\\1&1\end{pmatrix}\mathbf{v}=0 \Rightarrow \mathbf{v}_1=(1,-1)^T$

$\lambda_2=5$: $(A-5I)\mathbf{v}=\begin{pmatrix}-1&2\\1&-2\end{pmatrix}\mathbf{v}=0 \Rightarrow \mathbf{v}_2=(2,1)^T$

$P=\begin{pmatrix}1&2\\-1&1\end{pmatrix}$, $D=\begin{pmatrix}2&0\\0&5\end{pmatrix}$

(3) $A^n=PD^nP^{-1}=\frac{1}{3}\begin{pmatrix}2^n+2\cdot5^n&2\cdot5^n-2^{n+1}\\5^n-2^n&2\cdot2^n+5^n\end{pmatrix}$

---

## 予測問題 3 ★★ (ODE — 高確率)

**[III]**

**(1)** 次の微分方程式を解け。

$$\frac{dy}{dx}=\frac{y}{x},\quad y(1)=2$$

**(2)** 次の2階線形微分方程式を解け。

$$y''+4y'+4y=0$$

**(3)** 次の非同次微分方程式を解け。

$$y''-y=\sin x$$

**予測根拠**: ODE は2/4年出題 (R8-1, R7)。非同次 ODE は R7 で出題済み。

---

**解答**:

(1) 変数分離: $\frac{dy}{y}=\frac{dx}{x}$; $\ln|y|=\ln|x|+C$; $y=Ax$。$y(1)=2 \Rightarrow A=2$

$$y=2x$$

(2) 特性方程式: $r^2+4r+4=(r+2)^2=0$; $r=-2$ (重根)

$$y=(C_1+C_2x)e^{-2x}$$

(3) 同次解: $r^2-1=0\Rightarrow r=\pm1$; $y_h=C_1e^x+C_2e^{-x}$

特殊解: $y_p=A\sin x+B\cos x$

代入: $(-A\sin x-B\cos x)-(A\sin x+B\cos x)=\sin x$

$-2A\sin x-2B\cos x=\sin x \Rightarrow A=-\frac{1}{2}, B=0$

$$y=C_1e^x+C_2e^{-x}-\frac{1}{2}\sin x$$

---

## 予測問題 4 ★★ (ベクトル — 高確率)

**[IV]** $\mathbf{a}=(2,1,-1)$, $\mathbf{b}=(1,-1,2)$, $\mathbf{c}=(3,0,1)$ について:

**(1)** $\mathbf{a}\cdot\mathbf{b}$ を求めよ。

**(2)** $\mathbf{a}\times\mathbf{b}$ を求めよ。

**(3)** $\mathbf{a},\mathbf{b},\mathbf{c}$ を3辺とする平行六面体の体積を求めよ。

**解答**:

(1) $\mathbf{a}\cdot\mathbf{b}=2-1-2=-1$

(2) $\mathbf{a}\times\mathbf{b}=(1\cdot2-(-1)(-1), (-1)\cdot1-2\cdot2, 2\cdot(-1)-1\cdot1)=(2-1,-1-4,-2-1)=(1,-5,-3)$

(3) $\det\begin{pmatrix}2&1&-1\\1&-1&2\\3&0&1\end{pmatrix}=2(-1-0)-1(1-6)+(-1)(0+3)=−2+5−3=0$

体積 $=|0|=0$ (3ベクトルが同一平面内)

---

## 予測問題 5 ★★ (積分応用 — R6新出パターン)

**[追加]** 曲線 $y=\cos x$ ($0\le x\le\frac{\pi}{2}$) と $x$ 軸・$y$ 軸で囲まれた図形を $x$ 軸まわりに回転させてできる体積を求めよ。

**解答**:

$$V=\pi\int_0^{\pi/2}\cos^2x\,dx=\pi\int_0^{\pi/2}\frac{1+\cos2x}{2}dx=\frac{\pi}{2}\left[x+\frac{\sin2x}{2}\right]_0^{\pi/2}=\frac{\pi^2}{4}$$
