some_file = open("../files/example.txt", "r")

#print(some_file.read())
# Read the exact bites amount
#print(some_file.read(4))

# Read a single line
#print(some_file.readline())

# Get all lines as list
#print(some_file.readlines(), "\n")
print(some_file.read(4))
print(some_file.read(100))
print(some_file.read(100))

print("=====")
# Read from current cursor position till the end
#print(some_file.read())

# Position cursor within the file
some_file.seek(0)
print(some_file.read(4))
# To open it as writable use r+
# some_file.write("test")

some_file.close()
