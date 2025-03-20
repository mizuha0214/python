#発注単位：8個
stock = {
    "nails": 125,# 釘（くぎ）
    "screws": 35,# ネジ
    "wingnuts": 8,#ウィングナット
    "washers": 24 #ワッシャー
}

order = ["screws", "wingnuts", "clips"]

#発注を何単位できるか求める。size = 発注単位
def get_batches(count: int, size: int):
    return count//size #整数で商を求める(小数点以下切り捨て)

result = {}
for name in order:
    count = stock.get(name, 0)#stockにない=在庫0個
    batches = get_batches(count, 8)
    if batches:
        result[name] = batches

#上記のコードを簡潔に。
#しかし、get_batches(stock.get(name, 0), 8)が2個登場
found = {name: get_batches(stock.get(name, 0), 8)
         for name in order
         if get_batches(stock.get(name, 0), 8)}
#しかし、get_batches(stock.get(name, 0), 8)が2個登場。仕様変更に弱い。

#解決方法　ウォオラス演算子(:=)を使う。（項目10: 代入式で繰り返しを防ぐ）
found = {name: batches for name in order
         if (batches:= get_batches(stock.get(name, 0), 8))}
print(found)
#これだめ
# found = {name: (tenth := count//10)
#          for name, count in stock.items() if tenth>10 }

found = {name: tenth for name, count in stock.items()
if (tenth := count//10) > 0}

found = [(name, (tenth := count // 2))
         for name, count in stock.items() if tenth > 10]
print(found)

half = [(squared := last**2) for count in stock.values() if (last := count//2) > 10]
print(f"Last item of {half} is {last}**2 = {squared}")# Last item of [3844, 289, 144] is 12**2 = 144

for count in stock.values():
    last = count//2
    squared = last**2
print(f"{count}//2 = {last}; {last}**2 = {squared}")# Last item of [3844, 289, 144] is 12**2 = 144
# 24//2 = 12; 12**2 = 144