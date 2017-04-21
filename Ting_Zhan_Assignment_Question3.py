##R refers to diameter of a pizza, p refers to the price of a pizza
import math
def main():
    R = float(input('Enter the diameter(inch) of pizza:'))
    Price = float(input('Enter the price(USD dollar) of pizza:'))
    print('the cost per square inch of a circular pizza is', round(Price/(math.pi*(R/2)**2),2))

main()
