
def critic(lenT, n):
    return  n * lenT - n

def draw (text, width = 1, height = 1):
    indexH = 0
    lol = 0
    for m in range(len(text)* height -1):
        k = 0
        x = 0
        reverse = True
        toBePrinted = ""

        if( m == critic(len(text), indexH)):
            indexH+=1
            text = text[::-1]
            while x<=width:
                toBePrinted = toBePrinted + text[k]

                if(k == len(text) - 1 or k == 0):
                    reverse = not reverse
                    x += 1
                if(reverse):
                    k = k-1
                else:
                    k = k+1
            print toBePrinted
            lol = 0
            if(indexH == height+1):
                return
        else:
            indexW = 0
            lol += 1
            for j in range(width*len(text)):
                f = lol
                ilk = text[f]
                iki = text[-f - 1]
                if(j==critic(len(text), indexW)):
                    a = ilk if indexW%2 == 0 else iki
                    toBePrinted+= a
                    indexW+=1
                else:
                    toBePrinted+=" "
            print toBePrinted



draw("REKTO",4,2)
