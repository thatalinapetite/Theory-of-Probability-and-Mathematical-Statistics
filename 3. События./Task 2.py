n = 13
a = [0] * (n * 3)
sum = 0

for i in range(1, n):
    for j in range(1, n):
        for k in range(1, n):
            a[i + j + k] += 1

for i in range(3, 37):
    sum += a[i]
    print('Сумму', i, 'дает количество наборов:', a[i], ';', 'вероятность:', a[i] / sum)