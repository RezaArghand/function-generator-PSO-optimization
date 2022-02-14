import math


def fitness_rasa(position):
    sumVal = 0.0
    crossVal = 1
    for i in range(len(position)):
        xi = math.floor(position[i])
        sumVal += xi
        crossVal = crossVal * xi

    result = abs(1 / (1 + crossVal)) + 100 * abs(sumVal - 500)

    return result