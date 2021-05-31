# cook your dish here
def sol(s):
    lang1 = 0
    lang2 = 0
    for i in s:
        lang1 = 0
        lang2 = 0
        for j in i:
            if j.islower() and j>="a" and j<="m":
                if lang2>0:
                    return "No"
                else:
                    lang1 += 1
            elif j.islower() and j<"a" and j>"m":
                return "No"
            else:
                if lang1>0:
                    return "No"
                elif j.isupper() and j>="N" and j<="Z":
                    lang2 += 1
                else:
                    return "No"
                    
    return "Yes"
    
    
if __name__ == "__main__":
    t = int(input())
    while t>0:
        try:
            arr = input()
            s = []
            temp = ""
            for i in arr:
                if i.isalpha() == True and i!=" ":
                    temp = temp+i 
                elif i == " ":
                    if len(temp)>0:
                        s.append(temp)
                        temp = ""
            
            if len(temp)>0:
                s.append(temp)
            print(sol(s))
            
        except Exception as e:
            print(e)
        t = t-1
                    
else:
    pass