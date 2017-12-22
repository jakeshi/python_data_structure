class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext
        
class Linked_List:

    def __init__(self):
        self.head = None
        
    def isEmpty(self):
        return self.head == None
    
    def add(self,newdata):
        temp = Node(newdata)
        temp.setNext(self.head)
        self.head = temp
        
    def size(self):
    	current = self.head
    	count = 0
		while current != None:
			count = count + 1
			current = current.getNext()
	
		return count
        
    def search(self,target):
    	res = False
    	current=self.head
    	while not res and current!= None:
    		if current.getData()==target:
    			return True
    		else:
    			current = current.getNext()
    	return res
    	
        
