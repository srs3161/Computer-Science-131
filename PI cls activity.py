class Room:
    def __init__(self, name):
        self.name = name
        self.items = []
        self.exits = []
        self.grabbables = []
        self.exitNames = []
        self.itemDescriptions = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        self._name = value

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self,value):
        self._items = value

    @property
    def exits(self):
        return self._exits

    @exits.setter
    def exits(self,value):
        self._exits = value

    @property
    def grabbables(self):
        return self._grabbables

    @grabbables.setter
    def grabbables(self,value):
        self._grabbables = value

    @property
    def exitNames(self):
        return self._exitNames

    @exitNames.setter
    def exitNames(self,value):
        self._exitNames = value

    @property
    def itemDescriptions(self):
        return self._itemDescriptions

    @itemDescriptions.setter
    def itemDescriptions(self,value):
        self._itemDescriptions = value

    def addExit(self,exitName,destinationRoom):
        self.exitNames.append(exitName)
        self.exits.append(destinationRoom)

    def addItem(self,itemName,itemDescription):
        self.items.append(itemName)
        self.itemDescriptions.append(itemDescription)

    def addGrabbable(self,grabbable):
        self.grabbables.append(grabbable)


    def __str__(self):
        s = ''
        #let's concatenate the room name
        s+="You are in "+self.name+"\n\n"

        #then let's add the items
        s+="You see:\n"
        for item in self.items:
            s+=item+"\n"

        s+="\n"

        #and now the exits
        s+="Exits to the:\n"
        for exitName in self.exitNames:
            s+=exitName+"\n"

        s+="\n"
        
        return s 

def createRooms():
    r1 = Room("Room 1")
    r2 = Room("Room 2")
    r3 = Room("Room 3")
    r4 = Room("Room 4")

    r1.addExit("east", r2)
    r1.addExit("south",r3)
    r2.addExit("west",r1)
    r2.addExit("south",r4)
    r3.addExit("north",r1)
    r3.addExit("east",r4)
    r4.addExit("north",r2)
    r4.addExit("west",r3)


    r1.addItem("skunk","a stinky, but super cute skunk")
    r2.addItem("elephant","a hulking big gray elephant")
    r3.addItem("the stay puft marshmallow man", "he's huge")
    r4.addItem("a dog","the dog is sleeping peacefully, but growling here and there")


    currentRoom = r1

    return currentRoom

currentRoom = createRooms()

print(currentRoom)

#core game loop
#go back and forth between
#printing the current room
#and receiving and executing input

while(True):
    print(currentRoom)
    userInput = input("What would you like to do: ")
    allInputs = userInput.split(" ")
    verb = allInputs[0]
    noun = allInputs[1]
    print(verb)
    print(noun)






