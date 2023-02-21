import json
path = 'D:\Python_Lab_Cycles\Lab_cycle_2\QN3\iris.json'
with open(path,'r') as f:
    data = json.loads(f.read())

#makes json file to list
def readaslist(path):
    with open(path,'r') as f:
        data = json.loads(f.read())
    for stuff in data :
        print(stuff)

# for l in listx:
#     print(l)

#makes to dict not done
# print(new)

#make list if species is setosa and display details
def setosa(path):
    with open(path,'r') as f:
        data = json.load(f)
    a = []
    for flowers in data:
        if (flowers['species']=="setosa"):
            a.append(flowers)
    print("\n details of setosa \n")
    for m in a:
        print(m)

#to print min petal area and max sepal area in each species
def min_max_area(path):
    with open(path,'r') as f:
        data = json.loads(f.read())
    species_list = []
    for area in data:
        species_list.append(area['species'])
    species_list = set(species_list)

    petal_list = []
    sepal_list = []
    print(species_list)
    for i in species_list:
        for j in data:
            if i==j['species']:
                petal_list.append(j['petalLength']*j['petalWidth'])
                sepal_list.append(j['sepalLength']*j['sepalWidth'])
        print("max are of ",i," sepals = ",round(max(sepal_list),2))
        print("min area of ",i," petals = ",round(min(petal_list),2),"\n")
        sepal_list.clear()
        petal_list.clear()

readaslist(path)
setosa(path)
min_max_area(path)




    
