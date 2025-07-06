# Creating a class.
class PythonSwitch():
    def main_function(self, name_of_day):
        default = "Incorrect name of day"
        method_name = 'day_' + str(name_of_day)
        method = getattr(self, method_name, lambda: default())
        return method()
    
    def day_1(self):
        return "Sunday"
    def day_2(self):
        return "Monday"
    def day_3(self):
        return "Tuesday"
    def day_4(self):
        return "Wednesday"
    def day_5(self):
        return "Thursday"
    def day_6(self):
        return "Friday"
    def day_7(self):
        return "Saturday"

# Creating an object of class.
my_switch = PythonSwitch()
print(my_switch.main_function(1)) # Calling function with passing argument value.
print(my_switch.main_function(3)) # Calling function.
