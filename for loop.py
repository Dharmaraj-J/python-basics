numbers = [4,2,1,34,5,6,1,78]
duplicate = None
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i] == numbers[j]:
          duplicate = numbers[i]
          print(duplicate)
          break
          


for i in range(len(numbers)):
    if numbers[i] == duplicate:
        print(i)