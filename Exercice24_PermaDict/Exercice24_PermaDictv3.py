from collections import UserDict

class PermaDict(UserDict):
    
    def __init__(self,*args,silent=False,**kwargs):
        self.silent = silent
        super().__init__(*args,**kwargs)
        

    def __setitem__(self,key,value):
        if key in self and not self.silent:
            raise KeyError(f"'{key}' already in dictionary.")
        elif key not in self:
            super().__setitem__(key,value)
        
        
    def force_set(self,key,value):
          super().__setitem__(key,value)      

    def update(self,*args,force=False,**kwargs):
        
        if len(args)>0:
            iterations = args[0] if isinstance(args[0],list) else args[0].items()
            for key,value in iterations:
                if force is True: self.force_set(key,value)
                else: self[key] = value
        if len(kwargs)>0:
            for key,value in kwargs.items():
                if force is True: self.force_set(key,value)
                else: self[key] = value




if __name__ == "__main__":

    locations = PermaDict([('Kojo', "Houston"), ('Tracy', "Toronto")])
    list(locations)
    ['Kojo', 'Tracy']
    list(locations.keys())
    ['Kojo', 'Tracy']
    list(locations.values())
    ['Houston', 'Toronto']
    for name, place in locations.items():
        print(f"{name} in {place}")

    locations = PermaDict({'Trey': "San Diego", 'Al': "San Francisco"})
    locations['Harry'] = "London"
    locations.update({'Russell': "Perth", 'Katie': "Sydney"})
    print(locations['Trey'])
    try: 
        locations['Harry'] = "Amsterdam"
    except Exception as e :
        print(e)

    try:
        locations.update({'Al': "Warsaw"})
    except Exception as e :
        print(e)   

    try:
        locations.update(Al="Siema")
    except Exception as e :
        print(e)  

    try:
        locations.update(y = 3, z = 0)
    except Exception as e :
        print(e)   

    try:
        locations.update(y = 3, z = 0)
    except Exception as e :
        print(e)   


    

    locations = PermaDict({'David': "Boston"})
    locations.force_set('David', "Amsterdam")
    locations.force_set('Asheesh', "Boston")
    locations.force_set('Asheesh', "San Francisco")

    print(locations)

    locations = PermaDict({'David': "Boston"}, silent=True)
    locations['David'] = "Amsterdam"
    locations['Asheesh'] = "Boston"
    print(dict(locations))
    # {'David': 'Boston', 'Asheesh': 'Boston'}

    locations = PermaDict({'David': "Boston"})
    locations.update([('David', 'Amsterdam'), ('Asheesh', 'SF')], force=True)
    print(dict(locations))
    #{'David': 'Amsterdam', 'Asheesh': 'SF'}
