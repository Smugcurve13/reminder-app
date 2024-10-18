reminder = input("did you work on project today: ")
if reminder == 'yes':
    userchoice = ''
    while userchoice != 'yes':
        userchoice = input("did you send msg : ")
        if userchoice == 'yes':
            print('ok, see you tomorrow')
            break
        else:
            print("send msg fast")
else:
    print('Understandable, Have a good day!')