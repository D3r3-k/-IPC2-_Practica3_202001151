class Mascota:
    def __init__(self, raza:str, edad:str):
        self.raza = raza
        self.edad = edad

class Perro(Mascota):
    def __init__(self, raza:str, edad:str):
        super().__init__(raza, edad)

class Gato(Mascota):
    def __init__(self, raza:str, edad:str):
        super().__init__(raza, edad)

class Conejo(Mascota):
    def __init__(self, raza:str, edad:str):
        super().__init__(raza, edad)