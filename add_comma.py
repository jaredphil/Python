# // Takes a file with 1 column of numbers and turns it into a new file with the numbers
# // in just one row separated by commas
data = open("workfile.txt").readlines()
file = open("newfile.txt", "w")
for n, line in enumerate(data):
    data[n] = line.rstrip()

file.write(','.join(data))
