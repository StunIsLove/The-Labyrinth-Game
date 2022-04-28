import sys
import math

r, c, a = [int(i) for i in input().split()]

def isOnMap(coords):
    if coords[0] < 0 or coords[0] >= r or coords[1] < 0 or coords[1] >= c:
        return False
    return True

def getTarget(vertex):
    row, column = vertex
    coordsSet = {(row - 1, column), (row + 1, column), (row, column - 1), (row, column + 1)}

    return {coords for coords in coordsSet if isOnMap(coords)}

def getFirstStep(parents, location, target):
    response = target
    while parents[response[0]][response[1]] != location:
        response = parents[response[0]][response[1]]

    return response

def searchBreadth(map, location, target):
    queue = []
    colour = []
    distance = []
    parents = []

    for row in range(len(map)):
        colour.append([])
        distance.append([])
        parents.append([])

        for collumn in range(len(map[row])):
            colour[row].append(0)
            distance[row].append(float('inf'))
            parents[row].append(None)

    colour[location[0]][location[1]] = 1
    distance[location[0]][location[1]] = 0

    queue.append(location)

    while queue != []:
        lastInQueue = queue.pop(0)
        forbidden_symbols = ['#']

        if target == '?':
            forbidden_symbols.append('C')
        targets = {x for x in getTarget(lastInQueue) if map[x[0]][x[1]] not in forbidden_symbols}

        for validatedTarget in targets:
            if colour[validatedTarget[0]][validatedTarget[1]] == 0:
                colour[validatedTarget[0]][validatedTarget[1]] = 1
                distance[validatedTarget[0]][validatedTarget[1]] = distance[lastInQueue[0]][lastInQueue[1]] + 1
                parents[validatedTarget[0]][validatedTarget[1]] = lastInQueue
                queue.append(validatedTarget)

                if map[validatedTarget[0]][validatedTarget[1]] == target:
                    return getFirstStep(parents, location, validatedTarget)

        colour[lastInQueue[0]][lastInQueue[1]] = 2

    return None


def findToNextStep(map, location, alarmActivated):
    if not alarmActivated:
        nextStep = searchBreadth(map, location, '?')
        if nextStep == None:
            return searchBreadth(map, location, 'C')
        return nextStep
    else:
        return searchBreadth(map, location, 'T')

def playLabyrinthGame():
    alarmActivated = False
    while True:
        kr, kc = [int(i) for i in input().split()]
        rows = []
        for i in range(r):
            rows.append(input())

        if rows[kr][kc] == 'C':
            alarmActivated = True
            alarm = a

        nextStep = findToNextStep(rows, (kr, kc), alarmActivated)

        if nextStep[0] > kr:
            print("DOWN")
        elif nextStep[0] < kr:
            print("UP")
        elif nextStep[1] > kc:
            print("RIGHT")
        else:
            print("LEFT")

playLabyrinthGame()
