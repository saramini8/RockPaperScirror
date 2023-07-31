#All we need for participants - Name, Point, Choice
class Participate:
    def __init__(self,name):
        self.name= name
        self.point= 0
        self.choice= ''

    def Choose(self):
        self.choice = input(f'Dear {self.name}, please choose one: Rock/Paper/Scissor\n')
        print(f'{self.name} choose {self.choice}')

    def toNum(self):
        ChosenNum ={
            "Rock": 0,
            "Paper": 1,
            "Scissor": 2
        }
        return ChosenNum[self.choice]

    def AddPoint(self):
        self.point+=1


#This is the main part which implement the game round
class GameRound:
    def __init__(self,p1,p2):

        self.rules = [
            [0,-1,1],
            [1,0,-1],
            [-1,1,0]
        ]

        p1.Choose()
        p2.Choose()

        result = self.compareChoices(p1,p2)
        if result==0:
                print("We have a draw")
        elif result == 1:
            print(f"{p1.name} is the winner here!")
            p1.AddPoint()
        else:
            print(f"{p2.name} is the winner!")
            p2.AddPoint()

    def compareChoices(self,p1,p2):
        return  self.rules[p1.toNum()][p2.toNum()]
            

#In this class, we decide to continue or end the game
class Game:
    def __init__(self):
        self.endOfTheGame = False
        self.p1 = Participate("Sara")
        self.p2 = Participate("Nima")

    def start(self):
        while not self.endOfTheGame:
            GameRound(self.p1,self.p2)
            self.checkEnd()
        

    def checkEnd(self):
        answer = input("Do you want to continue? Y/N\n")
        if answer == "Y":
            GameRound(self.p1,self.p2)
            self.checkEnd()
        else:
            print("Game ended...\n")
            self.detectWinner()
            self.endOfTheGame= True

    def detectWinner(self):
        if self.p1.point == self.p2.point:
            print("The result is draw!")
            print(f"{self.p1.name} = {self.p1.point} va {self.p2.name} = {self.p2.point}")
        elif self.p1.point > self.p2.point:
            print(f"Congrats {self.p1.name}! You are the winner.\n")
            print(f"{self.p1.name} = {self.p1.point} va {self.p2.name} = {self.p2.point}")
        else:
           print(f"Congrats {self.p2.name}! You are the winner.\n")
           print(f"{self.p1.name} = {self.p1.point} va {self.p2.name} = {self.p2.point}") 


        
game = Game()
game.start()



    