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

辞書と集合にも内包表記あり
リスト同様に、
×　for文、map(+filter)
○　辞書内包表記, 集合内包表記

```python
even_squares_dict = {x: x**2 for x in numbers if x%2 == 0}　#推奨。簡潔。
even_squares_set = {x**2 for x in numbers if x%2 == 0} #推奨。簡潔。
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
for文で書くと...
```python
found = {}
for name in order:
    count = stock.get(name, 0)#stockにない=在庫0個
    batches = get_batches(count, 8)
    if batches:
        result[name] = batches
```
&nbsp;
辞書内包表記を使うと...
良い点:　簡潔。
悪い点:　```get_batches(stock.get(name, 0), 8)```が2個あり、変更に弱い。
```python
found = {name: get_batches(stock.get(name, 0), 8)
         for name in order
         if get_batches(stock.get(name, 0), 8)}
```

---

- 解決方法：ウォオラス演算子(:=)を使う。（項目10: 代入式で繰り返しを防ぐ）
```python
found = {name: batches for name in order
         if (batches:= get_batches(stock.get(name, 0), 8))}
```
- 注意１：代入式は条件部分で使用
```python
found = {name: (tenth := count//10)　#NameError: name 'tenth' is not undefined
         for name, count in stock.items() if tenth>10 }
```
```python
found = {name: tenth for name, count in stock.items() #大丈夫
if (tenth := count//10) > 0}
```
---


- 注意２：ウォオラス演算子の有無で、変数スコープが変わる
```python
half = [(squared := last**2) for count in stock.values() if (last := count//2) > 10]
print(f"Last item of {half} is {last}**2 = {squared}")
# Last item of [3844, 289, 144] is 12**2 = 144 #参照できる
```
```python
for count in stock.values():
    last = count//2
    squared = last**2
print(f"{count}//2 = {last}; {last}**2 = {squared}")
# 24//2 = 12; 12**2 = 144　#参照できる
```
```python
half = [count//2 for count in stock.values()]
print(count) #エラー
```

---

## 項目30　リストを返さずにジェネレータを返すことを考える
結果をシーケンスで返したいとき、まず思いつくのはリスト

```python
#文字列中の単語のインデックスを求める
def index_words(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index+1)
    return result
```
**問題点**
- ```append```が煩わしい。```index+1```より```append```が目立っている。
- 入力文字列が膨大だと、メモリを食いつぶしかねない。

---

解決方法/ ジェネレータ関数を使う

```python
def index_words_iter(text):
    if text:
        yield 0
        yield 0
    for index, letter in enumerate(text):
        if letter == " ":
            yield index+1
```
- ジェネレータ関数（後スライドで再び説明）
  - 呼び出された時点では何も実行されないが、イテレータを返す。
  - nextを呼び出すと、イテレータがジェネレータ関数を次の```yield```まで進ませる。

```python
it = index_words_iter(speech)#イテレータを返す
print(next(it)) #5
print(next(it)) #8
result = list(itertools.islice(it, 0, 10))#リストに変換できる
```

---

## 項目31　引数に対してイテレータを使うときには確実さを優先する

```python
def normalize(numbers):#各都市への旅行者数は、全世界の旅行者数の何％か。
    total = sum(numbers) #全世界の旅行者数
    result = []
    for value in numbers:
        percent = 100*value/total
        result.append(percent)
    return result

def read_visits(data_path):#data_pathは、１行に１都市の旅行者数
    with open(data_path) as f:
        for line in f:
            yield int(line)

it = read_visits("my_numbers.txt")
percentages = normalize(it)
print(percentages) #[5.2, 0.4, 1.5, 3.4, 1.8,..]を期待していたが、[]　どうしてか？
```

---

イテレータは一回最後まで行くと終了。反復処理はできない。
- 全スライドのコードの問題点
```python
def normalize(numbers)
    total = sum(numbers) #イテレータが最後まで進む。
    result = []
    for value in numbers:　#もう最後まで行ったのでループできる要素なし。
        percent = 100*value/total
        result.append(percent)
    return resul
```
- 解決方法1：イテレータをリストに変換
  - 問題点：メモリ効率を高めるというイテレータの利点が消える
```python
def normalize_copy(numbers):
    numbers = list(numbers) #この行を追加
    total = sum(numbers)
    以下略
```

---

- 解決方法2：イテレータ自身ではなく、新たなイテレータを返す関数を引数にする
  - 問題点：lambda関数が煩わしい
```python
def normalize_func(get_iter):
    total = sum(get_iter())
    result = []
    for value in get_iter():
        percent = 100*value/total
        result.append(percent)
    return result

path = "my_numbers.txt"
percentages = normalize_func(lambda: read_visits(path))
```

---

- 解決方法3：イテレータを提供するクラスを実装
**イテレータとは？**
  - ```for x in foo```では、まず```foo```をイテレータに変換。
  - イテレータに変換できるものをイテラブルという。イテレータは```__iter__```と```__next__```を持ち、イテラブルは```__iter__```のみ持つ。 イテレータもイテラブル。

```python
class Counter: #イテレータクラス
    def __init__(self, start, end):
        self.current = start
        self.end = end
    def __iter__(self):
        return self  # 自分自身をイテレータとして返す
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration  # 終了
        value = self.current
        self.current += 1
        return value
```

---

- 解決方法3：イテレータクラスを実装
**では、ジェネレータ関数とは？** イテレータを作るための関数。
全スライドのようなイテレータを自分で実装すると...
  - ```__init__()```、```__iter__()```、```__next__()``` を全部書く
  - 状態 (```self.current```) を管理
  - ```StopIteration``` を扱う
   
  一方、ジェネレータ関数なら簡潔
```python
def counter(start, end):
    current = start
    while current < end:
        yield current  
        current += 1 
``` 

---

- 解決方法3：イテレータを提供するクラスを実装
全世界の旅行者数の話に戻ります。
```python
class ReadVisits: #イテラブルクラス
    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self): #ジェネレータ関数。イテレータを返す。
        with open(self.data_path) as f:
            for line in f:
                yield int(line)
```

```python
path = "my_numbers.txt"
visits = ReadVisits(path)
percentages = normalize(visits) #sum関数、forループでそれぞれ（別の）イテレータが返される。
print(percentages)
```
---

また、イテレータが引数になっていないか、確認すると安心。
イテレータに```__iter__()```を使うと、自身を返すことを利用。
```python
def normalize_defensive(numbers):
    if iter(numbers) is numbers: 
        raise TypeError("Must supply a container.")
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100*value/total
        result.append(percent)
    return result
```
```isinstance(numbers, collections.abc.Iterator)```を使ってもよい。

---

## 項目32　大きなリスト内包表記にはジェネレータ式を考える

リスト内包表記
良い点：簡潔
悪い点：入力データが膨大だと危険

```python
value = [len(x) for x in open("my_numbers.txt")]
print(value) #[100, 57, 18, 3, 45, 98, 30, 2, 33]
```

そこで、ジェネレータ式（リスト内表表記＋ジェネレータ関数）
```python
it = (len(x) for x in open("my_numbers.txt"))
print(next(it)) #100
print(next(it)) #57
```

---

さらに、ジェネレータ式を組み合わせることが可能
```python
it = (len(x) for x in open("my_numbers.txt"))
roots = (x**0.5 for x in it)
```
値1個ずつ、open() → len() → **0.5 が 連鎖的に処理されるため高速で、ストリーム処理に最適

---

## 項目33　yield fromで複数のジェネレータを作る
```python
#ジェネレータを使い、イメージの動きをアニメーションで示す。
#視覚効果を狙って、最初は速く動き、少し止まって、それからゆっくり動く。

def move(period, speed): #動く
    for _ in range(period):
        yield speed

def pause(delay): #止まる
    for _ in range(delay):
        yield 0

def animate(): #一連の動き
    for delta in move(4, 5.0):
        yield delta
    for delta in pause(3):
        yield delta
    for delta in move(2, 3.0):
        yield delta

def render(delta):
    #スクリーンで動かす
    ...

def run(func):
    for delta in func():
        render(delta)

run(animate)
```

---

yield fromを使うと...
```python
def animate_composed():
    yield from move(4, 5.0) 
    yield from pause(3)
    yield from move(2, 3.0)
```
- 簡潔
- 処理速度が速い
```move```, ```pause```でyieldされた値は、animate_composed()のyieldには渡らずに、直接外に出る。

---

## 項目34　sendでジェネレータにデータを注入するのは避ける
```send```を使えば、```yield```で値を受け取る
（＋```yield```で値を返す(```next```)の動作も伴う）

---

```send```を使って、振幅が変化する波を作れる　
```python
def wave_modulating(steps):
    step_size = 2 * math.pi / steps
    amplitude = yield 
    for step in range(steps):
        radians = step * step_size
        fraction = math.sin(radians)
        output = amplitude * fraction
        amplitude = yield output

def transmit(output):
    if output is None:
        print(f"output is None")
    else:
        print(f"Output: {output:>5.1f}")

def run_modulating(it):
    amplitudes = [None, 7, 7, 7, 2, 2, 2, 2, 10, 10, 10, 10, 10]

    for amplitude in amplitudes:
        output = it.send(amplitude)
        transmit(output)

run_modulating(wave_modulating(12))
```

---

しかし、yield fromを使うと予期しない出力（次スライドに出力）
```python
def complex_wave_modulating():
    yield from wave_modulating(3)
    yield from wave_modulating(4)
    yield from wave_modulating(5)

run_modulating(complex_wave_modulating())
```
```python
>>>#実際の出力           >>>#期待する出力
Output is None          Output is None
Output: 0.0             Output: 0.0
Output: 0.0             Output: 0.0
Output: 0.0             Output: 0.0
Output is None          Output: 0.0 
Output: 0.0             Output: 0.0
Output: 0.0             Output: 0.0 
Output: 0.0             Output: 0.0
Output is None          Output: 0.0
Output: 0.0             Output: 0.0
...                     ...
```

---

解決方法：ラジオ波の関数にイテレータを渡す
```python
def wave_cascading(amplitude_it, steps):
    step_size = 2 * math.pi / steps
    for step in range(steps):
        radians = step * step_size
        fraction = math.sin(radians)
        amplitude = next(amplitude_it)
        output = amplitude * fraction
        yield output
```
？？ここで、最もいいのはイテレータはどこからでもよく、完全に動的であること

---

## 項目34　ジェネレータでthrowによる状態遷移を起こすのは避ける

ジェネレータの機能
- yield from
- sendメソッド
- **throwメソッド**

throwメソッドとは？
throwが呼び出されると、ジェネレータは通常のように実行を続けず、代わりに例外を発生させる。
```python
class MyError(Exception):
    pass

def my_generator():
    yield 1
    yield 2
    yield 3

it = my_generator()
print(next(it)) #1
print(next(it)) #2
print(it.throw(MyError("test error"))) #Traceback... MyError: test error
print(next(it))
```

---

問題点：throwを使うとコードが複雑になる
なぜ、より本質的にはなにがいけなかったんだろう？なんでイテラブルクラスにしたらコードが短縮された？
非同期機能を。。？
```python
class Reset(Exception):
    pass

def timer(period):
    current = period
    while current:
        current -= 1
        try:
            yield current
        except Reset:
            current = period

def check_for_reset():
   #外部イベントをポーリングして待つ

def announce(remaining):
    print(f"{remaining} ticks remaining")

def run():
    it = timer(4)
    while True:
        try:
            if check_for_reset():
                current = it.throw(Reset())
            else:
                current = next(it)
        except StopIteration:
            break
        else:
            announce(current)
```

---

- 解決方法：イテラブルクラスを実装 ##なんでイテラブル？イテレータクラスではだめなのか
```python
class Timer:
    def __init__(self, period):
        self.current = period
        self.period = period
    
    def reset(self):
        self.current = self.period

    def __iter__(self):
        while self.current:
            self.current -= 1
            yield self.current

def run():
    timer = Timer(4)
    for current in timer:
        if check_for_reset():
            timer.reset()
        announce(current)
```
- つなげる
- ふるい分ける
- 組み合わせる
```python
import itertools
```

---

**つなげる**
- chain
```python
it = itertools.chain([1, 2, 3], [4, 5, 6])
print(list(it)) #[1, 2, 3, 4, 5, 6] 

#よりchainが適した例
it = itertools.chain(range(10**7), range(10**7))
```

- repeat
```python
it = itertools.repeat("hello", 3)
print(list(it))
```

- cycle
```python
it = itertools.cycle([1, 2])
result = [next(it) for _ in range(10)]
print(result) #[1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
```

--- 

- tee：複数のイテレータを作成
```python
#it1, it2, it3は別々のイテレータ
# 最初に進んだイテレータがデータ取得して他のイテレータのためにキャッシュ
it1, it2, it3 = itertools.tee(["first", "second"], 3)
print(["first", "second"])
print(["first", "second"])
print(["first", "second"])
```

- zip_longest：短いほうのイテレータが終了したら指定値で埋める
```python
keys = ["one", "two", "three"]
values = [1, 2]

normal = list(zip(keys, values))
print(normal) #[("one", 1), ("two", 2)]

it = itertools.zip_longest(keys, values, fillvalue="nope")
longest = list(it)
print(longest)#[("one", 1), ("two", 2), ("three", "Nope")]
```

---

**ふるい分ける**
- islice リストのスライスと同様
- takewhile
関数が False を返すまで、イテラブルから要素を順に取得
filterは全要素をチェックするが、takewhileは途中で断ち切る
- dropwhile
takewhileの反対で、関数がFalseを返すまで要素をスキップ
- filterfalse
filterの逆で、関数がfalseになる要素を返す
filterと処理速度の違いはないが、fiiler + notより読みやすい
















































