# Dynamic Program to find minimum number of coins required to make change
import sys 
import matplotlib.pyplot as plt

# function 
def DPchangeMaking(den, m, n): 
	
	# min. number of coins 
	table = [0 for i in range(n + 1)] 

	# default case 
	table[0] = 0

	# Initialize all table values as Infinite 
	for i in range(1, n + 1): 
		table[i] = sys.maxsize 

	# finds minimum coins required from 1 to n 
	for i in range(1, n + 1): 
		
		# coins do not go past i value 
		for j in range(m): 
			if (den[j] <= i): 
				x = table[i - den[j]] 
				if (x != sys.maxsize and
					x + 1 < table[i]): 
					table[i] = x + 1
	return table[n] 
 
# Greedy Program to find minimum number of coins required to make change

# function
def GDYchangeMaking(den, n):
    #sort descending
    den.sort(reverse=True)
    #initilize
    denoms = []
    #main loop
    for x in den:
            while(x<=n):
                denoms.append(x)
                n-=x #what is left
    return len(denoms)

# main 
if __name__ == "__main__": 
    den = [1, 4, 6] # Given denominations
    m = len(den) 
    n = 9 # Amount to make change for
    print("Minimum coins required for DP Algo is: ",DPchangeMaking(den, m, n)) 
    print("Minimum coins required for Greedy Algo is: ",GDYchangeMaking(den, n))

cR1 = []
set1 = [1, 4, 6]
m1 = len(set1)
for n in range(1, 1000):
    greedy1 = GDYchangeMaking(set1, n)
    dynamic1 = DPchangeMaking(set1, m1, n)
    cR1.append(dynamic1/greedy1)


cR2 = []
set2 = [1,5,6,9]
m2 = len(set2)
for n in range(1, 1000):
    greedy2 = GDYchangeMaking(set2, n)
    dynamic2 = DPchangeMaking(set2, m2, n)
    cR2.append(dynamic2/greedy2)


cR3 = []
set3 = [1,3,4]
m3 = len(set3)
for n in range(1, 1000):
    greedy3 = GDYchangeMaking(set3, n)
    dynamic3 = DPchangeMaking(set3, m3, n)
    cR3.append(dynamic3/greedy3)



z = [n for n in range(1,1000)]
plt1 = plt.scatter(z, cR1, s = 1, alpha=0.7, c = 'blue')
plt1 = plt.xlabel('n')
plt1 = plt.ylabel('Competative Ratio for set [1,4,6]')
plt1 = plt.show()
#plt.savefig('firstSet.png')

z = [n for n in range(1,1000)]
plt2 = plt.scatter(z, cR2, s = 1, alpha=0.7, c = 'red')
plt2 = plt.xlabel('n')
plt2 = plt.ylabel('Competative Ratio for set [1, 5, 6, 9]')
plt2 = plt.show()
#plt.savefig('secondSet.png')

z = [n for n in range(1,1000)]
plt3 = plt.scatter(z, cR3, s = 1, alpha=0.7, c = 'green')
plt3 = plt.xlabel('n')
plt3 = plt.ylabel('Competative Ratio for set [1, 3, 4]')
plt3 = plt.show()
#plt.savefig('thirdSet.png')
