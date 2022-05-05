import copy

phase = 1
# 1 - name armies
# 2 - buy units
# 3 - skirmish
# 4 - melee
# 5 - routing

class Unit:
    def __init__(self):
        self.name = ""
        self.damage = 0
        self.defense = 0
        self.count = 0
        self.cost = 0
        self.info = ""

    def special(self):
        return 0

    def skirmish(self):
        return self.damage * self.count

    def melee(self):
        return self.damage * self.count

    def rout(self, hunt):
        if (hunt):
            return 2 * self.damage * self.count
        else:
            return 0

    def getDefense(self):
        return self.defense * self.count

    def getCost(self):
        return self.cost

    def getName(self):
        return self.name

    def getInfo(self):
        return self.info

    def getCount(self):
        return self.count

    def setCount(self, count):
        self.count = count

class Archer(Unit):
    def __init__(self):
        self.name = "Archer"
        self.damage = 1
        self.defense = 0
        self.count = 0
        self.cost = 10
        self.info = "Bad in melee but good in skirmish and hunting down"

    def skirmish(self):
        return 10 * self.damage * self.count

    def melee(self):
        return 0

    def rout(self, hunt):
        if (hunt):
            return 5 * self.damage * self.count
        else:
            return 0

class Soldier(Unit):
    def __init__(self):
        self.name = "Soldier"
        self.damage = 1
        self.defense = 1
        self.count = 0
        self.cost = 5
        self.info = "Weak alone but strong in groups"

        def special(self):
            if count >= 20:
                self.damage = 2
            if count >= 80:
                self.damage = 3
            if count >= 150:
                self.damage = 5
                

class ShieldBearer(Unit):
    def __init__(self):
        self.name = "Shield bearer"
        self.damage = 2
        self.defense = 2
        self.count = 0
        self.cost = 20
        self.info = "Good defense that increases, but bad in routs"

    def special(self):
        if phase == 5:
            self.defense = 0
        else:
            defense *= 2

    def rout(self, hunt):
        return 0

unit_types = [Archer(), Soldier(), ShieldBearer()]

def displayShop():
    print("=======SHOP=======")
    for unit_type in unit_types:
        name = unit_type.getName()
        cost = unit_type.getCost()
        info = unit_type.getInfo()
        print("##################")
        print("Name: " + name)
        print("Cost: " + str(cost))
        print("info: " + info)
        print("##################")

def main():
    phase = 1
    fight1 = []
    fight2 = []
    print("Name the armies")
    army1 = input("Enter the name of army one: ")
    army2 = input("Enter the name of army two: ")
    print("-------------------------------------------------------")
    phase = 2
    print("Buy your armies")
    print(army1 + " you go first")
    displayShop()
    fund1 = 1000
    fund2 = 1000
    while True:
        print("FUNDS: " + str(fund1))
        choice = input("(1) To buy, (2) to exit: ")
        if choice == "1":
            while True:
                buy_unit = input("Enter unit to be bought or (2) to exit: ")
                if buy_unit == "2":
                    break;
                unit_found = -1
                for i in range(len(unit_types)):
                    if unit_types[i].getName() == buy_unit:
                        unit_found = i
                        break;
                if unit_found >= 0:
                    try:
                        buy_count = int(input("Enter amount to buy: ").rstrip())
                        if buy_count > 0:
                            confirmed = False
                            the_cost = unit_types[unit_found].getCost() * buy_count
                            if the_cost <= fund1:
                                confirm_buy = input("Enter (1) to confirm buying, anything else to cancel: ")
                                if(confirm_buy == "1"):
                                    confirmed = True
                                    fund1 -= the_cost
                                else:
                                    print("The buying has been cancelled")
                            else:
                                print("Insufficient Funds")
                            if confirmed:
                                exists = -1
                                for i in range(len(fight1)):
                                    if fight1[i].getName() == buy_unit:
                                        exists = i
                                        break;
                                if exists >= 0:
                                    fight1[exists].setCount(buy_count + fight1[exists].getCount())
                                else:
                                    print("A")
                                    fight1.append(copy.copy(unit_types[unit_found]))
                                    print("B")
                                    fight1[-1].setCount(buy_count)
                                    print(fight1[-1].getCount())
                                    print(unit_types[unit_found].getCount())
                        else:
                            print("Input must be positive")
                    except:
                        print("Invalid Input")
                        
                else:
                    print("No such unit exists")
        elif choice == "2":
            break;
        else:
            print("Invalid Input")
    
    
main()
