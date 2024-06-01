#Non-void function
def convert_to_rupees(dollars, conversion_rate):
    return dollars * conversion_rate

# main
dollars = 100
conversion_rate = 83.42  #The day on which this code was written 1 dollar was equal 83.42 rupees
rupees = convert_to_rupees(dollars, conversion_rate)
print(f"{dollars} dollars is equal to {rupees} rupees.")



#Void function
def print_conversion_to_rupees(dollars, conversion_rate):
    rupees = dollars * conversion_rate
    print(f"{dollars} dollars is equal to {rupees} rupees.")

# main
dollars = 150
conversion_rate = 83.42  #The day on which this code was written 1 dollar was equal 83.42 rupees
print_conversion_to_rupees(dollars, conversion_rate) 
