d = {
    'george': 18,
    'allen': 20,
    'karan': 10,
    'george': 18,
    10:100
}

# printing key only
print(d.keys())

# in looping
for key in d:
    print(key)

print('\n')

# printing values
print(d.values())   

# in looping
for value in d.values():
    print(value)

# printing key value pair
print(d.items())

# in looping

for key,value in d.items():
    print(key,':',value)