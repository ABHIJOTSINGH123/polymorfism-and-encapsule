class cat:
    def __init__(self, name, color, breed,age):
        self.name = name
        self.color = color
        self.breed = breed
        self.age=age
    def info(self):
        print(f"Iam a cat.My name is{self.name} and my color is{self.color} and My breed is{self.breed}.My age is{self.age}.")
    def make_sound(self):
        print("Meow")
class dog:
    def __init__(self, name, color, breed,age):
        self.name = name
        self.color = color
        self.breed = breed
        self.age=age
    def info(self):
        print(f"I am a dog. My name is{self.name} and my color is{self.color} and My breed is{self.breed}. My age is{self.age}.")
    def make_sound(self):
        print("Woof")
cat1=cat(
    "TOM","white","persian cat",5
)
dog1=dog(
    "Max","black","german shepherd",7
)
for animal in(cat1,dog1):
    animal.info()
    animal.make_sound()
   
