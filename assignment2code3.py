def inches_to_centimeters_loop(heights_inches):
    heights_centimeters = []
    for height in heights_inches:
      
        height_cm = height * 2.54
        heights_centimeters.append(round(height_cm, 2))
    return heights_centimeters

def inches_to_centimeters_comprehension(heights_inches):
    return [round(height * 2.54, 2) for height in heights_inches]

def main():
  
    heights_inches = []
    num_customers = int(input("Enter the number of customers: "))
    for i in range(num_customers):
        height = float(input(f"Enter height in inches for customer {i + 1}: "))
        heights_inches.append(height)


    heights_cm_loop = inches_to_centimeters_loop(heights_inches)
    print("Heights in Centimeters (Using Nested Loop):", heights_cm_loop)

  
    heights_cm_comprehension = inches_to_centimeters_comprehension(heights_inches)
    print("Heights in Centimeters (Using List Comprehension):", heights_cm_comprehension)

if __name__ == "__main__":
    main()
