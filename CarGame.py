import random

class Car:
    def __init__(self, name=""):
        self.name = name
        self.position = 0
        
    def getPosition(self):
        return self.position
    
    def getName(self):
        return self.name
    
class CarGame:
    def __init__(self):
        self.car = None
        self.nums = 0
        self.carList = []
        
        self.getCarNames()
        self.getGameNum()
        
        self.startGame()
        self.getScore()
        
    def getGameNum(self):
        self.nums = int(input("시도할 회수는 몇회인가요?"))
        return True
    
    def getCarNames(self):
        self.cars = input("경주할 자동차 이름을 입력하세요.(이름은 쉼표(,) 기준으로 구분)").split(',')
        self.carList = []
        for i in range(len(self.cars)):
            self.carList.append(Car(self.cars[i]))    

    def startGame(self):
        for i in range(self.nums):
            self.playGame()
    
    def playGame(self):
        for i in range(len(self.carList)):
            self.carList[i].position += self.action()
            print(f"{self.carList[i].name} : {self.carList[i].position}")
        print()
        
    def action(self):
        return 1 if random.randint(0, 9) >= 4 else 0 
    
    def getScore(self):
        maxVal = max(map(Car.getPosition, self.carList))
        self.winners = [c.name for c in self.carList if c.position == maxVal]
        print(",".join(self.winners) + "가 최종 우승했습니다.")
        
if __name__ == "__main__":
    game = CarGame()
