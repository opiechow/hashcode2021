in_file = "inputs/a.txt"

with open(in_file, "r") as f:
    first_line = f.readline()
    print(first_line.split())

