def get_total(l):
    temp = l.split(",")
    year = 0
    total = 0
    for i in range(len(temp)):
        if i == 0:
            year = int(temp[i])
        else:
            total += int(temp[i])
    return (year, total)

# insert
def insert(l, t):
    d = get_total(l)
    temp = t
    if temp == []:
        temp = [d]
    elif d[0] < temp[0][0]:
        temp = [d] + temp
    elif d[0] > temp[0][0]:
        temp = [temp[0]] + insert(l, temp[1:])
    return temp

# constructing
def sortList():
    # sortList
    csv = "emission_per_year.csv"
    tree = []
    for line in open(csv, "r"):
        if line[0] == "Y":
            pass
        else:
            tree = insert(str(line), tree)
    return tree

import pandas
import seaborn
import matplotlib.pyplot as plt

def graph():
    # Creating data frame
    year = []
    tonnes = []
    temp = sortList()
    for i in temp:
        year.append(i[0])
        tonnes.append(i[1])
    data = {'Year':year, 'Tonnes':tonnes}  
    dataframe = pandas.DataFrame(data, columns = ['Year', 'Tonnes'])
    dataframe.plot(x='Year',y='Tonnes')
    plt.xlabel("Year")
    plt.ylabel("Global Emission")
    plt.title("Global Emissions over Time")
    
graph()