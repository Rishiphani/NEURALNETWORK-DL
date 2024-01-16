input_string = list(input("Enter the string : "))

if len(input_string) >= 2:
    del input_string[:2]

resultant_string = input_string[::-1]

print("Reversed Resultant String:", ''.join(resultant_string))


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


sum_result = num1 + num2
difference_result = num1 - num2
product_result = num1 * num2
quotient_result = num1 / num2

print("Sum:", sum_result)
print("Difference:", difference_result)
print("Product:", product_result)
print("Quotient:", quotient_result)
