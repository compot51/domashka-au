import numpy as np
import pygad

function_inputs = [6, -43, -17, 177, -53, -70]  # Решение ур-ий любой степени
desired_output = 0

num_genes = 1

def fitness_function(ga_instance, solution, solution_idx):
	output = 0
	for i in range(len(function_inputs)):
		output += function_inputs[i] * solution[0] ** (len(function_inputs) - i - 1)
	fitness = 1.0 / (np.abs(desired_output - output) + 0.000001)
	return fitness

num_generations = 100
num_parents_mating = 10

sol_per_pop = 20

ga_instance = pygad.GA(num_generations=num_generations,
                       num_parents_mating=num_parents_mating,
                       sol_per_pop=sol_per_pop,
                       num_genes=num_genes,
                       fitness_func=fitness_function)

ga_instance.run()

solution, solution_fitness, solution_idx = ga_instance.best_solution(ga_instance.last_generation_fitness)
print("Одно из решений уравнения: {solution}".format(solution=solution))
ga_instance.plot_fitness()
