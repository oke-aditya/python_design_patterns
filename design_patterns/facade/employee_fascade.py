from facade.employee_repository import EmployeeRepositry


class EmployeeFacade:
    employee_repository = EmployeeRepositry()

    # We just probably need 1 method so we expose only that
    def get_employee_details(self):
        return self.employee_repository.get_employee_details()
