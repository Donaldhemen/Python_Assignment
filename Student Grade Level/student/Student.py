class Student:
    def __init__(self, name:str, grade_level:int):
        self.name = name
        self.grade_level = grade_level
    def introduce(self):
        return f"My name is {self.name}, I am in grade {self.grade_level}"

    def promote(self):
        if self.grade_level < 12:
            self.grade_level += 1

    def has_passed(self, score:int):
        return score >= 50

    def update_name(self, new_name:str):
        self.name = new_name


    def is_graduating(self):
        return self.grade_level == 12