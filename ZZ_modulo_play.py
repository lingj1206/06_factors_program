keep_going = ""
while keep_going == "":
    num_lollies = int(input("how many lollies? "))
    num_students = int(input("How many students? "))
    
    lollies_per_student = num_lollies // num_students
    lollies_left = num_lollies % num_students

    if lollies_left == 1:
        lolly_pl = "lolly"
    else:
        lolly_pl = "lollies"

    print()
    print("You have {} lollies and {} students".format(num_lollies, num_students))
    print("Each student gets {} lollies".format(lollies_per_student))
    print("You have {} left".format(lollies_left))
    print()
    
    keep_going = input ("Again <enter>")
    print()