employee={
    "101":"Ravi",
    "102":"Anjali"
}

employee["103"]="Kiran"

print(employee)

employee["102"]="Priya"
print(employee)

del employee["101"]

print("Updated Dictionary:")
print(employee)
