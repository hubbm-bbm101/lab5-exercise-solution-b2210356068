#exercise1
N=int(input("enter a number "))
def sum_of_numbers(N) :
    sum=0 
    for n in range (1,N+1):
        if (n % 2 !=0) :
            sum=sum+n
            
    return sum   
print("Sum of odd numbers  :" , sum_of_numbers(N)) 



def avr_of_even_numbers(N) : 
    sum = 0 
    even_numbers= 0
    for n in range (1,1+N) :
        if (n % 2 == 0) :
            sum= sum + n
            even_numbers +=1
      
    return sum/even_numbers

print("Average of even numbers : " , avr_of_even_numbers(N)) 