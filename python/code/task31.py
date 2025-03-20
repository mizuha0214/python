#米国テキサス州の旅行者数の分析
#各都市への訪問者数は、テキサス州全体の何％か？
def normalize(numbers):
    total = sum(numbers) #テキサス州全体の旅行者数
    result = []
    for value in numbers:
        percent = 100*value/total
        result.append(percent)
    return result

visits = [15, 35, 80]
percentages = normalize(visits)
print(percentages)

#世界中の全都市に拡張。１行に１都市の数字。
def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)

it = read_visits("my_numbers.txt")
percentages = normalize(it)
print(percentages) #[]

#解決方法。でも入力でメモリ食いつぶし
def normalize_copy(numbers):
    numbers = list(numbers)
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100*value/total
        result.append(percent)
    return result

it = read_visits("my_numbers.txt")
percentages = normalize_copy(it)
print(percentages)

#関数を引数とする関数
def normalize_func(get_iter):
    total = sum(get_iter())
    result = []
    for value in get_iter():
        percent = 100*value/total
        result.append(percent)
    return result

path = "my_numbers.txt"
percentages = normalize_func(lambda: read_visits(path))

#コンテナクラスを実装
class ReadVisits:
    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)

path = "my_numbers.txt"
visits = ReadVisits(path)#この時点ではイテレータではない
percentages = normalize(visits)
print(percentages)
#欠点は入力データを複数回読み込んでしまうこと

#上記のコードを保証
def normalize_defensive(numbers):
    if iter(numbers) is numbers:
        raise TypeError("Must supply a container.")
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100*value/total
        result.append(percent)
    return result

#collections.abcを使う方法もある##上と何が違うのか？
from collections.abc import Iterator

def normalize_defensive(numbers):
    if isinstance(numbers, Iterator):
        raise TypeError("Must supply a container.")
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100*value/total
        result.append(percent)
    return result


