def unique_houses(filename):
    """TODO: Create a set of student houses.

    Iterates over the cohort_data.txt file to look for all of the included house names
    and creates a set called 'houses' that holds those names.

        ex. houses = set([ "Hufflepuff", 
                    "Slytherin", 
                    "Ravenclaw", 
                    "Gryffindor", 
                    "Dumbledore's Army"
            ])
    
    """

    houses = set()

    cohort_data = open(filename)
    for line in cohort_data:
        student_data = line.rstrip().split("|")
        houses.add(student_data[2])

    return houses


def sort_by_cohort(filename):
    """TODO: Sort students by cohort.

    Iterates over the data to create a list for each cohort, ordering students
    alphabetically by first name and tas separately. Returns list of lists.

        ex. winter_15 = ["alice tsao", "amanda gilmore", "anne vetto", "..." ]
        ex. all_students = [winter_15, spring_15, tas]
    
    """

#    all_students = []
#    winter_15 = []
    spring_15 = []
    tas = []
    all_student_info = []

    cohort_data = open(filename)
    
    for line in cohort_data:
        person_data = line.rstrip().split("|")
        if person_data[4] == "Spring 2015":
            spring_15.append(person_data[0] + " " + person_data[1])

        all_student_info.append(person_data) # created to iterate over in the list comprehension

    #practice list comprehension
    winter_15 = [student[0] + " " + student[1] for student in all_student_info if student[4] == "Winter 2015"]   
    tas = [student[0] + " " + student[1] for student in all_student_info if student[3] == "" and student[4] != ""]
    all_students = [winter_15, spring_15, tas]
    return all_students

def students_by_house(filename):
    """TODO: Sort students by house.

    Iterate over the data to create a list for each house, and sort students
    into their appropriate houses by last name. Sort TAs into a list called "tas".
    Return all lists in one list of lists.
        ex. hufflepuff = ["Gaikwad", "Wiedl", "..." ]
        ex. tas = ["Bryant", "Lefevre", "..."]
        ex. houses_tas = [ hufflepuff, 
                        gryffindor, 
                        ravenclaw, 
                        slytherin, 
                        dumbledores_army, 
                        tas 
            ]
    """

    all_students = []
    gryffindor = []
    hufflepuff = []
    slytherin = []
    dumbledores_army = []
    ravenclaw = []
    tas = []

    student_data = open(filename)
    for line in student_data:
        student_line_split = line.rstrip().split("|")
        if student_line_split[3] == "" and student_line_split[4] != "":
            tas.append(student_line_split[1])
        elif student_line_split[3] != "" and student_line_split[2] == "Gryffindor":
            gryffindor.append(student_line_split[1])
        elif student_line_split[3] != "" and student_line_split[2] == "Hufflepuff":
            hufflepuff.append(student_line_split[1])
        elif student_line_split[3] != "" and student_line_split[2] == "Slytherin":
            slytherin.append(student_line_split[1])
        elif student_line_split[3] != "" and student_line_split[2] == "Ravenclaw":
            ravenclaw.append(student_line_split[1])
        elif student_line_split[3] != "" and student_line_split[2] == "Dumbledore's Army":
            dumbledores_army.append(student_line_split[1])

    
    houses_tas = [gryffindor, hufflepuff, slytherin, ravenclaw, dumbledores_army, tas,]
    house_names = ['Gryffindor', 'Hufflepuff', 'Slytherin', "Dumbledore's Army", 'Ravenclaw', 'TAs']
    i = 0
    for house in houses_tas:
        house.sort()
        print str(house_names[i]) + ":", house
        i += 1

    all_students = [gryffindor, hufflepuff, slytherin, dumbledores_army, ravenclaw, tas]

    return all_students
    


def all_students_tuple_list(filename):
    """TODO: Create a list of tuples of student data.

    Iterates over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)
        ex. all_people = [
                ("Alice Tsao", "Slytherin", "Kristen", "Winter 2015"),
                ("Amanda Gilmore", "Hufflepuff", "Meggie", "Winter 2015"),
                # ...
            ]
    """

    student_list = []

    student_data = open(filename)

    for line in student_data:
        student_data_split = line.rstrip().split('|')
        st_name = student_data_split[0] + " " + student_data_split[1]
        student_info = [st_name, student_data_split[2], student_data_split[3], student_data_split[4]]
        student_tuple = tuple(student_info)
        # student_info = (st_name,student_data_split[2], student_data_split[3], student_data_split[4])        
        student_list.append(student_tuple)


    #print student_list
    return student_list


def find_cohort_by_student_name(student_list):
    """TODO: Given full name, return student's cohort.

    Use the above list of tuples generated by the preceding function to make a small
    function that, given a first and last name, returns that student's cohort, or returns
    'Student not found.' when appropriate. """

    wanted_student = raw_input("Please enter a student's name: ")

    student_names = []

    for student_tuple in student_list:
        student_names.append(student_tuple[0])

    if wanted_student in student_names:
        print student_list[student_names.index(wanted_student)][3]
        return student_list[student_names.index(wanted_student)][3]
        # for student_tuple in student_list:
        #     if student_tuple[0] == wanted_student:
        #         print student_tuple[3]
    else:
        print "Student not found."
        return "Student not found"


find_cohort_by_student_name(all_students_tuple_list('cohort_data.txt'))

##########################################################################################
# Further Study Questions


def find_name_duplicates(filename):
    """TODO: Using set operations, make a set of student first names that have duplicates.

    Iterates over the data to find any first names that exist across multiple cohorts. 
    Uses set operations (set math) to create a set of these names. 
    NOTE: Do not include staff -- or do, if you want a greater challenge. 

       ex. duplicate_names = set(["Sarah", "Nicole"])

    """

    duplicate_names = set()

    # Code goes here

    return duplicate_names


def find_house_members_by_student_name(student_list):
    """TODO: Create a function that, when given a name, returns everyone in
    their house that's in their cohort.

    Use the list of tuples generated by all_students_tuple_list to make a small function that,
    when given a student's first and last name, returns students that are in both that
    student's cohort and that student's house."""

    # Code goes here

    return

all_students_tuple_list('cohort_data.txt')