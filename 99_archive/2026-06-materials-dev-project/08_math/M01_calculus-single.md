# M01: 微分積分（1変数）

---

## 1. 極限（Limits）

### 定義

関数 $f(x)$ が $x \to a$ のとき $L$ に近づくとき、

$$\lim_{x \to a} f(x) = L$$

と書く。「$f(a)$ の値」とは異なる概念。

### 重要な極限公式

$$\lim_{x \to 0} \frac{\sin x}{x} = 1$$

$$\lim_{x \to \infty} \left(1 + \frac{1}{n}\right)^n = e \approx 2.71828$$

$$\lim_{x \to 0} \frac{e^x - 1}{x} = 1$$

### ロピタルの定理

$\lim_{x \to a} f(x) = \lim_{x \to a} g(x) = 0$ または $\pm\infty$ のとき:

$$\lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)}$$

**例:**
$$\lim_{x \to 0} \frac{\sin x}{x} \overset{\text{ロピタル}}{=} \lim_{x \to 0} \frac{\cos x}{1} = 1$$

---

## 2. 微分（Differentiation）

### 定義

$$f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$$

### 基本公式

| $f(x)$ | $f'(x)$ |
|--------|---------|
| $c$（定数） | $0$ |
| $x^n$ | $n x^{n-1}$ |
| $e^x$ | $e^x$ |
| $\ln x$ | $\dfrac{1}{x}$ |
| $\sin x$ | $\cos x$ |
| $\cos x$ | $-\sin x$ |
| $\tan x$ | $\sec^2 x = \dfrac{1}{\cos^2 x}$ |

### 積の微分・商の微分

$$[f(x) g(x)]' = f'(x) g(x) + f(x) g'(x)$$

$$\left[\frac{f(x)}{g(x)}\right]' = \frac{f'(x)g(x) - f(x)g'(x)}{[g(x)]^2}$$

### 合成関数の微分（チェーンルール）

$$[f(g(x))]' = f'(g(x)) \cdot g'(x)$$

**例:**
$$[\sin(x^2)]' = \cos(x^2) \cdot 2x = 2x\cos(x^2)$$

$$[e^{3x}]' = e^{3x} \cdot 3 = 3e^{3x}$$

$$[\ln(\cos x)]' = \frac{1}{\cos x} \cdot (-\sin x) = -\tan x$$

---

## 3. 高次導関数と応用

### 高次導関数

$$f''(x) = [f'(x)]', \quad f^{(n)}(x) = [f^{(n-1)}(x)]'$$

**例:** $f(x) = e^{ax}$ のとき $f^{(n)}(x) = a^n e^{ax}$

### 極値の判定

$f'(c) = 0$ かつ：

- $f''(c) > 0$ → $x = c$ で**極小（最小）**
- $f''(c) < 0$ → $x = c$ で**極大（最大）**
- $f''(c) = 0$ → さらに調査が必要

### テイラー展開（Taylor Expansion）

$x = a$ の周りでの展開:

$$f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!}(x-a)^n$$

$a = 0$ の場合をマクローリン展開という:

$$e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots$$

$$\sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots$$

$$\cos x = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \cdots$$

$$\ln(1+x) = x - \frac{x^2}{2} + \frac{x^3}{3} - \cdots \quad (|x| < 1)$$

$$\frac{1}{1-x} = 1 + x + x^2 + \cdots \quad (|x| < 1)$$

---

## 4. 積分（Integration）

### 不定積分の基本公式

| $f(x)$ | $\int f(x)\,dx$ |
|--------|----------------|
| $x^n$ ($n \neq -1$) | $\dfrac{x^{n+1}}{n+1} + C$ |
| $\dfrac{1}{x}$ | $\ln|x| + C$ |
| $e^x$ | $e^x + C$ |
| $e^{ax}$ | $\dfrac{e^{ax}}{a} + C$ |
| $\sin x$ | $-\cos x + C$ |
| $\cos x$ | $\sin x + C$ |
| $\dfrac{1}{1+x^2}$ | $\arctan x + C$ |

### 置換積分

$x = g(t)$ として $dx = g'(t)\,dt$:

$$\int f(x)\,dx = \int f(g(t))\,g'(t)\,dt$$

**例:**
$$\int x e^{x^2}\,dx \quad \Rightarrow \quad t = x^2, dt = 2x\,dx$$
$$= \int e^t \frac{dt}{2} = \frac{e^{x^2}}{2} + C$$

### 部分積分

$$\int f(x) g'(x)\,dx = f(x)g(x) - \int f'(x) g(x)\,dx$$

**LIATE 則（どちらを $f$ にするか）:**  
対数関数 > 逆三角 > 代数 > 三角 > 指数（左から優先して $f$ に）

**例:**
$$\int x e^x\,dx = x e^x - \int e^x\,dx = x e^x - e^x + C = (x-1)e^x + C$$

$$\int \ln x\,dx = x\ln x - \int x \cdot \frac{1}{x}\,dx = x\ln x - x + C$$

### 定積分と面積

$$\int_a^b f(x)\,dx = F(b) - F(a)$$

（$F'(x) = f(x)$）

$f(x) \geq 0$ のとき、$[a, b]$ における $y = f(x)$ の下の面積 $= \int_a^b f(x)\,dx$

---

## 5. 広義積分

$$\int_0^{\infty} e^{-x}\,dx = \lim_{R \to \infty} \int_0^R e^{-x}\,dx = \lim_{R \to \infty} [-e^{-x}]_0^R = 1$$

$$\int_0^{\infty} e^{-ax^2}\,dx = \frac{\sqrt{\pi}}{2\sqrt{a}} \quad (a > 0)$$（ガウス積分）

---

## 6. 試験頻出問題のパターン

### パターン 1: 微分の計算

**問:** $f(x) = x^3 \sin x$ を微分せよ。

**解:** 積の微分 → $f'(x) = 3x^2 \sin x + x^3 \cos x$

---

### パターン 2: 極値の判定

**問:** $f(x) = x^3 - 3x$ の極値を求めよ。

**解:**
$$f'(x) = 3x^2 - 3 = 3(x-1)(x+1)$$

$f'(x) = 0$ → $x = \pm 1$

| | $x<-1$ | $x=-1$ | $-1<x<1$ | $x=1$ | $x>1$ |
|--|--------|--------|---------|-------|-------|
| $f'$ | $+$ | $0$ | $-$ | $0$ | $+$ |
| $f$ | ↗ | 極大 | ↘ | 極小 | ↗ |

$f(-1) = 2$（極大）、$f(1) = -2$（極小）

---

### パターン 3: 定積分の計算

**問:** $\displaystyle\int_0^1 x e^{-x}\,dx$ を求めよ。

**解:** 部分積分（$f = x, g' = e^{-x}$）

$$= \left[-x e^{-x}\right]_0^1 + \int_0^1 e^{-x}\,dx = -e^{-1} + \left[-e^{-x}\right]_0^1 = -e^{-1} + (1 - e^{-1}) = 1 - 2e^{-1}$$

---

### パターン 4: テイラー展開の応用

**問:** $e^x$ の $x=0$ まわりの3次のテイラー多項式を求め、$\displaystyle\lim_{x \to 0} \frac{e^x - 1 - x}{x^2}$ を計算せよ。

**解:**
$$e^x \approx 1 + x + \frac{x^2}{2} + \frac{x^3}{6} + \cdots$$

$$\frac{e^x - 1 - x}{x^2} \approx \frac{\frac{x^2}{2} + O(x^3)}{x^2} \to \frac{1}{2} \quad (x \to 0)$$

---

_→ 次: M02 微分積分（多変数）_
