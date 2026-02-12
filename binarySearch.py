import json
class Student:
    def __init__(self, id, name, gpa):
        self.id = id
        self.name = name
        self.gpa = gpa
    def print_details(self):
        print("ID: " + str(self.id))
        print("Name: " + str(self.name))
        print(f"GPA: {self.gpa:.2f}")

def binary_search(data, name):
    low = 0
    high = len(data) - 1
    comparisons = 0

    while low <= high:
        mid = (low + high) // 2
        comparisons += 1

        if data[mid].name == name:
            print(f"Found {name} at index {mid}")
            data[mid].print_details()
            print(f"Comparisons times: {comparisons}")
            return
        
        elif data[mid].name < name:
            low = mid + 1
        else:
            high = mid - 1
    
    print(f"{name} does not exist.")
    print(f"Comparisons times: {comparisons}")

json_input = input()
data_list = json.loads(json_input)

students = []
for item in data_list:
    students.append(Student(item["id"], item["name"], item["gpa"]))

search_name = input()
binary_search(students, search_name)
