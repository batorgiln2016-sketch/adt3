# You can remove 'pass' if you written code in the function
# Do NOT use .append() or .pop() inside Enqueue() and Dequeue() - move the pointers yourself.

# Exercise 1
Queue = [-1, -1, -1, -1, -1, -1, -1, -1]
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
    global Queue, HeadPointer, TailPointer
    if IsFull():
        return False
    TailPointer = TailPointer + 1
    Queue[TailPointer] = Item
    return True


# Exercise 3
def Dequeue():
    global Queue, HeadPointer, TailPointer
    if IsEmpty():
        return -1
    Item = Queue[HeadPointer]
    HeadPointer = HeadPointer + 1
    return Item


# Exercise 4
def Peek():
    global Queue, HeadPointer, TailPointer
    if IsEmpty():
        return -1
    return Queue[HeadPointer]


def ShowQueue():
    global Queue, HeadPointer, TailPointer
    if IsEmpty():
        return ""
    Result = []
    for i in range(HeadPointer, TailPointer + 1):
        Result.append(str(Queue[i]))
    return " ".join(Result)

# Exercise 5
def Canteen(Commands):
    global Queue, HeadPointer, TailPointer
    for i in range(8):
        Queue[i] = -1
    HeadPointer = 0
    TailPointer = -1
    Served = []
    for Command in Commands:
        if Command == "serve":
            Student = Dequeue()
            if Student != -1:
                Served.append(Student)
        else:
            Parts = Command.split(" ")
            Enqueue(Parts[1])
    return Served
