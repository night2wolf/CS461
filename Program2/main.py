import random
import data
import fitness
import crossovermutate
import copy
# Create a generation of 1000 random schedules and evaluate

generation_size = 1000
generation = []
scores = []
for i in range(generation_size):
    schedule = fitness.create_schedule()
    generation.append(schedule)
    scores.append(fitness.fitness_evaluate(schedule))
topchild, topscore, averagechild, distribution = crossovermutate.l2normalize(
    scores, generation)
best_child = generation[topchild]
new_gen = []
for i in range(generation_size):
    new_gen.append(crossovermutate.create_child(distribution, generation))
running_best = topscore
running_average = averagechild
print("Best Child of generation: " + str(running_best))
for i in range(len(best_child)):
    print(str(best_child[i].clas) + " : " + str(best_child[i].class_size) + " : " + str(best_child[i].time) + " : " +
          str(best_child[i].instructor) + " : " + str(best_child[i].location) + " : " + str(best_child[i].location_size))

print("Average Child of Generation: " + str(running_average) + '\n')

# Create Subsequent generations until we reach convergence
counter = 0
while counter < 3:
    gen_score = []
    # Evaluate generation
    for i in range(len(new_gen)):
        gen_score.append(fitness.fitness_evaluate(new_gen[i]))
    topchild, topscore, averagechild, distribution = crossovermutate.l2normalize(
        gen_score, new_gen)
    last_best = running_best
    # Set top score of all generations
    if topscore > running_best:
        running_best = topscore
        running_best_child = new_gen[topchild]
    best_child = new_gen[topchild]
    # Measure if we are only increasing by 0.2% else reset the counter
    if running_best <= 1.002 * last_best:
        counter = counter + 1
    else:
        counter = 0
    print("Best Child of generation: " + str(topscore))
    for i in range(len(best_child)):
        print(str(best_child[i].clas) + " : " + str(best_child[i].class_size) + " : " + str(best_child[i].time) + " : " +
              str(best_child[i].instructor) + " : " + str(best_child[i].location) + " : " + str(best_child[i].location_size))
    print("Average Child of Generation: " + str(averagechild) + '\n')
    # Create new generation
    last_gen = copy.deepcopy(new_gen)
    new_gen = []
    for i in range(len(last_gen)):
        new_gen.append(crossovermutate.create_child(distribution, last_gen))

print("Over all best Child with score: " + str(running_best))
for i in range(len(running_best_child)):
    print(str(running_best_child[i].clas) + " : " + str(running_best_child[i].class_size) + " : " + str(running_best_child[i].time) + " : " +
          str(running_best_child[i].instructor) + " : " + str(running_best_child[i].location) + " : " + str(running_best_child[i].location_size))
print('\n' + "Violation List : ")
a = fitness.eval_violations(running_best_child)
print(*a, sep="\n")
