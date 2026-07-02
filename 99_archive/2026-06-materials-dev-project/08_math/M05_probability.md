# M05: 確率・統計

---

## 1. 確率の基礎

### 基本用語

- **標本空間** $\Omega$: すべての起こりうる結果の集合
- **事象** $A \subseteq \Omega$
- **確率** $P(A)$: $0 \leq P(A) \leq 1$, $P(\Omega) = 1$

### 加法定理

$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

$A, B$ が**互いに排反**（$A \cap B = \emptyset$）なら: $P(A \cup B) = P(A) + P(B)$

### 条件付き確率

$$P(A|B) = \frac{P(A \cap B)}{P(B)} \quad (P(B) > 0)$$

「$B$ が起きたという条件のもとで $A$ が起きる確率」

### 独立性

$P(A \cap B) = P(A)P(B) \Leftrightarrow$ $A$ と $B$ は**独立**（$P(A|B) = P(A)$）

### ベイズの定理

$$P(A|B) = \frac{P(B|A)P(A)}{P(B)}$$

**全確率の公式:** $\{A_1, A_2, \ldots, A_n\}$ が $\Omega$ の分割なら:

$$P(B) = \sum_{i=1}^n P(B|A_i)P(A_i)$$

---

## 2. 確率変数（Random Variables）

### 離散確率変数

$P(X = x_k) = p_k$（確率質量関数）

**期待値（平均）:** $E[X] = \sum_k x_k p_k$

**分散:** $V[X] = E[(X - \mu)^2] = E[X^2] - (E[X])^2$

**標準偏差:** $\sigma = \sqrt{V[X]}$

### 連続確率変数

$p(x)$: 確率密度関数（PDF）

$$P(a \leq X \leq b) = \int_a^b p(x)\,dx, \quad \int_{-\infty}^{\infty} p(x)\,dx = 1$$

**期待値:** $E[X] = \int_{-\infty}^{\infty} x p(x)\,dx$

**分散:** $V[X] = \int_{-\infty}^{\infty} (x-\mu)^2 p(x)\,dx$

---

## 3. 主要な確率分布

### 二項分布 $B(n, p)$

$n$ 回の試行、各回で確率 $p$ で成功する場合の成功回数 $X$:

$$P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$$

$$E[X] = np, \quad V[X] = np(1-p)$$

### ポアソン分布 $\text{Po}(\lambda)$

平均発生率 $\lambda$ の稀な事象の発生回数:

$$P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}$$

$$E[X] = V[X] = \lambda$$

### 正規分布 $N(\mu, \sigma^2)$

$$p(x) = \frac{1}{\sqrt{2\pi}\sigma} \exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)$$

$$E[X] = \mu, \quad V[X] = \sigma^2$$

**標準化:** $Z = \frac{X - \mu}{\sigma} \sim N(0, 1)$

標準正規分布の重要値:
- $P(-1 \leq Z \leq 1) \approx 0.683$（68%）
- $P(-2 \leq Z \leq 2) \approx 0.954$（95%）
- $P(-3 \leq Z \leq 3) \approx 0.997$（99.7%）

### 指数分布 $\text{Exp}(\lambda)$

$$p(x) = \lambda e^{-\lambda x} \quad (x \geq 0)$$

$$E[X] = \frac{1}{\lambda}, \quad V[X] = \frac{1}{\lambda^2}$$

**無記憶性:** $P(X > s + t | X > s) = P(X > t)$

---

## 4. 中心極限定理

$X_1, X_2, \ldots, X_n$ が同一分布 $(\mu, \sigma^2)$ から独立に得られるとき:

$$\bar{X} = \frac{1}{n}\sum_{i=1}^n X_i \xrightarrow{d} N\left(\mu, \frac{\sigma^2}{n}\right) \quad (n \to \infty)$$

標準化: $Z = \frac{\bar{X} - \mu}{\sigma/\sqrt{n}} \to N(0,1)$

---

## 5. 大数の法則

$$\frac{1}{n}\sum_{i=1}^n X_i \xrightarrow{p} \mu \quad (n \to \infty)$$

標本平均は真の期待値に収束する。

---

## 6. 統計的推定

### 点推定

- 標本平均 $\bar{X}$ は母平均 $\mu$ の不偏推定量
- 標本分散 $s^2 = \frac{1}{n-1}\sum(X_i - \bar{X})^2$ は母分散 $\sigma^2$ の不偏推定量（$n-1$ に注意）

### 区間推定（信頼区間）

母平均 $\mu$ の 95% 信頼区間（母分散 $\sigma^2$ 既知）:

$$\bar{X} - 1.96\frac{\sigma}{\sqrt{n}} \leq \mu \leq \bar{X} + 1.96\frac{\sigma}{\sqrt{n}}$$

---

## 7. 試験頻出パターン

### パターン 1: 条件付き確率・ベイズ

**問:** ある工場に機械 A, B, C がある。生産量の割合は 50%, 30%, 20% で、不良品率はそれぞれ 1%, 2%, 3%。ランダムに製品を1つ選んだとき不良品だった。機械 A が作った確率は？

**解（ベイズ）:**

$P(\text{不良}) = 0.5 \times 0.01 + 0.3 \times 0.02 + 0.2 \times 0.03 = 0.005 + 0.006 + 0.006 = 0.017$

$P(A|\text{不良}) = \frac{0.5 \times 0.01}{0.017} = \frac{0.005}{0.017} \approx 0.294$

---

### パターン 2: 二項分布

**問:** コインを10回投げるとき、表が7回以上出る確率を求めよ。

**解:**

$$P(X \geq 7) = \sum_{k=7}^{10}\binom{10}{k}\left(\frac{1}{2}\right)^{10}$$

$$= \frac{\binom{10}{7} + \binom{10}{8} + \binom{10}{9} + \binom{10}{10}}{2^{10}} = \frac{120 + 45 + 10 + 1}{1024} = \frac{176}{1024} = \frac{11}{64}$$

---

### パターン 3: 正規分布

**問:** ある試験の点数は $N(70, 100)$（平均70、標準偏差10）に従う。  
80点以上の割合を求めよ。（$P(Z \leq 1) = 0.841$）

**解:**

$$P(X \geq 80) = P\left(Z \geq \frac{80-70}{10}\right) = P(Z \geq 1) = 1 - 0.841 = 0.159 \approx 15.9\%$$

---

_← 前: M04 | → 次: M06 複素数_
