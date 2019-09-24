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

def determine_location_size(location):
    location_size = 0
    if location == 'Haag301':
        location_size = 70
    if location == 'Haag206':
        location_size = 30
    if location == 'Royall204':
        location_size = 70
    if location == 'Katz209':
        location_size = 50
    if location == 'Flarsheim310':
        location_size = 80
    if location == 'Flarsheim260':
        location_size = 25
    if location == 'Bloch0009':
        location_size = 30                
    return location_size

#Create a Random Schedule using all the classes
def create_schedule():
    random_schedule = []
    for i in range(len(data.classes)):
        location = random.choice(data.locations)
        class_schedule = data.Schedule(data.classes[i],data.class_size[i],random.choice(data.times),random.choice(data.instructors),location,determine_location_size(location))
        random_schedule.append(class_schedule)
        """
        print(str(class_schedule.clas) + " : " + 
              str(class_schedule.class_size) + " : " +  
              str(class_schedule.time) + " : " + 
              str(class_schedule.instructor) + " : " + 
              str(class_schedule.location) + " : " +
              str(class_schedule.location_size))
        """
    return random_schedule
def fitness_evaluate(schedule):
    score = 0
    Hare_counter = 0
    Bingham_counter = 0
    Kuhail_counter = 0
    Mitchell_counter = 0
    Rao_counter = 0
    # For each course that is taught by an instructor who can teach it: +3
    for i in range(len(schedule)):        
        for j in range(len(data.Hare_classes)):
            if schedule[i].clas == data.Hare_classes[j] and schedule[i].instructor == "Hare":
                score = score + 3
        for k in range(len(data.Bingham_classes)):
            if schedule[i].clas == data.Bingham_classes[k] and schedule[k].instructor == "Bingham":
                score = score + 3
        for l in range(len(data.Kuhail_classes)):
            if schedule[i].clas == data.Kuhail_classes[l] and schedule[l].instructor == "Kuhail":
                score = score + 3
        for m in range(len(data.Mitchell_classes)):
            if schedule[i].clas == data.Mitchell_classes[m] and schedule[m].instructor == "Mitchell":
                score = score + 3
        for n in range(len(data.Rao_classes)):
            if schedule[i].clas == data.Rao_classes[n] and schedule[n].instructor == "Rao":
                score = score + 3        
        # For each course that is the only course scheduled in that room at that time: +5
        counter = 0
        for j in range(len(schedule)):
            if schedule[i].time == schedule[j].time and schedule[i].location == schedule[j].location:
                # count each instance of a conflict
                counter = counter + 1                
        # If the counter is only 1 that means it is by itself and we give a reward
        if counter == 1:
            score = score + 5     
        """         
        # For each course that is in a room large enough to accommodate it: +5
        Haag 301 (70), Haag 206 (30), Royall 204 (70), Katz 209 (50),
        Flarsheim 310 (80), Flarsheim 260 (25), Bloch 0009 (30)
        """
        if schedule[i].location_size >= schedule[i].class_size:
            score = score + 5
        """
        # Room capacity is no more than twice the expected enrollment: +2
        CS 101A (40), CS 101B (25), CS 201A (30), CS 201B (30), CS 191A (60),
        CS 191B (20), CS 291B (40), CS 291A (20), CS 303 (50), CS 341 (40), CS 449 (55), CS 461 (40).
        """
        enrollment = schedule[i].class_size * 2
        if enrollment >= schedule[i].location_size:
            score = score +2
        # For each course that does not have the same instructor teaching another course at the same time: +5
        counter = 0
        for j in range(len(schedule)):
            if schedule[i].time == schedule[j].time and schedule[i].instructor == schedule[j].instructor:
                # count each instance of a conflict
                counter = counter + 1
        # If the counter is only 1 that means it is by itself and we give a reward
        if counter == 1:
            score = score + 5
        # Keep a running count of who is teaching
        if schedule[i].instructor == "Hare" :
            Hare_counter = Hare_counter + 1
        if schedule[i].instructor == "Bingham" :
            Bingham_counter = Bingham_counter + 1
        if schedule[i].instructor == "Kuhail":
            Kuhail_counter = Kuhail_counter + 1
        if schedule[i].instructor == "Mitchell" :
            Mitchell_counter = Mitchell_counter + 1
        if schedule[i].instructor == "Rao":
            Rao_counter = Rao_counter + 1    
           
    # For each schedule that has the same instructor teaching more than 4 courses: -5 per course over 4
    if Hare_counter > 4:
        score = score - (5*(Hare_counter-4))
    if Bingham_counter > 4:
        score = score - (5*(Bingham_counter-4))
    if Kuhail_counter > 4:
        score = score - (5*(Kuhail_counter-4))
    if Mitchell_counter > 4:
        score = score - (5*(Mitchell_counter-4))
    if Rao_counter > 4:
        score = score - (5*(Rao_counter-4))
    
    # For each schedule that has Rao or Mitchell(graduate faculty) teaching more courses than Hare or Bingham: -5 % to total fitness score. (Same number of courses is OK.)
    Mitchell_Rao_courses = Mitchell_counter + Rao_counter
    Hare_Bingham_courses = Hare_counter + Bingham_counter    
    if Mitchell_Rao_courses > Hare_Bingham_courses:
        score = score * .95

    return score

"""    
sch = create_schedule()
#for i in range(len(sch)):
#    print(str(sch[i].clas) + " : " + str(sch[i].instructor) + '\n')
score = fitness_evaluate(sch)
print(str(score))
"""

