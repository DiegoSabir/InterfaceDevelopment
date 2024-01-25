"""
Store the names of 8 employees of a company and their salaries in two tuples, respectively. Then:
1. Display the tuple of names and the tuple of salaries.
2. Display the names of the employees with the highest and lowest salaries.
"""

employees = ("Diego", "Pablo", "Ivan", "Roberto", "Fran", "Angel", "David", "Marcos")
salaries = (1000, 1200, 900, 1500, 1100, 1300, 950, 1400)

print("Employee Names:", employees)
print("Employee Salaries:", salaries)

maxSalary = salaries.index(max(salaries))
employeeWithMaxSalary = employees[maxSalary]

minSalary = salaries.index(min(salaries))
employeeWithMinSalary = employees[minSalary]

print("Employee with the highest salary:", employeeWithMaxSalary, " = ", maxSalary, "€")
print("Employee with the lowest salary:", employeeWithMinSalary, " = ", minSalary, "€")
