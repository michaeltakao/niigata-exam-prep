---
title: M05 積分 — 定積分・面積・広義積分・重積分
---

# M05 積分

## 1. 定積分の基本

### 微積分学の基本定理

::: formula
$$\int_a^b f(x)\,dx = [F(x)]_a^b = F(b)-F(a)$$

$F'(x)=f(x)$ となる原始関数 $F$ を見つけて代入するだけ
:::

### 主要な積分公式

| 関数 $f(x)$ | 原始関数 $F(x)$ |
|---|---|
| $x^n$ ($n\neq-1$) | $\frac{x^{n+1}}{n+1}$ |
| $\frac{1}{x}$ | $\ln|x|$ |
| $e^x$ | $e^x$ |
| $\sin x$ | $-\cos x$ |
| $\cos x$ | $\sin x$ |
| $\frac{1}{1+x^2}$ | $\arctan x$ |
| $\frac{1}{\sqrt{1-x^2}}$ | $\arcsin x$ |

---

## 2. 部分積分

::: formula
$$\int u\,dv = uv - \int v\,du$$

実用形: $\int f(x)g'(x)\,dx = f(x)g(x) - \int f'(x)g(x)\,dx$
:::

### 覚え方 — "たちつてと" の逆順で $u$ を選ぶ

「**対数 → 逆三角 → 多項式 → 三角 → 指数**」の順で $u$ に選ぶと計算が進む

### 例題

::: example
$$\int_0^\pi x\sin x\,dx$$

$u=x$, $dv=\sin x\,dx$ とすると $du=dx$, $v=-\cos x$

$$= [-x\cos x]_0^\pi + \int_0^\pi\cos x\,dx = \pi + [\sin x]_0^\pi = \pi+0 = \mathbf{\pi}$$
:::

---

## 3. 面積計算

### 曲線と直線 (または曲線と曲線) で囲まれた面積

::: formula
交点を $x=\alpha, \beta$ ($\alpha<\beta$) として:

$$S = \int_\alpha^\beta |f(x)-g(x)|\,dx$$

$f(x)\ge g(x)$ が確認できれば絶対値不要: $S=\int_\alpha^\beta [f(x)-g(x)]\,dx$
:::

### 例題

::: example
$y=x^2$ と $y=x+2$ で囲まれた面積を求めよ。

交点: $x^2=x+2 \Rightarrow x^2-x-2=0 \Rightarrow (x+1)(x-2)=0 \Rightarrow x=-1,2$

$[-1,2]$ で $x+2\ge x^2$ を確認（$x=0$: $2>0$ ✓）

$$S=\int_{-1}^2(x+2-x^2)\,dx=\left[\frac{x^2}{2}+2x-\frac{x^3}{3}\right]_{-1}^2$$

$x=2$: $2+4-\frac{8}{3}=6-\frac{8}{3}=\frac{10}{3}$

$x=-1$: $\frac{1}{2}-2+\frac{1}{3}=\frac{3-12+2}{6}=-\frac{7}{6}$

$$S=\frac{10}{3}-\left(-\frac{7}{6}\right)=\frac{20}{6}+\frac{7}{6}=\mathbf{\frac{9}{2}}$$
:::

---

## 4. 広義積分

積分範囲が無限大、または被積分関数が特異点を持つ場合。

### 種類と収束条件

::: formula
$$\int_1^\infty \frac{1}{x^p}\,dx\quad \begin{cases}\text{収束} & p>1\\\text{発散} & p\le1\end{cases}$$

$$\int_0^1 \frac{1}{x^p}\,dx\quad \begin{cases}\text{収束} & p<1\\\text{発散} & p\ge1\end{cases}$$
:::

### 例題

::: example
(A) $\int_0^\infty xe^{-x}\,dx$

部分積分: $u=x$, $dv=e^{-x}dx \Rightarrow du=dx$, $v=-e^{-x}$

$$=\lim_{R\to\infty}\left([-xe^{-x}]_0^R+\int_0^Re^{-x}dx\right)=0+[-e^{-x}]_0^\infty=0-(-1)=\mathbf{1}$$

（$\lim_{R\to\infty}Re^{-R}=0$ をロピタルで確認）

(B) $\int_0^1\frac{1}{\sqrt{x}}\,dx = \int_0^1 x^{-1/2}\,dx = [2\sqrt{x}]_0^1 = \mathbf{2}$
:::

---

## 5. 重積分

### 累次積分

::: formula
$$\iint_D f(x,y)\,dA = \int_a^b\left(\int_{g(x)}^{h(x)}f(x,y)\,dy\right)dx$$

まず内側の積分 ($y$ について)、次に外側 ($x$ について)
:::

### 積分順序の交換

被積分関数が $x$ を先に積分できない形 ($e^{x^2}$ 等) のとき、順序を交換する。

**手順**:
1. 元の積分の領域 $D$ を図示
2. $x,y$ の役割を入れ替えて範囲を書き直す

### 例題 — 順序交換

::: example
$$\int_0^1\int_y^1 e^{x^2}\,dx\,dy$$

元の領域: $\{(x,y)\mid 0\le y\le x, 0\le x\le 1\}$

$x$ を外側に:
$$=\int_0^1\int_0^x e^{x^2}\,dy\,dx = \int_0^1 x e^{x^2}\,dx = \frac{1}{2}[e^{x^2}]_0^1 = \frac{e-1}{2}$$
:::

---

## 6. よくある間違い

::: warning
- **部分積分の符号**: $-\int v\,du$ のマイナスを忘れやすい
- **広義積分の収束確認**: 極限が存在するか確認してから値を書く
- **面積の絶対値**: どちらの関数が上か確認してから引く順を決める
- **重積分の範囲**: 内側の積分の範囲に $x$ が含まれる（定数ではない）
:::

---

## 7. 新潟大学での出題パターン

::: examtip
- **毎年**: 定積分（部分積分）+ 面積 + 広義積分 の3小問セット
- **R7 問題I**: 重積分 + 積分順序交換
- **よく出る組み合わせ**: $\int x\sin x\,dx$ (部分積分)、$\int_0^\infty xe^{-x}dx$ (広義積分+部分積分)
:::
