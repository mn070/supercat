""" A program to select and breed bigger size maine coon cats """

import time
import random
import statistics


# Constants
target_weight = 500         # weights are in lbs
num_cats = 20               # Total number of adult cats can be held by the lab
min_weight = 8
max_weight = 30
common_weight = 20
mutate_odd = 0.01           # probability of a mutation in the lab
mutate_min = 0.5            # ratio of the undesired outcome 
mutate_max = 1.2            # ratio of the most mutated cat 
litter_size = 4
litter_annually = 3
generation_limit = 100 


# getting even number of cats for pairing
if num_cats % 2 != 0:
    num_cats += 1


# Itinialize the population
def populate(num_cats, min_weight, max_weight, common_weight):
    for i in range(num_cats):
        return [int(random.triangular(min_weight, max_weight, common_weight))]


# Grading: chosing the fitness of the cats based on the population's mean and the target
def fitness(population, target_weight):
    avge = statistics.mean(population)
    return avge/target_weight


# Select and store the cats that meet the target_weight
def select(population, to_keep):
    sorted_population = sorted(population)
    sorted_males_females = len(sorted_population)//2       # get the total of males and females population by dividing the sorted population 
    females = sorted_population[:sorted_males_females]
    males = sorted_population[sorted_males_females:]
    """ After dividing the sorted population, assume that females have the smaller weights than the males.
    --> females = first half of the sorted population and males are the second half """

    # Calculate the desired number of male and female cats to keep because the lab has a limit space (should be down to the num_cats value)
    to_keep_for_each_gender = to_keep//2

    # use the negative slicing to get the end of the two lists of females and males to get the biggest cats
    selected_females = females[-to_keep_for_each_gender:]
    selected_males = males[-to_keep_for_each_gender:]

    return selected_females, selected_males


# Next step is to breed the cats
def breed(selected_females, selected_males, litter_size):
    random.shuffle(selected_males)
    random.shuffle(selected_females)
    children = []
    for male, female in zip(selected_males, selected_females):
        for child in range(litter_size):
            child = random.randint(male, female)
            children.append(child)
    return children


# Look for children with mutation from the breeded children
def mutated_children(children, mutate_odd, mutate_min, mutate_max):
    for index, cat in enumerate(children):
        if mutate_odd >= random.random():
            children[index] = round(cat * random.uniform(mutate_min, mutate_max))
    
    return children


# Main function: displays important results and breaks the breeding program when the limit is reached - generational_limit = 500
def main():
    generations = 0
    parents = populate(num_cats, min_weight, max_weight, common_weight)
    print("Initial population weights: {}".format(parents))
    population_fitness = fitness(parents, target_weight)
    print("Initial population fitness: {}".format(population_fitness))
    print("Number of cats to keep: {}".format(num_cats))

    avge_weight = []

    while population_fitness < 1 and generations < generation_limit:
        selected_males, selected_females = select(parents, num_cats)
        children = breed(selected_males, selected_females, litter_size)
        children = mutated_children(children, mutate_odd, mutate_min, mutate_max)
        parents = selected_females + selected_males + children
        population_fitness = fitness(parents, target_weight)

        print("Generation {} fitness = {:.4f}".format(generations, population_fitness))

        avge_weight.append(int(statistics.mean(parents)))
        generations += 1
    
    print("Average weight per generation: {} lbs".format(avge_weight))
    print("\nNumber of generations: {}".format(generations))
    print("Number of years: {}".format(int(generations/litter_annually)))



if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    duration = end_time - start_time
    print("\nRuntime for this program was {} seconds.".format(duration))
 







    
