start = input("Если вы хотите начать работу с калькулятором введите: start: ")
a = input("веди")

amo = 0

for i in str(a):
    amo += int(i)
print("crjk", amo)
avg = amo / len(a)
print("Среднее арифметическое:", avg)
print(str(a).count("0"))