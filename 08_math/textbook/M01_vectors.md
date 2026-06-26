---
title: M01 ベクトル — 内積・外積・体積
---

# M01 ベクトル

## 1. 直感的説明

ベクトルとは「向きと大きさを持つ矢印」のことです。
$$\mathbb{R}^3$$ のベクトル $$\mathbf{a} = (a_1, a_2, a_3)$$ は、空間内の矢印を表します。

---

## 2. 内積 (ドット積)

### 定義

$$\mathbf{a} \cdot \mathbf{b} = a_1 b_1 + a_2 b_2 + a_3 b_3$$

幾何的意味: $$\mathbf{a} \cdot \mathbf{b} = |\mathbf{a}||\mathbf{b}|\cos\theta$$ （$$\theta$$ は2ベクトルのなす角）

<div class="callout callout-formula" markdown="1">

**内積の性質**

- $$\mathbf{a}\cdot\mathbf{b} = 0$$ ⟺ $$\mathbf{a} \perp \mathbf{b}$$ (直交)
- $$\mathbf{a}\cdot\mathbf{a} = |\mathbf{a}|^2$$
- 交換法則: $$\mathbf{a}\cdot\mathbf{b} = \mathbf{b}\cdot\mathbf{a}$$

</div>

### 手順

1. 対応する成分を掛け合わせる
2. 合計する

### 例題 — 内積を求める

<div class="callout callout-example" markdown="1">

$$\mathbf{a}=(1,2,-1)$$, $$\mathbf{b}=(3,-1,2)$$ の内積を求めよ。

**解**: $$\mathbf{a}\cdot\mathbf{b} = 1\times3 + 2\times(-1) + (-1)\times2 = 3-2-2 = \mathbf{-1}$$

</div>

---

## 3. 外積 (クロス積)

### 定義 (行列式表現)

$$\mathbf{a}\times\mathbf{b} = \begin{vmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\\a_1&a_2&a_3\\b_1&b_2&b_3\end{vmatrix}$$

$$= (a_2b_3-a_3b_2)\,\mathbf{i} - (a_1b_3-a_3b_1)\,\mathbf{j} + (a_1b_2-a_2b_1)\,\mathbf{k}$$

幾何的意味: $$|\mathbf{a}\times\mathbf{b}| = |\mathbf{a}||\mathbf{b}|\sin\theta$$ = $$\mathbf{a}$$, $$\mathbf{b}$$ が作る平行四辺形の面積

<div class="callout callout-formula" markdown="1">

**外積の性質**

- $$\mathbf{a}\times\mathbf{b}$$ は $$\mathbf{a}$$ と $$\mathbf{b}$$ の両方に垂直
- $$\mathbf{a}\times\mathbf{b} = -(\mathbf{b}\times\mathbf{a})$$ (反交換)
- $$\mathbf{a}\times\mathbf{a} = \mathbf{0}$$

</div>

### 手順 — 覚え方

$$\mathbf{a}\times\mathbf{b} = \begin{pmatrix}a_2b_3-a_3b_2\\a_3b_1-a_1b_3\\a_1b_2-a_2b_1\end{pmatrix}$$

各成分: 残った2×2行列の行列式（符号は $$+, -, +$$）

### 例題 — 外積を求める

<div class="callout callout-example" markdown="1">

$$\mathbf{a}=(1,2,-1)$$, $$\mathbf{b}=(3,-1,2)$$ の外積を求めよ。

**解**:
$$\mathbf{a}\times\mathbf{b} = \begin{vmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\\1&2&-1\\3&-1&2\end{vmatrix}$$

- $$\mathbf{i}$$: $$2\times2-(-1)\times(-1) = 4-1=3$$
- $$\mathbf{j}$$: $$-(1\times2-(-1)\times3) = -(2+3)=-5$$
- $$\mathbf{k}$$: $$1\times(-1)-2\times3 = -1-6=-7$$

$$\therefore \mathbf{a}\times\mathbf{b} = \mathbf{(3,-5,-7)}$$

</div>

---

## 4. 平行六面体の体積 (スカラー三重積)

### 定義

3つのベクトル $$\mathbf{a}, \mathbf{b}, \mathbf{c}$$ が作る平行六面体の体積:

$$V = |\mathbf{a}\cdot(\mathbf{b}\times\mathbf{c})|$$

<div class="callout callout-formula" markdown="1">

**スカラー三重積 = 行列式**

$$\mathbf{a}\cdot(\mathbf{b}\times\mathbf{c}) = \begin{vmatrix}a_1&a_2&a_3\\b_1&b_2&b_3\\c_1&c_2&c_3\end{vmatrix}$$

（3行3列行列の行列式として一発で計算できる）

</div>

### 手順

1. 3つのベクトルを行として3×3行列を作る
2. 行列式を計算する
3. 絶対値が体積

### 例題 — 新潟大学類題

<div class="callout callout-example" markdown="1">

$$\mathbf{a}=(1,2,-1)$$, $$\mathbf{b}=(2,-1,3)$$, $$\mathbf{c}=(1,1,1)$$ を3辺とする平行六面体の体積を求めよ。

**解**:
$$V=\left|\begin{vmatrix}1&2&-1\\2&-1&3\\1&1&1\end{vmatrix}\right|$$

第1行展開:
$$= 1\cdot\begin{vmatrix}-1&3\\1&1\end{vmatrix} - 2\cdot\begin{vmatrix}2&3\\1&1\end{vmatrix} + (-1)\cdot\begin{vmatrix}2&-1\\1&1\end{vmatrix}$$

$$= 1(-1-3) - 2(2-3) + (-1)(2+1)$$

$$= -4+2-3 = -5$$

$$V = |-5| = \mathbf{5}$$

</div>

---

## 5. よくある間違い

<div class="callout callout-warning" markdown="1">

- **外積の符号忘れ**: $$\mathbf{j}$$ 成分は $$-$$ (マイナス) がつく
- **外積の交換順序**: $$\mathbf{a}\times\mathbf{b} \neq \mathbf{b}\times\mathbf{a}$$（符号が逆）
- **スカラー三重積と体積**: 行列式の値が負でも体積は正（絶対値を取る）

</div>

---

## 6. 新潟大学での出題パターン

<div class="callout callout-examtip" markdown="1">

- **R8-1 問題I**: 内積・外積・平行六面体体積の3小問セット
- **R7 問題III**: 行列式＝平行六面体体積として出題
- **毎回**: 3×3行列の行列式計算が必要 → M02 の行列式も合わせて練習すること

</div>
