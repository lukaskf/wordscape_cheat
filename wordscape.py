import enchant
import sys
import itertools

d = enchant.Dict("en_US")

def main():
	n = input("Please Enter Number of Letters:")
	n = int(n)
	i = 0
	letters = ""
	print("When entering letters, do one at a time -_-")
	while i < n:
		l = input("Please Input (next) Letter:")
		letters += l
		i+=1
	result = find(letters, n)
	for element in result:
		print(element)

def find(letters, n): #call check for each length of word 3,4...etc.
	toolObjects= []
	words=[]
	i = 3
	while i <= n:
		toolObjects.append(itertools.permutations(letters,i))
		i+=1
	for obj in toolObjects:
		for tup in obj:
			word = ""
			for letter in tup:
				word+=letter
			if d.check(word) and (word not in words):
				words.append(word)
	return(words)



if __name__ == "__main__":
	main()
