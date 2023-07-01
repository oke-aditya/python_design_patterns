from builder.director import Director

if __name__ == "__main__":
    d = Director()
    eng_student = d.create_engineering_student()
    print(eng_student.name, eng_student.roll_no, eng_student.age)
