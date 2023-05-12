import json
file_path = 'Lab_cycle_2\QN3\iris.json'

# read as list


def list_read(file_path):
    print("\nprinting list line by line \n")
    list_file = open(file_path, 'r')
    list_done = list_file.readlines()
    for k in list_done:
        print(k, end=" ")

# read as dict


def list_to_dict(file_path):
    print("\nprinting each as dict values \n")
    list_dict = open(file_path, 'r')
    # makes to python file so we can use python operations
    dicts = json.load(list_dict)
    for i in dicts:
        for key, value in i.items():
            print("{} : {} ".format(key, value), end=" , ")
        print("")


# make list if species is setosa and display details
def setosa(path):
    print("\n Details of setosa \n")
    with open(path, 'r') as f:
        data = json.load(f)
    a = []
    for flowers in data:
        if (flowers['species'] == "setosa"):
            a.append(flowers)
    for m in a:
        print(m)

# to print min petal area and max sepal area in each species


def min_max_area(path):
    print("\nMax and Min area of petal and sepal in each species \n")
    with open(path, 'r') as f:
        data = json.loads(f.read())
    species_list = []
    for area in data:
        species_list.append(area['species'])
    species_list = set(species_list)

    petal_list = []
    sepal_list = []
    # print(species_list)
    for i in species_list:
        for j in data:
            if i == j['species']:
                petal_list.append(j['petalLength']*j['petalWidth'])
                sepal_list.append(j['sepalLength']*j['sepalWidth'])
        print("\nMax and min areas of ", i, "\n")
        print("max are of ", i, " sepals = ", round(max(sepal_list), 2))
        print("min area of ", i, " petals = ", round(min(petal_list), 2), "\n")
        sepal_list.clear()
        petal_list.clear()

# Sort the list of dictionaries according to the total area


def sort_with_area(file_path):
    print("\nAdding new key TotalArea and sorting according to it \n")
    area_list = open(file_path, 'r')
    area_sort = json.load(area_list)
    for i in area_sort:
        i['TotalArea'] = round(
            i['sepalLength']*i['sepalWidth']+i['petalLength']*i['petalWidth'], 2)
        # round(i['TotalArea'],2)
    area_sort.sort(key=lambda x: x['TotalArea'])
    for k in area_sort:
        print(k)


list_read(file_path)
list_to_dict(file_path)
setosa(file_path)
min_max_area(file_path)
sort_with_area(file_path)
