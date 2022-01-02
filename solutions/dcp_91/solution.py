functions = []
for i in range(10):
    functions.append(lambda j=i: j)

for f in functions:
    print(f())
