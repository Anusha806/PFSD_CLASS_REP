
#3rd programe
'''
class BankAccount:
    def __init__(self,accountNumber,name,balance):
        self.accountNumber=accountNumber
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"Deposit of Rs.{amount} successful.")
        else:
            print("Invalid deposit amount.")
    def withdrawal(self,amount):
        if 0<amount<=self.balance:
            self.balance-=amount
            print(f"Withdrawal of Rs.{amount} successful.")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def bank_fees(self):
        fees=0.05*self.balance
        self.balance-=fees
        print(f"Bank fees of Rs. {fees} applied.")
    def display(self):
        print(f"Account Number: {self.accountNumber}")
        print(f"Account Holder: {self.name}")
        print(f"balance : Rs. {self.balance}")

account1=BankAccount(accountNumber=123456,name="John Doe",balance=1000)
account1.display()
account1.deposit(500)
account1.withdrawal(200)
account1.bank_fees()
account1.display()
'''


#1st program
'''
class py_solution:
    def sub_sets(self, sset):
        return self.subsetsRecur([], sorted(sset))    
    def subsetsRecur(self, current, sset):
        if sset:
            return self.subsetsRecur(current, sset[1:]) + self.subsetsRecur(current + [sset[0]], sset[1:])
        return [current]
for name in py_solution.__dict__:
    print(name)
'''

#2rd programe

class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

    def display_attributes(self):
        print("Attributes and their values:")
        print(f"Student ID: {self.student_id}")
        print(f"Student Name: {self.student_name}")
        print(f"Student Class: {self.student_class}")

    def remove_attribute(self, attribute_name):
        if hasattr(self, attribute_name):
            delattr(self, attribute_name)
            print(f"\nAttribute '{attribute_name}' removed.")

# Create an instance of the Student class
student_instance = Student(student_id=1, student_name="John Doe")

# Add a new attribute
student_instance.student_class = "Class 10"

# Display all attributes and their values
student_instance.display_attributes()

# Remove the student_name attribute
student_instance.remove_attribute("student_name")

# Display the remaining attributes and their values
student_instance.display_attributes()
