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
        class_schedule = data.Schedule(data.classes[i],random.choice(data.times),random.choice(data.instructors),random.choice(data.locations))
        random_schedule.append(class_schedule)
        print(str(class_schedule.clas) + " : " + 
              str(class_schedule.time) + " : " + 
              str(class_schedule.instructor) + " : " + 
              str(class_schedule.location))
    return random_schedule
def fitness_evaluate(schedule):
    score = 0
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
    
        # Room capacity is no more than twice the expected enrollment: +2
        """
        # For each course that does not have the same instructor teaching another course at the same time: +5
        counter = 0
        for j in range(len(schedule)):
            if schedule[i].time == schedule[j].time and schedule[i].instructor == schedule[j].instructor:
                # count each instance of a conflict
                counter = counter + 1
        # If the counter is only 1 that means it is by itself and we give a reward
        if counter == 1:
            score = score + 5
    
    # For each schedule that has the same instructor teaching more than 4 courses: -5 per course over 4
    
    """
    # For each schedule that has Rao or Mitchell(graduate faculty) teaching more courses than Hare or Bingham: -5 % to total fitness score. (Same number of courses is OK.)
    """
    return score
sch = create_schedule()
#for i in range(len(sch)):
#    print(str(sch[i].clas) + " : " + str(sch[i].instructor) + '\n')
score = fitness_evaluate(sch)
print(str(score))

# Create a generation of 1000 random schedules 
"""
generation = []
for i in range(1000):
    yeet = create_schedule()
    generation.append(yeet)
print(str(generation))    
"""
