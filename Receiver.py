
str = ""
for i in range(0, len(binary), 8):
    binc = binary[i:i + 8]
    num = int(binc, 2)
    str += chr(num)
print(str)