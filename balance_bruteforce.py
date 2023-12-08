import json
import random

# checks if we place all the points within a given distance
# it takes all possible orbits, distance that we need all the points should have in minimum.
#it returns true/false if we can place in the value or not

def canWePlace(orbits, dist, planets):
    n = len(orbits)
    # planets counts
    cntPlanets = 1
    #last planets position is taken as last one
    last = orbits[0]
    placed_positions = [last]

    for i in range(1, n):
        if orbits[i] - last >= dist:
            cntPlanets += 1
            # Take the last planet as last orbit
            last = orbits[i]
            placed_positions.append(last)
        if cntPlanets >= planets:
            return True, placed_positions
    return False, []

def bruteForceSolution(planets, k):
    n = len(planets)
    # sort the planets before performing operation
    planets.sort()
    limit = planets[n - 1] - planets[0]
    final_positions = []

    # check all possible places to fit the planets
    for i in range(1, limit + 1):
        # checks all possible value withint the limits
        can_place, positions = canWePlace(planets, i, k)
        if not can_place:
            #if we cannot place the planet, break in a place
            # and return maximum value that we have obtained till now
            break
        max_min_distance = i
        final_positions = positions

    return final_positions

# Step 1: Generate and write 100 random test samples to disk using brute-force approach
for i in range(100):
    # Generate random j (number of orbits) and k (number of planets)
    j = random.randint(4, 10)
    k = random.randint(3, j - 1)

    # Generate random orbits and k planets
    orbits = sorted(random.sample(range(1, 100), j))  # Assuming a range of 1 to 100 for simplicity

    # Brute-force solution to find the correct configuration
    brute_force_result = bruteForceSolution(orbits, k)

    # Write the data to disk as JSON
    data = {'orbits': orbits, 'k': k, 'brute_force_result': brute_force_result}
    with open(f'test_sample_{i}.json', 'w') as file:
        json.dump(data, file)
