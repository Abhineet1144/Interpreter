print("Type run to execute the code")
print("Leave blank to go to previous indentation\n\n")
c = ""
i = 0
line = 1
while True:
    if i < 0:
        i = 0
        
    if line < 10:
        sl = "00" + str(line) + "|"

    elif line < 100:
        sl = "0" + str(line) + "|"

    else:
        sl = "" + str(line) + "|"

        
    l = "\t" * (i) + input(sl + "\t" * (i))
    #l = l.replace("'", r"\'")
    line += 1
    '''if l.isspace():
        i -= 1
        continue'''
    
    if l.strip().lower() == "run":
        break

    try:
        if l.rstrip()[-1] == ":":
            i += 1
    except:
        i -= 1
        continue
        
    c += (l + "\n")

print("\n\nSource Code:\n", c, sep = "")
print("\nOUTPUT:")
op = str(exec(c))
op = op.strip("None")

print(op)
