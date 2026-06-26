---
title: M07 微分方程式 — 変数分離・2階線形ODE
---

# M07 微分方程式

## 1. 直感的説明

微分方程式とは「関数とその導関数の関係式」です。
「この速度で動く物体の位置は？」という問いに答えるのに使います。

---

## 2. 1階 変数分離形

$$\frac{dy}{dx} = f(x)\cdot g(y)$$

<div class="callout callout-formula" markdown="1">

**手順**:
1. $$\frac{dy}{g(y)} = f(x)\,dx$$ と分離する
2. 両辺を積分: $$\int\frac{dy}{g(y)} = \int f(x)\,dx$$
3. 積分定数 $$C$$ を含む一般解を得る
4. 初期条件があれば $$C$$ を定める

</div>

### 例題 — 新潟大学 R8-1 問題IV(3)

<div class="callout callout-example" markdown="1">

$$\frac{dy}{dx} = 2xy$$, $$y(0)=1$$

**Step 1**: 分離 $$\frac{dy}{y} = 2x\,dx$$

**Step 2**: 積分 $$\ln|y| = x^2 + C$$

**Step 3**: $$y = Ae^{x^2}$$ ($$A=e^C$$)

**Step 4**: $$y(0)=1\Rightarrow A=1$$

$$y = e^{x^2}$$

</div>

### 例題 — R7 問題II(1)

<div class="callout callout-example" markdown="1">

$$\frac{dy}{dx} = \frac{x}{y}$$, $$y(0)=2$$

分離: $$y\,dy = x\,dx$$

積分: $$\frac{y^2}{2} = \frac{x^2}{2} + C$$

$$y(0)=2$$: $$\frac{4}{2}=0+C \Rightarrow C=2$$

$$y = \sqrt{x^2+4} \quad (y>0)$$

</div>

---

## 3. 2階線形同次微分方程式

$$y'' + py' + qy = 0 \quad (p,q:\text{定数})$$

<div class="callout callout-formula" markdown="1">

**特性方程式**: $$r^2 + pr + q = 0$$

| 判別式 $$D=p^2-4q$$ | 解の形 |
|---|---|
| $$D>0$$: 実数根 $$r_1\neq r_2$$ | $$y=C_1e^{r_1x}+C_2e^{r_2x}$$ |
| $$D=0$$: 重根 $$r_1=r_2=r$$ | $$y=(C_1+C_2x)e^{rx}$$ |
| $$D<0$$: 複素数根 $$r=\alpha\pm\beta i$$ | $$y=e^{\alpha x}(C_1\cos\beta x+C_2\sin\beta x)$$ |

</div>

### 例題 — R7 問題II(2)

<div class="callout callout-example" markdown="1">

$$y'' - 3y' + 2y = 0$$

特性方程式: $$r^2-3r+2=0 \Rightarrow (r-1)(r-2)=0 \Rightarrow r=1,2$$

判別式 $$D=9-8=1>0$$ → 実数の異なる2根

$$y = C_1e^x + C_2e^{2x}$$

</div>

---

## 4. 2階線形非同次微分方程式

$$y'' + py' + qy = R(x)$$

<div class="callout callout-formula" markdown="1">

**一般解** = 同次の一般解 + 特殊解

$$y = y_h + y_p$$

$$y_h$$: $$R(x)=0$$ とした同次方程式の一般解
$$y_p$$: 非同次方程式の特殊解（1つ見つければよい）

</div>

### 特殊解の「当てずっぽう法」 (未定係数法)

| $$R(x)$$ の形 | $$y_p$$ の仮定形 |
|---|---|
| $$R(x)=Ae^{\alpha x}$$ (ただし $$\alpha$$ は特性根でない) | $$y_p=Be^{\alpha x}$$ |
| $$R(x)=A\sin\omega x$$ or $$A\cos\omega x$$ | $$y_p=B\sin\omega x+C\cos\omega x$$ |
| $$R(x)=An^n$$ | $$y_p=B_nx^n+\cdots+B_0$$ |

### 例題 — R7 問題II(3)

<div class="callout callout-example" markdown="1">

$$y'' - 3y' + 2y = e^{3x}$$

**Step 1 同次解**: $$y_h = C_1e^x+C_2e^{2x}$$（上と同じ）

**Step 2 特殊解**: $$y_p=Ae^{3x}$$ とおく（$$r=3$$ は特性根でない ✓）

代入: $$9Ae^{3x}-9Ae^{3x}+2Ae^{3x}=e^{3x}$$

$$2A=1 \Rightarrow A=\frac{1}{2}$$

**Step 3 一般解**:
$$y = C_1e^x + C_2e^{2x} + \frac{1}{2}e^{3x}$$

</div>

---

## 5. 物理との接続 — 空気抵抗ODE

速度に比例する抵抗: $$m\dot{v}=-kv$$ ($$k>0$$)

<div class="callout callout-formula" markdown="1">

変数分離で $$v(t)=v_0e^{-(k/m)t}$$

重力あり: $$m\dot{v}=-mg-kv$$（1階線形ODE、積分因子法または変数分離）

終端速度: $$\dot{v}=0 \Rightarrow v_{\infty}=-\frac{mg}{k}$$ (下向き)

</div>

---

## 6. よくある間違い

<div class="callout callout-warning" markdown="1">

- **変数分離**: $$y=0$$ の解を別途確認する（特異解）
- **特性方程式の符号**: $$y''+py'+qy=0$$ の $$p,q$$ をそのまま特性方程式に代入する（$$+$$ のまま）
- **特殊解の選び方**: $$R(x)=e^{\alpha x}$$ で $$\alpha$$ が特性根の場合は $$y_p=Axe^{\alpha x}$$ に変える

</div>

---

## 7. 新潟大学での出題パターン

<div class="callout callout-examtip" markdown="1">

- **R8-1 問題IV(3)**: 変数分離 ($$dy=2xy$$)
- **R7 問題II(1)(2)(3)**: 変数分離→2階同次→非同次 の3小問セット
- **連携**: 物理 P05（空気抵抗ODE）と数学 M07 は同じ解法

</div>
