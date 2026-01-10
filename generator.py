# One-Line Definition 

# yield creates a generator that returns values one at a time and remembers its state between calls.


def generate():
    for i in range(100000):
        yield f"Row{i}\n"


obj = generate()
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))


obj2 = generat()
print(obj2)