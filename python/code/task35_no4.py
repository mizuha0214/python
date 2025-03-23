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


def check_for_reset():
   #外部イベントをポーリングして待つ
    # return True
    ...


def announce(remaining):
    print(f"{remaining} ticks remaining")


def run():
    timer = Timer(4)
    for current in timer:
        if check_for_reset():
            timer.reset()
        announce(current)

run()