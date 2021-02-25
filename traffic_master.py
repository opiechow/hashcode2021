from collections import Counter

in_file = "inputs/f.txt"

streets = {}
car_routes = []
intersections = []
street_occurences = {}
result = []
count = 0

def count_street_occurences():
    flat_list = [item for sublist in car_routes for item in sublist]
    return Counter(flat_list)

def check_intersections_occurences():
    for i, intersection in enumerate(intersections):
        mapping = list(map((lambda x: {x: street_occurences[x]} if street_occurences[x] != 0 else None), intersection['in']))
        mapping = list(filter((lambda x: x is not None), mapping))
        if len(mapping):
            global count 
            count += 1
            result.append(i)
            result.append(len(mapping))
            for d in mapping:
                for key in d:
                    result.append(key + ' ' + str(d[key]))

with open(in_file, "r") as f:
    first_line = f.readline()
    duration, num_intersections, num_streets, num_cars, bonus_points = map(lambda x: int(x), first_line.split())
    for i in range(num_intersections):
        intersections.append({"in": [], "out": []})
    for i in range(num_streets):
        street_line = f.readline()
        elems = street_line.split()
        street_name = elems[2]
        street_beg = int(elems[0])
        street_end = int(elems[1])
        street_cost = int(elems[3])
        streets[street_name] = {"beg": street_beg, "end": street_end, "cost": street_cost}
        intersections[street_beg]["out"].append(street_name)
        intersections[street_end]["in"].append(street_name)
    for i in range(num_cars):
        car_line = f.readline()
        car_routes.append(car_line.split()[1:])

#print("duration: {}. num_intersections: {}, num_streets: {}, num_cars: {}, bonus_points: {} "
#      .format(duration, num_intersections, num_streets, num_cars, bonus_points))
#print("streets: {}".format(streets))
#print("car routes: {}".format(car_routes))
#for i in range(len(intersections)):
    #print("intersections[{}]: {}".format(i, intersections[i]))
#print(count_street_occurences())

street_occurences = count_street_occurences()
check_intersections_occurences()
print(count)
for el in result:
    print(el)
