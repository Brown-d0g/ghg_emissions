# let's go to miami to catch the heat

# bst, but good
# classes are cancelled

# a bst is a list of a data element and a list of a less bst, and a more bst
# or its a []
# then we store the key in last spot as a performance enhancer
# so [key, value, kids]

def insert(data, tree, func):
	key = func(data)
	if not key:
		return
	while tree:
		tree = tree[2][key > tree[0]]
	tree.extend([key, data, [[], []]])
	
def contains(key, tree):
	if not key:
		return
	while tree:
		if not tree:
			return
		if key == tree[0]:
			return tree[0:2]
		tree = tree[2][key > tree[0]]
		
# go in as long as you can then grab an element
def pop(tree):
	while any(tree[2]):
		if tree[2][0]:
			tree = tree[2][0]
		else:
			tree = tree[2][1]
	ret, _ = tree[0:2], tree.clear()
	return ret

# csv to Python, using bst by default
def csv_to_p(file, func):
	tree = []
	[insert(line, tree, func) for line in file]
	return tree

# file handling

# line to key
def get_key(l):
	# we need the 13th column but quotes mix it up
	key = ""
	commas = 0
	quotes = False
	for c in l:
		if c == '\"':
			quotes = not quotes
		if c == ',' and not quotes:
			commas += 1
		if commas == 13 and c.isalpha():
			key += c
		if commas == 14:
			# wipe out punctuation
			return key

def main():
	# compare two cycles
	csvs = ["2016_2700s.csv","2020_2800s.csv"]
	wood = [csv_to_p(open(s,"r"),get_key) for s in csvs]
	# with two bsts, we check for shared entries
	twos = []
	while wood[0]:
		curr = pop(wood[0])
		both = contains(curr[0], wood[1])
		if both:
			twos.append(curr + [both[1]])
	print(len(twos))
	print(twos[0])
	
main()