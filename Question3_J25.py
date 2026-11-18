class Animal:
    # Name, Sound : STRING
    # Size, Intelligence : INTEGER
    def __init__(self, Name, Sound, Size, Intelligence):
        self.__Name = Name
        self.__Sound = Sound
        self.__Size = Size
        self.__Intelligence = Intelligence

    def Description(self):
        return (f"The animal's name is {self.__Name}, "
                f"it makes a {self.__Sound}, its size is {self.__Size} "
                f"and its intelligence level is {self.__Intelligence}")

class Parrot(Animal):
    # WingSpan, NumberWords : INTEGER
    def __init__(self, Name, Sound, Size, Intelligence,
                 WingSpan, NumberWords):
        super().__init__(Name, Sound, Size, Intelligence)
        self.__WingSpan = WingSpan
        self.__NumberWords = NumberWords

    def ChangeNumberWords(self, Change):
        self.__NumberWords += Change

    def Description(self):
        return (super().Description() +
                f". It has a wingspan of {self.__WingSpan}cm "
                f"and can say {self.__NumberWords} words.")

class Wolf(Animal):
    # TerritorySize : INTEGER
    def __init__(self, Name, Sound, Size, Intelligence,
                 TerritorySize):
        super().__init__(Name, Sound, Size, Intelligence)
        self.__TerritorySize = TerritorySize

    def SetTerritorySize(self, Change):
        self.__TerritorySize += Change

    def Description(self):
        return (super().Description() +
                f". Its territory is {self.__TerritorySize} square miles.")

if __name__ == "__main__":
    Chewie = Parrot("Chewie", "Squawk", 1, 10, 30, 29)
    Nighteyes = Wolf("Nighteyes", "Howl", 8, 7, 100)
    Copper = Animal("Copper", "Neigh", 10, 6)
    Nighteyes.SetTerritorySize(-20)
    Chewie.ChangeNumberWords(2)
    print(Chewie.Description())
    print(Nighteyes.Description())
    print(Copper.Description())
