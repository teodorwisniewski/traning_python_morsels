
class NonNegativeIntegerParameters:

    def __init__(self,default=0):
        self.default = default

    def __get__(self,instance,default):
        return self.default
    
    def __set__(self,instance,value):
        
        if value<0: raise AttributeError(f"The value that you introduced {value} cannot be negative ")
        self.default = value


class ElectricalMachine:

    #descriptors
    power = NonNegativeIntegerParameters(0)

    def __init__(self, power,poles,phases,frequency):

        self.power = power
        self.poles = poles
        self.phases = phases
        self.frequency = frequency       
    
if __name__ == "__main__":

    machine_a = ElectricalMachine(12,2,3,50)
    print(f"here are value of power {machine_a.power}")
    machine_a.power = 50
    print(f"here are value of power {machine_a.power}")
    try:
        machine_a.power = -50
    except:
        print("Woops, negative value")
    machine_b = ElectricalMachine(1000,2,3,50)    
    print(f"here are value of power {machine_b.power}")
    machine_b.power = 33
    print(f"here are value of power {machine_b.power}")
    print(f"here are value of power {machine_a.power}")