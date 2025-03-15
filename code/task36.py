import itetools

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
first_five = itertools.islice(value, 5)
print(first_five) #[1, 2, 3, 4, 5]
#普通にリストのスライスもあったけ？
middle_odds = itertools.islice(values, 2, 8, 2)
print(middle_odds) #[3, 5, 7]
#同じやつがあるっけ

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
less_than_seven = lambda x: x < 7
it = itertools.takewhile(less_than_seven, values)
print(list(it)) #[1, 2, 3, 4, 5]

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
less_than_seven = lambda x: x < 7
it = itertools.dropwhile(less_than_seven, values)
print(list(it)) #[7, 8, 9, 10]


values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = lambda x: x % 2 == 0
it == itertools.filterfalse(evens, values)
print(it)
#普通のfilter文で返されるものもイテレータなんだっけ？

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def sum_modulo_20(first, second):
    output = first + second
    return output % 20

multiple = itertools.product([1, 2], ["a", "b"])

it = itertools.permutations([1, 2, 3, 4], 2)
#単語の意味は？

it = itertools.combinations([1, 2, 3, 4], 2)

it = itertools.combinations_with_replacement([1, 2, 3, 4], 2)
#上の重複許す版、意味はよくわからない