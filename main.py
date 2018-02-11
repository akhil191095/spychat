from spy_details import spy
print "Hello"

OLD_STATUS = ["Available","007","Can't talk spychat only","sleeping"]

friends = [{"name" : "Akshay" , "age" : 26 , "rating" : 3.6 } , {"name" : "Rohit" , "age" : 26 , "rating" : 3.8 } ]

def add_status(C_S):
    if C_S != None:
        print"Your Current Status is : " + C_S
    else:
        print "You don't have any Status"

    user_choice = raw_input("Do you want to select from old Status? Y or N ")

    if user_choice.upper() == "Y":
        serial_no = 1
        for status in OLD_STATUS:
            print str(serial_no) + " " + status
            serial_no = serial_no + 1
        user_status_selection = input ("Which one do you want to set this time? ")
        new_status = OLD_STATUS [user_status_selection - 1 ]

    elif user_choice.upper() == "N":
        new_status = raw_input("Write your status: ")
        OLD_STATUS.append (new_status)


    else:
        print "Invalid entry"

    return new_status

def add_friend():
    frnd = {
        "name" : " ",
        "age" : "0",
        "rating" : "0.0"
    }

    frnd["name"] = raw_input("Enter your Friends name : ")
    frnd_sal = raw_input("Mr. or Miss. ")
    frnd["name"] = frnd_sal + " " + frnd["name"]
    frnd["age"] = input ("Enter your Friends age:  ")
    frnd["rating"] = input("Enter rating of your Friend: ")

    if len(frnd["name"])>2 and 20<= frnd["age"]<= 50:
        friends.append(frnd)

    else:
        print "Friend cannot be added"
    return len(friends)

def select_frnd():
    serial_no = 1
    for frnd in friends:
        print  str(serial_no) + " " + frnd["name"]
        serial_no = serial_no + 1
        user_selected_frnd = input("Which one you want to send message to? ")
        user_index = friends[user_selected_frnd - 1]
        return user_index





def start_chat(spy_name,spy_age,spy_rating):
    current_status = None
    show_menu = True
    while show_menu:
        menu_choice = input("What do you want to do? \n 1.Add Status \n 2.Add Frriend \n 3. Send a message \n 0.Exit \n")
        if menu_choice == 1:
          current_status = add_status(current_status)
          print "Your new status is updated to "+ current_status
        elif menu_choice == 2:
            no_of_frnds = add_friend()
            print "I have  "+ str(no_of_frnds) + " Friends"
        elif menu_choice == 3:
            selected_friend = select_frnd()
            print "We are going to send a message to " + friends[selected_frnd]
        elif menu_choice == 0:
            show_menu = False
        else:
            print"invalid choice"


question = raw_input ("Are you a new user? YES or NO:")

if question.upper() == "NO":
    print "We already have your details"
    start_chat(spy["name"] , spy ["age"], spy["rating"])
elif question.upper() == "YES":

    spy = {
        "name" : " ",
        "age" : "0",
        "rating" : "0.0"
    }

    print "What is your name"

    spy["name"]=raw_input ()

    if len(spy["name"])>2:


        print "Are you a Mr. or Ms."
        spy_gender=raw_input ()
        print "Welcome" + " " + spy_gender + " " + spy["name"] + " " + "I'd like to know a little bit more about you"



        spy["age"]=input("what is your age")
        if spy["age"]>20 and spy["age"]<50:
            print"welcome spy"
            spy["rating"] = 0.0
            spy["rating"]=input("what is your rating as a spy")
            if spy["rating"] >=5:
                print"best spy"
            elif spy["rating"]<5 and spy["rating"]>3.5:
                print"good spy"
            elif spy["rating"] < 3.5 and spy["rating"] > 2.5:
                print"useless spy" \

            spy_is_online = True

            print "Authentication successfull : Welcome " + spy["name"]  + " age: " + str(spy["age"])  + " rating: " + str(spy["rating"])


            start_chat(spy_name, spy_age, spy_rating)
    else:
        print"error please enter your name" \

else:
    print"Invalid Entry"
