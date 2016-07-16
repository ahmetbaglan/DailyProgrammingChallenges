

setLetterOrigin = {'A':(9,1), 'B':(2,3), 'C':(2,3), 'D':(4,2), 'E':(12,1), 'F':(2,4), 'G':(3,2), 'H':(2,4), 'I':(9,1), 'J':(1,8), 'K':(1,5), 'L':(4,1), 'M':(2,3), 'N':(6,1),
             'O':(8,1), 'P':(2,3), 'Q':(1,10), 'R':(6,1), 'S':(4,1), 'T':(6,1), 'U':(4,1), 'V':(2,4), 'W':(2,4), 'X':(1,8), 'Y':(2,4), 'Z':(1,10), '_':(2,0)}

setLetter = setLetterOrigin.copy()
numIn = 20

score = 0
while(True):

    print "your score:",score
    letters = raw_input("please enter: ")

    if(letters == "new"):#If user enters 'new' just start over
        setLetter = setLetterOrigin.copy()
        score = 0
        continue

    if(len(letters)> numIn):#if the input is too long just do not accept
        print "too much letter"
        continue
    else:
        for l in letters:
            if( (l not in setLetter) or setLetter[l][0]<=0 ): #if the letter is in the set
                print "not possible since not enough " + l
                break
            else:
                setLetter[l] = (setLetter[l][0] - 1, setLetter[l][1])#update the dect
                score += setLetter[l][1]#update score
        else:#if l is not in the set below code wont be processed
            out = {}
            for i in setLetter.keys():#compute an output dictionary
                if(setLetter[i][0] in out):
                    out[setLetter[i][0]] = out[setLetter[i][0]] + (i,)
                else:
                    out[setLetter[i][0]] = (i,)

            keyList = out.keys()
            keyList.sort(reverse = True)

            for i in keyList:
                s = ""
                for k in sorted(out[i]):
                    s += (k + ", ")
                print str(i) + " : " + s#print output
