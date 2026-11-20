
Queue = [-1] * 50
HeadPointer = -1
TailPointer = -1


def Enqueue(Data):
    global Queue, HeadPointer, TailPointer
    if TailPointer == len(Queue) - 1:
        return False
    TailPointer += 1
    Queue[TailPointer] = Data
    if HeadPointer == -1:
        HeadPointer = 0
    return True


def Dequeue():
    global Queue, HeadPointer, TailPointer
    if HeadPointer == -1:
        return -1
    Data = Queue[HeadPointer]
    Queue[HeadPointer] = -1
    if HeadPointer == TailPointer:
        HeadPointer = -1
        TailPointer = -1
    else:
        HeadPointer += 1
    return Data



def CreateQueue():
    try:
        with open("QueueData.txt", "r") as DataFile:
            for Line in DataFile:
                Data = int(Line.strip())
                if not Enqueue(Data):
                    print("Queue full")
    except OSError as Error:
        print("Unable to open or read QueueData.txt:", Error)
    except ValueError:
        print("QueueData.txt contains an invalid integer.")


# Question 2(e)(i): extend the main program
if __name__ == "__main__":
    CreateQueue()
    Total = 0
    Data = Dequeue()
    while Data != -1:
        Total += Data
        Data = Dequeue()
    print("Total:", Total)
