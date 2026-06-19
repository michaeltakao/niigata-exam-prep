---
title: 物理 過去問 R6 (機械システム工学プログラム)
---

# 物理 過去問 — 令和6年度 機械システム工学プログラム

> 出典: 新潟大学工学部第3年次編入学 令和6年度 専門基礎科目(物理)
> プログラム: 機械システム工学プログラム

---

## 問題 I — 合成重心

図1の斜線部 — 半径 $r$ の円弧 ABC と線分 AC によって構成される図形の重心の $x$ 座標 $x_G$ を求めよ。
この図形は $x$ 軸に関して対称である。円周率を $\pi$、角度 $\alpha$ の単位は rad とする。

（図形: 原点 O から角度 $\alpha$ の扇形 OABC から、三角形 OAC を引いた月形領域）

**(1)** 二等辺三角形 OAC の面積 $S_1$ とその重心の $x$ 座標 $x_1$ を求めよ。

**(2)** 扇形 OABC の面積 $S_2$ とその重心の $x$ 座標 $x_2$ を求めよ。

**(3)** 問(1)(2)の結果を用いて $x_G$ を求めよ。また、$r=1$、$\alpha=\frac{\pi}{2}$ rad のときの $x_G$ の値を求めよ。

---

## 問題 II — 定滑車と物体の運動

図2(a): 半径 $R$ の定滑車に巻きついた糸の先端に質量 $m$ の物体がぶら下がっている。初期状態では手で支えられている。手を放した後の運動を求める。

**(1)** 定滑車を密度 $\rho$、半径 $R$、厚さ $h$ の一様な円板と考える。
図2(b) の微小幅 $dr$ を持つ円環要素の質量を求め、そこから円板の回転中心まわりの慣性モーメント $I$ を求めよ。

**(2)** 滑車の回転角度 $\theta$ rad、物体の位置 $y$ を定義する（初期状態で $\theta=0, y=0$）。
系の運動方程式を求め、物体の落下加速度の大きさ $\beta$ を求めよ。
さらに $\beta=\frac{1}{2}g$ となる滑車の質量 $m_p$ を求めよ。

---

## 解答方針

### I (1) 三角形の面積と重心

A = $(r\cos\alpha, r\sin\alpha)$、C = $(r\cos\alpha, -r\sin\alpha)$（$x$軸対称）

**面積**: 底辺 $AC=2r\sin\alpha$、高さ $=r\cos\alpha$（O から AC までの距離? → OBの定義が必要）

実際には OAC は頂角 $2\alpha$ の二等辺三角形:

$$S_1=\frac{1}{2}r^2\sin2\alpha=r^2\sin\alpha\cos\alpha$$

**重心の $x$ 座標**: 三角形の重心 = 頂点の平均

頂点 O=$(0,0)$、A=$(r\cos\alpha,r\sin\alpha)$、C=$(r\cos\alpha,-r\sin\alpha)$

$$x_1=\frac{0+r\cos\alpha+r\cos\alpha}{3}=\frac{2r\cos\alpha}{3}$$

### I (2) 扇形の面積と重心

$$S_2=\frac{1}{2}r^2\cdot2\alpha=r^2\alpha$$

扇形の重心の $x$ 座標（既知公式）:
$$x_2=\frac{2r\sin\alpha}{3\alpha}$$

（証明: $x_2=\frac{1}{S_2}\int_0^\alpha r\cos\theta\cdot\frac{1}{2}r^2\,d\theta\cdot2$... 積分で導出可）

### I (3) 合成重心

月形領域 = 扇形 − 三角形

$$x_G=\frac{S_2 x_2-S_1 x_1}{S_2-S_1}=\frac{r^2\alpha\cdot\frac{2r\sin\alpha}{3\alpha}-r^2\sin\alpha\cos\alpha\cdot\frac{2r\cos\alpha}{3}}{r^2\alpha-r^2\sin\alpha\cos\alpha}$$

$$=\frac{\frac{2r^3\sin\alpha}{3}-\frac{2r^3\sin\alpha\cos^2\alpha}{3}}{r^2(\alpha-\sin\alpha\cos\alpha)}=\frac{\frac{2r^3\sin\alpha(1-\cos^2\alpha)}{3}}{r^2(\alpha-\sin\alpha\cos\alpha)}$$

$$=\frac{2r\sin^3\alpha}{3(\alpha-\sin\alpha\cos\alpha)}$$

$r=1, \alpha=\frac{\pi}{2}$ のとき:

$\sin\frac{\pi}{2}=1$、$\cos\frac{\pi}{2}=0$

$$x_G=\frac{2\cdot1\cdot1^3}{3\left(\frac{\pi}{2}-1\cdot0\right)}=\frac{2}{3\cdot\frac{\pi}{2}}=\frac{4}{3\pi}$$

### II (1) 慣性モーメントの導出

半径 $r$ の円環要素 (幅 $dr$, 厚さ $h$, 密度 $\rho$):

質量: $dm = \rho\cdot2\pi r\cdot h\cdot dr$

$dm$ の慣性モーメント: $dI = r^2\,dm = 2\pi\rho h r^3\,dr$

積分:
$$I=\int_0^R 2\pi\rho h r^3\,dr=2\pi\rho h\left[\frac{r^4}{4}\right]_0^R=\frac{\pi\rho h R^4}{2}$$

円板の全質量 $m_p=\rho\pi R^2 h$ を使うと:

$$\boxed{I=\frac{1}{2}m_p R^2}$$

### II (2) 運動方程式と加速度

糸がすべらない: $y=R\theta$（下向きを $y$ 正）→ $\ddot{y}=R\ddot{\theta}$

物体 $m$ の運動方程式（下向き正）:
$$mg-T=m\ddot{y}=m\beta\quad\cdots(1)$$

滑車の回転方程式（時計回り正）:
$$TR=I\ddot{\theta}=I\frac{\beta}{R}\quad\cdots(2)$$

(2) より $T=\frac{I\beta}{R^2}=\frac{m_p\beta}{2}$（$I=\frac{1}{2}m_pR^2$を代入）

(1)に代入:
$$mg-\frac{m_p\beta}{2}=m\beta\Rightarrow mg=\beta\left(m+\frac{m_p}{2}\right)$$

$$\boxed{\beta=\frac{mg}{m+\frac{m_p}{2}}}$$

$\beta=\frac{1}{2}g$ のとき:
$$\frac{1}{2}g=\frac{mg}{m+\frac{m_p}{2}}\Rightarrow m+\frac{m_p}{2}=2m\Rightarrow m_p=2m$$

---

## R6機械が物理 Tier 分析に与える影響

| トピック | R8 | R7 | **R6機** | 頻度 | 変更 |
|---|:---:|:---:|:---:|:---:|---|
| 運動方程式の立式 | ✓ | ✓ | **✓** | 3/3 | Tier 1 ★ 維持 |
| 複数物体の連立 | ✓ | ✓ | **✓** | 3/3 | Tier 1 ★ 維持 |
| 摩擦力 | ✓ | ✓ | — | 2/3 | Tier 1 維持 |
| 慣性モーメント (積分) | — | ✓ | **✓** | 2/3 | **Tier 1 に昇格** |
| **重心の計算 (面積分割)** | — | — | **✓** | 1/3 | **Tier 1 新出** |
| 角運動量保存 | — | ✓ | — | 1/3 | Tier 1 維持 |
| 空気抵抗ODE | ✓ | — | — | 1/3 | Tier 1 維持 |
