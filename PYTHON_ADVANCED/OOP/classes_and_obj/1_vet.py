class Vet:

    animals = []
    space = 5

    def __init__(self, name) -> str:
        self.name = name
        self.animal_name = []

    
    def register_animal(self, animal):
        if Vet.space > len(Vet.animals): 

            self.animal_name.append(animal)
            Vet.animals.append(animal)
        
            return f"{animal} registered in the clinic"
        
        return 'Not enough space'
    
    def unregister_animal(self, animal):
        if animal in self.animals:
            Vet.animals.remove(animal)
            self.animal_name.remove(animal)

            return f"{animal} unregistered successfully"
        return f"{animal} not in the clinic"
    
    def info(self):
        return f"{self.name} has {len(self.animal_name)} animals. {Vet.space - len(Vet.animals)} space left in clinic"
import unittest


class Tests(unittest.TestCase):
    def test_init(self):
        vet = Vet("Bob")
        Vet.animals = []
        Vet.space = 5
        self.assertEqual(vet.name, "Bob")
        self.assertEqual(vet.animals, [])
        self.assertEqual(Vet.animals, [])
        self.assertEqual(Vet.space, 5)

    def test_register_successfull(self):
        vet = Vet("Bob")
        Vet.animals = []
        Vet.space = 5
        vet2 = Vet("Peter")
        res = vet.register_animal("Doggy")
        self.assertEqual(res, "Doggy registered in the clinic")
        self.assertEqual(vet.animals, ["Doggy"])
        self.assertEqual(vet.animals, ["Doggy"])
        self.assertEqual(vet2.animals, [])

    def test_register_unsuccessfull(self):
        vet = Vet("Bob")
        Vet.animals = []
        Vet.space = 5
        for i in range(6):
            vet.register_animal(str(i))
        res = vet.register_animal("Doggy")
        self.assertEqual(res, "Not enough space")
        self.assertEqual(len(Vet.animals), 5)
        self.assertEqual(len(vet.animals), 5)

    def test_unregister_successfull(self):
        vet = Vet("Bob")
        Vet.animals = []
        Vet.space = 5
        vet.register_animal("Kitty")
        res = vet.unregister_animal("Kitty")
        self.assertEqual(res, "Kitty unregistered successfully")
        self.assertEqual(vet.animals, [])
        self.assertEqual(Vet.animals, [])


if __name__ == "__main__":
    unittest.main()