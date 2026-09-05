# warmup
for w in range(1_000_000):
    x = (w * w)
try:
    import os.path
    import sys
    import time


    sys.set_int_max_str_digits(1000000000)
    PATH = os.path.join(os.getcwd(), "output.txt")
    def normal(n):
        a = 0
        b = 1
        for i in range(n):
            a, b = b, a + b
        return b


    def fast(n):
        if n == 0:
            return 0, 1
        a, b = fast(n // 2)
        c = a * (2 * b - a)
        d = a * a + b * b
        if n % 2 == 0:
            return c, d
        else:
            return d, c + d


    def fib_gen(n, way, out: bool):
        if os.path.exists(PATH):
            os.remove(PATH)
        start = time.time()

        if way == "fast":
            result, _ = fast(n)
        elif way == "normal":
            result = normal(n)
        else:
            print("invalid input")
            return
        if out:
            with open(PATH, "w") as f:
                f.write(str(result))
        else:
            ...
        end = time.time()
        t = end - start
        print(
            f"The process took {int(t // 3600):02}:{int(t % 3600 // 60):02}:{int(t % 60):02}.{int(t % 1 * 1000):03} seconds.")


    while True:
        try:
            output = int(input("Generate output.txt? (1 or 0): ").lower().replace("f", "")) == 1
            break
        except ValueError:
            ...
    while True:
        try:
            inp = int(input("Enter a number: "))
            w = input("Normal or fast: ")
            fib_gen(inp, w, output)
        except ValueError:
            print("Invalid input")
except KeyboardInterrupt:
    print("Made By: RequestTimeout(GitHub: https://github.com/RequestTimeout)")
