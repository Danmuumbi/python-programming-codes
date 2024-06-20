a = [1,2,3]
c = [2,3,4]
t = [3,5,6]
result = list(map(lambda x,y,z:x+y+z,a,c,t))
print(result)

a = [1,2,3]
c = [2,3,5,4]
t = [3,5,6]
result = list(map(lambda x,y,z:x+y+z,a,c,t))
print(result)
fibonacci = [0,1,1,2,3,5,8,13,21,34,55]
odd_numbers = list(filter(lambda x: x % 2, fibonacci))
print(odd_numbers)