file_name = "elements.txt"
with open(file_name, 'r') as f:
	data = f.read().split()
ones = []
twos = []
for loc in range(1, len(data), 3):
	if len(data[loc]) == 1:
		ones.append(data[loc])
	else:
		twos.append(data[loc])


def has_one(word):
	return word[0].upper() in ones

def has_two(word):
	return word[0:2].lower().title() in twos

def can_elementize(word):
	#print(word)
	if len(word) == 0:
		return True
	one = has_one(word)
	two = has_two(word)
	path1 = path2 = False
	if two and len(word) >= 2:
		path2 = can_elementize(word[2:])
	if one and len(word) >= 1:
		path1 = can_elementize(word[1:])
	return path1 or path2

def elementize(word):
	manip = ""
	loc = 0
	while can_elementize(word) and loc < len(word):
		if has_two(word[loc:]) and can_elementize(word[loc+2:]):
			manip += word[loc:loc+2].lower().title()
			loc += 2
		else:
			manip += word[loc].upper()
			loc += 1
	if len(manip) == 0:
		return "No spelling found"
	return manip

word = "0"
while len(word) > 0:
	word = input("Enter a word: ")
	print(elementize(word))
