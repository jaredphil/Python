# // Takes a file with 1 column of numbers and turns it into a new file with the numbers
# // in just one row separated by commas
data = open("1000kHz BK 1024samples.txt").readlines()
file = open("newfile.txt", "w")
# for i in range (1, 10):
#     print(i)
for n, line in enumerate(data):
    data[n] = line.rstrip()
    file.write(data[n])
    file.write(',')
    if n %10 == 9:
        file.write('\n')

        
# file.write(','.join(data[line(0,10)]))

# file.write(','.join(data))
