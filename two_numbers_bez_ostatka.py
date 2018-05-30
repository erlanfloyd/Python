k = 1
for i in (range(1, 21)):
    for j in range(1, 21):
        if (k * j) % i == 0:
            k *= j
            break
print(k)