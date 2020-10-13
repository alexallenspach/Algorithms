#Exhaustive Search Algorithm for Knapsack
import random as rand
import time
from operator import itemgetter
import altair as alt
import pandas as pd
from altair import Color, Scale

# Function that generates random numbers
# Format to random numbers = [(item #, item weight, item value)]
# Starts at item 0 and ends at item n-1
def random_numbers(n):
    result1 = []
    for i in range(n):
        result1.append((i, rand.randrange(1,10000,1), rand.randrange(1,100,1)))
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

# Greedy Search Algorithm: Take most valuable item that fits, repeat until bag is full
def knapsack_greedy_search(integers, max_weight, keyFunc=value):
    sack = []
    ks_weight = 0
    ks_value = 0
    sortAlgo = sorted(integers, key=itemgetter(2), reverse=False) #Sort items from smallest value to largest value
    print ('Items in order:', sortAlgo)
    while len(sortAlgo) > 0:
        item = sortAlgo.pop() # no index is specified so pop removes and returns last item in the list. This allows the largest value to be picked first. 
        if weight(item) + ks_weight <= max_weight:
            sack.append(item)
            ks_weight += weight(item)
            ks_value += value(item)
    return sack, ks_weight, ks_value

n = 3
max_w = 10000
data1 = random_numbers(n)
print ('There are a total of:', 2**n, 'subsets')
start_time = time.time() # Start the exhaustive search timer
kn1, optimum_w1, optimum_v1 = knapsack_exhaustive_search(data1, max_w)
print("Exhaustive Algorithm Execution Time: %s seconds" % (time.time() - start_time)) # Timer ends after exhaustive search ran successfully
print ('All items with its respected weight and value:', data1)
print ('knapsack:', kn1)
print ('optimum weight:', optimum_w1)
print ('optimum value:', optimum_v1)

print ('\nThere are a total of:', n**2, 'subsets')
start_time = time.time() # Start the greedy search timer
kn2, optimum_w2, optimum_v2 = knapsack_greedy_search(data1, max_w, value)
print("Greedy Algorithm Execution Time: %s seconds" % (time.time() - start_time)) # Timer ends after greedy search ran successfully
print ('knapsack:', kn2)
print ('optimum weight:', optimum_w2)
print ('optimum value:', optimum_v2)
print ("Exhaustive total value / Greedy total value = ", optimum_v1/optimum_v2)


df = pd.read_csv('/Users/alexallenspach/Documents/CS4720/HW2_PlotsData.csv')

alt.data_transformers.enable('default', max_rows=None)

chart1 = alt.Chart(df).mark_circle(size=50).encode(
    Color('Algorithm:N',
          scale=Scale(domain=['Exhaustive', 'Greedy'],
                      range=['#1f77b4', '#e377c2'])),
    x=alt.X('n:Q', scale=alt.Scale(zero=False)),
    y=alt.Y('Time:Q', scale=alt.Scale(zero=False)),
    tooltip=['n', 'Time', 'Algorithm'],
    opacity=alt.value(1)
).properties(background='white')

chart1
chart.save('scatterPlot1.png', scale_factor=2.0)

df = pd.read_csv('/Users/alexallenspach/Documents/CS4720/HW2_PlotsData.csv')

alt.data_transformers.enable('default', max_rows=None)

chart2 = alt.Chart(df).mark_circle(size=50).encode(
    Color('Algorithm:N',
          scale=Scale(domain=['Exhaustive', 'Greedy'],
                      range=['#1f77b4', '#e377c2'])),
    x=alt.X('n:Q', scale=alt.Scale(zero=False)),
    y=alt.Y('Weight:Q', scale=alt.Scale(zero=False)),
    tooltip=['n', 'Weight', 'Algorithm'],
    opacity=alt.value(1)
).properties(background='white')

chart2
chart.save('scatterPlot2.png', scale_factor=2.0)

df = pd.read_csv('/Users/alexallenspach/Documents/CS4720/HW2_PlotsData.csv')

alt.data_transformers.enable('default', max_rows=None)

chart3 = alt.Chart(df).mark_circle(size=50).encode(
    x=alt.X('N:Q', scale=alt.Scale(zero=False)),
    y=alt.Y('Accuracy:Q', scale=alt.Scale(zero=False)),
    tooltip=['N', 'Accuracy'],
    opacity=alt.value(1)
).properties(background='white')

chart3
chart.save('scatterPlot3.png', scale_factor=2.0)
