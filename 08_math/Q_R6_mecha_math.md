---
title: 数学 過去問 R6 (機械システム工学プログラム)
---

# 数学 過去問 — 令和6年度 機械システム工学プログラム

> 出典: 新潟大学工学部第3年次編入学 令和6年度 専門基礎科目(数学)
> プログラム: 機械システム工学プログラム

---

## 問題 I

**(1)** 次の極限値を求めよ。ただし $\displaystyle\lim_{\theta\to0}\frac{\sin\theta}{\theta}=1$ とする。

$$\lim_{\theta\to0}\frac{1-\cos2\theta}{\theta^2}$$

**(2)** 次の関数を微分せよ。

$$y = x^3\cos 2x$$

**(3)** 次の定積分の値を求めよ。

$$\int_0^{\pi/2}\cos^3 x\sin x\,dx$$

---

## 問題 II

曲線 $\sqrt{x}+\sqrt{2y}=1$ ($0\le x\le 1$) について、以下の問いに答えよ。

**(1)** グラフの概形を描け。

**(2)** この曲線と両座標軸で囲まれた図形 $S$ の面積を求めよ。

**(3)** 図形 $S$ を $x$ 軸のまわりに回転させてできる回転体の体積を求めよ。

---

## 解答方針

### I (1) 極限

半角公式: $1-\cos2\theta=2\sin^2\theta$

$$\lim_{\theta\to0}\frac{1-\cos2\theta}{\theta^2}=\lim_{\theta\to0}\frac{2\sin^2\theta}{\theta^2}=2\left(\lim_{\theta\to0}\frac{\sin\theta}{\theta}\right)^2=2\times1^2=\mathbf{2}$$

### I (2) 積の微分

積の微分: $(uv)'=u'v+uv'$

$u=x^3,\;v=\cos2x$

$u'=3x^2,\;v'=-2\sin2x$

$$y'=3x^2\cos2x+x^3\cdot(-2\sin2x)=x^2(3\cos2x-2x\sin2x)$$

### I (3) 置換積分

$t=\cos x$ とおくと $dt=-\sin x\,dx$

$x:0\to\frac{\pi}{2}$ のとき $t:1\to0$

$$\int_0^{\pi/2}\cos^3x\sin x\,dx=-\int_1^0 t^3\,dt=\int_0^1 t^3\,dt=\left[\frac{t^4}{4}\right]_0^1=\mathbf{\frac{1}{4}}$$

### II (1) グラフの概形

$\sqrt{x}+\sqrt{2y}=1\Rightarrow\sqrt{2y}=1-\sqrt{x}\Rightarrow y=\frac{(1-\sqrt{x})^2}{2}$

定義域: $0\le x\le1$（$1-\sqrt{x}\ge0$ から）

端点: $(0,\frac{1}{2})$, $(1,0)$

$x=0$: $y=\frac{1}{2}$、$x=1$: $y=0$。上に凸な曲線。

### II (2) 面積

$$S=\int_0^1 y\,dx=\int_0^1\frac{(1-\sqrt{x})^2}{2}\,dx$$

$t=\sqrt{x}$（$x=t^2$, $dx=2t\,dt$）とおく。$x:0\to1$ で $t:0\to1$

$$=\int_0^1\frac{(1-t)^2}{2}\cdot2t\,dt=\int_0^1 t(1-t)^2\,dt$$

$=\int_0^1 t(1-2t+t^2)\,dt=\int_0^1(t-2t^2+t^3)\,dt$

$=\left[\frac{t^2}{2}-\frac{2t^3}{3}+\frac{t^4}{4}\right]_0^1=\frac{1}{2}-\frac{2}{3}+\frac{1}{4}=\frac{6-8+3}{12}=\mathbf{\frac{1}{12}}$

### II (3) 回転体の体積

パップス・ギュルダンの定理または直接積分:

$$V=\pi\int_0^1 y^2\,dx=\pi\int_0^1\frac{(1-\sqrt{x})^4}{4}\,dx$$

$t=\sqrt{x}$（$dx=2t\,dt$）:

$$=\frac{\pi}{4}\int_0^1(1-t)^4\cdot2t\,dt=\frac{\pi}{2}\int_0^1 t(1-t)^4\,dt$$

$\int_0^1 t(1-t)^4\,dt$: ベータ関数 $B(2,5)=\frac{1!\cdot4!}{6!}=\frac{24}{720}=\frac{1}{30}$

$$V=\frac{\pi}{2}\cdot\frac{1}{30}=\mathbf{\frac{\pi}{60}}$$

---

## R6 機械が Tier 分析に与える影響

| トピック | R8-1 | R8-2 | R7 | R6機 | 頻度 | Tier変更 |
|---|:---:|:---:|:---:|:---:|:---:|---|
| **積分 (定積分・面積)** | ✓ | ✓ | ✓ | **✓** | 4/4 | **Tier 1 ★ 確定** |
| **極限** | ✓ | — | — | **✓** | 2/4 | **Tier 1 に昇格** |
| 回転体の体積 | — | — | — | **✓** | 1/4 | Tier 1 新出 |
| 積の微分 | — | — | — | **✓** | 1/4 | Tier 2 新出 |
