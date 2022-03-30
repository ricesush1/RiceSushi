class factorial:

    def __call__(self, n):
        f = 1
        for i in range(1, n + 1):
            f = f * i
        return f


n = int(input("Enter a number:"))

obj = factorial()
f = obj.__call__(n)
print("Factorial is:", f)