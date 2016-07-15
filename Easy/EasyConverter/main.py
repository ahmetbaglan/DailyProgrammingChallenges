import math

roundDigit = 2

def check(fromType,toType,allowed):
    for i in allowed.keys():
        if((fromType in allowed[i]) and (toType in allowed[i])):
            return i
    return None


def convertAngle(f,t,v):

     if(f == 'd' and t == 'r'):
        return  str(v * math.pi/180) + t
     elif ( f == 'r' and t == 'd'):
         return  str(v * 180/math.pi) + t

     return None


def convertTemp(f,t,v):
    def celToFah(c):
        return str(32 + 1.8 * c) + t
    def fahToCel(f):
        return str((f-32)/1.8) + t

    if(f == 'k' and t == 'c'):
        return  str(v - 273) + t
    elif ( f == 'c' and t == 'k'):
        return  str(v + 273) + t
    elif (f == 'c' and t == 'f'):
        return celToFah(v)
    elif (f == 'f' and t== 'c'):
        return fahToCel(v)
    elif (f == 'k' and t=='f'):
        return celToFah(v-100)
    elif(f == 'f' and t == 'k'):
        return fahToCel(v)+100
    else:
        return None
    return None



def main():
    allowed_conversions = {'ang' : ['d','r'], 'temp':['k','c','f']}
    while(True):
        a = raw_input("Please Enter Your Input: ")
        fromType = a[-2]
        toType = a[-1]
        value = float(a[:-2])

        convertType = check(fromType,toType,allowed_conversions)
        if(convertType == None):
            print "Not a possible conversion"
        elif(convertType == 'ang'):
            print convertAngle(fromType,toType,value)
        elif( convertType == 'temp'):
            print convertTemp(fromType,toType,value)


main()







