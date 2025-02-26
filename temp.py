keyword_table = {
    "if": 0x01,
    "input": 0x02,
    "int": 0x03,
    "for": 0x04,
    "def": 0x05,
    "return": 0x06,
    "while": 0x07,
    "print": 0x08,
    "+": 0x09,
    "=": 0x10,
    "*": 0x11,
    "/": 0x12,
    "(": 0x13, 
    ")": 0x14,
    ":": 0x15,
    ",": 0x16,
    "==": 0x17,
    "!=": 0x18,
    ">": 0x19,
    "<": 0x20,
    ">=": 0x21,
    "<=": 0x22
}

symbol_table = {

}

arr = []
with open("sourcecode.txt", 'r') as f:
    for line in f:
        if line[0] != "#" and line != '\n':
            arr.append(line.strip())

lex = [i.split() for i in arr]
print(lex)

tokenizedlist = []

tokenid = 0x50

for c, j in enumerate(lex):
    line = j
    x = ""
    for n in line:
        try:
            hexvalue = keyword_table[n]
        except KeyError:
            if n in symbol_table:
                hexvalue = symbol_table[n]
            else:
                symbol_table[n] = tokenid
                hexvalue = tokenid
                tokenid += 1
        x = x + str(hex(hexvalue))
    tokenizedlist.append(x)
    x = ""

def ifcheck(line):
    tokened = line.split("0x")
    tokened.pop(0)
    print(tokened)
    if tokened[0] == "1" and tokened[-1] == 15:
        if hex(int(tokened[1])) not in symbol_table.values():
            
            raise ValueError("Variable does not exist")
        elif tokened[2] not in [str(i) for i in range(17, 23)]:
            raise SyntaxError("No comparison(for this example)")
        elif hex(int(tokened[3])) not in symbol_table.values():
            raise ValueError("Variable does not exist")
    else:
        raise SyntaxError("No if!")
    
    print("pass")


print(symbol_table)

for i in tokenizedlist:
    ifcheck(i)
#j = i.split("0x")
#    for n in j:
#        print(n)








