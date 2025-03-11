numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#for文 非推奨
squares = []
for x in numbers:
    squares.append(x**2)

#内包表記　推奨
squares = [x**2 for x in numbers]
# print(squares)

#map　非推奨
squares_iterator = map(lambda x: x**2, numbers)
squares = list(squares_iterator)
# print(type(squares_iterator))
# print(squares)

#for文
squares = []
for x in numbers:
    if x%2 == 0:
        squares.append(x**2)
# print(squares)
#map+filter
squares_iterator = map(lambda x: x**2, filter(lambda x: x%2==0, numbers))
# print(type(filter(lambda x: x%2==0, numbers)))
squares = list(squares_iterator)
# print(squares)
#リスト内包表記
squares = [x**2 for x in numbers if x%2 == 0]







#mapとは？
# map(関数, イテラブル) → イテレータ（mapオブジェクト）
# list(map(関数, イテラブル))でlistに変換
#lambda式
def sample(i):
    return i**2
# print(sample(10))

sample = lambda i: i**2
# print(sample(10))
#よって
squares = list(map((lambda x: x**2), numbers))
# print(squares)
#辞書内包表記
even_squares_dict = {x: x**2 for x in numbers if x%2 == 0}


