---
title: M02 行列基礎 類題ドリル
---

# M02 行列の基礎 類題ドリル

## Easy

**E1.** $A=\begin{pmatrix}2&1\\3&4\end{pmatrix}$, $B=\begin{pmatrix}1&0\\2&1\end{pmatrix}$. $AB$ を求めよ。

**E2.** $\det\begin{pmatrix}3&2\\1&4\end{pmatrix}$

**E3.** $\begin{pmatrix}1&2\\3&4\end{pmatrix}^{-1}$

**E4.** $A=\begin{pmatrix}2&1\\1&2\end{pmatrix}$. $A^2$ を求めよ。

**E5.** $\det\begin{pmatrix}1&0&0\\2&3&0\\4&5&6\end{pmatrix}$（下三角行列）

**E6.** $\begin{pmatrix}2&0\\0&3\end{pmatrix}^5$

**E7.** $\begin{pmatrix}1&2\\3&6\end{pmatrix}$ の行列式を求め、逆行列が存在するか判定せよ。

**E8.** $A=\begin{pmatrix}1&1\\0&1\end{pmatrix}$. $A^3$ を計算せよ。

**E9.** $A=\begin{pmatrix}3&0\\0&-2\end{pmatrix}$. $A^{10}$ を求めよ。

**E10.** $\det\begin{pmatrix}2&1\\-1&3\end{pmatrix}$

---

**E1:** $\begin{pmatrix}4&1\\11&4\end{pmatrix}$  
**E2:** $10$  
**E3:** $\frac{1}{-2}\begin{pmatrix}4&-2\\-3&1\end{pmatrix}=\begin{pmatrix}-2&1\\3/2&-1/2\end{pmatrix}$  
**E4:** $\begin{pmatrix}5&4\\4&5\end{pmatrix}$  
**E5:** $18$（対角成分の積）  
**E6:** $\begin{pmatrix}32&0\\0&243\end{pmatrix}$  
**E7:** $\det=0$、逆行列なし  
**E8:** $\begin{pmatrix}1&3\\0&1\end{pmatrix}$  
**E9:** $\begin{pmatrix}3^{10}&0\\0&(-2)^{10}\end{pmatrix}=\begin{pmatrix}59049&0\\0&1024\end{pmatrix}$  
**E10:** $7$

---

## Medium

**M1.** $A=\begin{pmatrix}1&2&0\\0&1&3\\0&0&1\end{pmatrix}$. $A^{-1}$ を拡大行列法で求めよ。

**M2.** $A=\begin{pmatrix}2&1\\1&2\end{pmatrix}$. 対角化して $A^n$ を求めよ。 ← R8-2 出題

**M3.** $A=\begin{pmatrix}1&2&3\\0&2&1\\0&0&3\end{pmatrix}$. $\det(A)$ と $A^{-1}$ を求めよ。

**M4.** $\det\begin{pmatrix}1&2&0\\3&1&-1\\2&4&1\end{pmatrix}$ ← R7 出題

**M5.** $A=\begin{pmatrix}3&1\\0&2\end{pmatrix}$. 対角化せよ。 ← R8-2 出題

**M6.** $A=\begin{pmatrix}1&1\\1&1\end{pmatrix}$. $A^n$ を求めよ（$n\ge1$）。

**M7.** 連立方程式 $\begin{cases}x+2y=5\\3x+y=10\end{cases}$ を行列で解け。

**M8.** $A=\begin{pmatrix}0&1\\-2&3\end{pmatrix}$. $A^{-1}$ と $\det(A)$ を求めよ。

**M9.** $AB=I$ となる $B$ を求めよ。$A=\begin{pmatrix}3&2\\1&1\end{pmatrix}$

**M10.** $A=\begin{pmatrix}2&0\\1&2\end{pmatrix}$. 固有値を求め、対角化可能か判定せよ。

---

**M1:** $\begin{pmatrix}1&-2&6\\0&1&-3\\0&0&1\end{pmatrix}$  
**M2:** $\lambda=1,3$; $A^n=\frac{1}{2}\begin{pmatrix}1+3^n&1-3^n\\1-3^n&1+3^n\end{pmatrix}$  
**M3:** $\det=6$; $A^{-1}=\frac{1}{6}\begin{pmatrix}6&-2&-4\\0&3&-1\\0&0&2\end{pmatrix}$  
**M4:** $-5$  
**M5:** $P=\begin{pmatrix}1&1\\0&1\end{pmatrix}^{-1}$... $\lambda=2,3$, $P=\begin{pmatrix}1&1\\-1&0\end{pmatrix}$  
**M6:** $\lambda=0,2$; $A^n=2^{n-1}A$ ($n\ge1$)  
**M7:** $\det=-5$; $x=3,y=1$  
**M8:** $\det=2$; $A^{-1}=\frac{1}{2}\begin{pmatrix}3&-1\\2&0\end{pmatrix}$  
**M9:** $B=A^{-1}=\begin{pmatrix}1&-2\\-1&3\end{pmatrix}$  
**M10:** 固有値 $\lambda=2$ (重根)、固有空間次元1 → **対角化不可能**

---

## Hard — 入試形式

**H1.** ← R8-2 完全模倣 ★

$A=\begin{pmatrix}2&1\\1&2\end{pmatrix}$ について:
(1) $A^2$ を計算せよ。(2) $\det(A)$ と $A^{-1}$ を求めよ。(3) $A^n$ を $n$ の式で表せ。

**H2.** $A=\begin{pmatrix}1&2&0\\3&1&-1\\2&4&1\end{pmatrix}$. $\det(A)$ と $A^{-1}$ を求めよ。 ← R7 出題

**H3.** ← 筑波大類題

$A=\begin{pmatrix}1&0&1\\0&2&0\\1&0&1\end{pmatrix}$. 固有値を求め $A$ が対角化可能か判定せよ。

**H4.** ← 電通大類題

$A=\begin{pmatrix}3&-1&0\\-1&3&0\\0&0&2\end{pmatrix}$. 固有値・固有ベクトル・対角化。

**H5.** ← 長岡技科大類題 ★

$A=\begin{pmatrix}1&a&0\\a&1&a\\0&a&1\end{pmatrix}$ ($a\neq0$) の固有値と固有ベクトル。 ← R6人間支援 出題

---

**H1:** (3) $A^n=\frac{1}{2}\begin{pmatrix}1+3^n&1-3^n\\1-3^n&1+3^n\end{pmatrix}$  
**H2:** $\det=-5$; $A^{-1}=\frac{1}{-5}\begin{pmatrix}5&-2&-2\\-5&1&1\\10&0&-5\end{pmatrix}$  
**H3:** $\lambda=0,2,2$; $\dim E_2=2$ → 対角化可能  
**H4:** $\lambda=2,4,2$; 対角化可能  
**H5:** $\lambda=1,1\pm\sqrt{2}a$; 固有ベクトル $(1,0,-1)^T$, $(1,\pm\sqrt{2},1)^T$
