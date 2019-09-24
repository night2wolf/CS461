import random
import data
import fitness

#sch = fitness.create_schedule()
# for i in range(len(sch)):
#    print(str(sch[i].clas) + " : " + str(sch[i].instructor) + '\n')
#score = fitness.fitness_evaluate(sch)
# print(str(score))
# Create a generation of 1000 random schedules and evaluate
generation_size = 1000
generation = []
scores = []
for i in range(generation_size):
    schedule = fitness.create_schedule()
    generation.append(schedule)
    scores.append(fitness.fitness_evaluate(schedule))

print(str(scores))
# L2 Normalization
total = 0
for i in range(len(scores)):
    total = total + (scores[i]*scores[i])
l2normal = []
for i in range(len(scores)):
    l2normal.append(scores[i]*scores[i]/total)
print(str(l2normal))
l2verify = 0
for i in range(len(l2normal)):
    l2verify = l2verify + l2normal[i]
print(str(l2verify))


# Pick parents
# pick random number between 0 and 1
prob1 = random.uniform(0, 1)
prob2 = random.uniform(0, 1)

# lookup that # in probability distribution
for i in range(len(l2normal)):
    if prob1 >= l2normal[i] and prob1 <= l2normal[i+1]:
        picked1 = i
picked2 = 5

# set aside as parent #1,
parent1 = generation[picked1]
# repeat for parent #2
parent2 = generation[picked2]


# Crossover
split1 = random.randint(0, 11)
split2 = 11 - split1
child = []
for i in range(split1):
    # add split 1 of parent1 to child
    child.append(parent1[i])
for i in range(split2):
    # Add split 2 of parent2 to child
    child.append(parent2[i+split1])

# Mutation
