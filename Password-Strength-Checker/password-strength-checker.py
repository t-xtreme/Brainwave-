import string
# Read the user's password for validation and stores in variable `password` ?
password = input("\n \nEnter your password for validation :  ")

# Covert ASCII Characters in List for IF-ELSE comparison
upc = list(string.ascii_uppercase)
lwc = list(string.ascii_lowercase)
dig = list(string.digits)
spc = list(string.punctuation)

# Increase Count if "Not Found"
has_upc = 0
has_lwc = 0
has_dig = 0
has_spc = 0

# Check if password is minimum 8 characters long ? 
if password:
    print("[x] Checking its complexity...")
    
    # Now read each character in the `password` string
    for char in password:
        # print(char, end=", ")
        
        # Check if character of password string available in ASCII
        # If fouund then set value 1.
        if char in upc:
            has_upc = 1
        
        if char in lwc:
            has_lwc = 1
        
        if char in dig:
            has_dig = 1
        
        if char in spc:
            has_spc = 1

    
# If the value of any character is 0, it means that is not available in Password string
if len(password) >= 8 and has_upc == 1 and has_lwc == 1  and has_dig == 1  and has_spc == 1 :
    print("[x] Great ! Provided password is complex.")
    
else:
    print("[x] Sorry, the provided password is weak, please increase the complexity by using any missing characters ?")
    
    print(f"""
    -> Lenght of Password          : {len(password)}
    -> Number of Uppercase used    : {has_upc}
    -> Number of Lowercase used    : {has_lwc}
    -> Number of Digits used       : {has_dig}
    -> Number of Special Char used : {has_spc}
    """)

    print(f"""[x] Try to use the combination of these : 
    Uppercase   : {string.ascii_uppercase}
    Lowercase   : {string.ascii_lowercase}
    Digits      : {string.digits}
    Punctuation : {string.punctuation}
    """)
