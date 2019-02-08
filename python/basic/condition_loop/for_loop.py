my_list = {'key1': 1, 'key2': 2}

for x in my_list:
    print(x)

for x in my_list.items():
    print(x)
    # x= {key1: 1}

for x, y in my_list.items():
    print(x,y)

for x in my_list.values():
    print(x)

word = 'Kiran'
for name in word:
    print('letter:', name)

for index, letter in enumerate(word):
    print(index, letter)

mylist = []

for letter in word:
    mylist.append(letter)

print(mylist)

# convert string to string[]

wordArray = [letter for letter in word]

print(wordArray)


numArray = [num**2 for num in range(0,11)]
print('numArray', numArray)

numArray = [num**2 for num in range(0,11) if num%2 ==0]
print('numArray', numArray)

results = [ x if x%2 == 0 else 'ODD' for x in range(0,11)]
print(results)

# nested array
nestedList = []

for x in [2,4,6]:
    for y in [100,200,300]:
        nestedList.append(x*y)

print('nested List', nestedList)

nested_list= [x*y for x in [2,4,6] for y in [100,200,300]]

print('Nested_list', nested_list)
