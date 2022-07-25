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
    