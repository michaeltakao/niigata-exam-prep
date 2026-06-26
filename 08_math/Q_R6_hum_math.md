---
title: 数学 過去問 R6 (人間支援感性科学プログラム)
---

# 数学 過去問 — 令和6年度 (人間支援感性科学プログラム)

> 出典: 新潟大学工学部第3年次編入学 令和6年度 専門基礎科目(数学)
>
> **注意**: このPDFは人間支援感性科学プログラム用（数学+電気回路+プログラミング）。
> 数学部分は他プログラムと共通トピックが多い。

---

## 問題 I — 数学

### (1) 重積分 (ひし形領域)

次の重積分の値を求めよ。ただし $$x, y$$ は実数とする。

$$\iint_D (x^2 - y^2)\,dx\,dy, \quad D = \{(x,y) \mid \vert x\vert +\vert y\vert  \le 1\}$$

### (2) 3×3 行列の固有値・固有ベクトル

行列

$$A = \begin{pmatrix}1&a&0\\a&1&a\\0&a&1\end{pmatrix} \quad (a \neq 0)$$

の固有値と固有ベクトルを求めよ。

---

## 解答方針

### (1) ひし形領域の重積分

**領域の確認**: $$D=\{\vert x\vert +\vert y\vert \le1\}$$ はひし形（頂点: $$(1,0),(0,1),(-1,0),(0,-1)$$）

**方法**: 被積分関数の対称性を活用する。

$$x^2-y^2$$ は $$x$$ について偶関数、$$y$$ について偶関数。
領域 $$D$$ は $$x,y$$ 両軸について対称（偶関数領域）。

$$x^2$$ の積分と $$y^2$$ の積分は領域の対称性から等しい:

$$\iint_D x^2\,dxdy = \iint_D y^2\,dxdy$$

したがって:

$$\iint_D(x^2-y^2)\,dxdy = 0$$

---

**別解（直接計算）**:

$$y$$ の積分範囲: $$x$$ 固定で $$\vert y\vert \le1-\vert x\vert $$

$$x\ge0$$ のとき $$y\in[-(1-x), 1-x]$$

第1象限+第4象限 ($$x\in[0,1]$$):
$$\int_0^1\int_{-(1-x)}^{1-x}(x^2-y^2)\,dy\,dx$$

内側: $$\int_{-(1-x)}^{1-x}(x^2-y^2)\,dy = 2(1-x)\cdot x^2 - 2\cdot\frac{(1-x)^3}{3}$$

外側: 同様に $$x\in[-1,0]$$ も計算。

対称性から合計 $$= 0$$ が確認できる。

$$\boxed{\iint_D(x^2-y^2)\,dxdy = 0}$$

---

### (2) 3×3 三重対角行列の固有値

特性方程式 $$\det(A-\lambda I)=0$$:

$$\det\begin{pmatrix}1-\lambda&a&0\\a&1-\lambda&a\\0&a&1-\lambda\end{pmatrix}$$

$$=(1-\lambda)\left[(1-\lambda)^2-a^2\right]-a\left[a(1-\lambda)-0\right]$$

$$=(1-\lambda)^3 - a^2(1-\lambda) - a^2(1-\lambda)$$

$$=(1-\lambda)^3 - 2a^2(1-\lambda)$$

$$=(1-\lambda)\left[(1-\lambda)^2-2a^2\right]=0$$

固有値:
$$\lambda_1 = 1, \quad \lambda_{2,3} = 1 \pm \sqrt{2}\,\vert a\vert $$

（$$a\neq0$$ なので3つの固有値は全て異なる）

---

**固有ベクトル**:

$$\lambda_1=1$$:
$$(A-I)\mathbf{v}=\begin{pmatrix}0&a&0\\a&0&a\\0&a&0\end{pmatrix}\mathbf{v}=0$$

$$av_2=0\Rightarrow v_2=0$$、$$av_1+av_3=0\Rightarrow v_3=-v_1$$

$$\mathbf{v}_1 = \begin{pmatrix}1\\0\\-1\end{pmatrix}$$

$$\lambda_2=1+\sqrt{2}a$$ (a>0 として):
$$(A-\lambda_2 I)=\begin{pmatrix}-\sqrt{2}a&a&0\\a&-\sqrt{2}a&a\\0&a&-\sqrt{2}a\end{pmatrix}$$

第1行: $$-\sqrt{2}v_1+v_2=0\Rightarrow v_2=\sqrt{2}v_1$$

第3行: $$v_2=\sqrt{2}v_3\Rightarrow v_3=v_1$$

$$\mathbf{v}_2 = \begin{pmatrix}1\\\sqrt{2}\\1\end{pmatrix}$$

$$\lambda_3=1-\sqrt{2}a$$:

$$\mathbf{v}_3 = \begin{pmatrix}1\\-\sqrt{2}\\1\end{pmatrix}$$

---

## トピック分析への影響

| トピック | R8-1 | R8-2 | R7 | **R6** | 頻度 |
|---|:---:|:---:|:---:|:---:|---|
| 重積分 | ✓ | — | ✓ | **✓** | 3/4 |
| 固有値・固有ベクトル | — | ✓ | — | **✓** | 2/4 |

**R6 追加の示唆**:
- ひし形領域 $$\vert x\vert +\vert y\vert \le1$$ の重積分 → 対称性を使う技術が必要
- 3×3 行列の固有値 → **対象プログラムにより出題あり**
- 重積分は3/4年で出題 → **Tier 1 ★ 確定**
