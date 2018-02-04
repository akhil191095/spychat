from spy_details import spy_name,spy_age,spy_rating
print "Hello"

def start_chat(spy_name,spy_age,spy_rating):
    show_menu = True
    while show_menu:
        menu_choice = input("What do you want to do? \n 1.Add Status \n 2.Add Frriend \n 0.Exit \n")
        if menu_choice == 1:
            status = raw_input("Write your status ")
            print "Your status is: " + status
        elif menu_choice == 2:
            print"Will add a Friend"
        elif menu_choice == 0:
            show_menu = False
        else:
            print"invalid choice"


question = raw_input ("Are you a new user? YES or NO:")

if question.upper() == "NO":
    print "We already have your details"
    start_chat(spy_name, spy_age, spy_rating)
elif question.upper == "YES":

    print "What is your name"

    spy_name=raw_input ()

    if len(spy_name)>2:


        print "Are you a Mr. or Ms."
        spy_gender=raw_input ()
        print "Welcome" + " " + spy_gender + " " + spy_name + " " + "I'd like to know a little bit more about you"
        spy_age=0
        spy_age=raw_input ()


        spy_age=input("what is your age")
        if spy_age>20 and spy_age<50:
            print"welcome spy"
            spy_rating = 0.0
            spy_rating=input("what is your rating as a spy")
            if spy_rating >=5:
                print"best spy"
            elif spy_rating<5 and spy_rating>3.5:
                print"good spy"
            elif spy_rating < 3.5 and spy_rating > 2.5:
                print"useless spy" \

            spy_is_online = True

            print "Authentication successfull : Welcome " + spy_name + " "+"age:" + " " + str(spy_age) +" " + "rating:" + str(spy_rating)


            start_chat(spy_name, spy_age, spy_rating)
    else:
        print"error please enter your name" \

else:
    print"Invalid Entry"
