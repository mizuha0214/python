class Reset(Exception):
    pass


def timer(period): #ジェネレータ
    current = period
    while current:
        current -= 1
        try:
            yield current
        except Reset:
            current = period


def check_for_reset():
   #外部イベントをポーリングして待つ
    # return True
    ...

def announce(remaining):
    print(f"{remaining} ticks remaining")


#この中でexceptを使わなければいけないのは、for文をつかっていないからではないか？no4のようになぜできないのか？
def run():
    it = timer(4)
    # current = next(it)
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


run()