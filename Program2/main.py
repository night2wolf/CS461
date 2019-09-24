import random
import data
import fitness
import crossovermutate
# Create a generation of 1000 random schedules and evaluate

generation_size = 1000
generation = []
scores = []
for i in range(generation_size):
    schedule = fitness.create_schedule()
    generation.append(schedule)
    scores.append(fitness.fitness_evaluate(schedule))
topchild, averagechild, distribution = crossovermutate.l2normalize(
    scores, generation)
new_gen = []
for i in range(generation_size):
    new_gen.append(crossovermutate.create_child(distribution, generation))
running_best = topchild
running_average = averagechild
print("Best Child of generation: " + str(running_best))
print("Average Child of Generation: " + str(running_average))

counter = 0
while counter < 3:
    gen_score = []
    for i in range(len(new_gen)):
        gen_score.append(fitness.fitness_evaluate(new_gen[i]))
    topchild, averagechild, distribution = crossovermutate.l2normalize(
        gen_score, new_gen)
    running_best = topchild
    running_average = averagechild
    print("Best Child of generation: " + str(running_best))
    print("Average Child of Generation: " + str(running_average))
    next_gen = []
    for i in range(len(new_gen)):
        next_gen.append(crossovermutate.create_child(distribution, new_gen))
