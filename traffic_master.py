in_file = "inputs/a.txt"

streets = {}
car_routes = []

with open(in_file, "r") as f:
    first_line = f.readline()
    duration, num_intersections, num_streets, num_cars, bonus_points = map(lambda x: int(x), first_line.split())
    for i in range(num_streets):
        street_line = f.readline()
        elems = street_line.split()
        streets[elems[2]] = {"beg" : int(elems[0]), "end" : int(elems[1]), "cost" : int(elems[3])}
    for i in range(num_cars):
        car_line = f.readline()
        car_routes.append(car_line.split()[1:])

print("duration: {}. num_intersections: {}, num_streets: {}, num_cars: {}, bonus_points: {} "
      .format(duration, num_intersections, num_streets, num_cars, bonus_points))
print("streets: {}".format(streets))
print("car routes: {}".format(car_routes))



