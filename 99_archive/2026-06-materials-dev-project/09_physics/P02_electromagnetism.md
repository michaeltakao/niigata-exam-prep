# P02: 電磁気学（Electromagnetism）

---

## 1. 電場と電位

### クーロンの法則

$$\mathbf{F} = k_e \frac{q_1 q_2}{r^2} \hat{r}, \quad k_e = \frac{1}{4\pi\varepsilon_0} \approx 9 \times 10^9 \text{ N·m}^2/\text{C}^2$$

$\varepsilon_0 = 8.85 \times 10^{-12}$ F/m（真空の誘電率）

### 電場（Electric Field）

$$\mathbf{E} = \frac{\mathbf{F}}{q_0} = \frac{1}{4\pi\varepsilon_0} \frac{q}{r^2} \hat{r}$$

（点電荷 $q$ からの電場）

**重ね合わせの原理:** 複数の電荷が作る電場はベクトル和

### 電位（Electric Potential）

$$V = -\int_{\infty}^{\mathbf{r}} \mathbf{E} \cdot d\mathbf{l} = \frac{1}{4\pi\varepsilon_0}\frac{q}{r}$$

$$\mathbf{E} = -\nabla V = -\frac{\partial V}{\partial x}\hat{x} - \frac{\partial V}{\partial y}\hat{y} - \frac{\partial V}{\partial z}\hat{z}$$

**ポテンシャルエネルギー:** $U = qV$

---

## 2. ガウスの法則

$$\oint_S \mathbf{E} \cdot d\mathbf{A} = \frac{Q_\text{enc}}{\varepsilon_0}$$

（面 $S$ を囲む内部の電荷 $Q_\text{enc}$）

### 応用（高対称性）

**一様球対称電荷（半径 $R$、総電荷 $Q$）:**

$$E = \begin{cases}\dfrac{Q}{4\pi\varepsilon_0 r^2} & (r > R) \\\dfrac{Qr}{4\pi\varepsilon_0 R^3} & (r < R)\end{cases}$$

**無限長円柱（線電荷密度 $\lambda$）:**

$$E = \frac{\lambda}{2\pi\varepsilon_0 r}$$

**無限平面（面電荷密度 $\sigma$）:**

$$E = \frac{\sigma}{2\varepsilon_0}$$

---

## 3. コンデンサー（Capacitors）

### 静電容量（Capacitance）

$$C = \frac{Q}{V}$$

**平行平板コンデンサー:** $C = \varepsilon_0 \frac{A}{d}$（誘電体があれば $\varepsilon = \varepsilon_r \varepsilon_0$）

### 接続

- **並列:** $C_\text{total} = C_1 + C_2 + \cdots$
- **直列:** $\frac{1}{C_\text{total}} = \frac{1}{C_1} + \frac{1}{C_2} + \cdots$

### エネルギー

$$U = \frac{1}{2}CV^2 = \frac{Q^2}{2C} = \frac{1}{2}QV$$

---

## 4. 電流・抵抗・起電力

### オームの法則

$$V = IR, \quad \mathbf{J} = \sigma\mathbf{E}$$

（$\sigma$: 電気伝導率）

**抵抗率:** $R = \rho \frac{L}{A}$

### キルヒホッフの法則

1. **電流則（KCL）:** ノードに流れ込む電流の和 = 流れ出す電流の和（電荷保存）
2. **電圧則（KVL）:** 閉ループの電圧降下の和 = 0（エネルギー保存）

### 接続

- **直列:** $R_\text{total} = R_1 + R_2 + \cdots$
- **並列:** $\frac{1}{R_\text{total}} = \frac{1}{R_1} + \frac{1}{R_2} + \cdots$

### 電力

$$P = IV = I^2 R = \frac{V^2}{R}$$

### RC 回路

充電: $q(t) = Q_0(1 - e^{-t/RC})$, 時定数 $\tau = RC$

---

## 5. 磁場・ローレンツ力

### 磁場（Magnetic Field）

ビオ・サバールの法則:

$$d\mathbf{B} = \frac{\mu_0}{4\pi} \frac{I\,d\mathbf{l} \times \hat{r}}{r^2}$$

$\mu_0 = 4\pi \times 10^{-7}$ T·m/A（真空の透磁率）

**直線電流から距離 $r$ での磁場:**

$$B = \frac{\mu_0 I}{2\pi r}$$

**ソレノイド（内部）:** $B = \mu_0 n I$（$n$: 単位長さ当たりの巻数）

### アンペールの法則

$$\oint_C \mathbf{B} \cdot d\mathbf{l} = \mu_0 I_\text{enc}$$

### ローレンツ力

$$\mathbf{F} = q(\mathbf{E} + \mathbf{v} \times \mathbf{B})$$

磁場のみ: $\mathbf{F} = q\mathbf{v} \times \mathbf{B}$（磁場は仕事をしない → 速さ不変、方向のみ変化）

**荷電粒子の円運動:**

$$qvB = \frac{mv^2}{r} \Rightarrow r = \frac{mv}{qB}$$

---

## 6. 電磁誘導

### ファラデーの法則

$$\mathcal{E} = -\frac{d\Phi_B}{dt}$$

$\Phi_B = \int \mathbf{B} \cdot d\mathbf{A}$: 磁束

**レンツの法則:** 誘起起電力は磁束の変化を妨げる向きに生じる

### 自己インダクタンス

$$\mathcal{E}_L = -L\frac{dI}{dt}$$

**ソレノイド:** $L = \mu_0 n^2 V$（$V$: 体積）

**インダクタのエネルギー:** $U = \frac{1}{2}LI^2$

### RL 回路

$$L\frac{dI}{dt} + RI = \mathcal{E}$$

解: $I(t) = \frac{\mathcal{E}}{R}(1 - e^{-Rt/L})$, 時定数 $\tau = L/R$

---

## 7. マクスウェル方程式（積分形）

$$\oint \mathbf{E} \cdot d\mathbf{A} = \frac{Q_\text{enc}}{\varepsilon_0} \quad \text{（ガウス: 電場）}$$

$$\oint \mathbf{B} \cdot d\mathbf{A} = 0 \quad \text{（ガウス: 磁場・磁気単極子なし）}$$

$$\oint \mathbf{E} \cdot d\mathbf{l} = -\frac{d\Phi_B}{dt} \quad \text{（ファラデー）}$$

$$\oint \mathbf{B} \cdot d\mathbf{l} = \mu_0 I_\text{enc} + \mu_0\varepsilon_0 \frac{d\Phi_E}{dt} \quad \text{（アンペール-マクスウェル）}$$

---

## 8. 試験頻出パターン

### パターン 1: ガウスの法則

**問:** 半径 $R$、一様体積電荷密度 $\rho$ の球。$r < R$ および $r > R$ での電場を求めよ。

**解:**

$r > R$: $E \cdot 4\pi r^2 = \frac{Q}{\varepsilon_0} = \frac{\rho \frac{4}{3}\pi R^3}{\varepsilon_0}$ → $E = \frac{\rho R^3}{3\varepsilon_0 r^2}$

$r < R$: $E \cdot 4\pi r^2 = \frac{\rho \frac{4}{3}\pi r^3}{\varepsilon_0}$ → $E = \frac{\rho r}{3\varepsilon_0}$

---

### パターン 2: キルヒホッフの法則

**問:** 2つの起電力 $\mathcal{E}_1 = 10$ V, $\mathcal{E}_2 = 6$ V と3つの抵抗 $R_1 = 2\Omega, R_2 = 3\Omega, R_3 = 1\Omega$ からなる回路の各電流を求めよ。

→ ループ方程式を立てて連立方程式を解く（KCL + KVL を使用）

---

### パターン 3: 電磁誘導

**問:** 一辺 $L$ の正方形コイルが一様磁場 $B$ 中で角速度 $\omega$ で回転している。誘起起電力の最大値と時間変化を求めよ。

**解:**

$\Phi_B = BL^2 \cos\omega t$

$\mathcal{E} = -\frac{d\Phi_B}{dt} = BL^2\omega\sin\omega t$

最大値: $\mathcal{E}_\text{max} = BL^2\omega$

---

_← 前: P01 | → 次: P03 波動_
