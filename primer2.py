name = input('Vpiši svoje ime\n')

while True:
    try:
        age = int(input('Vpiši svojo starost\n'))
        break
    except ValueError:
        print('Vpiši starost s številko\n')

if age <= 99:
    letnica_rojstva = (2018-age) + 100
    letnica_rojstva_str = str(letnica_rojstva)
    print(name + ' v letu '+letnica_rojstva_str+' boste stari 100 let!')

    while True:
        try:
            nova_st = int(input('Vnesi novo število od 1 do 100\n'))
            break
        except ValueError:
            print('Vnesi število')
    i = 1
    if nova_st <=100:
        while i <= nova_st:
            i+=1
            print('V letu '+letnica_rojstva_str+' boste stari 100 let')
    else:
        print('Vnesel si preveliko število')
else:
    print('Vnesel si preveliko številko')