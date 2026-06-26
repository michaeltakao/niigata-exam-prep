---
title: P05 ODEを使った力学 — 空気抵抗・終端速度
---

# P05 ODEを使った力学

## 1. 直感的説明

空気抵抗は「速度に比例して反対向きに働く力」です。
速度が大きくなると抵抗も大きくなり、やがて重力と釣り合う → **終端速度**。

---

## 2. 速度比例抵抗

速度に比例する抵抗: $$\mathbf{F}_{\text{air}} = -k\mathbf{v}$$

### $$y$$ 方向 (鉛直)

<div class="callout callout-formula" markdown="1">

$$m\dot{v}_y = -mg - kv_y \quad (v_y: \text{上方向正})$$

これは1階線形ODE。

</div>

### 解法 (変数分離)

$$m\dot{v}_y + kv_y = -mg$$

斉次解: $$v_h = Ce^{-(k/m)t}$$

特殊解: $$v_p = -\frac{mg}{k}$$（定常状態）

一般解:
<div class="callout callout-formula" markdown="1">

$$v_y(t) = \left(v_{y0} + \frac{mg}{k}\right)e^{-(k/m)t} - \frac{mg}{k}$$

</div>

### 終端速度

$$t\to\infty$$ で:
<div class="callout callout-formula" markdown="1">

$$v_\infty = -\frac{mg}{k} \quad\text{（下向きに } \frac{mg}{k}\text{）}$$

</div>

---

## 3. 例題 — 新潟大学 R8 問題I (B)

<div class="callout callout-example" markdown="1">

初速の $$y$$ 成分 $$v_{y0}=v_0\sin\theta$$ のとき:

$$v_y(t) = \left(v_0\sin\theta+\frac{mg}{k}\right)e^{-(k/m)t} - \frac{mg}{k}$$

$$x$$ 方向 ($$\ddot{x}=-\frac{k}{m}\dot{x}$$):
$$v_x(t) = v_0\cos\theta\cdot e^{-(k/m)t}$$

終端速度 ($$y$$ 成分): $$\displaystyle-\frac{mg}{k}$$（下向き）

</div>

---

## 4. 数学との接続

この問題で使う ODE 解法 = **M07 の1階線形ODE**と同じ。

$$m\dot{v}+kv=-mg$$ を変数分離で解く:
$$\frac{dv}{mg/k+v}=-\frac{k}{m}dt \Rightarrow \ln\left\vert v+\frac{mg}{k}\right\vert =-\frac{k}{m}t+C$$

---

## 5. よくある間違い

<div class="callout callout-warning" markdown="1">

- **符号の向き**: 重力と空気抵抗の向きを両方チェックする
- **終端速度は速度の絶対値**: $$v_\infty=mg/k$$ (大きさ)、下向きに働く
- **$$x$$ 方向も ODE**: $$\ddot{x}=-(k/m)\dot{x}$$ → 等加速度ではない

</div>

---

## 6. 新潟大学での出題パターン

<div class="callout callout-examtip" markdown="1">

- **R8 問題I(4)(5)(6)**: 空気抵抗ODE → $$x,y$$ の速度 → 終端速度
- **数学 M07 と連携**: ODE を解く際に M07 の手順を使う

</div>
