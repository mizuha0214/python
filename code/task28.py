#リスト内包表記に適している例。簡潔で分かりやすい。
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flat = [x for row in matrix for x in row]
squared = [[x**2 for x in row] for row in matrix]

#リスト内包表記に適さない例。簡潔ではなくわかりづらい
my_lists = [
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]]
]
flat = [x for sublist1 in my_lists
        for sublist2 in sublist1
        for x in sublist2]
#上記の例は、for文の方が適している。インデントを付ける方が分かりやすい。
flat = []
for sublist1 in my_lists:
    for sublist2 in sublist1:
        flat.extend(sublist2)

#if文あるとき
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [x for x in a if x>4 if x%2 == 0]
c = [x for x in a if x>4 and x%2 == 0]
# print(b, c)

#より複雑なif文
matrix = [[1, 2, 3], [4, 5], [7, 8, 9]]
filterd = [[x for x in row if x%3 == 0] for row in matrix if sum(row) >= 10]
print(filterd)
filterd = [x for row in matrix if sum(row) >= 10 for x in row if x%3 == 0]
print(filterd)


