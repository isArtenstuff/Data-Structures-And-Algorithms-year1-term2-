class Student:
    def __init__(self, id, name, gpa):
        self.id = id
        self.name = name
        self.gpa = gpa
    def print_details(self):
        print("ID: " + str(self.id))
        print("Name: " + str(self.name))
        print(f"GPA: {self.gpa:.2f}")

class ProbHash:
    def __init__(self, size: int):
        self.size = size
        self.hash_table = [None] * size
    
    def hash(self, key):
        return key % self.size
    
    def rehash(self, hkey):
        return (hkey + 1) % self.size
    
    def insert_data(self, student):
        index = self.hash(student.id)
        count = 0
        while self.hash_table[index] is not None:
            index = self.rehash(index)
            count += 1
            if count == self.size:
                print(f"The list is full. {student.id} could not be inserted.")
                return
        print(f"Insert {student.id} at index {index}")
        self.hash_table[index] = student
    
    def search_data(self, std_id):
        index = self.hash(std_id)
        count = 0
        while count <= self.size:
            if self.hash_table[index] is not None and self.hash_table[index].id == std_id:
                print(f"Found {std_id} at index {index}")
                self.hash_table[index].print_details()
                return
            index = self.rehash(index)
            count += 1
        print(f"{std_id} does not exist.")
