import re
f = open("121516.csv","r")
o = open("output.csv","w")
cntr=0
date = None
for line in f:
    #print(line)
    if ",,,,," in line :
        if cntr > 8:
            break
    else:
        if cntr == 5:
            tokens = re.split("\s+", line)
            date = tokens[2]
            print tokens
            #print(tokens)
        elif cntr >= 8:
            line = line.replace(",,", ",")
            line = line.strip()
            o.write(line + "," + date +"\n")
    cntr +=1