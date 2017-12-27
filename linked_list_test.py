from DataStruct.linked_list import Linked_List, Node

mylist = Linked_List()
print (mylist)
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)
print (mylist.search(31))

print (mylist.search(117))

mylist.remove(31)
print (mylist.search(31))



