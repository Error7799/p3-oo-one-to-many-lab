class Pet:
    
    all = []
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    
    
    def __init__(self, name, pet_type, owner = None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"{pet_type} is a invalid pet type it has to be one of these {Pet.PET_TYPES}")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        
        Pet.all.append(self)

class Owner:
    def __init__(self, name):
        self.name = name
        
    def pets(self):
        return[pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise Exception(f"{pet} is a invalid pet type")
    
    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)
            
        pass
         