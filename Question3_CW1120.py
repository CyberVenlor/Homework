class SaleData:
    # ID : STRING
    # Quantity : INTEGER
    def __init__(self, ID, Quantity):
        self.ID = ID
        self.Quantity = Quantity


# CircularQueue : ARRAY[0:4] OF SaleData
CircularQueue = [SaleData("", -1) for Index in range(5)]
Head = 0
Tail = 0
NumberOfItems = 0


def Enqueue(NewRecord):
    global CircularQueue, Tail, NumberOfItems
    if NumberOfItems == len(CircularQueue):
        return -1
    CircularQueue[Tail] = NewRecord
    Tail = (Tail + 1) % len(CircularQueue)
    NumberOfItems += 1
    return 1


def Dequeue():
    global CircularQueue, Head, NumberOfItems
    if NumberOfItems == 0:
        return SaleData("", -1)
    RemovedRecord = CircularQueue[Head]
    CircularQueue[Head] = SaleData("", -1)
    Head = (Head + 1) % len(CircularQueue)
    NumberOfItems -= 1
    return RemovedRecord


def EnterRecord():
    ID = input("ID: ")
    Quantity = int(input("Quantity: "))
    NewRecord = SaleData(ID, Quantity)
    if Enqueue(NewRecord) == -1:
        print("Full")
    else:
        print("Stored")


if __name__ == "__main__":
    for Index in range(6):
        EnterRecord()
    RemovedRecord = Dequeue()
    if RemovedRecord.ID == "":
        print("Queue empty")
    else:
        print("Removed:", RemovedRecord.ID, RemovedRecord.Quantity)
    EnterRecord()
    print("Records in CircularQueue:")
    for Record in CircularQueue:
        print(Record.ID, Record.Quantity)
