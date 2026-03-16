class add:
     def __init__(self, a,b):
        self.a = b
        self.b = b
        
     def addition(self):
        print(self.a +self.b)
    
        
class multi:
     def __init__(self, c,d):
        self.c = c
        self.d = d
        
     def multiply(self):
        print(self.c *self.d)
        
class both(add, multi):
    def __init__(self e,f):
          
      super(). __init__(self e,f)
    self.e = e
    self .f =f
        
        
I = both(2,3)
print(both.addition())