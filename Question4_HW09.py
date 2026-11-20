class Character:
    # Name : STRING
    # XPosition, YPosition : INTEGER
    def __init__(self, Name, XPosition, YPosition):
        self.__Name = Name
        self.__XPosition = XPosition
        self.__YPosition = YPosition

    def GetXPosition(self):
        return self.__XPosition

    def GetYPosition(self):
        return self.__YPosition

    def SetXPosition(self, Value):
        self.__XPosition += Value
        if self.__XPosition > 2000:
            self.__XPosition = 2000
        elif self.__XPosition < 0:
            self.__XPosition = 0

    def SetYPosition(self, Value):
        self.__YPosition += Value
        if self.__YPosition > 2000:
            self.__YPosition = 2000
        elif self.__YPosition < 0:
            self.__YPosition = 0

    def Move(self, Direction):
        if Direction == "up":
            self.SetYPosition(5)
        elif Direction == "down":
            self.SetYPosition(-5)
        elif Direction == "left":
            self.SetXPosition(-5)
        elif Direction == "right":
            self.SetXPosition(5)

class BikeCharacter(Character):
    def __init__(self, Name, XPosition, YPosition):
        super().__init__(Name, XPosition, YPosition)

    def Move(self, Direction):
        if Direction == "up":
            self.SetYPosition(15)
        elif Direction == "down":
            self.SetYPosition(-15)
        elif Direction == "left":
            self.SetXPosition(-15)
        elif Direction == "right":
            self.SetXPosition(15)

def main():
    Maya = Character("Maya", 30, 70)
    Leo = BikeCharacter("Leo", 120, 40)
    Name = input("Choose character (maya/leo): ").strip().lower()
    while Name not in ["maya", "leo"]:
        Name = input("Enter maya or leo: ").strip().lower()
    Direction = input("Direction (up/down/left/right): ").strip().lower()
    while Direction not in ["up", "down", "left", "right"]:
        Direction = input("Enter up, down, left or right: ").strip().lower()
    if Name == "maya":
        Current = Maya
    else:
        Current = Leo
    Current.Move(Direction)
    print(Name.capitalize() + "'s new position is X =",
          Current.GetXPosition(), "Y =", Current.GetYPosition())


if __name__ == "__main__":
    main()
