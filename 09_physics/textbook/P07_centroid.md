---
title: P07 重心の計算 — 面積分割・合成重心 (R6新出)
---

# P07 重心の計算

> **R6機械で初出題。** 積分を使った重心計算と面積分割による合成重心。

## 1. 直感的説明

重心とは「釣り合いの点」です。平面図形の重心 $$(x_G, y_G)$$ は:

$$x_G=\frac{\iint_D x\,dA}{\iint_D dA}=\frac{\iint_D x\,dA}{S}$$

---

## 2. 基本公式

### 複合図形の合成重心

<div class="callout callout-formula" markdown="1">

$$x_G=\frac{S_1 x_1+S_2 x_2+\cdots}{S_1+S_2+\cdots}$$

引き算の場合 (大きい図形から小さい図形を引く):

$$x_G=\frac{S_{\text{大}}\cdot x_{\text{大}}-S_{\text{小}}\cdot x_{\text{小}}}{S_{\text{大}}-S_{\text{小}}}$$

</div>

### 三角形の重心

<div class="callout callout-formula" markdown="1">

$$x_G=\frac{x_A+x_B+x_C}{3}, \quad y_G=\frac{y_A+y_B+y_C}{3}$$

</div>

### 扇形の重心

<div class="callout callout-formula" markdown="1">

半角 $$\alpha$$、半径 $$r$$ の扇形（対称軸が $$x$$ 軸）:

$$x_G=\frac{2r\sin\alpha}{3\alpha}$$

**導出**: $$x_G=\frac{1}{S}\int_0^\alpha r\cos\theta\cdot\frac{1}{2}r^2\,d\theta\cdot2$$
$$=\frac{1}{r^2\alpha}\cdot\frac{r^3\sin\alpha}{1}=\frac{2r\sin\alpha}{3\alpha}$$

</div>

---

## 3. 例題 — R6機械 問題I 完全解答

<div class="callout callout-example" markdown="1">

半径 $$r$$、頂角 $$2\alpha$$ の扇形から中心の二等辺三角形を除いた「月形」領域の重心 $$x_G$$。

**Step 1**: 三角形 OAC

頂点 O=(0,0), A=$$(r\cos\alpha, r\sin\alpha)$$, C=$$(r\cos\alpha, -r\sin\alpha)$$

$$S_1=r^2\sin\alpha\cos\alpha=\frac{r^2\sin2\alpha}{2}$$

$$x_1=\frac{0+r\cos\alpha+r\cos\alpha}{3}=\frac{2r\cos\alpha}{3}$$

**Step 2**: 扇形 OABC

$$S_2=r^2\alpha,\quad x_2=\frac{2r\sin\alpha}{3\alpha}$$

**Step 3**: 合成重心

$$x_G=\frac{S_2 x_2-S_1 x_1}{S_2-S_1}$$

$$=\frac{r^2\alpha\cdot\frac{2r\sin\alpha}{3\alpha}-\frac{r^2\sin2\alpha}{2}\cdot\frac{2r\cos\alpha}{3}}{r^2\alpha-\frac{r^2\sin2\alpha}{2}}$$

分子: $$\frac{2r^3\sin\alpha}{3}-\frac{r^3\sin2\alpha\cos\alpha}{3}=\frac{2r^3\sin\alpha}{3}-\frac{r^3\cdot2\sin\alpha\cos^2\alpha}{3}$$

$$=\frac{2r^3\sin\alpha(1-\cos^2\alpha)}{3}=\frac{2r^3\sin^3\alpha}{3}$$

分母: $$r^2\left(\alpha-\sin\alpha\cos\alpha\right)=r^2\left(\alpha-\frac{\sin2\alpha}{2}\right)$$

$$\boxed{x_G=\frac{2r\sin^3\alpha}{3\left(\alpha-\sin\alpha\cos\alpha\right)}}$$

$$r=1, \alpha=\frac{\pi}{2}$$:

$$x_G=\frac{2\cdot1\cdot1^3}{3\left(\frac{\pi}{2}-1\cdot0\right)}=\frac{2}{\frac{3\pi}{2}}=\frac{4}{3\pi}\approx0.424$$

</div>

---

## 4. よくある間違い

<div class="callout callout-warning" markdown="1">

- **扇形の重心は中心ではない**: $$x_G=\frac{2r\sin\alpha}{3\alpha}$$ (常に $$x_G<r$$)
- **引き算の符号**: 月形 = 扇形 − 三角形 なので分子も $$S_2x_2-S_1x_1$$
- **三角形の重心**: 頂点の平均（面積重心・質量重心ともに同じ）

</div>

---

## 5. 新潟大学での出題パターン

<div class="callout callout-examtip" markdown="1">

- **R6機械 問題I**: 月形重心の3小問（三角形→扇形→合成）
- **計算テクニック**: $$\sin^3\alpha=\sin\alpha(1-\cos^2\alpha)=\sin\alpha-\sin\alpha\cos^2\alpha$$ を使う
- **数値代入は最後**: 一般式を求めてから $$r,\alpha$$ を代入する

</div>
