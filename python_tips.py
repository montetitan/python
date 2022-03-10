#python tips


#join strings
a = ["Geeks", "For", "Geeks"]
print(" ".join(a))

#find module path
import os
import socket
  
print(os)
print(socket)


# enumerate function in loops
l1 = ["eat","sleep","repeat"]
 
# printing the tuples in object directly
for ele in enumerate(l1):
    print (ele)
for count,ele in enumerate(l1):
  print(count)
  print(ele)


# check neat f.close 
try:
    with open("output", "w") as outfile:
        outfile.write('Hello World')
except IOError:
    print ('oops!')

#### f format string
name = 'Tushar'
age = 23
print(f"Hello, My name is {name} and I'm {age} years old.")


#### check 3 largest nos
import heapq
scores = [51, 33, 64, 87, 91, 75, 15, 49, 33, 82]
print(heapq.nlargest(3, scores))  # [91, 87, 82]
print(heapq.nsmallest(5, scores))  # [15, 33, 33, 49, 51]


#list comprehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even_numbers = [number for number in numbers if number % 2 == 0]

print(even_numbers)

#merge dict
dict2 = {'name': 'Fatos', 'surname': 'Morina', 'location': 'Bavaria, Munich'}
dict1 = {'name': 'Fatos', 'location': 'Munich'}
dict2.update(dict1)

{**dict1, **dict2}

#or dict2 | dict1 for 3.9 python and higher

#string to list

import ast

def string_to_list(string):
    return ast.literal_eval(string)

string = "[[1, 2, 3],[4, 5, 6]]"
my_list = string_to_list(string)
print(my_list)  # [[1, 2, 3], [4, 5, 6]]


## generators to save memory
import sys
my_l = [i for i in range(10000)]
sum(my_l)#49995000
sys.getsizeof(my_l,"bytes") #87616
my_g = (i for i in range(10000))
sum(my_g) #49995000
sys.getsizeof(my_g) #112
type(my_l)#<class 'list'>
type(my_g)
#<class 'generator'>


# using counters to check count item
from collections import Counter

result = Counter("Banana")
print(result)  # Counter({'a': 3, 'n': 2, 'B': 1})


result = Counter([1, 2, 1, 3, 1, 4, 1, 5, 1, 6])
print(result)  # Counter({1: 5, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1})



# Generate a UUID from a host ID, sequence number, and the current time
import uuid
print(uuid.uuid1())  # 308490b6-afe4-11eb-95f7-0c4de9a0c5af
# Generate a random UUID
print(uuid.uuid4())  # 93bc700b-253e-4081-a358-24b60591076a


####itertools use to reduce time
import time
import itertools
start_time = time.time()
r= []
listA = [1,2,3,4,5]
listB = [11,12,13,14,15]

# for x in listA:
#  for y in listB:
#     r.append((x, y))

for x, y in itertools.product(listA, listB):
   r.append((x, y))

print (r)
#main()
print("--- %s seconds ---" % (time.time() - start_time))
