# P03: 波動・熱力学

---

## Part A: 波動（Waves）

---

## A1. 波動の基本

### 波の基本式

$$y(x, t) = A\sin(kx - \omega t + \phi)$$

- $A$: 振幅（amplitude）
- $k = 2\pi/\lambda$: 波数（wave number）
- $\omega = 2\pi f$: 角振動数
- $\lambda$: 波長, $f = 1/T$: 振動数, $T$: 周期
- $\phi$: 初期位相

**波の速さ:**

$$v = \lambda f = \frac{\omega}{k}$$

### 波動方程式

$$\frac{\partial^2 y}{\partial t^2} = v^2 \frac{\partial^2 y}{\partial x^2}$$

---

## A2. 重ね合わせと干渉

### 定在波（Standing Waves）

同じ振幅・波長で逆向きに進む2つの波:

$$y_1 = A\sin(kx - \omega t), \quad y_2 = A\sin(kx + \omega t)$$

$$y_1 + y_2 = 2A\sin(kx)\cos(\omega t)$$

**節（node）:** $\sin(kx) = 0$ → $x = n\lambda/2$

**腹（antinode）:** $|\sin(kx)| = 1$ → $x = (2n+1)\lambda/4$

### 弦の共鳴

両端固定の弦（長さ $L$）:

$$\lambda_n = \frac{2L}{n}, \quad f_n = \frac{nv}{2L} \quad (n = 1, 2, 3, \ldots)$$

$n = 1$: 基本振動、$n > 1$: 高調波

---

## A3. 音波とドップラー効果

### 音速

$$v_\text{sound} = \sqrt{\frac{\gamma RT}{M}} \approx 340 \text{ m/s}（室温）$$

$\gamma$: 比熱比, $R$: 気体定数, $T$: 絶対温度, $M$: 分子量

### ドップラー効果

音源速度 $v_s$、観測者速度 $v_o$（音源に向かう方向を正）:

$$f' = f \cdot \frac{v + v_o}{v - v_s}$$

（$v$: 音速）

**例:** 音源が近づくとき（$v_s > 0$, $v_o = 0$）: $f' = f\frac{v}{v-v_s} > f$（高く聞こえる）

---

## A4. 光波と干渉

### ヤングの二重スリット

スリット間隔 $d$、スクリーンまでの距離 $L$:

**明線（干渉強め）:** $d\sin\theta = m\lambda$ → $y_m = m\frac{\lambda L}{d}$

**暗線（干渉弱め）:** $d\sin\theta = (m + \frac{1}{2})\lambda$

### 薄膜干渉

薄膜（厚さ $d$、屈折率 $n$）:

光路差 = $2nd$

**強め合い（反射率の違いに注意）:**  
両界面で固定端反射なら: $2nd = m\lambda$

### 回折格子

$$d\sin\theta = m\lambda$$

---

## Part B: 熱力学（Thermodynamics）

---

## B1. 熱力学の法則

### 第0法則: 熱平衡の推移律

A と C が熱平衡、B と C が熱平衡 → A と B も熱平衡

### 第1法則: エネルギー保存

$$\Delta U = Q - W$$

- $\Delta U$: 内部エネルギーの変化
- $Q$: 系が吸収した熱
- $W$: 系が外にした仕事 $W = \int p\,dV$

### 第2法則: エントロピーの増大

孤立系のエントロピー $S$ は単調に増加する（または変化しない）。

$$dS = \frac{dQ_\text{rev}}{T}$$

### 第3法則: 絶対零度

$T \to 0$ K のとき $S \to 0$（または定数）

---

## B2. 理想気体

$$PV = nRT$$

$n$: モル数, $R = 8.314$ J/(mol·K), $T$: 絶対温度

### 内部エネルギー

- 単原子理想気体: $U = \frac{3}{2}nRT$
- 2原子理想気体: $U = \frac{5}{2}nRT$

### 比熱

| | 単原子 | 2原子 |
|--|--------|-------|
| $C_V$（定積） | $\frac{3}{2}R$ | $\frac{5}{2}R$ |
| $C_P$（定圧） | $\frac{5}{2}R$ | $\frac{7}{2}R$ |
| $\gamma = C_P/C_V$ | $\frac{5}{3}$ | $\frac{7}{5}$ |

---

## B3. 熱力学的過程

| 過程 | 条件 | 仕事 | 熱 |
|------|------|------|-----|
| 等積（isochoric） | $V = \text{const}$ | $W = 0$ | $Q = nC_V\Delta T$ |
| 等圧（isobaric） | $P = \text{const}$ | $W = P\Delta V = nR\Delta T$ | $Q = nC_P\Delta T$ |
| 等温（isothermal） | $T = \text{const}$ | $W = nRT\ln(V_2/V_1)$ | $Q = W$ |
| 断熱（adiabatic） | $Q = 0$ | $W = -\Delta U = -nC_V\Delta T$ | $Q = 0$ |

**断熱過程の関係式:**

$$PV^\gamma = \text{const}, \quad TV^{\gamma-1} = \text{const}$$

---

## B4. カルノーサイクルと熱効率

**カルノーサイクル:** 2つの等温過程 + 2つの断熱過程

$$\eta_\text{Carnot} = 1 - \frac{T_L}{T_H}$$

（$T_H$: 高温源温度、$T_L$: 低温源温度、すべて絶対温度）

**どんな熱機関も:** $\eta \leq \eta_\text{Carnot}$

---

## B5. エントロピー

$$\Delta S = \int \frac{dQ_\text{rev}}{T}$$

**理想気体のエントロピー変化:**

$$\Delta S = nC_V\ln\frac{T_2}{T_1} + nR\ln\frac{V_2}{V_1}$$

**熱伝導（不可逆過程）:**

高温 $T_1$ から低温 $T_2$ へ熱 $Q$ が移動:

$$\Delta S_\text{total} = Q\left(\frac{1}{T_2} - \frac{1}{T_1}\right) > 0$$

---

## 試験頻出パターン

### パターン 1: カルノー効率

**問:** 高温 500 K、低温 300 K のカルノー機関の効率、および熱源から 1000 J 吸収したとき仕事と放出熱を求めよ。

**解:**

$\eta = 1 - 300/500 = 0.4 = 40\%$

$W = 0.4 \times 1000 = 400$ J

$Q_L = 1000 - 400 = 600$ J

---

### パターン 2: 断熱変化

**問:** 単原子理想気体 1 mol を断熱的に体積を $V_0$ から $2V_0$ に膨張させた。初期温度 $T_0$ のとき、最終温度を求めよ。

**解:**

$TV^{\gamma-1} = \text{const}$、$\gamma = 5/3$

$T_0 V_0^{2/3} = T_f (2V_0)^{2/3}$

$T_f = T_0 / 2^{2/3} = T_0 \cdot 2^{-2/3}$

---

### パターン 3: ドップラー効果

**問:** 振動数 400 Hz の音源が 20 m/s で近づいてくる。音速 340 m/s として観測者が聞く振動数を求めよ。

**解:**

$$f' = 400 \times \frac{340}{340 - 20} = 400 \times \frac{340}{320} = 425 \text{ Hz}$$

---

_← 前: P02 | (物理教科書 完)_
