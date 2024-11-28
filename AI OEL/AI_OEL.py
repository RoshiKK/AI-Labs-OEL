import random

# Fitness Function: Minimize maximum load
def fitness_function(chromosome, tasks, num_processors):
    processor_loads = [0] * num_processors
    for i, task in enumerate(tasks):
        processor_loads[chromosome[i]] += task
    max_load = max(processor_loads)
    baseline = sum(tasks)  # Worst-case load if all tasks are assigned to one processor
    return baseline - max_load  # Shift fitness to ensure non-negative values

# Generate Initial Population
def generate_population(size, num_tasks, num_processors):
    return [[random.randint(0, num_processors - 1) for _ in range(num_tasks)] for _ in range(size)]

# Selection (Tournament)
def select_parents(population, fitness):
    selected = random.choices(population, weights=[f + 1 for f in fitness], k=2)
    return selected

# Crossover (Single Point)
def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    offspring1 = parent1[:point] + parent2[point:]
    offspring2 = parent2[:point] + parent1[point:]
    return offspring1, offspring2

# Mutation (Change task assignment)
def mutate(chromosome, mutation_rate, num_processors):
    if random.random() < mutation_rate:
        idx = random.randint(0, len(chromosome) - 1)
        chromosome[idx] = random.randint(0, num_processors - 1)
    return chromosome

# Genetic Algorithm
def genetic_algorithm(tasks, num_processors, pop_size, generations, mutation_rate):
    num_tasks = len(tasks)
    population = generate_population(pop_size, num_tasks, num_processors)
    print("\nInitial Population:")
    for i, p in enumerate(population):
        print(f"Chromosome {i + 1}: {p}")

    for generation in range(generations):
        fitness = [fitness_function(chromosome, tasks, num_processors) for chromosome in population]
        print(f"\nGeneration {generation + 1}: Best Fitness = {max(fitness)}")

        if max(fitness) <= 0:
            raise ValueError("Fitness values are invalid. Check input tasks and processor count.")

        new_population = []
        for _ in range(pop_size // 2):
            parent1, parent2 = select_parents(population, fitness)
            offspring1, offspring2 = crossover(parent1, parent2)
            offspring1 = mutate(offspring1, mutation_rate, num_processors)
            offspring2 = mutate(offspring2, mutation_rate, num_processors)
            new_population.extend([offspring1, offspring2])
        population = new_population

    best_solution = max(population, key=lambda c: fitness_function(c, tasks, num_processors))
    return best_solution, sum(tasks) - fitness_function(best_solution, tasks, num_processors)

# Main Execution
if __name__ == "__main__":
    print("=== Genetic Algorithm: Task Scheduling ===")
    tasks = list(map(int, input("Enter task durations separated by spaces: ").split()))
    num_processors = int(input("Enter the number of processors: "))
    pop_size = int(input("Enter population size: "))
    generations = int(input("Enter number of generations: "))
    mutation_rate = float(input("Enter mutation rate (0 to 1): "))

    try:
        best_solution, best_fitness = genetic_algorithm(
            tasks=tasks,
            num_processors=num_processors,
            pop_size=pop_size,
            generations=generations,
            mutation_rate=mutation_rate
        )

        print("\n=== Final Results ===")
        print(f"Best Task Assignment: {best_solution}")
        print(f"Minimum Maximum Load: {best_fitness}")
    except ValueError as e:
        print(f"Error: {e}")
