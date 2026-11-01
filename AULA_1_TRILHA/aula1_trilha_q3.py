entrada = input().split()
originais = [int(item) for item in entrada]
ordenados = sorted(originais)

for item in ordenados:
    print(item)
print()
for item in originais:
    print(item)