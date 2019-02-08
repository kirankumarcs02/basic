lst = ['a','b','c']

for number,item in enumerate(lst):
    print(number)
    print(item)

for count,item in enumerate(lst):
    if count >= 2:
        break
    else:
        print(item)

months = ['March','April','May','June']

print(list(enumerate(months,start=3)))



