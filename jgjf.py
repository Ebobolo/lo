a = 13335
print(a)
print(str(a))
print(len(str(a)))
amo = 0

for i in str(a):
    amo += int(i)
print(amo)

print(str(a).count("3"))