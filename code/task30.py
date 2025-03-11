import itertools


def index_words(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index+1)
    return result

speech = "Four score and seven years ago..."
speech = "Four"
result = index_words(speech)
print(result)#[0, 5, 11, 15, 21, 27,,,,,]
#コードが複雑で読みにくい
#リストに追加される値より、result.appendが目立つ

#ジェネレータ関数を使う
def index_words_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == " ":
            yield index+1

#ジェネレータ関数を呼び出した時点では何も実行されない。イテレータを返すだけ。
#nextが呼ばれるたびに、イテレータは、ジェネレータを次のyieldまで進める。
it = index_words_iter(speech)
#1個目のyieldまで進む
print(next(it)) #0
#2個目のyieldまで進む
# print(next(it)) #5

#イテレータはリストに変換できる
result = list(index_words_iter(speech))
print(result)

#また、ジェネレータはメモリ食いつぶしを防ぐ
#ファイルから一行ずつ読み込む例
def index_file(handle):
    offset = 0
    for line in handle:
        if line:
            yield offset
        for letter in line:
            offset += 1
            if letter == " ":
                yield offset
#メモリは行の最大長あれば大丈夫
with open("speech.txt") as f:
    it = index_file(f)
    results = itertools.islice(it, 0, 10) #最初の10個
    print(list(results))
