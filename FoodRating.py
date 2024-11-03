#⭐️ Food Ratings Challenge by CodeDex
while True: 
    try:  
        rating = float(input('Please input your rating out of 5: '))  
        
        if 0 <= rating <= 5:   
            if rating > 4.5:  
                print('Extraordinary')  
            elif rating > 4:  
                print('Excellent')  
            elif rating > 3:  
                print('Good')  
            elif rating > 2:  
                print('Fair')  
            elif rating > 0:  
                print('Poor')  
            elif rating == 0:  
                print('Should not be allowed to exist')  
            break    
        else:  
            print('Invalid input, please rate from 0 to 5')   
    except ValueError:  
        print('Invalid input, please enter a number.')  
