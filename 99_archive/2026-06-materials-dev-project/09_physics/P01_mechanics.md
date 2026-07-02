# P01: 力学（Mechanics）

---

## 1. 運動方程式（Newton's Second Law）

$$\mathbf{F} = m\mathbf{a} = m\ddot{\mathbf{r}}$$

1次元: $F = m\ddot{x}$

### 主要な力

| 力 | 式 |
|----|-----|
| 重力 | $F = -mg$（下向き正で $+mg$） |
| 弾性力（フック） | $F = -kx$ |
| 摩擦力（動） | $f = \mu_k N$（運動方向と逆向き） |
| 摩擦力（静） | $f \leq \mu_s N$ |
| 空気抵抗 | $F = -bv$ または $F = -bv^2$ |

---

## 2. エネルギーと仕事

### 仕事（Work）

$$W = \int_{\mathbf{r}_1}^{\mathbf{r}_2} \mathbf{F} \cdot d\mathbf{r}$$

一定力の場合: $W = \mathbf{F} \cdot \Delta\mathbf{r} = F\Delta r\cos\theta$

### 運動エネルギー（Kinetic Energy）

$$K = \frac{1}{2}mv^2$$

**仕事-エネルギー定理:** $W_\text{net} = \Delta K$

### ポテンシャルエネルギー（Potential Energy）

- 重力: $U = mgh$
- 弾性: $U = \frac{1}{2}kx^2$

### 力学的エネルギー保存則

保存力のみが働くとき:

$$E = K + U = \text{一定}$$

$$\frac{1}{2}mv_1^2 + U_1 = \frac{1}{2}mv_2^2 + U_2$$

---

## 3. 運動量・衝突（Momentum and Collisions）

### 運動量と力積

$$\mathbf{p} = m\mathbf{v}, \quad \mathbf{F} = \frac{d\mathbf{p}}{dt}$$

力積（impulse）: $\mathbf{J} = \int \mathbf{F}\,dt = \Delta\mathbf{p}$

### 運動量保存則（外力がゼロの系）

$$\mathbf{p}_\text{total} = \sum m_i \mathbf{v}_i = \text{一定}$$

### 衝突

**弾性衝突:** $K$ 保存 + $p$ 保存

1次元の場合:

$$v_1' = \frac{m_1 - m_2}{m_1 + m_2}v_1 + \frac{2m_2}{m_1 + m_2}v_2$$

$$v_2' = \frac{2m_1}{m_1 + m_2}v_1 + \frac{m_2 - m_1}{m_1 + m_2}v_2$$

**完全非弾性衝突:** $p$ 保存、$K$ は保存されない

$$m_1 v_1 + m_2 v_2 = (m_1 + m_2)V$$

**反発係数 $e$:**

$$e = -\frac{v_1' - v_2'}{v_1 - v_2} = \frac{\text{衝突後の相対速度}}{\text{衝突前の相対速度}}$$

$e = 1$: 弾性衝突、$e = 0$: 完全非弾性

---

## 4. 単振動（Simple Harmonic Motion）

運動方程式: $m\ddot{x} = -kx$

$$\ddot{x} + \omega^2 x = 0, \quad \omega = \sqrt{\frac{k}{m}}$$

一般解:

$$x(t) = A\cos(\omega t + \phi)$$

- $A$: 振幅, $\omega$: 角振動数, $\phi$: 初位相
- 周期 $T = \frac{2\pi}{\omega}$, 振動数 $f = \frac{1}{T}$

**エネルギー:**

$$E = \frac{1}{2}kA^2 = \frac{1}{2}mv_\text{max}^2 = K + U = \text{一定}$$

**単振り子（小角近似）:** $\omega = \sqrt{g/l}$

---

## 5. 回転運動

### トルクと角加速度

$$\tau = rF\sin\theta = I\alpha$$

慣性モーメント $I$:
- 質点: $I = mr^2$
- 薄い棒（端を軸）: $I = \frac{1}{3}ml^2$
- 薄い棒（中心を軸）: $I = \frac{1}{12}ml^2$
- 円板（中心を軸）: $I = \frac{1}{2}mr^2$
- 球（中心を軸）: $I = \frac{2}{5}mr^2$

### 角運動量

$$L = I\omega, \quad \tau = \frac{dL}{dt}$$

**角運動量保存則:** $\tau_\text{ext} = 0 \Rightarrow L = \text{一定}$

### 回転の運動エネルギー

$$K_\text{rot} = \frac{1}{2}I\omega^2$$

**転がり運動（スリップなし）:** $v = r\omega$

$$K_\text{total} = \frac{1}{2}mv^2 + \frac{1}{2}I\omega^2$$

---

## 6. 万有引力

$$F = G\frac{m_1 m_2}{r^2}$$

$G = 6.674 \times 10^{-11}$ N·m²/kg²

**ケプラーの法則:**
1. 楕円軌道の法則
2. 面積速度一定の法則（角運動量保存）
3. 周期の法則: $T^2 \propto a^3$（$a$: 半長軸）

**円軌道:** 重力 = 向心力

$$\frac{GMm}{r^2} = \frac{mv^2}{r} \Rightarrow v = \sqrt{\frac{GM}{r}}$$

---

## 7. 試験頻出パターン

### パターン 1: エネルギー保存

**問:** 高さ $h = 10$ m の斜面（摩擦なし）から初速 0 でスライドした。底での速度を求めよ。（$g = 10$ m/s²）

**解:** $mgh = \frac{1}{2}mv^2 \Rightarrow v = \sqrt{2gh} = \sqrt{200} = 10\sqrt{2}$ m/s

---

### パターン 2: 弾性衝突

**問:** 質量 2 kg の物体（速度 4 m/s）が静止している質量 1 kg の物体に弾性衝突した。衝突後の速度を求めよ。

**解:**

$$v_1' = \frac{2-1}{2+1} \times 4 = \frac{4}{3} \text{ m/s}$$

$$v_2' = \frac{2 \times 2}{2+1} \times 4 = \frac{16}{3} \text{ m/s}$$

**確認（エネルギー保存）:** $\frac{1}{2}(2)(4)^2 = 16$ J → $\frac{1}{2}(2)(4/3)^2 + \frac{1}{2}(1)(16/3)^2 = 16/9 + 128/9 = 144/9 = 16$ J ✓

---

### パターン 3: 単振動

**問:** ばね定数 $k = 100$ N/m のばねに質量 $m = 1$ kg のおもりをつけた。初期位置 $x_0 = 0.1$ m、初速 $v_0 = 0$。  
(a) 角振動数と周期  
(b) $t = 0.1$ s 後の位置と速度

**解:**

(a) $\omega = \sqrt{100/1} = 10$ rad/s, $T = 2\pi/10 = \pi/5 \approx 0.628$ s

(b) $x(t) = 0.1\cos(10t)$

$x(0.1) = 0.1\cos(1) \approx 0.1 \times 0.540 = 0.054$ m

$v(t) = -0.1 \times 10\sin(10t) \Rightarrow v(0.1) = -\sin(1) \approx -0.841$ m/s

---

_← 前: M06 | → 次: P02 電磁気学_
