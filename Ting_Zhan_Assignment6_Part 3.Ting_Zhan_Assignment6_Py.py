def safe_input(prompt,convert ='float'):#to set convert's default value as float
    while True:
        answer = input(prompt)
        if convert == 'int':
            try:
                answer = int(answer)
                print(answer) ##print out the integer
                return answer
            except ValueError:
                print('Retype your answer.')
                
        elif convert == 'float':
            try:
                answer = float(answer)
                print(answer)
                return answer
            
            except ValueError:
                print('Retype your answer.')
                

        elif convert == 'string':
            print(answer) #we dont need to use the try&except here
            return answer
        
        else:
            print('Be serious!')

siblings = safe_input("How many siblings do you have?", convert='int')
degrees_c = safe_input("Enter the current temperature in Celsius.")
first_name = safe_input("What is your first name?", convert='string')









