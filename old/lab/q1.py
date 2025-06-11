class student():
    def __init__(self,name,roll_number,marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks
    
    def display(self):
        print(f"Name: {self.name}\nRoll Number: {self.roll_number}\nMarks: {self.marks}")

A = student("Nigga_Slayer","2024eeb1196","69")

A.display()