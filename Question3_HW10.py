class EventItem:
    # EventName, EventType : STRING
    # Difficulty : INTEGER
    def __init__(self, EventName, EventType, Difficulty):
        self.__EventName = EventName
        self.__EventType = EventType
        self.__Difficulty = Difficulty

    def GetName(self):
        return self.__EventName

    def GetDifficulty(self):
        return self.__Difficulty

    def GetEventType(self):
        return self.__EventType

class Character:
    # CharacterName : STRING
    # Run, Swim, Climb, Cycle : INTEGER
    def __init__(self, CharacterName, Run, Swim, Climb, Cycle):
        self.__CharacterName = CharacterName
        self.__Run = Run
        self.__Swim = Swim
        self.__Climb = Climb
        self.__Cycle = Cycle

    def GetName(self):
        return self.__CharacterName

    def CalculateScore(self, EventType, Difficulty):
        if EventType == "run":
            Skill = self.__Run
        elif EventType == "swim":
            Skill = self.__Swim
        elif EventType == "climb":
            Skill = self.__Climb
        else:
            Skill = self.__Cycle
        if Skill >= Difficulty:
            return 100
        Difference = Difficulty - Skill
        return 110 - 20 * Difference

def main():
    Group = [None] * 5
    Group[0] = EventItem("Hill climb", "climb", 3)
    Group[1] = EventItem("River dash", "swim", 4)
    Group[2] = EventItem("Track sprint", "run", 5)
    Group[3] = EventItem("Mountain pass", "cycle", 2)
    Group[4] = EventItem("Rock face", "climb", 4)
    Kai = Character("Kai", 5, 3, 5, 1)
    Rue = Character("Rue", 2, 2, 3, 4)
    KaiPoints = 0
    RuePoints = 0
    for Event in Group:
        Type = Event.GetEventType()
        Difficulty = Event.GetDifficulty()
        KaiChance = Kai.CalculateScore(Type, Difficulty)
        RueChance = Rue.CalculateScore(Type, Difficulty)
        if KaiChance > RueChance:
            KaiPoints += 1
            print(Event.GetName() + ": " + Kai.GetName() + " wins")
        elif RueChance > KaiChance:
            RuePoints += 1
            print(Event.GetName() + ": " + Rue.GetName() + " wins")
        else:
            print(Event.GetName() + ": draw")
    if KaiPoints > RuePoints:
        print(Kai.GetName(), "wins the group with", KaiPoints, "points")
    elif RuePoints > KaiPoints:
        print(Rue.GetName(), "wins the group with", RuePoints, "points")
    else:
        print("The group is a draw")


if __name__ == "__main__":
    main()
