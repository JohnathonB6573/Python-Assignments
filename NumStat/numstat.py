#initialization
file1 = "numbers.txt"
arr = [100]
f = open(file1, "r")
Sum = 0
Count = 0
Average = 0
Maximum = 0
Minimum = 0
Range = 0

#reading the file and adding it to a dynamic array
while f.read():
    arr.append(f.readline())

for x in range(len(arr)):
    Sum += int(float(arr[x]))

Count = len(arr)

#print
print("File name:", f.name)
print("Sum:", Sum)
print("Count:", Count)
print("Average:", Average)
print("Maximum:", Maximum)
print("Minimum:", Minimum)

#close file
f.close()


