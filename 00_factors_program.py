from distutils.command.build_scripts import first_line_re


def statement_generator(text, decoration):

    ends = decoration * 5

    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()
    
    return ""

def instructions():

    statement_generator("Instructions / Information", "=")
    print()
    print("Please choosea data type (image / text / integer)")
    print()
    print("this program assumes that images are being represented in 24bit colour (ie: 24 bits per pixel). For text, we assume that ascii encoding is being used (8 bits per character).")
    print()
    print("complete as many calculations as necessary, pressing <enter> at the end of each calculation or any key to quit.")
    print()

    return ""

def num_check(question, low):
    valid = False
    while not valid:

        error = ("Please enter a number that is more than (or equal to) {} without a decimal point".format(low))

        try:

            response = int(input(question))
            
            if response >= low:
                return response

            else:
                print(error)
                print()
        
        except ValueError:
            print(error)


statement_generator("Factors Calculator", "`")
first_time = input("Press <enter> to see th instructions or any key to continue.")
if first_time == "":
    instructions()

keep_going = ""
while keep_going == "":

    comment = ""

    var_to_factor = num_check("Number? ")

    if var_to_factor != 1:
        factor_list = get_factors(var_to_factor)
    else:
        factor_list = ""
        comment = "One is UNITY!  It only has one factor.  Itself :)"

    if len(factor_list) == 2:
        comment = "{} is a prime number.".format(var_to_factor)
    elif len(factor_list) % 2 ==1:
        comment = "{} is a perfect square".format(var_to_factor)

    if var_to_factor == 1:
        heading = "One is special..."
    
    else:
        heading = "Factors of {}".format(var_to_factor)

    statement_generator(heading, "*")
    print()
    print(factor_list)
    print(comment)
