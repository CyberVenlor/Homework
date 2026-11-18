class NewRecord:
    # Key, Item1, Item2 : INTEGER
    def __init__(self, Key=-1, Item1=-1, Item2=-1):
        self.Key = Key
        self.Item1 = Item1
        self.Item2 = Item2

HashTable = [None] * 200
Spare = [None] * 100

def Initialise():
    for Index in range(200):
        HashTable[Index] = NewRecord()
    for Index in range(100):
        Spare[Index] = NewRecord()

def CalculateHash(Key):
    return Key % 200

def InsertIntoHash(Record):
    Index = CalculateHash(Record.Key)
    if HashTable[Index].Key == -1:
        HashTable[Index] = Record
    else:
        for Index in range(100):
            if Spare[Index].Key == -1:
                Spare[Index] = Record
                return

def CreateHashTable():
    with open("HashData.txt", "r") as File:
        for Line in File:
            Fields = Line.strip().split(",")
            Record = NewRecord(int(Fields[0]),
                               int(Fields[1]), int(Fields[2]))
            InsertIntoHash(Record)

def PrintSpare():
    Count = 0
    for Record in Spare:
        if Record.Key != -1:
            print(Record.Key, end=" ")
            Count += 1
            if Count % 10 == 0:
                print()
    print()

if __name__ == "__main__":
    Initialise()
    CreateHashTable()
    PrintSpare()
