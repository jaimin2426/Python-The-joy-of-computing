import string
# dictionary to store mappings
dict = {}
data = ""

# open output file in write mode
file = open("op_file.txt", "w")

# create dictionary mapping ascii_letters to themselves
for i in range(len(string.ascii_letters)):
    dict[string.ascii_letters[i]] = string.ascii_letters[i-1]

print(dict)

# open input file in read mode
with open("ip_file.txt") as f:
    while True:
        c = f.read(1)   # read one character
        if not c:
            print("End of file")
            break
        if c in dict:
            data = dict[c]
        else:
            data = c
        file.write(data)
        print(data)

file.close()
