'''
_ Requirements .. 
- Company System :
    - create company
    - create sections for company
    -add employees to sections 
    - get all employees in section 
    - add raise to employee 
    - add deduction to employee 
    - get employee byy year in section
    - get sum of salaries in section
    - get company salaries
    - get employee avg salaries in section
    - get all company employees avg salaries
    - get all company salaries
    - get employees byy section
    - get all employees avg salaries
'''

'''
- Requirements analysis ...
- Company Stem :
    - Company class :
        - create company
        - create section for company 
        - get sum of salaries in company
        - get all employees avg salaries
        - get all company salaries
        - get all employees in company
        - get employees by section
        - get all employees avg salaries

    - Section class :
        - add employee
        - get all employees in section
        - get all sections avg salaries
        - get sum of salaries in section
        - get employee by year in section
        - get sections salaries

    - Employee class :
        - create employee
        - add salary raise for employee 
        - add salary deduction for employee 
'''

class Company:
    # create company
    def __init__(self,name):
        self.name = name
        self.sections = []

    # create section for company
    def add_section_to_company(self,section):
        self.sections.append(section) 

    # get all company sections
    def get_all_company_sections(self):
        return [section.name for section in self.sections]
     
    # get avg salary by section 
    def get_avg_salary_by_section(self):
        return {section.name:section.get_avg_section_salary() for section in self.sections}

    # get all employees avg salaries
    def get_avg_salary_all_employees(self):
        all_employees_salaries = [employee.salary for section in self.sections for employee in section.employees]
        return sum(all_employees_salaries)/len(all_employees_salaries)


    # get all employees in company
    def get_all_company_employees(self):
        all_employees = []
        for section in self.sections:
            all_employees.extend([employee.name for employee in section.get_employees_in_section()])
        return all_employees 
    
    # get employees byy section
    def get_employees_by_section(self):
        return {section.name:[f"{employee.name} : {employee.salary}" for employee in section.get_employees_in_section()] for section in self.sections}


class Section:
    # create section 
    def __init__(self,name):
        self.name = name
        self.employees = []
    
    # add employee
    def add_employee_to_section(self,employee):
        self.employees.append(employee)

    # get all employees in section
    def get_employees_in_section(self):
        return [e for e in self.employees]

    # get sum of salaries in section
    def get_sum_section_salaries(self):
        all_section_salaries = [employee.salary for employee in self.employees]
        return sum(all_section_salaries)
    
    # get all sections avg salaries
    def get_avg_section_salary(self):
        all_section_salaries = [employee.salary for employee in self.employees]
        return sum(all_section_salaries)/len(all_section_salaries)

    # get sections salaries
    def get_sections_salaries(self):
        return [employee.salary for employee in self.get_employees_in_section()]

class Employee:
    # create employee
    def __init__(self,name,salary,start_year):
        self.name = name
        self.salary = salary
        self.start_tear = start_year
        self.raise_amount = 0
        self.deduction_amount = 0

    # add salary raise for employee 
    def apply_raise(self,amount):
        self.salary += amount
        self.raise_amount += amount

    # add salary deduction for employee
    def apply_deduction(self,amount):
        self.salary -= amount
        self.deduction_amount += amount




# create company
CodeIt = Company("CodeIt") 

#create section
HR = Section("HR") 
CodeIt.add_section_to_company(HR) #  add section to company

# create employees
Omar = Employee("omar",1300,2020) 
Nohha = Employee("noha",1100,2021)
Ahmed = Employee("ahmed",1200,2022)

# add employees ins section
HR.add_employee_to_section(Omar)
HR.add_employee_to_section(Nohha)
HR.add_employee_to_section(Ahmed)

Programmers = Section("Programmers")
CodeIt.add_section_to_company(Programmers)
 
Mohamed = Employee("mohamed",1500,2020)
Sara = Employee("sara",1200,2021)
Ali = Employee("ali",1100,2022)
Programmers.add_employee_to_section(Mohamed)
Programmers.add_employee_to_section(Sara)
Programmers.add_employee_to_section(Ali)

# print(CodeIt.get_employees_by_section())
# Nohha.apply_deduction(70)
# Ahmed.apply_deduction(100)
# Omar.apply_raise(50)

# print(CodeIt.get_employees_by_section())

# print(HR.get_sum_section_salaries())

print(HR.get_sections_salaries())

# print(CodeIt.get_avg_salary_all_employees())
# print(CodeIt.get_avg_salary_by_section())

# print(Programmers.get_section_salaries())
# print(HR.get_avg_section_salary())

# print(CodeIt.get_employees_by_section())
# print(CodeIt.get_all_company_employees())
# print(CodeIt.get_all_company_employees())
# print(Section.get_employees_in_section(Programmers))
# print(CodeIt.get_all_company_sections())
# print(HR.employees)
# print(Programmers.employees)