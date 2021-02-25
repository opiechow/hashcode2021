from collections import Counter

in_file = "inputs/a.txt"

streets = {}
car_routes = []
intersections = []
street_occurences = {}
result = []

def count_street_occurences():
    flat_list = [item for sublist in car_routes for item in sublist]
    return Counter(flat_list)
    
def check_intersections_occurences():
    for intersection in intersections:
        len = map((lambda x: {x: street_occurences[x]}), intersection['in'])
        print(list(len))

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

print("duration: {}. num_intersections: {}, num_streets: {}, num_cars: {}, bonus_points: {} "
      .format(duration, num_intersections, num_streets, num_cars, bonus_points))
print("streets: {}".format(streets))
print("car routes: {}".format(car_routes))
for i in range(len(intersections)):
    print("intersections[{}]: {}".format(i, intersections[i]))
print(count_street_occurences())
street_occurences = count_street_occurences()
check_intersections_occurences()
