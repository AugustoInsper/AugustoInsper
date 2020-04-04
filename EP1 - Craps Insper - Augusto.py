import random
import time
fichas=100
fase='\nPRIMEIRA FASE: Come Out\n'

while input('\n\nPara nova(s) aposta(s), digite "s" e aperte "Enter", caso contrário, somente aperte "Enter": ')=='s':
    
    print('\nVocê tem {0} fichas'.format(fichas))
    time.sleep(1)
    print(fase)
    time.sleep(1)
    if fase=='\nPRIMEIRA FASE: Come Out\n':
        print('Essas são as apostas possíveis:\nPass Line Bet\nField\nAny Craps\nTwelve\n')
    else:
        print('Essas são as apostas possíveis:\nField\nAny Craps\nTwelve')
    time.sleep(2)
    print('\nDigite "s" nos seguintes tipos de aposta que desejar apostar e "n" nos quais não desejar apostar:')
    time.sleep(1)
    
    
    #Mostrando os tipos de apostas disponíveis:
    
    if fase=='\nPRIMEIRA FASE: Come Out\n':
        plb=input('Pass Line Bet: ')
    fd=input('Field: ')
    ac=input('Any Craps: ')
    tw=input('Twelve: ')
    
    
    #Pedindo as apostas:
    
    if plb=='s' and fase=='\nPRIMEIRA FASE: Come Out\n':
        aposta_plb=int(input('\nDigite aqui o valor da sua aposta para Pass Line Bet: '))
    if fd=='s':
        aposta_fd=int(input('\nDigite aqui o valor da sua aposta para Field: '))
    if ac=='s':
        aposta_ac=int(input('\nDigite aqui o valor da sua aposta para Any Craps: '))
    if tw=='s':
        aposta_tw=int(input('\nDigite aqui o valor da sua aposta para Twelve: '))
    

    r=random.randint(2,12) #somas possíveis dos resultados de dois dados

    
    # Para o tipo de aposta Pass Line Bet:
    
    if plb=='s' and fase=='\nPRIMEIRA FASE: Come Out\n':
        
        print('\nPass Line Bet:')
        time.sleep(1)
        print('A soma dos dados foi {0}'.format(r))
        time.sleep(1)
        
        if r==7 or r==11:
            print('Ganhou a aposta')
            fichas+=aposta_plb
            
        elif r==2 or r==3 or r==12:
            print('Perdeu a aposta')
            fichas-=aposta_plb
            
        else:
            fase='\nSEGUNDA FASE: Point\n'
            print(fase)
            while True:
                time.sleep(1)
                r2=random.randint(2,12)
                print('A nova soma dos dados foi {0}'.format(r2))
                if r2==r:
                    fichas+=aposta_plb
                    print('Ganhou a aposta')
                    break
                elif r2==7:
                    fichas=0
                    print('Perdeu tudo!')
                    break
            if r2==7:
                break
        
        time.sleep(1)
        print('Você tem {0} fichas'.format(fichas))


    # Para o tipo de aposta Field:

    if fd=='s':
        
        print('\nField:')
        time.sleep(1)
        print('A soma dos dados foi {0}'.format(r))
        time.sleep(1)
        
        if 5<=r<=8:
            fichas=0
            print('Perdeu tudo!')
            break
            
        elif r==2:
            fichas+=2*aposta_fd
            print('Ganhou a aposta em dobro')
            
        elif r==12:
            fichas+=3*aposta_fd
            print('Ganhou a aposta em triplo')
            
        else:
            fichas+=aposta_fd
            print('Ganhou a aposta')
            
        time.sleep(1)
        print('Você tem {0} fichas'.format(fichas))


    # Para o tipo de aposta Any Craps:
  
    if ac=='s':
        
        print('\nAny Craps:')
        time.sleep(1)
        print('A soma dos dados foi {0}'.format(r))
        time.sleep(1)
        
        if r==2 or r==3 or r==12:
            fichas+=7*aposta_ac
            print('Ganhou 7x (sete vezes) a aposta')
        
        else:
            fichas-=aposta_ac
            print('Perdeu a aposta')
            
        time.sleep(1)
        print('Você tem {0} fichas'.format(fichas))



    # Para o tipo de aposta Twelve:

    if tw=='s':
        
        print('\nTwelve:')
        time.sleep(1)
        print('A soma dos dados foi {0}'.format(r))
        time.sleep(1)
        
        if r==12:
            fichas+=30*aposta_tw
            print('Ganhou 30x (trinta vezes) a aposta')
            
        else:
            fichas-=aposta_tw
            print('Perdeu a aposta')
            
        time.sleep(1)
        print('Você tem {0} fichas'.format(fichas))
  

# Finalização:

time.sleep(1)
print('FIM DE JOGO')
time.sleep(1)
print('Você terminou com {0} fichas'.format(fichas))