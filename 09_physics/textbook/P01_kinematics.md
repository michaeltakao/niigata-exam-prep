---
title: P01 運動学 — 1D/2D運動・ベクトル表示
---

# P01 運動学

## 1. 直感的説明

運動学は「力を無視して、位置・速度・加速度の関係を記述する」分野です。
「どこにいるか」「どれくらいの速さか」「どれくらい速度が変わっているか」を扱います。

---

## 2. 1次元運動

### 基本的な関係

::: formula
$$v = \frac{dx}{dt} = \dot{x}, \quad a = \frac{dv}{dt} = \ddot{x}$$

等加速度運動 ($a=\text{const}$):
$$v = v_0 + at, \quad x = x_0 + v_0t + \frac{1}{2}at^2, \quad v^2 = v_0^2 + 2a(x-x_0)$$
:::

---

## 3. 2次元運動 (ベクトル表示)

位置ベクトル $\mathbf{r}=(x,y)^T$、速度 $\mathbf{v}=\dot{\mathbf{r}}$、加速度 $\mathbf{a}=\dot{\mathbf{v}}$

各成分は独立に扱える:
$$\ddot{x} = a_x, \quad \ddot{y} = a_y$$

---

## 4. 斜方投射 (空気抵抗なし)

::: formula
$$\ddot{x}=0, \quad \ddot{y}=-g$$

$$x(t)=v_0\cos\theta\cdot t, \quad y(t)=v_0\sin\theta\cdot t-\frac{1}{2}gt^2$$

到達距離: $R=\frac{v_0^2\sin2\theta}{g}$ （$\theta=45°$ で最大）
:::

### 例題

::: example
初速 $v_0=20\,\text{m/s}$, $\theta=30°$, $g=9.8\,\text{m/s}^2$ で投射。

水平距離:
$$R=\frac{(20)^2\sin60°}{9.8}=\frac{400\cdot\frac{\sqrt{3}}{2}}{9.8}\approx35.4\;\text{m}$$
:::

---

## 5. よくある間違い

::: warning
- **$x$ 方向は等速**: $\ddot{x}=0$ なので $v_x=v_0\cos\theta$ は一定
- **最高点での速度**: $v_y=0$, $v_x=v_0\cos\theta\neq0$（速度0にはならない）
:::

---

## 6. 新潟大学での出題パターン

::: examtip
- **R8 問題I**: 斜方投射の完全解析（空気抵抗なし→あり）
- **必要な前提**: 斜方投射は P02 (運動方程式) を学んでから解くのが正式
:::
