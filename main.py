import mileskm
import inchcm
import feetm
import yardm
import gallonsl
import poundkg
import ounceg

value = float(input("How many units of your chosen item would you like to convert? "))
choice = int(input("What would you like to convert? Press: \n1 for inches to centimeters\n2 for miles to kilometers\n3 for feet to meters\n4 for yards to meters\n5 for gallons to liters\n6 for pounds to ounces\n7 for ounces to grams\n8 for cm to inches \n9 for km to miles\n10 for meters to feet\n11 for meters to yards\n12 for liters to gallons\n13 for kilograms to pounds\n14 for grams to ounce\nFinally, press anything else to stop the program."))

if choice == 1:
    inchcm.inchtocm(value)
elif choice == 2:
    mileskm.milestokm(value)
elif choice == 3:
    feetm.feettom(value)
elif choice == 4:
    yardm.yardtom(value)
elif choice == 5:
    gallonsl.gallonstol(value)
elif choice == 6:
    poundkg.poundstokg(value)
elif choice == 7:
    ounceg.ouncetograms(value)
elif choice == 8:
    inchcm.cmtoinch(value)
elif choice == 9:
    mileskm.kmtomiles(value)
elif choice == 10:
    feetm.mtofeet(value)
elif choice == 11:
    yardm.mtoyard(value)
elif choice == 12:
    gallonsl.ltogallons(value)
elif choice == 13:
    poundkg.kgtopounds(value)
elif choice == 14:
    ounceg.gramstoounce(value)
else:
    print("Goodbye!")