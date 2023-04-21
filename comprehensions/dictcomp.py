keys = ['a','b','c','d','e']
values = [1,2,3,4,5]

dict = {keys:values for keys,values in zip(keys,values)}
print(dict)



sdict = {x.upper(): x*3 for x in 'coding'}
print (sdict)



l = 'jdk'
dic = {
    x: {y: x + y for y in l} for x in l
}
 
print(dic)