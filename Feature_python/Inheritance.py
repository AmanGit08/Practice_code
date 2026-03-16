class vechile:
    def __init__(self, year, manufacturer):
        self.year = year
        self.manufacturer = manufacturer
        
    def getcardetail(self):
        return self.year ,self.manufacturer
    
class suv(vechile):
    def __init__(self, vechicle_name, type_of_fuel, year, manufacturer):
        super(). __init__(year,manufacturer)#this is calling the constructor tof the parent class
        self.vechicle_name = vechicle_name
        self.type_of_fuel = type_of_fuel
        
    def getcardetail(self):
        return self.year ,self.manufacturer, self.vechicle_name, self.type_of_fuel
        
        
class child_of_suv(suv):
    def __init__(self,  Vechice_name, type_of_fuel, year, manufacturer):
        super().__init__(Vechice_name, type_of_fuel, year, manufacturer)
        

ins = child_of_suv("ABC", "CNG", 2026, "MARuti")
print(ins.getcardetail())
            
        
        
    