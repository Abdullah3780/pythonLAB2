# Create a class Computer with properties: Brand Name, Speed,
# Memory Size. Constructor initialize these properties and
# show function display properties of and object. Call
# functions using object.
class Computer:
    Brand_Name = ''
    SpeedGHz = 0
    MemorySizeINGBs = 0

    def __init__(self):
        self.Brand_Name = 'IBM'
        self.SpeedGHz = 2.6
        self.MemorySizeINGBs = 500

    def showData(self):
        print("Brand Name : ", self.Brand_Name)
        print("Speed in GHz : ", self.SpeedGHz)
        print("Memory Size : ", self.MemorySizeINGBs)


compter1 = Computer()
compter1.showData()
