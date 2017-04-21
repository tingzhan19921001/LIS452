def main():
    p = eval(input("principal:"))
    apr = eval(input("annual interest rate:"))
    n = eval(input("investment years:"))
    p = p*(1-(1+apr)**n)/(-apr)
    print("the total amount is:",p)
main()
