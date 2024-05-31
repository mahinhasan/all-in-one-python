class Dog:
    species = "Canis Familiaris"

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def speak(self,sound):
        return f"{self.name} says {sound}"


buddy = Dog("Buddy",5)
print(buddy.speak("woof"))