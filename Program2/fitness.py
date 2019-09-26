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
        class_schedule = data.Schedule(data.classes[i],data.class_size[i],random.choice(data.times),random.choice(data.instructors),location,determine_location_size(location), [])
        random_schedule.append(class_schedule)

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
        # For each course that is in a room large enough to accommodate it: +5
        if schedule[i].location_size >= schedule[i].class_size:
            score = score + 5
       # Room capacity is no more than twice the expected enrollment: +2
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
        schedule[11].violations.append("Hare teaching too many courses")
    if Bingham_counter > 4:
        score = score - (5*(Bingham_counter-4))
        schedule[11].violations.append("Bingham teaching too many courses")
    if Kuhail_counter > 4:
        score = score - (5*(Kuhail_counter-4))
        schedule[11].violations.append("Kuhail teaching too many courses")
    if Mitchell_counter > 4:
        score = score - (5*(Mitchell_counter-4))
        schedule[11].violations.append("Mitchell teaching too many courses")
    if Rao_counter > 4:
        score = score - (5*(Rao_counter-4))
        schedule[11].violations.append("Rao teaching too many courses")
    
    # For each schedule that has Rao or Mitchell(graduate faculty) teaching more courses than Hare or Bingham: -5 % to total fitness score. (Same number of courses is OK.)
    Mitchell_Rao_courses = Mitchell_counter + Rao_counter
    Hare_Bingham_courses = Hare_counter + Bingham_counter    
    if Mitchell_Rao_courses > Hare_Bingham_courses:
        score = score * .95
    """
    CS 101 and CS 191 are usually taken the same semester; the same applies to CS 201 and CS 291.
    Therefore apply these rules to those pairs of courses:
    Courses are scheduled for same time: -10% to score
    Courses are scheduled for adjacent times: +5% to score
    if these courses are scheduled for adjacent times, and are in the same building: +5 points
    Are both on the quad (Haag, Royall, Flarsheim):
    no modification
    1 is in Katz and the other isn’t: -3%
    1 is in Bloch and the other isn’t: -3%
    (Yes, if one’s in Katz and the other’s in Bloch, that’s -6%)
    """
    # since we know specifically the index of these classes we can use it to our advantage:
    # CS 101A [0] CS 101B [1], CS191A [4], CS191B[5],CS201A[2],CS101B[3],CS291B[6],CS291A[7]
    # Check if scheduled at same time
    if schedule[0].time == schedule[4].time:
        score = score * .90
    if schedule[0].time == schedule[5].time:
        score = score * .90
    if schedule[1].time == schedule[4].time:
        score = score * .90
    if schedule[1].time == schedule[5].time:
        score = score * .90    
    if schedule[2].time == schedule[6].time:
        score = score * .90
    if schedule[2].time == schedule[7].time:
        score = score * .90
    if schedule[3].time == schedule[6].time:
        score = score * .90
    if schedule[3].time == schedule[7].time:
        score = score * .90
    # Check if scheduled in Katz or Bloch   for 101 and 191  
    if schedule[0].location == 'Katz209' and schedule[4].location != 'Katz209':
        score = score * .97
    if schedule[0].location == 'Katz209' and schedule[5].location != 'Katz209':
        score = score * .97
    if schedule[1].location == 'Katz209' and schedule[4].location != 'Katz209':
        score = score * .97
    if schedule[1].location == 'Katz209' and schedule[5].location != 'Katz209':
        score = score * .97
    if schedule[4].location == 'Katz209' and schedule[0].location != 'Katz209':
        score = score * .97
    if schedule[4].location == 'Katz209' and schedule[1].location != 'Katz209':
        score = score * .97
    if schedule[5].location == 'Katz209' and schedule[0].location != 'Katz209':
        score = score * .97
    if schedule[5].location == 'Katz209' and schedule[1].location != 'Katz209':
        score = score * .97
    if schedule[0].location == 'Bloch0009' and schedule[4].location != 'Bloch0009':
        score = score * .97
    if schedule[0].location == 'Bloch0009' and schedule[5].location != 'Bloch0009':
        score = score * .97
    if schedule[1].location == 'Bloch0009' and schedule[4].location != 'Bloch0009':
        score = score * .97
    if schedule[1].location == 'Bloch0009' and schedule[5].location != 'Bloch0009':
        score = score * .97
    if schedule[4].location == 'Bloch0009' and schedule[0].location != 'Bloch0009':
        score = score * .97
    if schedule[4].location == 'Bloch0009' and schedule[1].location != 'Bloch0009':
        score = score * .97
    if schedule[5].location == 'Bloch0009' and schedule[0].location != 'Bloch0009':
        score = score * .97
    if schedule[5].location == 'Bloch0009' and schedule[1].location != 'Bloch0009':
        score = score * .97
    # Check if scheduled in Katz or Bloch   for 201 and 291
    if schedule[2].location == 'Katz209' and schedule[6].location != 'Katz209':
        score = score * .97
    if schedule[2].location == 'Katz209' and schedule[7].location != 'Katz209':
        score = score * .97
    if schedule[3].location == 'Katz209' and schedule[6].location != 'Katz209':
        score = score * .97
    if schedule[3].location == 'Katz209' and schedule[7].location != 'Katz209':
        score = score * .97
    if schedule[6].location == 'Katz209' and schedule[2].location != 'Katz209':
        score = score * .97
    if schedule[6].location == 'Katz209' and schedule[3].location != 'Katz209':
        score = score * .97
    if schedule[7].location == 'Katz209' and schedule[2].location != 'Katz209':
        score = score * .97
    if schedule[7].location == 'Katz209' and schedule[3].location != 'Katz209':
        score = score * .97
    if schedule[2].location == 'Bloch0009' and schedule[6].location != 'Bloch0009':
        score = score * .97
    if schedule[2].location == 'Bloch0009' and schedule[7].location != 'Bloch0009':
        score = score * .97
    if schedule[3].location == 'Bloch0009' and schedule[6].location != 'Bloch0009':
        score = score * .97
    if schedule[3].location == 'Bloch0009' and schedule[7].location != 'Bloch0009':
        score = score * .97
    if schedule[6].location == 'Bloch0009' and schedule[2].location != 'Bloch0009':
        score = score * .97
    if schedule[6].location == 'Bloch0009' and schedule[2].location != 'Bloch0009':
        score = score * .97
    if schedule[7].location == 'Bloch0009' and schedule[3].location != 'Bloch0009':
        score = score * .97
    if schedule[7].location == 'Bloch0009' and schedule[3].location != 'Bloch0009':
        score = score * .97
    # Courses are scheduled for adjacent times: +5% to score
    # if these courses are scheduled for adjacent times, and are in the same building: +5 points
    # CS 101A [0] CS 101B [1], CS191A [4], CS191B[5],CS201A[2],CS201B[3],CS291B[6],CS291A[7]
    # Check if scheduled adjacent for 101A and 191A
    for i in range(len(data.times)):
        if i-1 == -1:
            if schedule[0].time == data.times[i] and schedule[4].time == data.times[i+1]:
                score = score * 1.05
                if schedule[0].location == schedule[4].location:
                    score = score +5
                if schedule[0].location[0:3] == 'Haag' and schedule[4].location[0:3] == 'Haag':
                    score = score +5
                if schedule[0].location[0:8] == 'Flarsheim' and schedule[4].location[0:8] == 'Flarsheim':
                    score = score + 5
        if i+1 == 7:
            if schedule[0].time == data.times[i] and schedule[4].time == data.times[i-1]:
                score = score * 1.05
                if schedule[0].location == schedule[4].location:
                    score = score +5
                if schedule[0].location[0:3] == 'Haag' and schedule[4].location[0:3] == 'Haag':
                    score = score + 5
                if schedule[0].location[0:8] == 'Flarsheim' and schedule[4].location[0:8] == 'Flarsheim':
                    score = score + 5
        else:
            if schedule[0].time == data.times[i] and (schedule[4].time == data.times[i-1] or schedule[4].time == data.times[i+1]):
                score = score * 1.05
                if schedule[0].location == schedule[4].location:
                    score = score +5
                if schedule[0].location[0:3] == 'Haag' and schedule[4].location[0:3] == 'Haag':
                    score = score + 5
                if schedule[0].location[0:8] == 'Flarsheim' and schedule[4].location[0:8] == 'Flarsheim':
                    score = score + 5
    # Check if scheduled adjacent for 101A and 191B
    for i in range(len(data.times)):
        if i-1 == -1:
            if schedule[0].time == data.times[i] and schedule[5].time == data.times[i+1]:
                score = score * 1.05
                if schedule[0].location == schedule[5].location:
                    score = score +5
                if schedule[0].location[0:3] == 'Haag' and schedule[5].location[0:3] == 'Haag':
                    score = score +5
                if schedule[0].location[0:8] == 'Flarsheim' and schedule[5].location[0:8] == 'Flarsheim':
                    score = score + 5
        if i+1 == 7:
            if schedule[0].time == data.times[i] and schedule[5].time == data.times[i-1]:
                score = score * 1.05
                if schedule[0].location == schedule[5].location:
                    score = score +5
                if schedule[0].location[0:3] == 'Haag' and schedule[5].location[0:3] == 'Haag':
                    score = score + 5
                if schedule[0].location[0:8] == 'Flarsheim' and schedule[5].location[0:8] == 'Flarsheim':
                    score = score + 5
        else:
            if schedule[0].time == data.times[i] and (schedule[5].time == data.times[i-1] or schedule[5].time == data.times[i+1]):
                score = score * 1.05
                if schedule[0].location == schedule[5].location:
                    score = score +5
                if schedule[0].location[0:3] == 'Haag' and schedule[5].location[0:3] == 'Haag':
                    score = score + 5
                if schedule[0].location[0:8] == 'Flarsheim' and schedule[5].location[0:8] == 'Flarsheim':
                    score = score + 5
    # Check if scheduled adjacent for 101B and 191A                    
    for i in range(len(data.times)):
        if i-1 == -1:
            if schedule[1].time == data.times[i] and schedule[4].time == data.times[i+1]:
                score = score * 1.05
                if schedule[1].location == schedule[4].location:
                    score = score +5
                if schedule[1].location[0:3] == 'Haag' and schedule[4].location[0:3] == 'Haag':
                    score = score +5
                if schedule[1].location[0:8] == 'Flarsheim' and schedule[4].location[0:8] == 'Flarsheim':
                    score = score + 5
        if i+1 == 7:
            if schedule[1].time == data.times[i] and schedule[4].time == data.times[i-1]:
                score = score * 1.05
                if schedule[1].location == schedule[4].location:
                    score = score +5
                if schedule[1].location[0:3] == 'Haag' and schedule[4].location[0:3] == 'Haag':
                    score = score + 5
                if schedule[1].location[0:8] == 'Flarsheim' and schedule[4].location[0:8] == 'Flarsheim':
                    score = score + 5
        else:
            if schedule[1].time == data.times[i] and (schedule[4].time == data.times[i-1] or schedule[4].time == data.times[i+1]):
                score = score * 1.05
                if schedule[1].location == schedule[4].location:
                    score = score +5
                if schedule[1].location[0:3] == 'Haag' and schedule[4].location[0:3] == 'Haag':
                    score = score + 5
                if schedule[1].location[0:8] == 'Flarsheim' and schedule[4].location[0:8] == 'Flarsheim':
                    score = score + 5
    # Check if scheduled adjacent for 101B and 191B
    for i in range(len(data.times)):
        if i-1 == -1:
            if schedule[1].time == data.times[i] and schedule[5].time == data.times[i+1]:
                score = score * 1.05
                if schedule[1].location == schedule[5].location:
                    score = score +5
                if schedule[1].location[0:3] == 'Haag' and schedule[5].location[0:3] == 'Haag':
                    score = score +5
                if schedule[1].location[0:8] == 'Flarsheim' and schedule[5].location[0:8] == 'Flarsheim':
                    score = score + 5
        if i+1 == 7:
            if schedule[1].time == data.times[i] and schedule[5].time == data.times[i-1]:
                score = score * 1.05
                if schedule[1].location == schedule[5].location:
                    score = score +5
                if schedule[1].location[0:3] == 'Haag' and schedule[5].location[0:3] == 'Haag':
                    score = score + 5
                if schedule[1].location[0:8] == 'Flarsheim' and schedule[5].location[0:8] == 'Flarsheim':
                    score = score + 5
        else:
            if schedule[1].time == data.times[i] and (schedule[5].time == data.times[i-1] or schedule[5].time == data.times[i+1]):
                score = score * 1.05
                if schedule[1].location == schedule[5].location:
                    score = score +5
                if schedule[1].location[0:3] == 'Haag' and schedule[5].location[0:3] == 'Haag':
                    score = score + 5
                if schedule[1].location[0:8] == 'Flarsheim' and schedule[5].location[0:8] == 'Flarsheim':
                    score = score + 5
    # Check if scheduled adjacent for 201A and 291A
    for i in range(len(data.times)):
        if i-1 == -1:
            if schedule[2].time == data.times[i] and schedule[6].time == data.times[i+1]:
                score = score * 1.05
                if schedule[2].location == schedule[6].location:
                    score = score +5
                if schedule[2].location[0:3] == 'Haag' and schedule[6].location[0:3] == 'Haag':
                    score = score +5
                if schedule[2].location[0:8] == 'Flarsheim' and schedule[6].location[0:8] == 'Flarsheim':
                    score = score + 5
        if i+1 == 7:
            if schedule[2].time == data.times[i] and schedule[6].time == data.times[i-1]:
                score = score * 1.05
                if schedule[2].location == schedule[6].location:
                    score = score +5
                if schedule[2].location[0:3] == 'Haag' and schedule[6].location[0:3] == 'Haag':
                    score = score + 5
                if schedule[2].location[0:8] == 'Flarsheim' and schedule[6].location[0:8] == 'Flarsheim':
                    score = score + 5
        else:
            if schedule[2].time == data.times[i] and (schedule[6].time == data.times[i-1] or schedule[6].time == data.times[i+1]):
                score = score * 1.05
                if schedule[2].location == schedule[6].location:
                    score = score +5
                if schedule[2].location[0:3] == 'Haag' and schedule[6].location[0:3] == 'Haag':
                    score = score + 5
                if schedule[2].location[0:8] == 'Flarsheim' and schedule[6].location[0:8] == 'Flarsheim':
                    score = score + 5
    # Check if scheduled adjacent for 201A and 291B
    for i in range(len(data.times)):
        if i-1 == -1:
            if schedule[2].time == data.times[i] and schedule[7].time == data.times[i+1]:
                score = score * 1.05
                if schedule[2].location == schedule[7].location:
                    score = score +5
                if schedule[2].location[0:3] == 'Haag' and schedule[7].location[0:3] == 'Haag':
                    score = score +5
                if schedule[2].location[0:8] == 'Flarsheim' and schedule[7].location[0:8] == 'Flarsheim':
                    score = score + 5
        if i+1 == 7:
            if schedule[2].time == data.times[i] and schedule[7].time == data.times[i-1]:
                score = score * 1.05
                if schedule[2].location == schedule[7].location:
                    score = score +5
                if schedule[2].location[0:3] == 'Haag' and schedule[7].location[0:3] == 'Haag':
                    score = score + 5
                if schedule[2].location[0:8] == 'Flarsheim' and schedule[7].location[0:8] == 'Flarsheim':
                    score = score + 5
        else:
            if schedule[2].time == data.times[i] and (schedule[7].time == data.times[i-1] or schedule[7].time == data.times[i+1]):
                score = score * 1.05
                if schedule[2].location == schedule[7].location:
                    score = score +5
                if schedule[2].location[0:3] == 'Haag' and schedule[7].location[0:3] == 'Haag':
                    score = score + 5
                if schedule[2].location[0:8] == 'Flarsheim' and schedule[7].location[0:8] == 'Flarsheim':
                    score = score + 5
    # Check if scheduled adjacent for 201B and 291A                
    for i in range(len(data.times)):
        if i-1 == -1:
            if schedule[3].time == data.times[i] and schedule[6].time == data.times[i+1]:
                score = score * 1.05
                if schedule[3].location == schedule[6].location:
                    score = score +5
                if schedule[3].location[0:3] == 'Haag' and schedule[6].location[0:3] == 'Haag':
                    score = score +5
                if schedule[3].location[0:8] == 'Flarsheim' and schedule[6].location[0:8] == 'Flarsheim':
                    score = score + 5
        if i+1 == 7:
            if schedule[3].time == data.times[i] and schedule[6].time == data.times[i-1]:
                score = score * 1.05
                if schedule[3].location == schedule[6].location:
                    score = score +5
                if schedule[3].location[0:3] == 'Haag' and schedule[6].location[0:3] == 'Haag':
                    score = score + 5
                if schedule[3].location[0:8] == 'Flarsheim' and schedule[6].location[0:8] == 'Flarsheim':
                    score = score + 5
        else:
            if schedule[3].time == data.times[i] and (schedule[6].time == data.times[i-1] or schedule[6].time == data.times[i+1]):
                score = score * 1.05
                if schedule[3].location == schedule[6].location:
                    score = score +5
                if schedule[3].location[0:3] == 'Haag' and schedule[6].location[0:3] == 'Haag':
                    score = score + 5
                if schedule[3].location[0:8] == 'Flarsheim' and schedule[6].location[0:8] == 'Flarsheim':
                    score = score + 5
    # Check if scheduled adjacent for 201B and 291B
    for i in range(len(data.times)):
        if i-1 == -1:
            if schedule[3].time == data.times[i] and schedule[7].time == data.times[i+1]:
                score = score * 1.05
                if schedule[3].location == schedule[7].location:
                    score = score + 5
                if schedule[3].location[0:3] == 'Haag' and schedule[7].location[0:3] == 'Haag':
                    score = score + 5
                if schedule[3].location[0:8] == 'Flarsheim' and schedule[7].location[0:8] == 'Flarsheim':
                    score = score + 5
        if i+1 == 7:
            if schedule[3].time == data.times[i] and schedule[7].time == data.times[i-1]:
                score = score * 1.05
                if schedule[3].location == schedule[7].location:
                    score = score + 5
                if schedule[3].location[0:3] == 'Haag' and schedule[7].location[0:3] == 'Haag':
                    score = score + 5
                if schedule[3].location[0:8] == 'Flarsheim' and schedule[7].location[0:8] == 'Flarsheim':
                    score = score + 5
        else:
            if schedule[3].time == data.times[i] and (schedule[7].time == data.times[i-1] or schedule[7].time == data.times[i+1]):
                score = score * 1.05
                if schedule[3].location == schedule[7].location:
                    score = score + 5
                if schedule[3].location[0:3] == 'Haag' and schedule[7].location[0:3] == 'Haag':
                    score = score + 5
                if schedule[3].location[0:8] == 'Flarsheim' and schedule[7].location[0:8] == 'Flarsheim':
                    score = score + 5

    return score


