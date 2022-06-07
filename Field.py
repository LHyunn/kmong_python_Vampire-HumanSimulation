import random
import matplotlib.pyplot as plt
from entity import *
import random



XMAX = 100
YMAX = 100


def HumanBeVampired(human):
    vampire = Vampire([human.pos[0], human.pos[1]], [XMAX, YMAX], human.health, human.stack)
    return vampire

def HumanMeetWater(HumanList, WaterList):
    for human in HumanList:
        for water in WaterList:
            if abs(human.pos[0] - water.pos[0]) <= 1 and abs(human.pos[1] - water.pos[1]) <= 1:
                human.health += 50
                print("Human{} has met water, human{} gained health 50.".format(human.pos, human.pos))
                WaterList.remove(water)
                print("Water{} has been removed.".format(water.pos))

def HumanMeetFood(HumanList, FoodList):
    for human in HumanList:
        for food in FoodList:
            if abs(human.pos[0] - food.pos[0]) <= 1 and abs(human.pos[1] - food.pos[1]) <= 1:
                human.health += 30
                print("Human{} has met food, human{} gained health 30.".format(human.pos, human.pos))
                FoodList.remove(food)
                print("Food{} has been removed.".format(food.pos))

def HumanMeetGarlic(HumanList, GarlicList):
    for human in HumanList:
        for garlic in GarlicList:
            if abs(human.pos[0] - garlic.pos[0]) <= 1 and abs(human.pos[1] - garlic.pos[1]) <= 1:
                human.health += 100
                print("Human{} has met garlic, human{} gained health 100.".format(human.pos, human.pos))
                GarlicList.remove(garlic)
                print("Garlic{} has been removed.".format(garlic.pos))

def VampireMeetVampire(VampireList):
    for vampire1 in VampireList:
        for vampire2 in VampireList:
            if vampire1 != vampire2:
                if abs(vampire1.pos[0] - vampire2.pos[0]) <= 1 and abs(vampire1.pos[1] - vampire2.pos[1]) <= 1:
                    if vampire1.stack == 0 and vampire2.stack == 0:
                        vampire1.stack = 1
                        vampire2.stack = 1
                        vampire1.health -= 20
                        vampire2.health -= 20
                        print("Vampire{} and Vampire{} have met, vampire{} lost health 20, vampire{} lost health 20.".format(vampire1.pos, vampire2.pos, vampire1.pos, vampire2.pos))
    for vampire in VampireList:
        if vampire.health <= 0:
            VampireList.remove(vampire)
            print("Vampire{} has died.".format(vampire.pos))
    for vampire1 in VampireList:
        for vampire2 in VampireList:
            vampire1.stack = 0
            vampire2.stack = 0

def VampireMeetHuman(VampireList, HumanList):
    for vampire in VampireList:
        for human in HumanList:
            if abs(vampire.pos[0] - human.pos[0]) <= 1 and abs(vampire.pos[1] - human.pos[1]) <= 1:
                if vampire.stack == 0 and human.stack == 0:
                    vampire.stack = 1
                    human.stack = 1
                    if random.randint(0, 100) <= 30:
                        vampire.health -= 30
                        print("Human{} has attacked Vampire, vampire{} lost health 30. now {}".format(human.pos, vampire.pos, vampire.health))
                    else:
                        vampire2 = HumanBeVampired(human)
                        VampireList.append(vampire2)
                        HumanList.remove(human)
                        print("Vampire{} has attacked human, human{} is now a vampire.".format(vampire.pos, human.pos))
    for vampire in VampireList:
        if vampire.health <= 0:
            VampireList.remove(vampire)
            print("Vampire{} has died.".format(vampire.pos))
    for vampire in VampireList:
        for human in HumanList:
            vampire.stack = 0
            human.stack = 0

def HumanMeetHuman(HumanList):
    for human1 in HumanList:
        for human2 in HumanList:
            if human1 != human2:
                if abs(human1.pos[0] - human2.pos[0]) <= 1 and abs(human1.pos[1] - human2.pos[1]) <= 1:
                    if human1.stack == 0 and human2.stack == 0:
                        human1.stack = 1
                        human2.stack = 1
                        if random.randint(0, 100) <= 40:
                            if random.randint(0, 100) <= 50:
                                human1.health += 20
                                human2.health -= 20
                                print("Human{} and Human{} have met, human{} gained health 20, human{} lost health 20.".format(human1.pos, human2.pos, human1.pos, human2.pos))
                            else :
                                human1.health -= 20
                                human2.health += 20
                                print("Human{} and Human{} have met, human{} lost health 20, human{} gained health 20.".format(human1.pos, human2.pos, human1.pos, human2.pos))
                        else:
                            human1.health += 10
                            human2.health += 10
                            print("Human{} and Human{} help each other, both gain 10 health. ".format(human1.pos, human2.pos))
    for human in HumanList:
        if human.health <= 0:
            HumanList.remove(human)
            print("human{} has died.".format(human.pos))
    for human1 in HumanList:
        for human2 in HumanList:
            human1.stack = 0
            human2.stack = 0
    








def main():

    HumanList = []
    numOfHuman = 40
    VampireList = []
    numofVampire = 10
    WaterList = []
    numofWater = 5
    FoodList = []
    numofFood = 5
    GarlicList = []
    numofGarlic = 5

    HumanList = []
    VampireList = []
    WaterList = []
    FoodList = []
    GarlicList = []

    for i in range(numOfHuman):
        HumanList.append(Human([random.randint(0, XMAX), random.randint(0, YMAX)],[XMAX, YMAX],100, random.randint(10,50), 0))
    for i in range(numofVampire):
        VampireList.append(Vampire([random.randint(0, XMAX), random.randint(0, YMAX)],[XMAX, YMAX],100, 0))
    for i in range(numofWater):
        WaterList.append(Water([random.randint(0, XMAX), random.randint(0, YMAX)],[XMAX, YMAX]))
    for i in range(numofFood):
        FoodList.append(Food([random.randint(0, XMAX), random.randint(0, YMAX)],[XMAX, YMAX]))
    for i in range(numofGarlic):
        GarlicList.append(Garlic([random.randint(0, XMAX), random.randint(0, YMAX)],[XMAX, YMAX]))


    for i in range(50):
        xvalues_human = []
        yvalues_human = []

        xvalues_vampire = []
        yvalues_vampire = []

        xvalues_water = []
        yvalues_water = []

        xvalues_food = []
        yvalues_food = []

        xvalues_garlic = []
        yvalues_garlic = []
        
        for human in HumanList:
            human.stepChange()
            xvalues_human.append(human.pos[0])
            yvalues_human.append(human.pos[1])
            ㅋㅋㅋㅋ
        for vampire in VampireList:
            vampire.stepChange()
            xvalues_vampire.append(vampire.pos[0])
            yvalues_vampire.append(vampire.pos[1])
        
        for water in WaterList:

            xvalues_water.append(water.pos[0])
            yvalues_water.append(water.pos[1])

        for food in FoodList:

            xvalues_food.append(food.pos[0])
            yvalues_food.append(food.pos[1])

        for garlic in GarlicList:

            xvalues_garlic.append(garlic.pos[0])
            yvalues_garlic.append(garlic.pos[1])
    

        HumanMeetHuman(HumanList)
        VampireMeetHuman(VampireList, HumanList)
        VampireMeetVampire(VampireList)
        HumanMeetFood(HumanList, FoodList)
        HumanMeetWater(HumanList, WaterList)
        HumanMeetGarlic(HumanList, GarlicList)



        plt.scatter(xvalues_human, yvalues_human, c="red", marker = "o")
        plt.scatter(xvalues_vampire, yvalues_vampire, c="black", marker ='o')   
        plt.scatter(xvalues_water, yvalues_water, c="blue", marker = "s")
        plt.scatter(xvalues_food, yvalues_food, c="brown", marker="s") 
        plt.scatter(xvalues_garlic, yvalues_garlic, c="grey", marker='^')
        plt.xlim(0,XMAX)
        plt.ylim(0,YMAX)
        plt.pause(0.05)
        plt.clf()
        print(i)

        
    print("After simulation, there are {} humans and {} vampires.".format(len(HumanList), len(VampireList)))
    print("Left humans are:")
    for human in HumanList:
        print(human.pos)
    print("Left vampires are:")
    for vampire in VampireList:
        print(vampire.pos)

   
        


    
if __name__ == "__main__":
    main()