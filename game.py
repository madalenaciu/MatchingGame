from time import sleep
   

def name(n):
    """
    Epistrefei taksinomhmenh lista onomatwn
    n--o arithmos twn paiktwn
    """
    list1=[] #lista onomatwn
    for i in range (n):
        nam=input('Δώστε όνομα παίκτη:')
        list1.append(nam)
    list1.sort()
    return list1

def trapoula(d):
    """
    Dhmiourgei lista me ta hartia ths trapoulas analoga  me to bathmo dyskolias
    d--bathmos dyskolias

    """
    from random import shuffle
    listn=['A' , '1' , '2' , '3' , '4' , '5', '6' , '7' , '8' , '9']
    lists=['K' , 'Q', 'J']
    liste=['♥' , '♠' ,'♣', '♦']
    list2=[] #lista me ta trapouloharta
    if d==1:
        for i in liste:
            for j in lists:
                list2.append(i+j)
            list2.append(i+'10')
    elif d==2:
        for i in liste:
            for j in listn:
                list2.append(i+j)
    else:
        for i in liste:
            for j in lists:
                list2.append(i+j)
            for z in listn:
                list2.append(i+z)
    shuffle(list2)
    return nest(list2 , d)

def empty(d):
    """
    Dhmiourgei lista  me ton xarakthra 'X' analoga me ton bathmo dyskolias , h opoia anaparista thn kleisth trapoula
    d--bathmos dyskolias 

    """
    listx=[]
    if d==1:
        for i in range(16):
            listx.append('X')
    elif d==2:
        for i in range(40):
            listx.append('X')
    else:
        for i in range(52):
            listx.append('X')
    return nest(listx , d)

def nest(ls , d):
    """ 
    Epistrefei fwliasmenh lista
    ls--dwsmenh lista
    d--bathmos dyskolias
    """
    if d==1:
        l=4 #krataei ton arithmo twn stoixeiwn ana grammh
    elif d==2:
        l=10
    else:
        l=13
    list4=[] 
    k=0 #deikths pou anaparista thn thesh twn  stoixeiwn thw listas ls 
    m=1 #deikths pou anaparista ton arithmo ths sthlhs(1-4) kai eisxwreite vw prvto stoixeio ths listas
    list3=[str(x) for x in range(l+1)]#Kataskeuazei thn prvth grammh tou pinaka poy periexei thn arithmhsh
    list4.append(list3)
    for i in range(0 , len(ls) , l):
        list3=[]
        s=0
        list3.append(str(m))
        m=m+1 #afksanetai kata 1 mexri na ftasei ton arithmo twn sthlwn tou pinaka
        while s<l:
            list3.append(ls[k])
            s=s+1
            k=k+1
        list4.append(list3)
    return list4 #fwliasmenh lista

def table(ls ):
    """
    Epmfanizei  thn trapoula se morfh pinaka
    ls--fwliasmenh lista

    """
    for item in ls: 
        k=''
        for h in item:
            k=k+h+" "*(5-len(h)) #H praksh (5-len(h))*" " mas bohthaei stona ftiaksoume omoiomorfa ton pinaka
        print(k)


def func(s, m):
    """
    Epistrefei  egkyrh timh(arithmos grammhs 'h sthlhs) pou dinei o paikths gia thn epilogh ths kartas
    s--orio elegxoy wste mia timh tou paikth na  einai egkyrh
    m--arithmos kartas
    """
    if m==1:
        if s==4:
            n1=int(input('Δώσε την γραμμή της πρώτης κάρτας:'))
        else:
            n1=int(input('Δώσε την στήλη της πρώτης κάρτας:'))
    elif m==2:
        if s==4:
            n1=int(input('Δώσε την γραμμή της δεύτερης κάρτας:'))
        else:
            n1=int(input('Δώσε την στήλη της δεύτερης κάρτας:'))
    else:
        if s==4:
            n1=int(input('Δώσε την γραμμή της κάρτας:'))
        else:
            n1=int(input('Δώσε την στήλη της κάρτας:'))

    while (n1)<=0 or (n1)>s:
        n1=int(input('Λάθος εκχώρηση! Ξαναπροσπάθησε:'))
    return (n1)

def funcX( r , c , listaX , fin , listaT):
    """
    Epistrefei to stoixeio ths listas pou anaparista ta trapouloxarta  , to opoio den perilambanetai sthn lista me ta 'X'
    r--arithmos grammhs
    c--arithmos sthlhs
    listaX--lista pou anaparista thn kleisth trapoula
    fin--orio elegxou
    listaT--lista pou anaparista ta trapouloxarta

    """
    if listaX[r][c] != 'X':
        print('Η κάρτα είναι ήδη ανοιχτή')
        r=func(4 , 3)#grammh kartas
        c=func(fin ,3) #sthlh kartas
    listaX[r][c]=listaT[r][c]#antikathista thn kleisth karta me thn antistoixh karta ths trapoulas
    return listaT[r][c]


def menu ():
    """
    Emfanizei to menu epilogwn stous paiktes kai ylopoiei to paixnidi

    """
    print('Καλωσήρθατε στο Matching Game!!')
    sleep(1)
    print('Menu')
    players=int(input('Eπιλέξτε έναν αριθμό παικτών από 2 και πάνω:'))
    while (players) < 2:
        players=int(input('Μη έγκυρος αριθμός παικτών!Eπιλέξτε έναν αριθμό παικτών από 2 και πάνω:'))
    sleep(1)
    print('Βαθμός δυσκολίας:')
    print('1.Eύκολο')
    print('2.Μέτριο')
    print('3.Δύσκολο')
    dif=int(input('Επιλέξτε βαθμό δυσκολίας:'))
    while dif< 1 or dif>3:
        dif=int(input('Λάθος! Επιλέξτε έναν έγκυρο βαθμό δυσκολίας (1 , 2 , 3):'))
    names=name(players) #lista me ta onomata twn paiktwn
    t=trapoula(dif) #fwliasmenh lista me thn trapoula
    x=empty(dif)  #fwliasmenh lista krummenhs trapoulas
    print('Προσπαθήστε να απομνημονεύσετε τα φύλλα της τράπουλας:')
    table(t) #Emfanizei anoixth thn trapoula 
    sleep(4)
    print('To παιχνίδι ξεκινάει')
    sleep(1)
    print('Οι παίκτες παίζουν με αλφαβητική σειρά:')
    for k in range (players):
        print( str(k+1)+ ':' + names[k])
    score=[] #lista pou sygkratei to score twn paiktwn 
    for i in range(players):
        score.append(0)
    if dif==1:
        amount=16 #ammount-synolo kleistwn kartwn
        y=4 #y-arithos stoiheiwn ana grammhs analoga me to epipedo dyskolias
    elif dif==2:
        amount=40
        y=10
    else:
        amount=52
        y=13
    pl=1 #deikths pou deixnei poios paikths agwnizetai
    cardK=False #metablhth pou exei ws timh ths thn timh True sthn periptwsh poy yparksei trith karta kai einai 'k'
    while amount >=2:
        sleep(1)
        print('Παίζει ο παίκτης:',pl )
        table(x) #Emfanizei thn kleisth trapoula
        x1=func(4 , 1) #grammh prwths kartas
        y1=func(y , 1) #sthlh prwths kartas
        num1=funcX(x1,y1 , x , y , t) #prwth epilegmenh karta
        table(x)
        x2=func(4 , 2) #grammh deyterhs kartas
        y2=func(y , 2) #sthlh deyterhs kartas
        num2=funcX(x2 , y2 ,x, y , t ) #deyterh epilegmenh karta
        table(x)
        if num1[-1]==num2[-1]:
            amount=amount-2 #An duo kartes einai idies toteto plhthos twn kleistwn kartwn meiwnetai kata duo
            if num1[-1]=='A':
                score[pl-1]+=1
            elif num1[-1]=='J' or num1[-1]=='K' or num1[-1]=='Q':
                score[pl-1]+=10
            elif int(num1[-1])==0:
                score[pl-1]+=10
            else:
                score[pl-1]+=int(num1[-1])
        elif (num1[-1]=='Q' and num2[-1]=='K') or (num1[-1]=='K' and num2[-1]=='Q'):
            print('Επιλέξτε μία τρίτη κάρτα:')
            x3=func(4, 3) #grammh triths kartas
            y3=func(y,3)  #sthlh triths kartas
            num3=funcX(x3 , y3 , x , y , t) #trith karta
            table(x)
            if num1[-1]==num3[-1]:
                score[pl-1]+=10
                x[x2][y2]='X' #kleinei thn deyterh karta
                amount=amount-2
            elif num2[-1]==num3[-1]:
                score[pl-1]+=10
                x[x1][y1]='X'#kleinei thn prwth karta
                amount=amount-2
            else:    #kleinei kai tis treis kartes
                x[x1][y1]='X'
                x[x2][y2]='X'
                x[x3][y3]='X'
            if num3[-1]=='K' and (num3[-1]==num1[-1] or num3[-1]==num2[-1]):
                pl=pl+1  
                cardK=True
        else:
            x[x1][y1]='X'
            x[x2][y2]='X'
        if (num1[-1]==num2[-1]):
            if (num1[-1]!='J' and num1[-1]!='K') or (num2[-1]!='J' and num2[-1]!='K'): 
                pl=pl+1
            elif num1[-1]=='K':
                if players==2:
                    pl=pl
                elif pl==players:
                    pl=2
                else:
                    pl=pl+2
        else:
            pl=pl+1
        if pl>players:
            if cardK==False:
                pl=1 
            else:
                if pl-2==players: #An yparksei trith karta h opoia exei ton xarakthra 'K' kai o paikths pou epaize htan o teleutaios : paizei o 2os paikths
                    pl=2
                elif pl-1==players:#An yparksei trith karta h opoia exei ton xarakthra 'K' kai o paikths pou epaize htan o proteleutaios : paizei o 1os paikths
                    pl=1
                
                
    maximum=score[0] #Evresh tou megistou score kai kata synepeia eyresh tou nikhth
    for i in range (1 , players):
        if maximum<score[i]:
            maximum=score[i]
    nikhtes=[] #lista pou periexei ta onomata twn paiktwn pou exoyn idio score me to maximum
    for i in range (1,players):
        if maximum==score[i]:
            nikhtes.append(names[i])
    if len(nikhtes)==1:
        print('O νικητής του παιχνιδιού είναι ο ' , nikhtes[0])
    else:
        print('Το παιχνίδι λήγει με ισοπαλία ανάμεσα στους παίκτες:')
        for i in (nikhtes):
            print(i)
    sleep(2)
    print('Tέλος παιχνιδιού')
    
    


if __name__ == "__main__":
    menu()



 
       




        






    



