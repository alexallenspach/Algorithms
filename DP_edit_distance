# DP Edit Distance

#function
def editDistDP(s1, s2, x, y): 
	# table for storing 
	dpTable = [[0 for a in range(y+1)] for a in range(x+1)] 

	for i in range(x+1): 
		for j in range(y+1): 

			# first word empty, insert char of second word
			if i == 0: 
				dpTable[i][j] = j # Min. operations = j 

			# second word empty, remove chars of second word 
			elif j == 0: 
				dpTable[i][j] = i # Min. operations = i 

			# last char same so ignore
			elif s1[i-1] == s2[j-1]: 
				dpTable[i][j] = dpTable[i-1][j-1] 

			# last char different, so three actions are determined (insert, remove, or replace)
			else: 
				dpTable[i][j] = 1 + min(dpTable[i][j-1],        # Insert 
                                                dpTable[i-1][j],	        # Remove 
						dpTable[i-1][j-1])              # Replace 

	return dpTable[x][y] 

#Main
s1 = "kitten"
s2 = "sitting"

print(editDistDP(s1, s2, len(s1), len(s2)))
