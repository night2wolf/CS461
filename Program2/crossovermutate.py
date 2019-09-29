import fitness
import data
import random


def l2normalize(scores, generation):
    # L2 Normalization
    total = 0
    topscore = 0
    scoretotal = 0
    for i in range(len(scores)):
        scoretotal = scoretotal + scores[i]
        total = total + (scores[i]*scores[i])
        if scores[i] > topscore:
            topscore = scores[i]
            topchild = i
    average = scoretotal / len(scores)
    l2normal = []
    for i in range(len(scores)):
        l2normal.append(scores[i]*scores[i]/total)
    l2distrib = []
    l2verify = 0
    for i in range(len(l2normal)):
        l2verify = l2verify + l2normal[i]
        l2distrib.append(l2verify)
    return topchild,topscore, average, l2distrib


def create_child(l2distrib, generation):
    # Pick parents
    # pick random number between 0 and 1
    prob1 = random.uniform(0, 1)
    prob2 = random.uniform(0, 1)
    picked1 = -1
    picked2 = -1

    # lookup that # in probability distribution
    for i in range(len(l2distrib)):
        if prob1 > l2distrib[i-1] and prob1 <= l2distrib[i]:
            picked1 = i
        if prob2 > l2distrib[i-1] and prob2 <= l2distrib[i]:
            picked2 = i

    # set aside as parent #1,
    parent1 = generation[picked1]
    # repeat for parent #2
    parent2 = generation[picked2]

    # Crossover
    split1 = random.randint(0, 11)
    split2 = 12 - split1
    child = []
    for i in range(split1):
        # add split 1 of parent1 to child
        child.append(parent1[i])
    for i in range(split2):
        # Add split 2 of parent2 to child
        child.append(parent2[i+split1])

    # Mutation
    for i in range(len(child)):
        mutate = random.randint(1, 100)
        if mutate == 1:
            child[i].time = random.choice(data.times)
        mutate = random.randint(1, 100)
        if mutate == 1:
            child[i].instructor = random.choice(data.instructors)
        mutate = random.randint(1, 100)
        if mutate == 1:
            child[i].location = random.choice(data.locations)
            child[i].location_size = fitness.determine_location_size(
                child[i].location)
    return child
