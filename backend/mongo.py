import pymongo
from pyparsing import condition_as_parse_action
import math
import sys
import os
import signal
import colorama
colorama.init()

client = pymongo.MongoClient(
    "mongodb+srv://thoroute-app:thoroute%402022adi@thoroute.vd7gshc.mongodb.net/?retryWrites=true&w=majority")

db = client.users
buses = client.users.buses
routes = client.users.routes
optimal = client.users.optimal
print("Succesfully connected to MongoDB")

def cclear():
    os.system('cls')
    


class bus:
    def show_bus(self):
        bus = buses.find()
        for i in bus:
            print(i)

    def show_route(self):
        rt = routes.find()
        for i in rt:
            print(i)

    def insert_bus(self):
        id = input("Enter bus id: ")
        provider = input("Enter provider: ")
        bnumber = input("Enter bus number: ")
        mileage = float(input("Enter mileage (in Km/L): "))
        condition = input("Enter condition (poor/good/excellent): ")
        driven = float(input("Enter distance driven (in Km): "))
        age = float(input("Enter age of bus: "))
        capacity = int(input("Enter max seating capacity: "))
        qualityrating = (mileage*capacity)/(age*(driven/10000))
        buses.insert_one({'id': id,
                          'provider': provider,
                          'number': bnumber,
                          'mileage': mileage,
                          'condition': condition,
                          'distancedriven': driven,
                          'age': age,
                          'capacity': capacity,
                          'qualityrating': qualityrating})

    def insert_route(self):
        id = input("Enter route id: ")
        name = input("Enter route name: ")
        length = float(input("Enter length of route (in Km): "))
        stops = int(input("Enter number of stops: "))
        avgpeople = int(input("Enter average people per travel: "))
        rtquakity = (avgpeople/((length/100)*stops))
        avgperstop = round((avgpeople/stops))
        routes.insert_one({'routeid': id,
                           'name': name,
                           'length': length,
                           'stops': stops,
                           'avgpeople': avgpeople,
                           'avgperstop': avgperstop,
                           'rtquality': rtquakity})

    def optimize(self):
        optimal.delete_many({})
        bus = list(buses.find().sort('qualityrating', pymongo.DESCENDING))
        route = list(routes.find().sort('rtquality', pymongo.DESCENDING))
        """
        for i in range(len(bus)):
            print(bus[i]['busid'],":",route[i]['routeid'])
        if(len(bus) != len(route)):
            print("Error: Number of buses and routes are not equal")
        else:
            print("Calculating optimal routes...")
            for i in route:
                i.update({'flag': False})
            for i in bus:
                for j in route:
                    if j['flag'] == False:
                        combo = 0
                        if(i['qualityrating']*j['rtquality'] > combo):
                            combo = i['qualityrating']*j['rtquality']
                            rid = j
                        j.update({'flag': True})
                        break
                print(i['busid'], ":", rid['routeid'])
        """
        if(len(bus) != len(route)):
            print("Error: Number of buses and routes are not equal")
            print("Please add more buses or routes")
        else:
            for i in range(len(bus)):
                optimal.insert_one(
                    {'busid': bus[i]['id'], 'routeid': route[i]['routeid']})
                print(bus[i]['id'], ":", route[i]['routeid'])
            print("Optimal routes calculated & added to database")

    def delete_bus(self):
        id = input("Enter ID of bus to be deleted: ")
        buses.delete_one({'id': id})

    def delete_route(self):
        id = input("Enter ID of route to be deleted: ")
        routes.delete_one({'routeid': id})


colors = {
    "info":     "35m",  # Orange for info messages
    "error":    "31m",  # Red for error messages
    "ok":       "32m",  # Green for success messages
    "menu2c":  "\033[46m",  # Light blue menu
    "menu1c":  "\033[44m",  # Blue menu
    "close":  "\033[0m"  # Color coding close
}
cc = "\033[0m"
ct = "\033[101m"
cs = "\033[41m"
c1 = colors["menu1c"]
c2 = colors["menu2c"]


programtitle = "Thoroute Backend Services"

menu1_colors = {
    "ct": ct,
    "cs": cs,
    "opt": c2
}
menu1_options = {
    "title":  "Options",
    "1":      "View Buses",
    "2":      "View Routes",
    "3":      "Add Bus",
    "4":      "Add Route",
    "5":      "Delete Bus",
    "6":      "Delete Route",
    "7":      "Optimize Buses for Routes",
    "8":      "Clear the Console",
    "0":      "Quit (or use CTRL+C)",
}


def printWithColor(color, string):
    print("\033["+colors[color]+" "+string+cc)


def printError():
    printWithColor("error", "Error!!")
    return 1


def printSuccess():
    printWithColor("ok", "Success!!")
    return 0


def exit():
    sys.exit()


def sigint_handler(signum, frame):
    print("CTRL+C exit")
    sys.exit(0)


class menu_template():

    def __init__(self, options, colors):
        self.menu_width = 50  # Width in characters of the printed menu
        self.options = options
        self.colors = colors

    def createMenuLine(self, letter, color, length, text):
        menu = color+" ["+letter+"] "+text
        line = " "*(length-len(menu))
        return menu+line+cc

    def createMenu(self, size):
        line = self.colors["ct"] + " "+programtitle
        line += " "*(size-len(programtitle)-6)
        line += cc
        print(line)  # Title
        line = self.colors["cs"] + " "+self.options["title"]
        line += " "*(size-len(self.options["title"])-6)
        line += cc
        print(line)  # Subtitle
        for key in self.options:
            if(key != "title"):
                print(self.createMenuLine(
                    key, self.colors["opt"], size, self.options[key]))

    def printMenu(self):
        self.createMenu(self.menu_width)

    def action(self, ch):
        brr = bus()
        if ch == '1':
            brr.show_bus()
        elif ch == '2':
            brr.show_route()
        elif ch == '3':
            brr.insert_bus()
        elif ch == '4':
            brr.insert_route()
        elif ch == '5':
            brr.delete_bus()
        elif ch == '6':
            brr.delete_route()
        elif ch == '7':
            brr.optimize()
        elif ch == '8':
            cclear()
        elif (ch == ''):
            pass  # Print menu again
        elif ch == '0':
            sys.exit()
        else:
            printError()


class menu1(menu_template):
    pass


class menu_handler:

    def __init__(self):
        self.current_menu = "main"
        self.m1 = menu1(menu1_options, menu1_colors)

    def menuExecution(self):
        if(self.current_menu == "main"):
            self.m1.printMenu()
        else:
            self.m2.printMenu()
        choice = input(" >> ")
        if(self.current_menu == "main"):
            if(choice == "9"):
                self.current_menu = "second"
            else:
                self.actuator(0, choice)
        else:
            if(choice == '9'):
                self.current_menu = "main"
            else:
                self.actuator(1, choice)
        print("\n")

    def actuator(self, type, ch):
        if type == 0:
            self.m1.action(ch)
        else:
            self.m2.action(ch)


# Main Program
if __name__ == "__main__":
    x = menu_handler()
    signal.signal(signal.SIGINT, sigint_handler)
    while True:
        x.menuExecution()
