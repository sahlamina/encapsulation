# basic class of earphones
class Earphones:
    def __init__(self, name, brand):
        self.name = name
        self._brand = brand
    # basic methods fot earphone class
    def on(self):
        print(self.name + " turned on.")

    def off(self):
        print(self.name + " turned off.")

    def connect(self):
        print(self.name + " are connected")

    def disconnect(self):
        print(self.name + " are disconnected")

    def display_info(self):
        print(self.name)
        print(self._brand)

# i can call all my attributes and methods here with the single underscore
# airpods = Earphones("Airpods", "Apple")
# airpods.on()
# airpods.display_info()
# print(airpods._brand)

# new class to test how the dunder will affect the class
class Airpods_Pro:
    def __init__(self, name, brand):
        self.name = name
        self.__brand = brand

    def display_info_one(self):
        print(self.name)
        print(self.__brand)


airpodspro = Airpods_Pro("AirPodsPro", "Apple")
airpodspro.display_info_one()

# cant access this variable from outside the class
print(airpodspro.__brand)
