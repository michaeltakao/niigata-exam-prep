# M02: 微分積分（多変数）

---

## 1. 偏微分（Partial Differentiation）

$f(x, y)$ の $x$ に関する偏微分:

$$\frac{\partial f}{\partial x} = f_x(x, y) = \lim_{h \to 0} \frac{f(x+h, y) - f(x, y)}{h}$$

（$y$ を定数として $x$ で微分する）

### 計算例

$f(x, y) = x^3 y^2 + \sin(xy)$ のとき:

$$f_x = 3x^2 y^2 + y\cos(xy)$$

$$f_y = 2x^3 y + x\cos(xy)$$

### 高次偏導関数

$$f_{xx} = \frac{\partial^2 f}{\partial x^2}, \quad f_{xy} = \frac{\partial^2 f}{\partial x \partial y} = \frac{\partial^2 f}{\partial y \partial x} = f_{yx}$$

（シュワルツの定理: 十分滑らかなら $f_{xy} = f_{yx}$）

---

## 2. 全微分（Total Differential）

$$df = \frac{\partial f}{\partial x} dx + \frac{\partial f}{\partial y} dy$$

**応用（誤差伝播）:** $z = f(x, y)$ での $x, y$ の微小変化 $\Delta x, \Delta y$ による $z$ の変化:

$$\Delta z \approx \frac{\partial f}{\partial x} \Delta x + \frac{\partial f}{\partial y} \Delta y$$

### 合成関数の微分（多変数版）

$z = f(x, y)$, $x = x(t)$, $y = y(t)$ のとき:

$$\frac{dz}{dt} = \frac{\partial f}{\partial x} \frac{dx}{dt} + \frac{\partial f}{\partial y} \frac{dy}{dt}$$

---

## 3. 勾配・方向微分

### 勾配（Gradient）

$$\nabla f = \text{grad}\, f = \left(\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}\right)$$

- 勾配ベクトルは **$f$ が最も急速に増加する方向** を指す
- 等高線（$f = \text{const}$）に直交する

### 方向微分（Directional Derivative）

単位ベクトル $\mathbf{u} = (u_1, u_2)$ 方向への微分:

$$D_{\mathbf{u}} f = \nabla f \cdot \mathbf{u} = f_x u_1 + f_y u_2$$

---

## 4. 極値（多変数）

$f(x, y)$ の停留点: $f_x = 0$ かつ $f_y = 0$ を満たす点

### ヘッセ行列による判定

$$H = \begin{vmatrix} f_{xx} & f_{xy} \\ f_{yx} & f_{yy} \end{vmatrix} = f_{xx} f_{yy} - (f_{xy})^2$$

| $H$ | $f_{xx}$ | 判定 |
|-----|---------|------|
| $H > 0$ | $> 0$ | 極小 |
| $H > 0$ | $< 0$ | 極大 |
| $H < 0$ | — | 鞍点（saddle point） |
| $H = 0$ | — | 判定不能 |

**例:** $f(x, y) = x^2 + y^2 - 2x - 4y + 5$ の極値を求めよ。

$$f_x = 2x - 2 = 0 \Rightarrow x = 1, \quad f_y = 2y - 4 = 0 \Rightarrow y = 2$$

$$f_{xx} = 2, f_{yy} = 2, f_{xy} = 0 \Rightarrow H = 4 - 0 = 4 > 0, \; f_{xx} > 0$$

→ $(1, 2)$ で極小、$f(1, 2) = 1 + 4 - 2 - 8 + 5 = 0$

---

## 5. ラグランジュ乗数法（制約条件下の最適化）

**問題:** $g(x, y) = 0$ の制約下で $f(x, y)$ を最大化（最小化）せよ。

**条件:**

$$\nabla f = \lambda \nabla g \quad \Leftrightarrow \quad \begin{cases} f_x = \lambda g_x \\ f_y = \lambda g_y \end{cases}$$

**例:** $x^2 + y^2 = 1$ の制約下で $f(x, y) = x + 2y$ の最大値を求めよ。

$$\nabla f = (1, 2), \quad \nabla g = (2x, 2y)$$

$$1 = 2\lambda x, \quad 2 = 2\lambda y \Rightarrow x = \frac{1}{2\lambda}, \quad y = \frac{1}{\lambda}$$

$x^2 + y^2 = 1$ に代入: $\frac{1}{4\lambda^2} + \frac{1}{\lambda^2} = 1 \Rightarrow \lambda = \pm\frac{\sqrt{5}}{2}$

最大値: $f = \frac{1}{2\lambda} + \frac{2}{\lambda} = \frac{5}{2\lambda} = \pm\sqrt{5}$ → 最大値 $\sqrt{5}$

---

## 6. 重積分（Double Integrals）

$$\iint_D f(x, y)\,dA = \int_a^b \int_{g_1(x)}^{g_2(x)} f(x, y)\,dy\,dx$$

### 累次積分の交換（フビニの定理）

$$\int_a^b \int_c^d f(x, y)\,dy\,dx = \int_c^d \int_a^b f(x, y)\,dx\,dy$$

### 極座標への変換

$x = r\cos\theta$, $y = r\sin\theta$, $dA = r\,dr\,d\theta$:

$$\iint_D f(x, y)\,dA = \int_{\theta_1}^{\theta_2} \int_{r_1}^{r_2} f(r\cos\theta, r\sin\theta)\,r\,dr\,d\theta$$

**例:** $x^2 + y^2 \leq 1$ における $\iint_D (x^2 + y^2)\,dA$

極座標で: $\int_0^{2\pi} \int_0^1 r^2 \cdot r\,dr\,d\theta = 2\pi \cdot \frac{1}{4} = \frac{\pi}{2}$

---

## 7. 試験頻出パターン

### パターン 1: 偏微分の計算

**問:** $f(x, y) = x^2 y + e^{xy}$ の $f_x, f_y, f_{xy}$ を求めよ。

**解:**
$$f_x = 2xy + ye^{xy}, \quad f_y = x^2 + xe^{xy}$$
$$f_{xy} = 2x + e^{xy} + xye^{xy}$$

---

### パターン 2: 停留点と極値

**問:** $f(x, y) = x^3 + y^3 - 3xy$ の停留点を求め、極値を判定せよ。

**解:**
$$f_x = 3x^2 - 3y = 0 \Rightarrow y = x^2$$
$$f_y = 3y^2 - 3x = 0 \Rightarrow x = y^2$$

$y = x^2$ を $x = y^2$ に代入: $x = (x^2)^2 = x^4 \Rightarrow x(x^3 - 1) = 0 \Rightarrow x = 0, 1$

停留点: $(0, 0)$ と $(1, 1)$

$f_{xx} = 6x, f_{yy} = 6y, f_{xy} = -3$

- $(0,0)$: $H = 0 \cdot 0 - 9 = -9 < 0$ → **鞍点**
- $(1,1)$: $H = 6 \cdot 6 - 9 = 27 > 0$, $f_{xx} = 6 > 0$ → **極小** $f(1,1) = -1$

---

### パターン 3: 重積分

**問:** $\displaystyle\int_0^1 \int_0^{1-x} (x + y)\,dy\,dx$ を計算せよ。

**解:**
$$\int_0^{1-x} (x+y)\,dy = \left[xy + \frac{y^2}{2}\right]_0^{1-x} = x(1-x) + \frac{(1-x)^2}{2}$$

$$= x - x^2 + \frac{1 - 2x + x^2}{2} = \frac{1}{2} - \frac{x^2}{2}$$

$$\int_0^1 \left(\frac{1}{2} - \frac{x^2}{2}\right)dx = \frac{1}{2} - \frac{1}{6} = \frac{1}{3}$$

---

_← 前: M01 | → 次: M03 線形代数_
