x = [0,9,3,5,7,-1]
i = 0
s = 0
t = 0
low = pow(10, 9)
while (x[t] != -1):
    i = i + 1
    s = s + x[t]
    if (x[t] < low):
        low = x[t]
    t = t+1 
c = i+1
s = s - 1
min = low
mean = s / c
print("Count =\n", c, "\nSum =\n", s, "\nMinimum =\n ", min, "\nMean =\n", mean)
