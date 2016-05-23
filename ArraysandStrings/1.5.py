"""
check if two strings are at most one edit distance away
"""



def checkDist(string1, string2):
	if abs(len(string1)-len(string2)) > 1: return False
	else:
		if len(string1) > len(string2): 
			A = string2 
			B = string1
		else:
			A = string1
			B = string2
		newA, newB = getRemain(A, B)
		if newA == newB: return True
	return False

def getRemain(A, B):  
	# string A and B have lengths that are at most differ for 1, len(A) <= len(B)
	# find the first one letter that differs A and B and return the remaining letters
	if len(A) < len(B):
		for i in range(0, len(A)):
			if A[i] != B[i]:				
				newB = B[:i]+B[i+1:]
				return A, newB		
		return A, B[:-1]
	else:
		for i in range(0, len(A)):
			if A[i] != B[i]:
				newA = A[:i]+A[i+1:]
				newB = B[:i]+B[i+1:]
				return newA, newB
			else:
				return A, B

def main():
	s1 = "pale"
	s2 = "bake"
	print checkDist(s1, s2)

if __name__ == "__main__":
	main()




















