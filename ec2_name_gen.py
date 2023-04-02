"""
Python code to generate a random EC2 name for set depts
Johnny Mac - 02 Apr 2023
"""
import random
import string

# need a little function to handle 'FinOps' and variations as an input.
# the two capital letters are otherwise tricky to handle in string comparisons!
def format_department(dept):
  if dept.lower() == "finops":
    return "FinOps"
  else:
    dept.lower()  
    return dept.title()

def main():

  allowed_departments = ["Accounting", "FinOps", "Marketing"]

  department = input("Enter your department (Accounting, FinOps or Marketing ONLY): ")
  department = department.strip()
  
  # call our function to format the user input in case user enters all lower
  # case or random capital letters for an approved department name
  department = format_department(department)
  
  if department not in allowed_departments:
    print("You are not authorized to use this application. Please contact your administrator.")
    return

  try:
    num_instances = int(input("Enter the number of EC2 instances you want names for: "))
  except ValueError:
    print("Invalid input. Please enter a valid number.")
    return

  include_department = input("Do you want to include the department name in the instance name? (y/n): ").lower()
  while include_department not in ["y", "n"]:
    print("Invalid input. Please enter 'y' or 'n'.")
    include_department = input("Do you want to include the department name in the instance name? (y/n): ").lower()

  generated_names = set()

  while len(generated_names) < num_instances:
    unique_name = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    if include_department == "y":
      unique_name = f"{department}_{unique_name}"
      generated_names.add(unique_name)

  print("\nGenerated instance names:")
  for name in generated_names:
    print(name)
      
if __name__ == "__main__":
    main()
    