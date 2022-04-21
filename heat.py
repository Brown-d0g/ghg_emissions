# let's go to miami to catch the heat

# bst, but good
# classes are cancelled

# a bst is a list - less, more, key, vals
# key is a name
# vals is a year indexed list of sets

def insert(data, tree, func, year):
	key, val = func(data)
	if not val:
		return
	# traverse
	while tree and key != tree[2]:
		tree = tree[key > tree[2]]
	if tree:
	# add value to key
		tree[3][year].add(val)
	elif not year:
	# add key to tree
		tree.extend([[],[], key, [{val},set()]])
		
def tolist(tree):
	if tree:
		# we have a two sets and want to add all pairs between sets
		return tolist(tree[0]) + [(one, two) for one in tree[3][0] for two in tree[3][1]] + tolist(tree[1])
	return []

# file handling

# line to key
def get_kv(l):
	# we need the 13th column but quotes mix it up
	key = ""
	val = ""
	commas = 0
	quotes = False
	for c in l:
		if c == '\"':
			quotes = not quotes
		elif c == ',' and not quotes:
			commas += 1
		elif commas == 13:
			key += c
		elif commas == 1 and (c.isupper() or c.isspace()):
			val += c
		elif commas == 14:
			# shorten val
			if "FOR" in val:
				val = val[:val.find("FOR")]
			if "PRES" in val:
				val = val[:val.find("PRES")]
			if "AMER" in val:
				val = val[:val.find("AMER")]
			val = val.replace("FRIENDS OF","")
			val = val.replace("COMMITTEE","")
			val = val.replace("TO ELECT","")
			val = val.replace("INC","")
			val = val.replace("CAMPAIGN","")
			val.strip()
			return key, val

# make the dictionary
def getd():
	# compare two cycles
	csvs = ["2016_2700s.csv","2020_2800s.csv"]
	# with two bsts, we check for shared entries
	tree = []
	[insert(line, tree, get_kv, n) for n in [0,1] for line in open(csvs[n],"r")]
	twos = [donr for donr in tolist(tree) if all(donr)]
	d = { one : { two : 0 for two in set([donr[1] for donr in twos]) } for one in set([donr[0] for donr in twos]) }
	for donr in twos:
		d[donr[0]][donr[1]] += 1
	for one in d:
		for two in d[one]:
			d[one][two] = d[one][two].bit_length().bit_length()
	return d

# we need a few imports to make the map

import pandas
import seaborn
import matplotlib.pyplot as plt

def heat():

	df = pandas.DataFrame.from_dict(getd())
	
	blues = seaborn.color_palette("light:b", as_cmap=True)
	plt.rcParams['figure.figsize'] = [10, 10]
	plt.rcParams['figure.dpi'] = 100
	plt.tick_params(axis='both', which='major', labelsize=10, labelbottom = False, bottom=False, top = False, left = False, labeltop=True)
	
	p = seaborn.heatmap(df)
	f = p.get_figure()
	f.savefig("heat.png",bbox_inches='tight')
	
heat()