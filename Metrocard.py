#Name: Geethika Sasikumar
#Date: October 11, 2017
#This program says if unlimited or regular metrocard is better

x = (int(input('Please enter the number of rides: ')))

regularcard = 2.48*x
unlimitedcard = 31/x

if x == 1 or x == 2:
    print('You should buy a regular ticket')

else:
    print('You should buy a 7- day ticket')

if regularcard < unlimitedcard:
        print('You should buy a regular ticket')

else:
    print('You should buy a regular ticket')

