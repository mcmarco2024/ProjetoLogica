import random
palavras=['pytthon', 'programação ', 'desenvolvimento', 'tecnologia']
palavra=random.choice(palavras)
palavra_oculta=[ ]

for i in range(len(palavra)):
    palavra_oculta.append('?')
    vida=7
while True:
    if vida==7:
        print ('                _____________  ')
        print ('                I           I  ')
        print ('                            I  ')
        print ('                            I  ')
        print ('                            I  ')
        print ('                            I  ')
    elif vida==6:
        print ('                _____________   ')
        print ('                I            I  ')
        print ('                O            I  ')
        print ('                             I  ')
        print ('                             I  ')
        print ('                             I  ')
    elif vida==5:
        print ('                _____________  ')
        print ('               I            I  ')
        print ('               O            I  ')
        print ('              <             I  ')
        print ('                            I  ')
        print ('                            I  ')
    elif vida==4:
        print ('                _____________  ')
        print ('                 I           I  ')
        print ('                 O           I  ')
        print ('              <  I           I  ')
        print ('                             I  ')
        print ('                             I  ')
    elif vida==3: 
        print ('                _____________   ')
        print ('               I            I   ')
        print ('               O            I   ')
        print ('             < I >          I   ')
        print ('                            I   ')
        print ('                            I   ')
    elif vida==2:
        print ('                _____________   ')
        print ('               I            I   ')
        print ('               O            I   ')
        print ('            <  I >          I   ')
        print ('               I            I   ')
        print ('                            I   ')
    elif vida==1:
        print ('                _____________   ')
        print ('                I           I   ')
        print ('                O           I   ')
        print ('             <  I >         I   ')
        print ('                I           I   ')
        print ('               /            I   ')
    elif vida==0:
        print ('                _____________   ')
        print ('                I            I  ')
        print ('                O            I  ')
        print ('             <  I >          I  ')
        print ('                I            I  ')
        print ('               /|            I  ')
        break
    print ('palavra secreta:', palavra_oculta)
    letra=input('digite uma letra\n\n')
    if not (letra in palavra):
        vida=vida-1
    else:
        if letra in palavra and letra in palavra_oculta:
            vida=vida-1
        else:
            for i in range(len(palavra)):
                if letra == palavra [i]:
                    palavra_oculta[i]=palavra [i]
    if vida==0:
        print ("Fim do jogo você  perdeu")
        break
    if "?" not in palavra_oculta:
        print ('Parabéns  você  venceu o jogo')
        print (f'palavra{palavra} descoberta')
        break

