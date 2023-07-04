from prototype.student import Student

if __name__ == "__main__":
    st = Student(age=10, roll_no=12)

    st_clone = st.clone()

    print(st_clone.age)
    print(st_clone.roll_no)
    print(st_clone.school)


