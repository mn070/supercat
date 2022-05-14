- Genetic algorithms: finding the best solution within criteria
- Unlike brute force, genetic algorithms don't try every possible solution

This project will use genetic algorithms to create a large population of giant cats (a new race of super cat)
Psuedocode:
- Itinialize a range of population (based on weights)
- Grading: evaluate fitness by comparing weights to a target weights
- Select and store the ones that meet target weight and discard the rest of the population
- Breeding: repopulation with the cats that passed the weights
- Mutation: to find the one that can a giant, but could also possibly get a reverse outcome

_____________________________________
Cat breed: maine coon ()
* Weights:
Female: min 8 - max 12 lbs
Male: min 15 - max 25 lbs
Max weight: 30 lbs
Number of kittens per litter: 4 - 5
Litters per year: 3
Life span: 13 - 17 years
_____________________________________

Variables and values (Assumptions)
-------------------------------------
target_weight = 500 lbs
num_cats = 20               # Total number of adult cats can be held by the lab
min_weight = 8
max_weight = 30
common_weight = 20
mutate_odd = 0.01           # probability of a mutation in the lab
mutate_min = 0.5            # ratio of the undesired outcome 
mutate_max = 1.2            # ratio of the most mutated cat 
litter_size = 4
litter_annually = 3
generation_limit = 500      # generational cutoff to stop breeding program

