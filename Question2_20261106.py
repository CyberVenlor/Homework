def InsertionSort(DataArray):
    for Index in range(1, len(DataArray)):
        Current = DataArray[Index]
        Position = Index - 1
        while Position >= 0 and DataArray[Position] > Current:
            DataArray[Position + 1] = DataArray[Position]
            Position -= 1
        DataArray[Position + 1] = Current
    return DataArray


def OutputArray(DataArray):
    for Index in range(len(DataArray)):
        if Index > 0:
            print(" ", end="")
        print(DataArray[Index], end="")
    print()


def Search(DataArray, ItemToFind):
    Lower = 0
    Upper = len(DataArray) - 1
    while Lower <= Upper:
        Middle = (Lower + Upper) // 2
        if DataArray[Middle] == ItemToFind:
            return Middle
        if DataArray[Middle] < ItemToFind:
            Lower = Middle + 1
        else:
            Upper = Middle - 1
    return -1


def main():
    DataArray = [7, 12, 3, 48, 25, 61, 5, 39, 22, 8, 54, 17, 30, 2]
    OutputArray(DataArray)
    DataArray = InsertionSort(DataArray)
    OutputArray(DataArray)
    for ItemToFind in [2, 61, 54, 33]:
        Index = Search(DataArray, ItemToFind)
        if Index == -1:
            print(ItemToFind, "not found")
        else:
            print(ItemToFind, "found at index", Index)


if __name__ == "__main__":
    main()
