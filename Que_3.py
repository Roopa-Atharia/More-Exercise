user_input=(input("Enter the strong  passwaord "))
if len(user_input)>=6 and len(user_input)<=16:
    if "$" in user_input:
        if "2" in user_input or "8" in user_input:
            if "A" in user_input or  "Z" in user_input:
                print("strong password")
            else:
                print("weak password")   
        else:
            print("no")
    else:
        print("no")
else:
    print("no")