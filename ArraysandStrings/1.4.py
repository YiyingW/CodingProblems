"""
Palindrome Permuation: given a string, write a function to check if it is a permutation of 
a palindrome.
Input: Tact Coa
Output: True(permutations: "taco cat", "atco cta",...)
"""

def isPermutationOfPalindrome(phrase):
	table = buildCharFrequencyTable(phrase)
	return checkMaxOneOdd(table)

"""
check that no more than one character has an odd count
"""

def checkMaxOneOdd(table):
	foundOdd = 0
	for count in table:
		if (count%2==1):
			foundOdd += 1
	return foundOdd<=1

def buildCharFrequencyTable(phrase):
	table = [0]*26
	a = ord('a')
	z = ord('z')
	A = ord('A')
	Z = ord('Z')
	for letter in phrase:
		if ord(letter) >= a and ord(letter)<=z:
			table[ord(letter)-a] += 1
		elif ord(letter) >= A and ord(letter)<=Z:
			table[ord(letter)-A] += 1
	return table 

def main():
	phrase = 'yiying'
	print isPermutationOfPalindrome(phrase)

if __name__ == "__main__":
	main()