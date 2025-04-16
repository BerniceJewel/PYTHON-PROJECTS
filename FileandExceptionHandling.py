class WatchRepair:
    """Represents a specific watch repair job."""

    def __init__(self, customer_name, watch_brand, issue, repair_cost=0, status="Pending"):
        """
        Constructor to initialize a WatchRepair object.

        Args:
            customer_name (str): The name of the customer.
            watch_brand (str): The brand of the watch being repaired.
            issue (str): A description of the problem with the watch.
            repair_cost (float): The estimated or final cost of the repair (default is 0).
            status (str): The current status of the repair (default is "Pending").
        """
        self.customer_name = customer_name
        self.watch_brand = watch_brand
        self.issue = issue
        self.repair_cost = repair_cost
        self.status = status

    def diagnose(self, findings, estimated_cost):
        """Diagnoses the watch issue and sets the estimated cost."""
        print(f"Diagnosing {self.customer_name}'s {self.watch_brand} watch. Issue: {self.issue}")
        print(f"Findings: {findings}")
        self.repair_cost = estimated_cost
        self.status = "Diagnosed"
        print(f"Estimated repair cost: Ksh.{self.repair_cost}")

    def perform_repair(self, details):
        """Performs the repair and updates the status."""
        if self.status == "Diagnosed" or self.status == "Pending":
            print(f"Performing repair on {self.customer_name}'s {self.watch_brand} watch...")
            print(f"Repair details: {details}")
            self.status = "Repairing"
            print("Repair in progress.")
        else:
            print(f"Cannot perform repair. Current status: {self.status}")

    def mark_completed(self):
        """Marks the repair as completed."""
        if self.status == "Repairing":
            self.status = "Completed"
            print(f"Repair for {self.customer_name}'s {self.watch_brand} watch is now completed.")
        else:
            print(f"Cannot mark as completed. Current status: {self.status}")

    def update_cost(self, final_cost):
        """Updates the final repair cost."""
        self.repair_cost = final_cost
        print(f"Final repair cost for {self.customer_name}'s {self.watch_brand} watch: Ksh.{self.repair_cost}")

    def get_status(self):
        """Returns the current status of the repair."""
        return self.status

    def __str__(self):
        """String representation of the WatchRepair object."""
        return f"Repair for {self.customer_name}'s {self.watch_brand} watch. Issue: {self.issue}. Status: {self.status}. Cost: Ksh.{self.repair_cost}"

# Creating instances of WatchRepair
repair1 = WatchRepair("Alice Johnson", "Rolex", "Stopped ticking")
repair2 = WatchRepair("Bob Williams", "Seiko", "Broken strap", status="Diagnosed", repair_cost=25.00)

repair1.diagnose("Mainspring broken, needs replacement", 1500.00)
repair1.perform_repair("Replaced mainspring, cleaned and oiled movement")
repair1.mark_completed()
repair1.update_cost(1650.00)

print(repair1)
print(repair2.get_status())

#PART 2

class Person:
    """Base class for individuals."""
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hello, my name is {self.name}.")

class Superhero(Person):
    """Represents a superhero."""
    def __init__(self, name, super_name, power):
        super().__init__(name)
        self.super_name = super_name
        self.power = power

    def use_power(self):
        print(f"{self.super_name} uses their amazing power of {self.power}!")

    def reveal_identity(self):
        print(f"In my secret identity, I am {self.name}.")

class SuperheroWatchRepair(Superhero, WatchRepair):
    """A superhero who also runs a watch repair shop for super-tech."""
    def __init__(self, name, super_name, power, watch_brand, issue):
        Superhero.__init__(self, name, super_name, power)
        WatchRepair.__init__(self, name, watch_brand, issue) # Using name for customer

    def repair_super_tech(self, diagnostics, parts_needed, final_cost):
        print(f"{self.super_name} is expertly repairing the {self.watch_brand} watch.")
        self.diagnose(diagnostics, final_cost)
        print(f"Required parts: {parts_needed}")
        self.perform_repair("Replaced specialized components")
        self.mark_completed()
        self.update_cost(final_cost)

    def use_super_tools(self):
        print(f"{self.super_name} uses advanced super-tools for the repair!")

# Creating an instance of the SuperheroWatchRepair class
tech_hero = SuperheroWatchRepair("Tony Stark", "Iron Man", "Powered Armor", "Stark Industries Tech", "Arc Reactor malfunction")

tech_hero.introduce()
tech_hero.reveal_identity()
tech_hero.use_power()
tech_hero.repair_super_tech("Energy core unstable, capacitor overload", "Nano-capacitors x3, miniature regulator", 5000.00)
tech_hero.use_super_tools()
print(tech_hero)


class Vehicle:
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f"{self.name} is moving in a general way.")

class Car(Vehicle):
    def move(self):
        print(f"{self.name} is driving 🚗.")

class Plane(Vehicle):
    def move(self):
        print(f"{self.name} is flying ✈️.")

class Boat(Vehicle):
    def move(self):
        print(f"{self.name} is sailing ⛵.")

# Create a list of different vehicles
vehicles = [
    Car("SinoTrunk"),
    Plane("Boeing 747"),
    Boat("Sailboat"),
    Car("Discovery"),
    Plane("Cessna")
]

# Iterate through the list and call the move() method on each object
for vehicle in vehicles:
    vehicle.move()