import random as rand
import time
from operator import itemgetter
import matplotlib.pyplot as plt
import statistics

def random_numbers(n):
    result1 = []
    for i in range(n):
        result1.append((i, rand.randrange(1,100,1), rand.randrange(1,30,1)))
    return result1

# A list that shows every possible subset, including the empty set
def all_subsets(integers):
    result2 = [[]] #start with an empty list
    for j in integers:
	    new_subset = [r + [j] for r in result2] #[j] value gets added to every value in result2 
	    result2.extend(new_subset)
    return result2

# Exhaustive Search Algorithm: Goes through all possible answers and returns the best answer 
def knapsack_exhaustive_search(integers, max_weight):
    ks = [] #knapsack initialized to empty list
    best_weight = 0 #best weight is initialized to zero
    best_value = 0 #best value is initialized to zero
    for k in all_subsets(integers):
        current_weight = sum([e[1] for e in k])
        current_value = sum([e[2] for e in k])
        if current_value > best_value and current_weight <= max_weight:
            best_value = current_value
            best_weight = current_weight
            ks = k
    return ks, best_weight, best_value

def weight(item):
    return item[1]

def value(item):
    return item[2]

def density(item):
    return float(item[2])/item[1]

# Greedy Search Algorithm 1: Take most valuable item that fits, repeat until bag is full
def knapsack_greedy_search(integers, max_weight, keyFunc=value):
    sack2 = []
    ks_weight2 = 0
    ks_value2 = 0
    sortAlgo2 = sorted(integers, key=itemgetter(2), reverse=False) #Sort items from smallest value to largest value
    print ('Items in ascending order by value:', sortAlgo2)
    while len(sortAlgo2) > 0:
        item = sortAlgo2.pop() # no index is specified so pop removes and returns last item in the list. This allows the largest value to be picked first. 
        if weight(item) + ks_weight2 <= max_weight:
            sack2.append(item)
            ks_weight2 += weight(item)
            ks_value2 += value(item)
    return sack2, ks_weight2, ks_value2


# Greedy Search Algorithm 2: Take most valuable item by value/weight that fits, repeat until bag is full
def knapsack_greedy_search2(integers, max_weight, keyFunc=value):
    sack3 = []
    ks_weight3 = 0
    ks_value3 = 0
    sortAlgo3 = sorted(integers, key=keyFunc) #Sort items from smallest value to largest value
    print ('Items in ascending order by value/weight:', sortAlgo3)
    while len(sortAlgo3) > 0:
        item = sortAlgo3.pop() # no index is specified so pop removes and returns last item in the list. This allows the largest value to be picked first. 
        if weight(item) + ks_weight3 <= max_weight:
            sack3.append(item)
            ks_weight3 += weight(item)
            ks_value3 += value(item)
    return sack3, ks_weight3, ks_value3


n = 5
max_w = 100
data = random_numbers(n)

print ('Exhaustive Search')
start_time = time.time() # Start the exhaustive search timer
kn1, optimum_w1, optimum_v1 = knapsack_exhaustive_search(data, max_w)
print("Exhaustive Algorithm Execution Time: %s seconds" % (time.time() - start_time)) # Timer ends after exhaustive search ran successfully
print ('All items with its respected weight and value:', data)
print ('knapsack:', kn1)
print ('optimum weight:', optimum_w1)
print ('optimum value:', optimum_v1)

print ('\nGreedy Search 1')
start_time = time.time() # Start the greedy search timer
kn2, optimum_w2, optimum_v2 = knapsack_greedy_search(data, max_w, value)
print("Greedy Algorithm Execution Time: %s seconds" % (time.time() - start_time)) # Timer ends after greedy search ran successfully
print ('knapsack:', kn2)
print ('optimum weight:', optimum_w2)
print ('optimum value:', optimum_v2)

print ('\nGreedy Search 2')
start_time = time.time() # Start the greedy search timer
kn3, optimum_w3, optimum_v3 = knapsack_greedy_search2(data, max_w, density)
print("Greedy Algorithm Execution Time: %s seconds" % (time.time() - start_time)) # Timer ends after greedy search ran successfully
print ('knapsack:', kn3)
print ('optimum weight:', optimum_w3)
print ('optimum value:', optimum_v3)

optimalValue = optimum_v1
greedySolution = max(optimum_v2, optimum_v3)
if greedySolution == optimum_v2:
    print('\nBest greedy subset in format (weight, value) is:', '(' + str(optimum_w2) + ',', str(optimum_v2) + ')')
elif greedySolution == optimum_v3:
    print('\nBest greedy subset in format (weight, value) is:', '(' + str(optimum_w3) + ',', str(optimum_v3) + ')')

#Create Plot
cR1 = []
for n in range(1, 10000):
    n = 5
    max_w = 100
    data = random_numbers(n)

    start_time = time.time() # Start the exhaustive search timer
    kn1, optimum_w1, optimum_v1 = knapsack_exhaustive_search(data, max_w)

    start_time = time.time() # Start the greedy search timer
    kn2, optimum_w2, optimum_v2 = knapsack_greedy_search(data, max_w, value)

    start_time = time.time() # Start the greedy search timer
    kn3, optimum_w3, optimum_v3 = knapsack_greedy_search2(data, max_w, density)

    optimalValue = optimum_v1
    greedySolution = max(optimum_v2, optimum_v3)
    cR1.append(optimalValue/greedySolution)

z = [n for n in range(1,10000)]
plt1 = plt.scatter(z, cR1, s = 1, alpha=0.7, c = 'blue')
plt1 = plt.xlabel('n')
plt1 = plt.ylabel('Approximation Ratio')
plt1 = plt.show()
plt.savefig('HW6_3(b).png')

#Finding average approximation ratio
average = statistics.mean(cR1) 
  
# Printing the mean 
print("Mean is :", average) 
