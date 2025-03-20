#大きなリスト内包表記にはジェネレータ式を考える
#前に、内包表記に詰め込みすぎてはいけない、という話をした

#以下を、膨大な行数を持つファイルを扱ったら、もめりえらー
value = [len(x) for x in open("my_numbers.txt")]
print(value)

#解決方法：ジェネレータ式を使う（リスト内包表記とジェネレータを組み合わせたもの）
#???ジェネレータ式の評価値はイテレータで、
#???リスト内包表記にすると、yieldを書かなくていいのか
it = (len(x) for x in open("my_numbers.txt"))
print(it)#<generator object <genexpr> at 0x0000018E7C8BAA80>これはイテレータ？
print(next(it))#3
print(next(it))#4
print(next(it))#2
# print(next(it))#StopIteration

#さらに、ジェネレータ式を組み合わせることも可能
#ジェネレータ式から返されたイテレータを、別のジェネレータ式への入力とする
it = (len(x) for x in open("my_numbers.txt"))
roots = (x**0.5 for x in it)
print(next(roots))


