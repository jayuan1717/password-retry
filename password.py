password = 'a123456'
timep = 3
import time
while True:
    entre = input('please entre the password: ')
    if entre == password:
        time.sleep(1.5)
        print('You have logged in')
        break
    else:
        time.sleep(1)
        print('incorrect password')
        timep = timep - 1
        if timep == 0:
            time.sleep(2)
            print('this account will be lock for 3 hours!')
            break
        else:
            time.sleep(1.5)
            print('remaining trail: ' , timep)
            time.sleep(2)