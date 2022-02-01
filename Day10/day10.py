with open('test.txt') as file:
    lines = file.readlines()
    lines = [l.strip() for l in lines]


#print(lines)
chunk = []
sym = {"[": "]", "(": ")", "{": "}", "<": ">"}



for line in lines:
    for char in line:
        if char in sym.keys():
            chunk.append(char)
        #elif char in sym.values():
            

print(chunk)