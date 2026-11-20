class Tree:
    # PRIVATE TreeName : STRING
    # PRIVATE HeightGrowth : INTEGER
    # PRIVATE MaxHeight : INTEGER
    # PRIVATE MaxWidth : INTEGER
    # PRIVATE Evergreen : STRING
    def __init__(self, TreeName, HeightGrowth, MaxHeight,
                 MaxWidth, Evergreen):
        self.__TreeName = TreeName
        self.__HeightGrowth = HeightGrowth
        self.__MaxHeight = MaxHeight
        self.__MaxWidth = MaxWidth
        self.__Evergreen = Evergreen

    def GetTreeName(self):
        return self.__TreeName

    def GetGrowth(self):
        return self.__HeightGrowth

    def GetMaxHeight(self):
        return self.__MaxHeight

    def GetMaxWidth(self):
        return self.__MaxWidth

    def GetEvergreen(self):
        return self.__Evergreen


def ReadData():
    Trees = []  # ARRAY OF Tree
    # open() raises FileNotFoundError if Trees.txt is missing.
    with open("Trees.txt", "r") as DataFile:
        for Line in DataFile:
            Values = Line.strip().split(",")
            NewTree = Tree(Values[0], int(Values[1]), int(Values[2]),
                           int(Values[3]), Values[4])
            Trees.append(NewTree)
    return Trees


def PrintTrees(ThisTree):
    Message = (ThisTree.GetTreeName() + " has a maximum height "
               + str(ThisTree.GetMaxHeight()) + " a maximum width "
               + str(ThisTree.GetMaxWidth()) + " and grows "
               + str(ThisTree.GetGrowth()) + " cm a year. ")
    if ThisTree.GetEvergreen() == "Yes":
        print(Message + "It does not lose its leaves.")
    else:
        print(Message + "It loses its leaves each year.")


def ChooseTrees(Trees):
    MaxHeight = int(input("Maximum height (cm): "))
    MaxWidth = int(input("Maximum width (cm): "))
    Evergreen = input("Evergreen (Yes/No): ").strip().capitalize()
    ChosenTrees = []  # ARRAY OF Tree
    for ThisTree in Trees:
        if (ThisTree.GetMaxHeight() <= MaxHeight
                and ThisTree.GetMaxWidth() <= MaxWidth
                and ThisTree.GetEvergreen() == Evergreen):
            ChosenTrees.append(ThisTree)
    if len(ChosenTrees) == 0:
        print("No suitable trees.")
        return
    for ThisTree in ChosenTrees:
        PrintTrees(ThisTree)

    TreeName = input("Tree name: ")
    StartHeight = int(input("Height when bought (cm): "))
    for ThisTree in ChosenTrees:
        if ThisTree.GetTreeName() == TreeName:
            Years = 0
            Height = StartHeight
            while Height < ThisTree.GetMaxHeight():
                Height += ThisTree.GetGrowth()
                Years += 1
            print("Years to reach maximum height:", Years)
            return
    print("Tree not in the suitable list.")


if __name__ == "__main__":
    Trees = ReadData()
    PrintTrees(Trees[0])
    ChooseTrees(Trees)
