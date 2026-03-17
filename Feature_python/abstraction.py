from abc import ABC, abstractmethod
class government():
    def __init__(self, shop_name_application):
        self.application = shop_name_application
        
        
    @abstractmethod
    def get_license(self):
        pass
    
    