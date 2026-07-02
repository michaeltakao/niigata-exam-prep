# M06: 複素数

---

## 1. 複素数の基本

### 複素数の形式

$$z = a + bi \quad (a, b \in \mathbb{R}, i^2 = -1)$$

- $\text{Re}(z) = a$: 実部（real part）
- $\text{Im}(z) = b$: 虚部（imaginary part）
- $\bar{z} = a - bi$: 複素共役

### 演算

$$z_1 \pm z_2 = (a_1 \pm a_2) + (b_1 \pm b_2)i$$

$$z_1 z_2 = (a_1 a_2 - b_1 b_2) + (a_1 b_2 + a_2 b_1)i$$

$$\frac{z_1}{z_2} = \frac{z_1 \bar{z}_2}{|z_2|^2} = \frac{(a_1 a_2 + b_1 b_2) + (a_2 b_1 - a_1 b_2)i}{a_2^2 + b_2^2}$$

### 絶対値（modulus）

$$|z| = \sqrt{a^2 + b^2}, \quad |z|^2 = z\bar{z}$$

---

## 2. 極形式とオイラーの公式

### 極形式

$$z = r(\cos\theta + i\sin\theta) = re^{i\theta}$$

- $r = |z|$: 絶対値
- $\theta = \arg(z)$: 偏角（argument）

### オイラーの公式（最重要）

$$e^{i\theta} = \cos\theta + i\sin\theta$$

特別値:
$$e^{i\pi} = -1 \quad \text{（オイラーの等式）}$$
$$e^{i\pi/2} = i, \quad e^{-i\pi/2} = -i$$

### 積と商

$$z_1 z_2 = r_1 r_2 e^{i(\theta_1 + \theta_2)} \quad \Rightarrow \quad |z_1 z_2| = |z_1||z_2|, \; \arg(z_1 z_2) = \arg z_1 + \arg z_2$$

$$\frac{z_1}{z_2} = \frac{r_1}{r_2} e^{i(\theta_1 - \theta_2)}$$

---

## 3. ド・モアブルの定理

$$z^n = r^n (\cos n\theta + i\sin n\theta) = r^n e^{in\theta}$$

**応用（三角関数の公式導出）:**

$$(\cos\theta + i\sin\theta)^2 = \cos 2\theta + i\sin 2\theta$$

$$\Rightarrow \cos 2\theta = \cos^2\theta - \sin^2\theta, \quad \sin 2\theta = 2\sin\theta\cos\theta$$

---

## 4. $n$ 乗根（$n$-th roots）

$z^n = w$ の解（$w = r e^{i\phi}$）:

$$z_k = r^{1/n} e^{i(\phi + 2\pi k)/n} \quad (k = 0, 1, \ldots, n-1)$$

**例:** $z^4 = 1$ の解（$r=1, \phi=0$）

$$z_k = e^{i\pi k/2} \quad (k = 0,1,2,3)$$

$$z_0 = 1, \quad z_1 = i, \quad z_2 = -1, \quad z_3 = -i$$

---

## 5. 複素関数と留数定理（発展）

### 正則関数（holomorphic functions）

$\mathbb{C}$ 上で微分可能な関数。

**コーシー・リーマン方程式:**

$f(z) = u(x,y) + iv(x,y)$ が正則 $\Leftrightarrow$

$$\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}, \quad \frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}$$

### 留数定理

孤立特異点 $z_0$ での留数 $\text{Res}[f, z_0]$:

$$\oint_C f(z)\,dz = 2\pi i \sum_k \text{Res}[f, z_k]$$

（$C$ 内の特異点 $z_k$ の留数の和）

**単純極での留数:**

$$\text{Res}[f, z_0] = \lim_{z \to z_0} (z - z_0) f(z)$$

**応用（実積分の計算）:**

$$\int_{-\infty}^{\infty} \frac{1}{1+x^2}\,dx = \pi$$

$f(z) = \frac{1}{1+z^2} = \frac{1}{(z-i)(z+i)}$、上半平面内の極は $z = i$

$\text{Res}[f, i] = \frac{1}{2i}$

$$\int_{-\infty}^{\infty} \frac{dx}{1+x^2} = 2\pi i \cdot \frac{1}{2i} = \pi$$

---

## 6. 試験頻出パターン

### パターン 1: 極形式の計算

**問:** $z = 1 + \sqrt{3}i$ を極形式で表し、$z^6$ を求めよ。

**解:**

$|z| = \sqrt{1+3} = 2$, $\arg z = \arctan(\sqrt{3}/1) = \pi/3$

$z = 2e^{i\pi/3}$

$z^6 = 2^6 e^{i \cdot 6\pi/3} = 64 e^{i2\pi} = 64$

---

### パターン 2: ド・モアブルによる公式導出

**問:** $\cos 3\theta$ を $\cos\theta$ の多項式で表せ。

**解:**

$$(\cos\theta + i\sin\theta)^3 = \cos 3\theta + i\sin 3\theta$$

左辺 $= \cos^3\theta + 3\cos^2\theta(i\sin\theta) + 3\cos\theta(i\sin\theta)^2 + (i\sin\theta)^3$

$= \cos^3\theta - 3\cos\theta\sin^2\theta + i(3\cos^2\theta\sin\theta - \sin^3\theta)$

実部: $\cos 3\theta = \cos^3\theta - 3\cos\theta\sin^2\theta = \cos^3\theta - 3\cos\theta(1-\cos^2\theta) = 4\cos^3\theta - 3\cos\theta$

---

### パターン 3: 方程式の解

**問:** $z^3 = -8$ の3つの解を求めよ。

**解:** $-8 = 8e^{i\pi}$

$$z_k = 2e^{i(\pi + 2\pi k)/3} \quad (k = 0, 1, 2)$$

$$z_0 = 2e^{i\pi/3} = 1 + \sqrt{3}i$$

$$z_1 = 2e^{i\pi} = -2$$

$$z_2 = 2e^{i5\pi/3} = 1 - \sqrt{3}i$$

---

_← 前: M05 | (数学教科書 完)_
