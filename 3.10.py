list=['cats', 'dogs', 'bears', 'ponies', 'sheep']
#print a list
print(list)
#print a single element of the list
print(list[1])
#capitalize an element of the list
print(list[3].title())
#print the last element on the list
print(list[-1])
#change an element in the list
list[0] = 'chicken'
print(list)
#append an element to the list
list.append('butterfly')
print(list)
#insert an element into the list
list.insert(3, 'cow')
print(list)
#delete an element
del list[2]
print(list)
#pop off an element
list.pop(2)
print(list)
#remove the item by its name
list.remove('chicken')
print(list)
#alphebetize the list
list.sort()
print(list)
#reverse the orter
list.sort(reverse=True)
print(list)
#use sorted command
print(sorted(list))
# reverse the list
list.reverse()
#print the length of the list
print(len(list))

