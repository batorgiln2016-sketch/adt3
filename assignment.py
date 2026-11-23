# You can remove 'pass' if you written code in the function
# Do NOT use .append() or .pop() inside Enqueue() and Dequeue() - move the pointers yourself.

# Exercise 1
Queue = []
HeadPointer = 0
TailPointer = -1
# Write code here to fill Queue with 8 elements, all -1


def IsEmpty():
    global Queue, HeadPointer, TailPointer
    if HeadPointer > TailPointer:
        return True
    else:
        return False


def IsFull():
    global Queue, HeadPointer, TailPointer
    if TailPointer == 7:
        return True
    else:
        return False

# Exercise 2
def Enqueue(Item):
    # Write your code here
    pass


# Exercise 3
def Dequeue():
    # Write your code here
    pass


# Exercise 4
def Peek():
    # Write your code here
    pass


def ShowQueue():
    # Write your code here
    pass


# Exercise 5
def Canteen(Commands):
    # Write your code here
    pass
