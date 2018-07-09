class Employee(object):
    def __init__(self, new_name, new_job_title, new_start_date):
        self.name = new_name
        self.job_title = new_job_title
        self.start_date = new_start_date
    def getName(self):
        return self.name
    def getJobTitle(self):
        return self.job_title
    def getStartDate(self):
        return self.start_date
    def setName(self, new_name):
        self.name = new_name
    def setJobTitle(self, new_job_title):
        self.job_title = new_job_title
    def setStartDate(self, new_start_date):
        self.start_date = new_start_date
        




class Company(object):
    """This represents a company in which people work"""

    def __init__(self, company_name, date_founded):
        self.company_name = company_name
        self.date_founded = date_founded
        self.employees_retained = set()

    def get_company_name(self):
        """Returns the name of the company"""

        return self.company_name

    def addEmplyee(self, newEmployee):
        self.employees_retained.add(newEmployee)

    def getEmployees(self):
        return self.employees_retained

    # Add the remaining methods to fill the requirements above


mike = Employee("Mike", "Manager", "Oct 3rd")

GM = Company("General Motors", "Sometime")

GM.addEmplyee(mike)
print(GM.getEmployees())