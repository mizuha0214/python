#yield fromで複数のジェネレータを作る
#ジェネレータを使い、イメージの動きをアニメーションで示す。
#視覚効果を狙って、最初は速く動き、少し止まって、それからゆっくり動く
def move(period, speed):
    for _ in range(period):
        yield speed

def pause(delay):
    for _ in range(delay):
        yield 0

def animate():
    for delta in move(4, 5.0):
        yield delta
    for delta in pause(3):
        yield delta
    for delta in move(2, 3.0):
        yield delta

def render(delta):
    #スクリーンで動かす
    print(delta)

def run(func):
    for delta in func():
        render(delta)

# run(animate)

#yield fromで簡潔に。

def animate_composed():
    yield from move(4, 5.0) 
    yield from pause(3)
    yield from move(2, 3.0)

# run(animate_composed)
it = animate_composed()
print(next(it))