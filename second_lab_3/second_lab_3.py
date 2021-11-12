def факториал(n):
    ответ = 1
    while n != 0:
        ответ *= n
        n -= 1
    return ответ


длина = int(input("Введите длину: "))

num = 1

buf = list(list())

string = list(list())
string.append(list())
string[0].append(1)

while num != длина:
    for j in range(num):
        for k in range(int(факториал(num + 1) / num)):
            buf.append(string[j].copy())
            buf[len(buf) - 1].insert(k, num + 1)
    string = buf.copy()
    buf.clear()

    num += 1
print(string)