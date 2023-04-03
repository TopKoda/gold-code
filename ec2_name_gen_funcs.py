"""
Python code to generate a random EC2 name for set depts.
Have reworked previous ec2_name_gen.py script to demonstrate
functions, making the code more readable.

Johnny Mac - 03 Apr 2023
"""
import random
import string

"""
Start of functions
"""

# need a little function to handle 'FinOps' and variations as an input.
# the two capital letters are otherwise tricky to handle in string comparisons!
def format_department(dept):
  if dept.lower() == "finops":
    return "FinOps"
  else:
    dept.lower()
    return dept.title()

# get the user to input their department and call our function to format it
# so we can verify it's allowed. random accidental capital letters are accounted for.
def get_department():
  department = input("Enter your department (Accounting, FinOps or Marketing ONLY): ")
  department = department.strip()
  department = format_department(department)
  return department

# get the number of required EC2 instances from the user input.
def get_num_instances():
  try:
    num_instances = int(input("Enter the number of EC2 instances you want names for: "))
    return num_instances
  except ValueError:
    print("Invalid input. Please enter a valid number.")
    return None

# confirm if the user wants to include their department name in the EC2 instance name.
def get_include_department():
  include_department = input("Do you want to include the department name in the instance name? (y/n): ").lower()
  while include_department not in ["y", "n"]:
    print("Invalid input. Please enter 'y' or 'n'.")
    include_department = input("Do you want to include the department name in the instance name? (y/n): ").lower()
  return include_department

# generate the required number of unique EC2 instance names.
def generate_instance_names(department, num_instances, include_department):
  generated_names = set()

  while len(generated_names) < num_instances:
    unique_name = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    if include_department == "y":
      unique_name = f"{department}_{unique_name}"
    generated_names.add(unique_name)
  
  return generated_names

"""
End of functions
"""

def main():

  allowed_departments = ["Accounting", "FinOps", "Marketing"]

  department = get_department()

  if department not in allowed_departments:
    print("You are not authorized to use this application. Please contact your administrator.")
    return

  num_instances = get_num_instances()
  if num_instances is None:
    return

  include_department = get_include_department()

  generated_names = generate_instance_names(department, num_instances, include_department)

  print("\nGenerated instance names:")
  for name in generated_names:
    print(name)

if __name__ == "__main__":
    main()
