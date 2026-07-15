def student_details(**kwargs):
    print("Student Details:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")


student_details(name="Sai", age=21, branch="CSE", college="Aditya Engineering College")