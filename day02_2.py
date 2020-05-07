class person:
    name: str
    surname: str
    age: int

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
    def info(self):
        print(f"{self.name} {self.surname} {self.age}")
    def sya_as(self, message):
        return f"< {self.name}> {message}"

class user(person):
    passw: str

    def chk_pas(self, user_pass):
        return self.passw == user_pass

user = user("L","A",35)
user.passw = 123
user.info()

print(user.chk_pas(123))