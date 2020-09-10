# Sample script to convert a file from raw csv ( file generated for a day's data directly from .xls (file from the dining data)

import re, datetime, csv

def _cleanseCsv(inFile, outFile) :
    cntr=0
    date = None
    for line in inFile:
        #print(line)
        if ",,,,," in line :
            if cntr > 8:
                break
        else:
            if cntr == 5:
                tokens = re.split("\s+", line)
                date = tokens[2]
                #print tokens
                #print(tokens)
            elif cntr == 6:
                tokens = re.split(":", line)
                cafe = tokens[1]
                cafe = cafe.replace(',,,,','').strip()
                #print cafe
            elif cntr >= 8:
                line = line.replace(",,", ",")
                line = line.strip()
                day = datetime.datetime.strptime(date, '%Y-%m-%d').weekday()
                outFile.write(line + "," + date + "," + str(day)+ "," + cafe + "\n")
        cntr +=1

def cleanseCsv(list):
    for path in list:
        in1 = open(path,"r")
        p = path.split("/")
        print p[-1]
        p[-1] = "clean" + p[-1]
        delim='/'
        opPath = delim.join(p)
        opFile = open(opPath,"w")
        _cleanseCsv(in1, opFile)
        in1.close()
def main():
    in1 = open("121516.csv","r")
    clean1 = open("output.csv","w")
    in2 = open("121516.csv","r")
    clean2 = open("output1.csv","w")
    _cleanseCsv(in1, clean1)
    in1.close()
    in2.close()


if __name__ == '__main__':
    main()
