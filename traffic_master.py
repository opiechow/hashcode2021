in_file = "inputs/a.txt"

streets = {}
car_routes = []

with open(in_file, "r") as f:
    first_line = f.readline()
    duration, num_intersections, num_streets, num_cars, bonus_points = map(lambda x: int(x), first_line.split())
    for i in range(num_streets):
        pass
    for i in range(num_cars):
        pass

print("duration: {}. num_intersections: {}, num_streets: {}, num_cars: {}, bonus_points: {} "
      .format(duration, num_intersections, num_streets, num_cars, bonus_points))



