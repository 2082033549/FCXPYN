import operator
lt = [{'name':'wang','age':30},{'name':'zhang','age':20},{'name':'li','age':25}]
sorted_lt = sorted(lt,key=operator.itemgetter('age'))
print(sorted_lt)
