# L2 Normalization: Calculate Fitness score -> Square it ->
#    divide by sum of all classes -> generate cumulative probability
"""
Assess the fitness function as follows:
For each course that is taught by an instructor who can teach it: +3
For each course that is the only course scheduled in that room at that time: +5
For each course that is in a room large enough to accommodate it: +5
Room capacity is no more than twice the expected enrollment: +2
For each course that does not have the same instructor teaching another course at the same time: +5
For each schedule that has the same instructor teaching more than 4 courses: -5 per course over 4
For each schedule that has Rao or Mitchell (graduate faculty)
teaching more courses than Hare or Bingham: -5% to total fitness score. (Same number of courses is OK.)

CS 101 and CS 191 are usually taken the same semester; the same applies to CS 201 and CS 291.
Therefore apply these rules to those pairs of courses:
Courses are scheduled for same time: -10% to score
Courses are scheduled for adjacent times: +5% to score
if these courses are scheduled for adjacent times, and are in the same building: +5 points
"""
import data
import random

#Create a Random Schedule using all the classes
def create_schedule():
    random_schedule = []
    for i in range(len(data.classes)):
        class_schedule = data.Schedule
        class_schedule.clas = data.classes[i]
        class_schedule.time = random.choice(data.times)
        class_schedule.instructor = random.choice(data.instructors)
        class_schedule.location = random.choice(data.locations)
        random_schedule.append(class_schedule)
        print(str(class_schedule.clas) + " : " + 
              str(class_schedule.time) + " : " + 
              str(class_schedule.instructor) + " : " + 
              str(class_schedule.location) + '\n')
    return random_schedule
def fitness_evaluate(schedule):
    score = 0
    # For each course that is taught by an instructor who can teach it: +3
    for i in range(len(schedule)):
        print(str(schedule[i].clas) + " : " + str(schedule[i].instructor) + '\n' + str(score))
        for j in range(len(data.Hare_classes)):
            if schedule[i].clas == data.Hare_classes[j] and schedule[i].instructor == "Hare":
                score = score + 3
                """
        for k in range(len(data.Bingham_classes)):
            if schedule[i].clas == data.Bingham_classes[k]:
                score = score + 3
        for l in range(len(data.Kuhail_classes)):
            if schedule[i].clas == data.Kuhail_classes[l]:
                score = score + 3
        for m in range(len(data.Mitchell_classes)):
            if schedule[i].clas == data.Mitchell_classes[m]:
                score = score + 3
        for n in range(len(data.Rao_classes)):
            if schedule[i].clas == data.Rao_classes[n]:
                score = score + 3
        """
    # For each course that is the only course scheduled in that room at that time: +5

    # For each course that is in a room large enough to accommodate it: +5

    # Room capacity is no more than twice the expected enrollment: +2

    # For each course that does not have the same instructor teaching another course at the same time: +5

    # For each schedule that has the same instructor teaching more than 4 courses: -5 per course over 4

    # For each schedule that has Rao or Mitchell(graduate faculty) teaching more courses than Hare or Bingham: -5 % to total fitness score. (Same number of courses is OK.)

    return score
sch = create_schedule()
print(str(sch[0].clas) + " : " + str(sch[0].instructor) + '\n')
print(str(sch[1].clas) + " : " + str(sch[1].instructor) + '\n')
print(str(sch[2].clas) + " : " + str(sch[2].instructor) + '\n')
#for i in range(len(sch)):
#    print(str(sch[i].clas) + " : " + str(sch[i].instructor) + '\n')
#score = fitness_evaluate(sch)
#print(str(score))
"""
# Create a generation of 1000 random schedules 
generation = []
for i in range(1000):
    yeet = create_schedule()
    generation.append(yeet)
print(str(generation))    
"""
