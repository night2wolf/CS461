classes = ["CS101A", "CS101B", "CS201A", "CS201B", "CS191A", "CS191B", "CS291B",
           "CS291A", "CS303", "CS341", "CS449", "CS461"]
class_size = [40,25,30,30,60,20,40,20,50,40,55,40]
times = ['10A', '11A', '12P', '1P', '2P', '3P', '4P']
# Note: May need to do some string manipulation to get only the building and exclude room #
locations = ['Haag301', 'Haag206', 'Royall204', 'Katz209',
             'Flarsheim310', 'Flarsheim260', 'Bloch0009']
location_size = [70,30,70,50,80,25,30]
# Note: May need external logic to evaluate if a teacher can teach a class
instructors = ['Hare', 'Bingham', 'Kuhail', 'Mitchell', 'Rao']
# Lazy method
Hare_classes = ['CS101A', 'CS101B', 'CS201A', 'CS201B',
                'CS291A', 'CS291B', 'CS303', 'CS449', 'CS461']
Bingham_classes = ['CS101A', 'CS101B', 'CS201A', 'CS201B',
                   'CS191A', 'CS191B', 'CS291A', 'CS291B', 'CS449']
Kuhail_classes = ['CS303', 'CS341']
Mitchell_classes = ['CS191A', 'CS191B', 'CS291A', 'CS291B', 'CS303', 'CS341']
Rao_classes = ['CS291A', 'CS291B', 'CS303', 'CS341', 'CS461']

# Note: When generating schedules iterate through the classes list and assign an attribute for all,
#  Then evaluate with fitness function with the entire list of "Schedule" Objects.


class Schedule():
    def __init__(self, clas,class_size, time, instructor, location,location_size,violations):
        self.clas = clas
        self.class_size = class_size
        self.time = time
        self.instructor = instructor
        self.location = location
        self.location_size = location_size
        self.violations = violations
