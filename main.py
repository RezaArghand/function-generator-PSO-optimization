import random
import math  # cos() for Rastrigin
import copy  # array-copying convenience
import sys
from time import time  # max float
import ODE as ode
import numpy as np

import costFunction as costF
import functions
import parameters
import parameters as Par
import functions as fun
import matplotlib.pyplot as plt

start_time = time()


# -------fitness functions---------

# rastrigin function


def fitness_rastrigin(position):
    fitnessVal = 0.0
    for i in range(len(position)):
        xi = math.floor(position[i])
        fitnessVal += (xi * xi) - (10 * math.cos(2 * math.pi * xi)) + 10
    return fitnessVal


# sphere function


def fitness_sphere(position):
    fitnessVal = 0.0
    for i in range(len(position)):
        xi = math.floor(position[i])
        fitnessVal += (xi * xi)
    return fitnessVal


def fitness_test(position):
    # input = []
    # for i in position:
    #     input.append(int(math.floor(i)))
    result = costF.costNumber(position)
    return result


# -------------------------

# particle class


class Particle:
    def __init__(self, fitness, dim, minx, maxx, seed):
        self.rnd = random.Random(seed)

        # initialize position of the particle with 0.0 value
        self.position = [0.0 for i in range(dim)]

        # initialize velocity of the particle with 0.0 value
        self.velocity = [0.0 for i in range(dim)]

        # initialize best particle position of the particle with 0.0 value
        self.best_part_pos = [0.0 for i in range(dim)]

        # loop dim times to calculate random position and velocity
        # range of position and velocity is [minx, max]
        for i in range(dim):
            self.position[i] = ((maxx - minx) *
                                self.rnd.random() + minx)
            self.velocity[i] = ((maxx - minx) *
                                self.rnd.random() + minx)

        # compute fitness of particle
        self.fitness = fitness(self.position)  # curr fitness

        # initialize best position and fitness of this particle
        self.best_part_pos = copy.copy(self.position)
        self.best_part_fitnessVal = self.fitness  # best fitness


# particle swarm optimization function

fitnessPlot = []
iterPlot = []


def pso(fitness, max_iter, n, dim, minx, maxx, w, c1, c2, satisfaction_fitness):
    rnd = random.Random(0)

    # create n random particles
    swarm = [Particle(fitness, dim, minx, maxx, i) for i in range(n)]

    # compute the value of best_position and best_fitness in swarm
    best_swarm_pos = [0.0 for i in range(dim)]
    best_swarm_fitnessVal = sys.float_info.max  # swarm best

    # computer best particle of swarm and it's fitness
    for i in range(n):  # check each particle
        if swarm[i].fitness < best_swarm_fitnessVal:
            best_swarm_fitnessVal = swarm[i].fitness
            best_swarm_pos = copy.copy(swarm[i].position)

    # main loop of pso

    Iter = 0
    while Iter < max_iter:

        # after every 10 iterations
        # print iteration number and best fitness value so far
        if Iter % 10 == 0:
            print("Iter = " + str(Iter) + " best fitness = %.15f" %
                  best_swarm_fitnessVal)
            # print(best_swarm_pos)
            best_Possition = [math.floor(i) for i in best_swarm_pos]
            realBestPosition = best_swarm_pos
            print(best_Possition)
            print(costF.bestFunc(best_swarm_pos))
            # ode.solveAndPlot(costF.bestFunc(best_swarm_pos))
            if Iter < 2:
                k = open("00results.txt", "w")
                k.write("")
                k.close()
            f = open("00results.txt", "a")

            f.write("\n iteration => %s \n best cost => %s \n best position => %s \n best function => %s \n" % (
                str(Iter), best_swarm_fitnessVal, str(best_Possition), costF.bestFunc(best_swarm_pos)))
            f.close()
        for i in range(n):  # process each particle

            # compute new velocity of curr particle
            for k in range(dim):
                r1 = rnd.random()  # randomizations
                r2 = rnd.random()

                swarm[i].velocity[k] = (
                        (w * swarm[i].velocity[k]) +
                        (c1 * r1 * (swarm[i].best_part_pos[k] - swarm[i].position[k])) +
                        (c2 * r2 *
                         (best_swarm_pos[k] - swarm[i].position[k]))
                )

                # if velocity[k] is not in [minx, max]
                if swarm[i].velocity[k] < minx:
                    swarm[i].velocity[k] = minx
                elif swarm[i].velocity[k] > maxx:
                    swarm[i].velocity[k] = maxx
                # then clip it

            # compute new position using new velocity
            for k in range(dim):
                swarm[i].position[k] += swarm[i].velocity[k]

                if swarm[i].position[k] < minx:
                    swarm[i].position[k] = 2 * minx - swarm[i].position[k]
                elif swarm[i].position[k] > maxx:
                    swarm[i].position[k] = 2 * maxx - swarm[i].position[k]

            # compute fitness of new position
            swarm[i].fitness = fitness(swarm[i].position)

            # is new position a new best for the particle?
            if swarm[i].fitness < swarm[i].best_part_fitnessVal:
                swarm[i].best_part_fitnessVal = swarm[i].fitness
                swarm[i].best_part_pos = copy.copy(swarm[i].position)

            # is new position a new best overall?
            if swarm[i].fitness < best_swarm_fitnessVal:
                best_swarm_fitnessVal = swarm[i].fitness
                best_swarm_pos = copy.copy(swarm[i].position)

        # new randomization///////////////////////////////////////////////////////////////////////////////////////
        # randomizing several particles
        for j in range(parameters.number_randomize_particles_fullArea):
            hh = random.randint(0, n - 1)
            for k in range(dim):
                swarm[hh].position[k] = random.random() * maxx

            # compute fitness of new position
            swarm[hh].fitness = fitness(swarm[hh].position)

            # is new position a new best for the particle?
            if swarm[hh].fitness < swarm[hh].best_part_fitnessVal:
                swarm[hh].best_part_fitnessVal = swarm[hh].fitness
                swarm[hh].best_part_pos = copy.copy(swarm[hh].position)

            # is new position a new best overall?
            if swarm[hh].fitness < best_swarm_fitnessVal:
                best_swarm_fitnessVal = swarm[hh].fitness
                best_swarm_pos = copy.copy(swarm[hh].position)

        # randomizing first bit of best particle
        if Iter % 1 == 0:
            # print(functions.colored(255, 50, 50, "Randomization Happened, " + "iteration = " + str(Iter)))
            for j in range(Par.number_randomize_particles_firstBitOfBest):
                i = random.randint(0, n - 1)
                for k in range(dim):
                    swarm[i].position[k] = best_swarm_pos[k]
                swarm[i].position[-1] = random.random() * maxx
                # compute fitness of new position
                swarm[i].fitness = fitness(swarm[i].position)

                # is new position a new best for the particle?
                if swarm[i].fitness < swarm[hh].best_part_fitnessVal:
                    swarm[i].best_part_fitnessVal = swarm[i].fitness
                    swarm[i].best_part_pos = copy.copy(swarm[i].position)

                # is new position a new best overall?
                if swarm[i].fitness < best_swarm_fitnessVal:
                    best_swarm_fitnessVal = swarm[i].fitness
                    best_swarm_pos = copy.copy(swarm[i].position)

        if Iter % 500 == 0 or Iter < 30:
            print(functions.colored(255, 50, 50, "Big Randomization Happened, " + "iteration = " + str(Iter)))
            for i in range(n):
                for k in range(dim):
                    swarm[i].position[k] = random.randint(minx, maxx) * random.random()
        # w = parameters.W
        # swarm[i].velocity[k] = random.randint(minx, maxx)
        #     # for k in range(dim):

        # swarm[random.randint(0,n)].position[]

        # reset w
        if Iter % Par.w_reset_iteration == 0:
            w = Par.W
        # end new randomization///////////////////////////////////////////////////////////////////////////////////////////////////

        # plot iteration ft cost function
        # if Iter % 10 == 0 and Iter != 0 and best_swarm_fitnessVal < 5000:
        #     plt.plot(iterPlot, fitnessPlot)
        #     # plt.pause(0.05)
        #     plt.xlabel("iteration", fontsize='13')  # adds a label in the x axis
        #     plt.ylabel("cost function", fontsize='13')  # adds a label in the y axis
        #     plt.title("Convergance")
        #     # plt.legend(('YvsX'), loc='best')  # creates a legend to identify the plot
        #     # plt.savefig('Y_X.png')  # saves the figure in the present directory
        #     plt.grid()  # shows a grid under the plot
        #
        #     plt.savefig('02convergance.png')
        #     plt.close()
        fitnessPlot.append(best_swarm_fitnessVal)
        iterPlot.append(Iter)

        # for-each particle
        Iter += 1
        w = w * wDamp
        if best_swarm_fitnessVal < satisfaction_fitness:
            break
    # end_while
    return best_swarm_pos


# end pso


# ----------------------------
# Driver code for rastrigin function

dim = Par.varNum  # variables count
fitness = fitness_test  # fitness function name
wDamp = Par.damping_rate_W  # inertia damper
xmax = Par.max_of_variable  # max domain
xmin = Par.min_of_variable  # min domain
satisfaction_fitness = Par.satisfaction_cost_number  # satisfaction point
w = Par.W  # inertia
c1 = Par.C1  # cognitive (particle)
c2 = Par.C2  # social (swarm)
num_particles = Par.number_of_particles  # particle count
max_iter = Par.max_iteration_number  # max iteration

print("Setting num_particles = " + str(num_particles))
print("Setting max_iter    = " + str(max_iter))
print("\nStarting PSO algorithm\n")

best_position = pso(fitness, max_iter, num_particles,
                    dim, xmin, xmax, w, c1, c2, satisfaction_fitness)

BestPosition = [best_position[k] for k in range(dim)]
bestFunction = costF.bestFunc(BestPosition)
print("\nPSO completed\n")
print("\nBest variables:")
print([math.floor(best_position[k]) for k in range(dim)])
fitnessVal = fitness(best_position)
print("cost of best variables = " + str(fitnessVal))
print()
print("best function found = ")
print(bestFunction)
print()
end_time = time()
full_time = end_time - start_time
print("The time consumed = " + str(full_time // 60) + " minutes " + str(full_time % 60) + " seconds ")
print()
print()
iterP = iterPlot[10:]
fitnessP = fitnessPlot[10:]
fig = plt.figure(1)  # identifies the figure
plt.title("cost function", fontsize='16')  # title
plt.plot(iterP, fitnessP)  # plot the points
plt.xlabel("iteration", fontsize='13')  # adds a label in the x axis
plt.ylabel("cost function", fontsize='13')  # adds a label in the y axis
# plt.legend(('YvsX'), loc='best')  # creates a legend to identify the plot
# plt.savefig('Y_X.png')  # saves the figure in the present directory
plt.grid()  # shows a grid under the plot
plt.show()
