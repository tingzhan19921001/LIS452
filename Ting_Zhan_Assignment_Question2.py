## sum refers the addition of all numbers, count refers to how many numbers are entered, 
##solution 1 use else if to resolve
print('\nEnter a single integer to add to the series, or enter a blank line to quit.')
sum=0
count=0
while True:
    command = input('Next Number?')
    if command == ' ': 
        break

    else:
        n = int(command)
        sum = n + sum
        count = count+1
        average = sum/count

    print('the square is', n**2,
          ',', count,'numbers entered,', 'Sum is', sum,',''average is',('%.3f'%average))


print('Finished. Have a nice day!')


##solution 2_use range
numbers = int(input("How many numbers do you want to enter?"))
sum = 0
count = 0
for count in range(0, numbers):
     n = int(input('Next Number:'))
     sum = n + sum
     count = count + 1
     average = sum/count
     print('the square is', n**2,',', count,'numbers entered,', 'Sum is', sum,',''Average is',('%.3f'%average))
    


     
