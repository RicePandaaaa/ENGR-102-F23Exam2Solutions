def numcondition():
    """ 
    Asks for two values and verifies:
     - Sum exceeds 10
     - Product exceeds 20
    """

    # Get input
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    # Verify
    valid_sum = (a + b > 10)
    valid_product = (a * b > 20)

    # Both are true
    if valid_sum == valid_product == True:
        return True

    if valid_sum:
        return "Valid sum"

    if valid_product:
        return "Valid product" 
    
    # Both are false    
    return False
