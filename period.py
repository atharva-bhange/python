f = open(input("Enter file name: ") , "r")
for line in f:
    if line.startswith("test"):
        ls = [int(l) for l in line.split("=")[1].strip()[1:-1].split(",")]
        length = len(ls)
        counter = 0
        periods = []
        period = 0
        status = False
        for l in range(len(ls)):
            if ls[l] == 0:
                if l+1 < length  and l+2 <length:
                    if ls[l+1] == 1 and ls[l+2] == 1:
                        if status:
                            counter+=1
                            periods.append(period)
                            period = 1
                        else:
                            status = True
                            period+=1
                    elif status:
                        period +=1
                elif status:
                    period+=1
            elif status:
                period+=1
            if len(periods) ==2:
                break
        print(line.split("=")[0],periods[0])
