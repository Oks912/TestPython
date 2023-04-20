class Organization:

    def __init__(self, name:str=None, location:str=None, area:str=None, employees:str=None, department:str=None):
        self.name = name
        self.location = location
        self.area = area
        self.employees = employees
        self.department = department


    @classmethod
    def generate_employees(cls, employees, department):
        return cls(None, None, None, employees, department)


new_empl = Organization.generate_employees("Oksana", "IT")
print(new_empl.employees)
print(new_empl.department)
