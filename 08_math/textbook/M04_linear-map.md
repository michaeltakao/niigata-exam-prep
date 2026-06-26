---
title: M04 線形写像 — Im・Ker・基底
---

# M04 線形写像

## 1. 直感的説明

線形写像 $$f: \mathbb{R}^n \to \mathbb{R}^m$$ は「直線性を保つ変換」です。
「足し算とスカラー倍を保存する」関数と考えてください。

$$f(\mathbf{u}+\mathbf{v}) = f(\mathbf{u})+f(\mathbf{v}), \quad f(c\mathbf{u}) = cf(\mathbf{u})$$

行列 $$A$$ を使って $$f(\mathbf{x})=A\mathbf{x}$$ と表せます。

---

## 2. 表現行列

線形写像 $$f: \mathbb{R}^n \to \mathbb{R}^m$$ の表現行列 $$A$$ は:

<div class="callout callout-formula" markdown="1">

$$A = \begin{pmatrix}f(\mathbf{e}_1) & f(\mathbf{e}_2) & \cdots & f(\mathbf{e}_n)\end{pmatrix}$$

（標準基底 $$\mathbf{e}_1,\ldots,\mathbf{e}_n$$ の像を列に並べる）

</div>

### 例題

<div class="callout callout-example" markdown="1">

$$f:\mathbb{R}^3\to\mathbb{R}^2$$ が $$f(\mathbf{e}_1)=(1,2)^T$$, $$f(\mathbf{e}_2)=(-1,1)^T$$, $$f(\mathbf{e}_3)=(2,0)^T$$ のとき:

$$A = \begin{pmatrix}1&-1&2\\2&1&0\end{pmatrix}$$

</div>

---

## 3. 像 (Im) と核 (Ker)

### 核 (Kernel)

<div class="callout callout-formula" markdown="1">

$$\ker(f) = \{\mathbf{x}\in\mathbb{R}^n \mid f(\mathbf{x})=\mathbf{0}\} = \{\mathbf{x}\mid A\mathbf{x}=\mathbf{0}\}$$

**求め方**: $$A\mathbf{x}=\mathbf{0}$$ を行基本変形で解く

</div>

### 像 (Image)

<div class="callout callout-formula" markdown="1">

$$\operatorname{Im}(f) = \{f(\mathbf{x})\mid\mathbf{x}\in\mathbb{R}^n\} = \{A\mathbf{x}\mid\mathbf{x}\in\mathbb{R}^n\}$$

$$= $$ $$A$$ の**列ベクトルの張る部分空間** (列空間)

**求め方**: $$A$$ の列ベクトルのうち線形独立なものを基底とする

</div>

### 次元定理 (重要)

<div class="callout callout-formula" markdown="1">

$$\dim\ker(f) + \dim\operatorname{Im}(f) = n \quad (n = \text{定義域の次元})$$

</div>

---

## 4. 行基本変形による求解

### 手順 — ker を求める

1. $$(A\,\vert \,\mathbf{0})$$ を作る
2. 行基本変形で行簡約形 (RREF) にする
3. 自由変数を含む形で解を書く

### 例題 — Im と ker の計算

<div class="callout callout-example" markdown="1">

$$A = \begin{pmatrix}1&-1&2\\2&1&0\end{pmatrix}$$

**ker を求める**: $$A\mathbf{x}=\mathbf{0}$$

$$\begin{pmatrix}1&-1&2\\2&1&0\end{pmatrix}\to\begin{pmatrix}1&-1&2\\0&3&-4\end{pmatrix}\to\begin{pmatrix}1&0&2/3\\0&1&-4/3\end{pmatrix}$$

$$x_3=t$$ (自由変数) とすると: $$x_1=-\frac{2}{3}t$$, $$x_2=\frac{4}{3}t$$

$$\ker(f) = \operatorname{span}\left\{\begin{pmatrix}-2\\4\\3\end{pmatrix}\right\} \quad(\dim\ker=1)$$

**Im を求める**: $$A$$ の列は $$(1,2)^T$$, $$(-1,1)^T$$, $$(2,0)^T$$。

$$(1,2)^T$$ と $$(-1,1)^T$$ の行列式 $$= 1\cdot1-2\cdot(-1)=3\neq0$$ → 線形独立

$$\operatorname{Im}(f) = \mathbb{R}^2 \quad(\dim\operatorname{Im}=2)$$

**確認**: $$\dim\ker + \dim\operatorname{Im} = 1+2 = 3 = n$$ ✓

</div>

---

## 5. よくある間違い

<div class="callout callout-warning" markdown="1">

- **Im は行空間ではなく列空間**: $$A\mathbf{x}$$ は $$A$$ の列ベクトルの線形結合
- **ker の基底**: 自由変数で「整数化」してから基底を書く（分数のまま書いてもよいが整数の方が見やすい）
- **次元定理の確認**: Im と ker を求めたら必ず次元の和が $$n$$ になるか確認する

</div>

---

## 6. 新潟大学での出題パターン

<div class="callout callout-examtip" markdown="1">

- **R8-1 問題II**: 表現行列→Im(次元)→ker(次元) の3小問
- **定義を問う問題**: 「Im を求めよ」= 部分空間として表現、次元を答える
- **頻出**: $$3\to2$$ 次元写像の ker が1次元（自由変数1つ）のパターン

</div>
