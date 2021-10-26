sum = 0 
count = 0
temp = float(input())
while temp >= -300:
    sum = sum + temp
    count = count + 1
    temp = float(input())
print(sum / count)