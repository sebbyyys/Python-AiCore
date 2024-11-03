# TODO - Create a class called `Person`, then define it's constructor (the `__init__` method)
from datetime import datetime

class Person:
    def __init__(self, name, date_of_birth, friends):
        self.name = name
        self.date_of_birth = date_of_birth
        self.friends = friends if friends is not None else []
        
    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Date of Birth: {self.date_of_birth}\n"
                f"Number of Friends: {len(self.friends)}")

    def __gt__(self, other):
        self_birth = datetime.strptime(self.date_of_birth, '%d-%m-%Y')
        other_birth = datetime.strptime(other.date_of_birth, '%d-%m-%Y')
        if self_birth < other_birth:
            return(f"{self.name} is older than {other.name}")
        else:
            return(f"{other.name} is older than {self.name}")
        
    def add_friend(self, other_person):
        if other_person not in self.friends:
            self.friends.append(other_person)
            
        if self not in other_person.friends:
            other_person.friends.append(self)
            
            print(f"{self.name} and {other_person.name} are now friends!")
            
    def remove_friend(self, other):
        if other in self.friends:
            self.friends.remove(other)
            
        if self in other.friends:
            other.friends.remove(self)
            
            print(f"{self.name} and {other.name} are no longer friends!")
        
            

# Test the implementation
# Create people
person_1 = Person("Will", "03-04-1998", [])
person_2 = Person("Jane", "15-08-1995", [])
person_3 = Person("Alex", "20-12-1999", [])
        
# Test adding friends
print("\nInitial state:")
print(f"{person_1.name}'s friend count: {len(person_1.friends)}")
print(f"{person_2.name}'s friend count: {len(person_2.friends)}")

print("\nAdding friendship between Will and Jane:")
person_1.add_friend(person_2)
print(f"{person_1.name}'s friend count: {len(person_1.friends)}")
print(f"{person_2.name}'s friend count: {len(person_2.friends)}")

print("\nAdding friendship between Will and Alex:")
person_1.add_friend(person_3)
print(f"{person_1.name}'s friend count: {len(person_1.friends)}")
print(f"{person_3.name}'s friend count: {len(person_3.friends)}")

print("\nRemoving friendship between Will and Alex:")
person_1.remove_friend(person_3)
print(f"{person_1.name}'s friend count: {len(person_1.friends)}")
print(f"{person_3.name}'s friend count: {len(person_3.friends)}")

# Verify bidirectional relationship
print("\nVerifying bidirectional relationships:")
print(f"Is {person_2.name} in {person_1.name}'s friends list?: {person_2 in person_1.friends}")
print(f"Is {person_1.name} in {person_2.name}'s friends list?: {person_1 in person_2.friends}")
print(f"Is {person_1.name} in {person_3.name}'s friends list?: {person_1 in person_3.friends}")