

class PermaDict(dict):

    def __init__(self,*args,silent=False,**kwargs):
        super().__init__(*args,**kwargs)
        self.silent = silent
    
    def __setitem__(self,key,value):
        sentinel = object()
        quick_check = self.get(key,sentinel)
        if quick_check != sentinel: 
            if not self.silent: raise KeyError(f"'{key}' already in dictionary.")
        else:
            super().__setitem__(key,value)
    
    def __getitem__(self,key):
        return super().__getitem__(key)

    def update(self,*args,force=False,**kwargs):
        if force:
            super().update(*args,**kwargs)
        else:
            if len(args)>0:
                items = args[0]
                if isinstance(items,dict):
                    items = items.items()
                for key,value in items:
                    self[key]= value
            else:
                for key,value in kwargs.items():
                    self[key]= value 

    def force_set(self,key,value):
        super().__setitem__(key,value)


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
