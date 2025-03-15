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


#イテラブルクラスにすれば解決 ##なんでイテラブル？イテレータクラスではだめなのか
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