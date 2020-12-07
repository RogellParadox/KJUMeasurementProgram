print ('안녕하세요! \nWelcome to Kim Jong-Un Measurement Program! \nPlease choose your system of measurement!')
choice = int (input('1 for meter | 2 for foot: '))

if choice == 1:
    centim = float (input('Type your height (in m): '))
    kjheight = centim /1.65
    print ('You are ', kjheight, ' kimjongheight tall!')
elif choice == 2:
    feet = float (input('Type your height (in feet): '))
    kjheight = feet /5.5
    print ('You are ', kjheight, ' kimjongheight tall!')
else:
    print ('You didnot enter a valid option, moron!')
