import random
from IPython.display import clear_output
def alter (s,e,a):
    if a == s:
        return e
    elif a == e:
        return s
    else:
        return False
def board(value , loc , l):
    i = 0
    j = 0
    t = False
    if loc <= 0 or loc >= 10:
        t = False
        print "1.Error"
    elif loc >= 1 and loc <= 3:
        i = 0
        j = loc-1
        t = True
    elif loc >= 4 and loc <= 6:
        i = 1
        j = loc-4
        t = True
    elif loc >= 7 and loc <= 9:
        i = 2
        j = loc-7
        t = True
    else:
        print "2.Error"
        t = False
    if l[i][j] == ' ':
        l[i][j] = value
        t = True
    else:
        print "LOC Error"
        t = False
    if t == True:
        return l
    if t == False:
        return t
def display(l):
    clear_output()
    print l[2][0],' | ',l[2][1],' | ',l[2][2]
    print "_____________\n"
    print l[1][0],' | ',l[1][1],' | ',l[1][2]
    print "_____________\n"
    print l[0][0],' | ' ,l[0][1],' | ',l[0][2]
while(1):
    global l
    l = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    ll = l
    print "Player 1 ... Choose x or o !!!"
    q = str ((raw_input()).upper())
    print q
    while not (q == "X" or q == "O"):
        print "Player 1 ... Choose x or o !!!"
        q = str ((raw_input()).upper())
    display(board(' ',5,l))
    while(1):
        value = q
        print "Player ",value," play!!!!!!"
        z = int (raw_input())
        l = board(value,z,ll)
        while(l == False):
            z = int (raw_input())
            l = board(value,z,ll)
        if type(l) == list:
            ll = l
        clear_output()
        display(l)
        y = False
        q = alter("X","O",q)
        for i in xrange(0,3):
            if (l[i][1] == l[i][2] and l[i][0] == l[i][1] and l[i][0] != ' '):
                print "Won!!!!!!",value
                value = q
                y = True
                break
        if y:
            break
        for i in xrange(0,3):
            if(l[0][i] == l[1][i] and l[1][i] == l[2][i] and l[0][i] != ' '):
                print "Won!!!!!",value
                y = True
                break
        if y:
            break
        if(l[0][0] == l[1][1] and l[1][1] == l[2][2] and l[1][1] != ' '):
            print "Won!!!!",value
            break
        if(l[2][0] == l[1][1] and l[1][1] == l[0][2] and l[1][1] != ' '):
            print "Won!!!",value
            break
        k = 0
        for i in xrange(0,3):
            for p in xrange(0,3):
                if l[i][p] != ' ':
                    k += 1
        if k == 9:
            print "Draw!!!!"
            break
    print "Again ?? y,n"
    ans = (raw_input()).upper()
    if(ans == 'Y'):
        clear_output()
        continue
    else:
        break
