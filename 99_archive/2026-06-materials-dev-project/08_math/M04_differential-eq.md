# M04: 微分方程式

---

## 1. 変数分離法（Separation of Variables）

$\frac{dy}{dx} = f(x)g(y)$ の形の方程式:

$$\frac{dy}{g(y)} = f(x)\,dx \Rightarrow \int \frac{dy}{g(y)} = \int f(x)\,dx + C$$

**例 1:** $\frac{dy}{dx} = xy$

$$\frac{dy}{y} = x\,dx \Rightarrow \ln|y| = \frac{x^2}{2} + C \Rightarrow y = Ae^{x^2/2}$$

**例 2:** $\frac{dy}{dx} = \frac{x}{y}$

$$y\,dy = x\,dx \Rightarrow \frac{y^2}{2} = \frac{x^2}{2} + C \Rightarrow y^2 - x^2 = C$$（双曲線族）

---

## 2. 1階線形微分方程式

標準形: $\frac{dy}{dx} + P(x)y = Q(x)$

**解法（積分因子法）:**

積分因子 $\mu(x) = e^{\int P(x)\,dx}$ を両辺にかける:

$$\frac{d}{dx}[\mu(x) y] = \mu(x) Q(x)$$

$$y = \frac{1}{\mu(x)}\left[\int \mu(x) Q(x)\,dx + C\right]$$

**例:** $\frac{dy}{dx} - 2xy = x$

$P(x) = -2x$, $\mu = e^{\int -2x\,dx} = e^{-x^2}$

$$\frac{d}{dx}[ye^{-x^2}] = xe^{-x^2}$$

$$ye^{-x^2} = \int xe^{-x^2}\,dx = -\frac{1}{2}e^{-x^2} + C$$

$$y = -\frac{1}{2} + Ce^{x^2}$$

---

## 3. 2階定係数線形微分方程式

標準形: $y'' + py' + qy = r(x)$

### Step 1: 同次方程式の一般解（$r(x) = 0$）

特性方程式: $\lambda^2 + p\lambda + q = 0$

**場合分け:**

| 判別式 $D = p^2 - 4q$ | 特性根 | 一般解 |
|---------------------|-------|--------|
| $D > 0$ | $\lambda_1 \neq \lambda_2$（実根） | $y = C_1 e^{\lambda_1 x} + C_2 e^{\lambda_2 x}$ |
| $D = 0$ | 重根 $\lambda$ | $y = (C_1 + C_2 x)e^{\lambda x}$ |
| $D < 0$ | $\lambda = \alpha \pm \beta i$ | $y = e^{\alpha x}(C_1\cos\beta x + C_2\sin\beta x)$ |

**例 A（$D > 0$）:** $y'' - 5y' + 6y = 0$

$\lambda^2 - 5\lambda + 6 = (\lambda-2)(\lambda-3) = 0 \Rightarrow \lambda = 2, 3$

$y = C_1 e^{2x} + C_2 e^{3x}$

**例 B（$D < 0$）:** $y'' + 4y = 0$

$\lambda^2 + 4 = 0 \Rightarrow \lambda = \pm 2i$（$\alpha=0, \beta=2$）

$y = C_1\cos 2x + C_2\sin 2x$

**例 C（$D = 0$）:** $y'' - 4y' + 4y = 0$

$(\lambda-2)^2 = 0 \Rightarrow \lambda = 2$（重根）

$y = (C_1 + C_2 x)e^{2x}$

---

### Step 2: 特殊解（未定係数法）

非同次方程式 $y'' + py' + qy = r(x)$ の特殊解 $y_p$:

| $r(x)$ の形 | $y_p$ の試行形 |
|------------|-------------|
| 多項式 $a_n x^n + \cdots$ | 同次の多項式 |
| $e^{ax}$ | $Ae^{ax}$（$a$ が特性根でなければ） |
| $e^{ax}$（$a$ が特性根） | $Axe^{ax}$（重根なら $Ax^2 e^{ax}$） |
| $\cos(bx)$ または $\sin(bx)$ | $A\cos(bx) + B\sin(bx)$ |

**例:** $y'' - 3y' + 2y = e^{3x}$

同次方程式の解: $y_h = C_1 e^x + C_2 e^{2x}$（特性根 $\lambda = 1, 2$）

$3$ は特性根でないので $y_p = Ae^{3x}$ を試す:

$$9Ae^{3x} - 9Ae^{3x} + 2Ae^{3x} = e^{3x} \Rightarrow 2A = 1 \Rightarrow A = \frac{1}{2}$$

一般解: $y = C_1 e^x + C_2 e^{2x} + \frac{1}{2}e^{3x}$

---

## 4. 初期値問題

$y(x_0) = y_0$, $y'(x_0) = y_0'$ の初期条件から $C_1, C_2$ を決定する。

**例:** $y'' + y = 0$, $y(0) = 1$, $y'(0) = 0$

一般解: $y = C_1\cos x + C_2\sin x$

$y(0) = C_1 = 1$

$y'(x) = -C_1\sin x + C_2\cos x$, $y'(0) = C_2 = 0$

**解:** $y = \cos x$

---

## 5. ラプラス変換

$f(t)$ のラプラス変換:

$$\mathcal{L}\{f(t)\} = F(s) = \int_0^{\infty} e^{-st} f(t)\,dt$$

### 主要な変換対

| $f(t)$ | $\mathcal{L}\{f(t)\} = F(s)$ |
|--------|--------------------------|
| $1$ | $\dfrac{1}{s}$ |
| $t^n$ | $\dfrac{n!}{s^{n+1}}$ |
| $e^{at}$ | $\dfrac{1}{s-a}$ |
| $\sin(at)$ | $\dfrac{a}{s^2+a^2}$ |
| $\cos(at)$ | $\dfrac{s}{s^2+a^2}$ |

### 微分の性質

$$\mathcal{L}\{f'(t)\} = sF(s) - f(0)$$
$$\mathcal{L}\{f''(t)\} = s^2 F(s) - sf(0) - f'(0)$$

**応用:** 微分方程式 $y'' + 4y = \sin t$, $y(0) = y'(0) = 0$ をラプラス変換で解く。

$s^2 Y + 4Y = \frac{1}{s^2+1} \Rightarrow Y = \frac{1}{(s^2+1)(s^2+4)}$

部分分数分解: $Y = \frac{1}{3}\cdot\frac{1}{s^2+1} - \frac{1}{3}\cdot\frac{1}{s^2+4}$

逆変換: $y = \frac{1}{3}\sin t - \frac{1}{6}\sin 2t$

---

## 6. 試験頻出パターン

### パターン 1: 変数分離法

**問:** $\frac{dy}{dx} = \frac{y^2}{x}$, $y(1) = 2$ を解け。

**解:**
$$\frac{dy}{y^2} = \frac{dx}{x} \Rightarrow -\frac{1}{y} = \ln|x| + C$$

$y(1) = 2$: $-\frac{1}{2} = 0 + C \Rightarrow C = -\frac{1}{2}$

$$y = \frac{1}{\frac{1}{2} - \ln x} = \frac{2}{1 - 2\ln x}$$

---

### パターン 2: 2階定係数

**問:** $y'' - 2y' - 3y = 0$, $y(0) = 1$, $y'(0) = -1$ を解け。

**解:** $\lambda^2 - 2\lambda - 3 = (\lambda-3)(\lambda+1) = 0$

$y = C_1 e^{3x} + C_2 e^{-x}$

$y(0) = C_1 + C_2 = 1$

$y'(0) = 3C_1 - C_2 = -1$

連立: $4C_1 = 0 \Rightarrow C_1 = 0, C_2 = 1$

**解:** $y = e^{-x}$

---

_← 前: M03 | → 次: M05 確率・統計_
