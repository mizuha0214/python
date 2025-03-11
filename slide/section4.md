---
marp: true
header: "Effective Python 輪読会&nbsp;&nbsp;&nbsp;&nbsp; 4章&nbsp;内包表記とジェネレータ" 
footer: 齋藤瑞葉
paginate: true
---

# Effective Python 輪読会 第5回

---

## Effective Python（第２版）とは
定価：3960円（税込）　著者：Brett Slatkin　翻訳：黒川利明　技術監修：石本敦夫

Pythonのベストプラクティスを90項目も紹介した本。
効率的で堅牢であるだけでなく、読みやすく、保守しやすく、改善しやすいPythonicなコードを書く秘訣を教えてくれる。

**※ Python3.8までに対応！**

---

# 4章　内包表記とジェネレータ
##setumei

---

対象：リストや辞書など、集合体
・読みやすいように簡潔に書く
・メモリ効率を高める

---

## 項目27　mapやfilterの代わりにリスト内包表記を使う
リストからリストを作りたいなら...
- for文
- リスト内包表記
- map関数(+filter関数)

---

やりたいこと：
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  →  [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```
```python
squares = [] #非推奨。複数行で長い。
for x in numbers:
    squares.append(x**2)
```
```python
squares = [x**2 for x in numbers]　#推奨。簡潔。
```
```python
squares_iterator = map(lambda x: x**2, numbers) #非推奨。lamndaが煩わしい。
squares = list(squares_iterator)
```

---

やりたいこと
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  →  [4, 16, 36, 64, 100]
```python 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```
```python
squares = [] #非推奨。複数行で長い。
for x in numbers:
    if x%2 == 0:
        squares.append(x**2)
```
```python 
squares = [x**2 for x in numbers if x%2 == 0] #推奨。簡潔。
```
```python
squares_iterator = map(lambda x: x**2, filter(lambda x: x%2==0, numbers))
squares = list(squares_iterator) #非推奨。lambdaとfilterが煩わしい。
```

---

辞書にも内包表記あり
リスト同様に、
×　for文、map(+filter)
○　辞書内包表記推奨

```python
even_squares_dict = {x: x**2 for x in numbers if x%2 == 0}　#推奨。簡潔。
```

---

## 項目28　内包表記では3つ以上の式を避ける

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```
```python
flat = [x for row in matrix for x in row] #OK。式2つ。

squared = [[x**2 for x in row] for row in matrix] #OK。式2つ。
```

---

しかし、内包表記にもう一つループが増えると...
```python
my_lists = [
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]]
]
```
```python
flat = [x for sublist1 in my_lists #NG。式3つ。
        for sublist2 in sublist1
        for x in sublist2]
```
for文でインデントを付ける方が分かりやすい。
```python
flat = [] 
for sublist1 in my_lists:
    for sublist2 in sublist1:
        flat.extend(sublist2)
```

---

if文を複数書きたいとき
```python
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
filtered = [x for x in a if x>4 if x%2 == 0] #NG（？）。式3つ。
filtered = [x for x in a if x>4 and x%2 == 0]　#NG（？）。式3つ。
```
上記はまだ読みやすいが、
```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] #NG。式4つ。
filterd = [[x for x in row if x%3 == 0] for row in matrix if sum(row) >= 10]
```
&nbsp;  
**目安として、式3つ以上はやめておく。**
2つのループ、2つの条件、1つのループ＋1つの条件、まで
→これよりも複雑なら、for文

---

## 項目29　代入式を使い内包表記での繰り返し作業をなくす
顧客から注文が来るが、何発注単位の在庫があるか？
```python
#在庫
stock = {
    "nails": 125,# 釘（くぎ）
    "screws": 35,# ネジ
    "wingnuts": 8,#ウィングナット
    "washers": 24 #ワッシャー
}

#注文
order = ["screws", "wingnuts", "clips"]

#発注を何単位できるか。size = 発注単位。
def get_batches(count: int, size: int):　
    return count//size #整数で商を求める(小数点以下切り捨て)
```

---
for文で書くと、
```python
found = {}
for name in order:
    count = stock.get(name, 0)#stockにない=在庫0個
    batches = get_batches(count, 8)
    if batches:
        result[name] = batches
```
辞書内包表記を使うと、
Good:　簡潔。
Bad: 全く同じ```get_batches(stock.get(name, 0), 8)```が2個あり、変更に弱い。
```python
found = {name: get_batches(stock.get(name, 0), 8)
         for name in order
         if get_batches(stock.get(name, 0), 8)}
```

















