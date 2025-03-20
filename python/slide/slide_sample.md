---
marp: true
header: "Effective Python 輪読会 第3回"
footer: 諌山航太
paginate: true
math: mathjax
---

# Effective Python 第3回

---

# 3章　関数

---

## 項目19 複数の戻り値では、4個以上の変数なら決してアンパックしない

Python関数は（タプルを介して）複数の値を返せる。

```Python
def get_stats(number: list[float]):
  minimum = min(numbers)
  maximum = max(numbers)
  return minimum, maximum # カンマで区切ると、タプルになる

numbers = [0, 1, 2, 3]

minimum, maximum = get_stats(numbers) # アンパック代入
```

---

catch-allアンパックで受け取ることもできる。
ワニの体長の列に対して、平均の何％かを計算してソートする関数

```python
def get_avg_ratio(numbers):
  average = sum(numbers) / len(numbers)
  scaled = [ x / average for x in numbers ]
  scaled.sort(reverse=True)
  return scaled

lengths = range(0, 10)
longest, *middle, shortest = get_avg_ratio(lengths)
>>>

```

---

**アンチパターン**
４以上の長さのアンパックを用いて戻り値を受け取る

**推奨パターン**
３以下の長さのアンパックを用いて戻り値を受け取る

**ミスの発生のしやすさ、可読性の観点から**

---

**アンチパターン**
ワニの最大長、最小長、平均長、中央値、母集団のサイズを計算して返す関数

```python
def get_stats(numbers):
  mininum = min(numbers)
  maximum = max(numbers)
  count = len(numbers)
  average = sum(numbers) / count

  sorted_numbers = sorted(numbers)
  median = sorted_numbers[count // 2] # 簡単のため、奇数長のパターンのみ考慮

  return minimum, maximum, average, median, count

minimum, maximum, average, median, count = get_stats(length)
```

---
**問題点**

- 戻り値の順番を間違いやすい（型が同じなので、特定しにくい）
```python
# 正しい
minimum, maximum, average, median, count = get_stats(lengths)
# メディアンと平均が入れ替わっている...
minimum, maximum, median, average, count = get_stats(lengths)
```
- 戻り値を受け取る行が長く、改行を伴いやすい（読みにくい）
```python
minimum, maximum, average, median, count = get_stats(
  lengths)

minimum, maximum, average, median, count =\
  get_stats(lengths)
```

---