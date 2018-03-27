while True:
    try:
        num = int(input('Vpiši poljubno število!\n'))
        num2 = int(input('Vpiši še eno poljubno število!\n'))
        break
    except ValueError:
        print('Nisi vnesel števlke!\n')

rezultat_deljenja = num%num2
if num%2 is 0:
    if num%4 is 0:
        print('Število '+str(num) + ' je deljivo z 4')
    else:
        print('Število je sodo!')
else:
    print('število je liho')

if rezultat_deljenja is 0:
    print('Če delimo '+ str(num)+ ' s ' + str(num2)+ ' je rezult celo število')
else:
    print('Število '+ str(num)+ ' ni deljivo s ' +str(num2))