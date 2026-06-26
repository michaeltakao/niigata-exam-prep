---
title: M06 極限 — ロピタルの定理 (Tier 2)
---

# M06 極限

> **Tier 2**: 出題頻度は低いが R8-1 で出題あり。Tier 1 の習熟後に学習すること。

## 1. 基本的な極限

| 極限 | 値 |
|---|---|
| $$\lim_{x\to0}\frac{\sin x}{x}$$ | $$1$$ |
| $$\lim_{x\to0}\frac{1-\cos x}{x^2}$$ | $$\frac{1}{2}$$ |
| $$\lim_{x\to\infty}\left(1+\frac{1}{x}\right)^x$$ | $$e$$ |
| $$\lim_{x\to0}(1+x)^{1/x}$$ | $$e$$ |

---

## 2. ロピタルの定理

$$\frac{0}{0}$$ 型または $$\frac{\infty}{\infty}$$ 型の不定形に使える。

<div class="callout callout-formula" markdown="1">

$$\lim_{x\to a}\frac{f(x)}{g(x)} = \lim_{x\to a}\frac{f'(x)}{g'(x)}$$

条件: $$g'(x)\neq0$$ かつ右辺の極限が存在する場合

</div>

### 手順

1. $$\frac{0}{0}$$ か $$\frac{\infty}{\infty}$$ を確認する
2. 分子・分母それぞれを微分する（商の微分ではない）
3. 極限を取り直す
4. まだ不定形なら繰り返す

### 例題

<div class="callout callout-example" markdown="1">

$$\lim_{x\to0}\frac{e^x-1-x}{x^2}$$

$$x=0$$: 分子 $$=0$$, 分母 $$=0$$ → $$\frac{0}{0}$$ 型

1回目: $$\lim_{x\to0}\frac{e^x-1}{2x}$$ → まだ $$\frac{0}{0}$$

2回目: $$\lim_{x\to0}\frac{e^x}{2} = \frac{1}{2}$$

</div>

---

## 3. よくある間違い

<div class="callout callout-warning" markdown="1">

- **適用条件の確認**: ロピタルは不定形のときのみ使える。$$\frac{0}{1}$$ 型には使わない
- **商の微分との混同**: $$\frac{f'(x)}{g'(x)}$$ であり $$\left(\frac{f(x)}{g(x)}\right)'$$ ではない

</div>

---

## 4. 新潟大学での出題パターン

<div class="callout callout-examtip" markdown="1">

- **R8-1 問題IV(1)(2)**: $$\frac{\sin3x}{x}$$ (基本形) と $$\frac{e^x-1-x}{x^2}$$ (ロピタル2回)
- **Tier 2**: 基本的な不定形と2回のロピタルを使えれば十分

</div>
