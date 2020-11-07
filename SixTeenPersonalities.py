class Personality:
    # Alttaki değişkenleri her inputtan sonra puanlamaya göre arttır ya da azalt
    def __init__(self):
        self.Introver = 0
        self.Extraver = 0
        self.Sensing = 0
        self.Intuition = 0
        self.Thinking = 0
        self.Feelings = 0
        self.Judgement = 0
        self.Perception = 0
        self.CharacterType = ""

    def CalculateCharacter(self):
        if self.Introver > self.Extraver:
            self.CharacterType = self.CharacterType + "I"

        elif self.Extraver > self.Introver:
            self.CharacterType = self.CharacterType + "E"

        else:
            pass

        if self.Sensing > self.Intuition:
            self.CharacterType = self.CharacterType + "S"

        elif self.Intuition > self.Sensing:
            self.CharacterType = self.CharacterType + "N"

        else:
            pass

        if self.Thinking > self.Feelings:
            self.CharacterType = self.CharacterType + "T"

        elif self.Feelings > self.Thinking:
            self.CharacterType = self.CharacterType + "F"

        else:
            pass

        if self.Judgement > self.Perception:
            self.CharacterType = self.CharacterType + "J"

        elif self.Perception > self.Judgement:
            self.CharacterType = self.CharacterType + "P"

        else:
            pass

Personality = Personality()