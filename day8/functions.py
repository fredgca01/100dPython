def greet():
    print("Hello")
    print("How are you ?")

def greet_with_name(name, location):
    print(f"Hello {name}")
    print(f"Welcome in {location}")

greet()
greet_with_name("Fred", "Paris")
greet_with_name(location="New york", name="Vincent")