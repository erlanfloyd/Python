import statistics

example_list = [1,2,3,4,5,6,7,8,9,125,456,88]
x = statistics.mean(example_list)
print(x)

y = statistics.median(example_list)
print(y)

z = statistics.stdev(example_list)
print(z)

a = statistics.variance(example_list)
print(a)
