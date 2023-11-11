employee_list = []

print("----------------------------")
print("        員工薪資輸入        ")
print("    若姓名處未輸入則代表結束")
print("----------------------------")

while True:
    name = input("請輸入姓名:")

    if not name:
        break

    salary = input("請輸入薪資:")

    salary = int(salary)

    employee = {"eName": name, "eSalary": salary}
    employee_list.append(employee)

print("----------------------------")

total_salary = 0
for employee in employee_list:
    print(f"員工{employee['eName']} 的薪資為 {employee['eSalary']:,.0f}")
    total_salary += employee['eSalary']

average_salary = total_salary / len(employee_list) if len(employee_list) > 0 else 0
print("----------------------------")
print(f"合計薪資：{total_salary: >15,.0f}")
print(f"平均薪資：{average_salary: >15,.2f}")
print("============================")