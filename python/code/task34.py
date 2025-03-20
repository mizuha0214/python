import math

#簡単な例
def my_generator():
    received = yield 1
    print(f"received = {received}")
    received = yield 2
    print(f"received = {received}")

# it = iter(my_generator())
# output = next(it)
# print(f"output = {output}")
#
# try:
#     next(it)
# except StopIteration:
#     pass
# else:
#     assert False

# it = iter(my_generator())
# output = it.send(None)
# print(f"output = {output}")
#
# try:
#     print(it.send("hello!"))
#     it.send("hello2!")
# except StopIteration:
#     pass

#sendを使わない信号
def wave(amplitude, steps):
    step_size = 2 * math.pi / steps
    for step in range(steps):
        radians = step * step_size
        fraction = math.sin(radians)
        output = amplitude * fraction
        yield output

def run(it):
    for output in it:
        transmit(output)




#sendを使う信号
def wave_modulating(steps):
    step_size = 2 * math.pi / steps
    amplitude = yield
    for step in range(steps):
        radians = step * step_size
        fraction = math.sin(radians)
        output = amplitude * fraction
        amplitude = yield output

def transmit(output):
    if output is None:
        print(f"output is None")
    else:
        print(f"Output: {output:>5.1f}")

def run_modulating(it):
    amplitudes = [None, 7, 7, 7, 2, 2, 2, 2, 10, 10, 10, 10, 10]

    for amplitude in amplitudes:
        output = it.send(amplitude)
        transmit(output)

# run_modulating(wave_modulating(12))

#もっと複雑な波
def complex_wave():
    yield from wave(7.0, 3)
    yield from wave(2.0, 4)
    yield from wave(10.0, 5)

# run(complex_wave())

def complex_wave_modulating():
    yield from wave_modulating(3)
    yield from wave_modulating(4)
    yield from wave_modulating(5)

run_modulating(complex_wave_modulating())

#ではどうするか？
def wave_cascading(amplitude_it, steps):
    step_size = 2 * math.pi / steps
    for step in range(steps):
        radians = step * step_size
        fraction = math.sin(radians)
        amplitude = next(amplitude_it)
        output = amplitude * fraction
        yield output

def complex_wave_cascading():
    yield from wave_modulating(amplitude_it, 3)
    yield from wave_modulating(amplitude_it, 4)
    yield from wave_modulating(amplitude_it, 5)

        







