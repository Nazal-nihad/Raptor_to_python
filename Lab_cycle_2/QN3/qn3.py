import json
path = 'D:\Python_Lab_Cycles\Lab_cycle_2\QN3\iris.json'
with open(path) as f:
    data = json.loads(f.read())
new = json.dumps(data , indent =2 ,sort_keys=True)

#makes json file to list
listx = []
for stuff in data :
    listx.append(stuff)
listx = json.dumps(listx,indent=2,sort_keys=True)
print(listx)

#makes to dict not done
# dictx = ()
# for k in data:
#     dictx(k:)

#make list if species is setosa and display details
a = []
count=0
for flowers in data:
    if (flowers['species']=="setosa"):
        a.append(flowers)
        count+=1
new_a = json.dumps(a,indent=2)
print(new_a)
print(count)

#to print min petal area and max sepal area in each species
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



    
