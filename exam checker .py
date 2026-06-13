# take input for the student if he can take the exam or not
medical_cause = input("did you have medical cause? (y/n):").strip().upper()
# checking the user input and predict output accordingly
if medical_cause == 'y':  #condition1
    print ("you are allowed")
else:
    # take input of the attendence
    atten = int(input("enter attendance of student:"))
    if atten >= 75: #condition2 
        print("you are allowed")
    else:
        print("you are not allowed")
    





