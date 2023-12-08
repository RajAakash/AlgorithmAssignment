import json
import random

from balance_bruteforce import bruteForceSolution

# checks if we place all the points within a given distance
# it takes all possible orbits, distance that we need all the points should have in minimum.
#it returns true/false if we can place in the value or not

def canWePlace(stalls, dist, planets):
    n = len(stalls)
    cntPlanets = 1
    last = stalls[0]
    placed_positions = [last]

    for i in range(1, n):
        if stalls[i] - last >= dist:
            cntPlanets += 1
            last = stalls[i]
            placed_positions.append(last)
        if cntPlanets >= planets:
            return True, placed_positions
    return False, []

def efficientSolution(orbits, k):
    n = len(orbits)
    orbits.sort()

    low = 1
    high = orbits[n - 1] - orbits[0]
    max_min_distance = 0
    positions = []
    # uses the binary search to place the planets 
    while low <= high:
        mid = (low + high) // 2
        can_place, current_positions = canWePlace(orbits, mid, k)

        if can_place:
            low = mid + 1
            max_min_distance = mid
            positions = current_positions
        else:
            high = mid - 1

    return positions


# Step 2: Test your efficient solution with 100 test samples
for i in range(100):
    with open(f'test_sample_{i}.json', 'r') as file:
        data = json.load(file)

    print(f"\nTest Case {i + 1}:")
    print("Orbits:", data['orbits'])
    print("K:", data['k'])

    # Brute-force result
    brute_force_result = data['brute_force_result']
    print("Brute-Force Result:", brute_force_result)

    # Efficient solution
    efficient_result = efficientSolution(data['orbits'], data['k'])
    print("Efficient Result:", efficient_result)

    # Compare results
    assert brute_force_result == efficient_result

print("\nAll tests passed.")