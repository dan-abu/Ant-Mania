"""Ant mania: the simulator of a giant space ant invasion of planet Hiveum"""
import sys
import random
import time

class Colony:
    """Create a class representing a colony on planet Hiveum"""
    def __init__(self, name, tunnels):
        """Creating colony and colony attributes: colony name, colony tunnels and list of ants in the colony"""
        self.name = name
        self.tunnels = tunnels
        self.ants = []

    def add_ant(self, ant):
        """Adding an ant to the list of ants in the colony"""
        if ant not in self.ants:
            self.ants.append(ant)

    def remove_ant(self, ant):
        """Removing an ant from the list of ants in the colony"""
        self.ants.remove(ant)

    def is_destroyed(self):
        """Binary check if there are 2 or more ants in the colony"""
        return len(self.ants) >= 2

    def destroy(self):
        """Create method simulating two ants fighting and as a result destroying the colony, themselves and any other
        ants that were in the colony"""
        ant1, ant2 = self.ants[0], self.ants[1]
        print(f"A battle is happening at {self.name} between ant {ant1.id} and ant {ant2.id}!")
        time.sleep(2) #Pause for 2 seconds to build suspense
        print(f"Update. {self.name} has been destroyed by ant {ant1.id} and ant {ant2.id}!")
        time.sleep(2) #Pause for 2 seconds to build suspense
        for ant in self.ants:
            ants.remove(ant) #Destroy all ants in the colony
        colonies.remove(self) #Destroy colony
        for colony in colonies:
            if self in colony.tunnels.values():
                #Remove the destroyed colony's name and tunnels from other colonies
                del colony.tunnels[list(colony.tunnels.values()).index(self)]

class Ant:
    """Creating a class representing a giant space ant"""
    def __init__(self, id):
        """Creating ant and ant attributes: ID number, colony association and moves count"""
        self.id = id
        self.colony = None
        self.moves = 0

    def move(self):
       """Creating method that does the following:
            1.) Randomly assigns an ant to a colony
            2.) Moves the ant to a new colony that is connected to its current colony via a tunnel
            3.) Checks if there is another ant in the colony and executes the .destroy() method if necessary"""
       if self.colony is None:
           #1.) Randomly assigns an ant to a colony
           if not colonies:
                return
           self.colony = random.choice(colonies)
           self.colony.add_ant(self)
       else:
            if self.colony.is_destroyed():
                # 3.) Checks if there is another ant in the colony and executes the .destroy() method if necessary
                self.colony.destroy()
                self.colony = None
            else:
                # 2.) Moves the ant to a new colony that is connected to its current colony via a tunnel
                next_colony_name = random.choice(list(self.colony.tunnels.values()))
                try:
                    next_colony = next(colony for colony in colonies if colony.name == next_colony_name)
                    self.colony.remove_ant(self)
                    next_colony.add_ant(self)
                    self.colony = next_colony
                except StopIteration:
                    # Declaring an ant is potnetially trapped underground because its colony was destroyed
                    print(f"Ant {self.id} is trapped!")
                    time.sleep(2) #Pause for 2 seconds to build suspense
                    self.colony = None
                    ants.remove(self)
                    for colony in colonies:
                        colony.ants[:] = [ant for ant in colony.ants if self != ant]
       self.moves += 1

if __name__ == "__main__":
    # List of colonies and ants
    colonies = []
    ants = []

    # Reading Hiveum map txt file as a command line argument
    with open(sys.argv[1]) as file:
        for line in file:
            name, *tunnels = line.strip().split()
            colony_tunnels = {}
            for tunnel in tunnels:
                direction, other_colony = tunnel.split("=")
                colony_tunnels[direction] = other_colony
            colonies.append(Colony(name, colony_tunnels))

    # N number of ants based on command line argument
    num_ants = int(sys.argv[2])

    # Creating Ant IDs as per the input in the command line argument and appending to the ants list
    for i in range(num_ants):
        ants.append(Ant(i))

    print("""
          =====================
          WELCOME TO ANT MANIA!
          =====================
          """)    
    
    while ants and max(ant.moves for ant in ants) < 10000:
        for ant in ants:
            ant.move()

    if ants:
        print("The ants have exhausted themselves. The invasion has ended!\nThe following colonies are remaining:")
        # Printing remaining colonies in the same format as the Hiveum map input txt file
        for colony in colonies:
            print(f"{colony.name}", end="")
            for direction, other_colony in colony.tunnels.items():
                print(f" {direction}={other_colony}", end="")
            print()

        print("The following ants are remaining:")
        for ant in ants:
            print(ant.id)
        
        print("""
        ======================
        THANK YOU FOR PLAYING!
                THE END
        ======================
        """)
    else:
        print("All the ants have valiently died in battle or are trapped underground.\nThe invasion has ended!\nThe following colonies are remaining:")
        for colony in colonies:
            print(f"{colony.name}", end="")
            for direction, other_colony in colony.tunnels.items():
                print(f" {direction}={other_colony}", end="")
            print()
        
        print("""
        ======================
        THANK YOU FOR PLAYING!
                THE END
        ======================
        """)