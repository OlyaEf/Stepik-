# data В саду 88 фруктовых деревьев, из них 32 яблони, 22 груши, 16 слив, 17 вишни.
# в какой системе счисления посчитаны деревья?

for n in range(9, 16):
    if (int("32", n)+int('22', n)+int("16", n)+int('17', n)) == int('88', n):
        print(n)