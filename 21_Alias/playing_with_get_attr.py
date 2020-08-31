


class Jeep:

    hp = 300
    model = "Wrangler"

print(getattr(Jeep,'model',"ellooo"))
print(getattr(Jeep,'unknown_parameter',None))
print(Jeep.costqm)
print("The end")