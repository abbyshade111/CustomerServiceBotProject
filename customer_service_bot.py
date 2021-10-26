def cs_service_bot():
    print("Hello! Welcome to the DNS Cable Company's Service Portal. Are you a new or existing customer?")
    print("[1] New Customer")
    print("[2] Existing Customer")
    response = input("Please enter the number corresponding to your choice: ")
    if response == "1":
        new_customer()
    elif response == "2":
        existing_customer()
    else:
        print("Sorry, we didn't understand your selection")
        cs_service_bot()

def existing_customer():
    print("What kind of support do you need?")
    print("[1] Television Support")
    print("[2] Internet Support")
    print("[3] Speak to a support representative")
    response = input("Please enter the corresponding number to your choice: ")
    if response == "1":
        television_support()
    elif response == "2":
        internet_support()
    elif response == "3":
        live_rep("support")
    else:
        print("Sorry, we didn't understand your selection.")
        existing_customer()

def new_customer():
    print("We're excited to have you join the DNS family, how can we help you?")
    print("[1] Sign up for service.")
    print("[2] Schedule a home visit.")
    print("[3] Speak to a sales representative.")
    response = input("Please enter the corresponding number to your choice: ")
    if response == "1":
        sign_up()
    elif response == "2":
        home_visit()
    elif response == "3":
        live_rep("sales")
    else:
        print("Sorry, we didn't understand your selection.")
        new_customer()

def television_support():
    print("What is the nature of your problem?")
    print("[1] I can't access certain channels.")
    print("[2] My picture is blurry.")
    print("[3] I keep losing service.")
    print("[4] Other issues.")
    response = input("Please enter the corresponding number to your choice: ")
    if response == "1":
        print("Please check the channel lists at DefinitelyNotSinister.com. If the channel you cannot access is there, please contact a live representative.")
        did_that_help()
    elif response == "2":
        print("Try adjusting the antenna above your television set.")
        did_that_help()
    elif response == "3":
        print(
            "Is it raining outside? If so, wait until it is not raining and then try again.")
    elif response == "4":
        live_rep("support")
    else:
        print("Sorry, we didn't understand your selection.")
        television_support()

def internet_support():
    print("What is the nature of your problem?")
    print("[1] I can't connect to the internet.")
    print("[2] My connection is very slow.")
    print("[3] I can't access certain sites.")
    print("[4] Other issues.")
    response = input("Please enter the corresponding number to your choice: ")
    if response == "1":
        print("Unplug your router, then plug it back in, then give it a good whack, like the Fonz.")
        did_that_help()
    elif response == "2":
        print("Make sure that all cell phones and other people's computers are not connected to the internet, so that you cam have all the bandwidth.")
        did_that_help()
    elif response == "3":
        print(
            "Move to a different region or install a VPN. Some areas block certain sites.")
        did_that_help()
    elif response == "4":
        live_rep("support")
    else:
        print("Sorry, we didn't understand your selection.")
        internet_support()

def did_that_help():
    print("Did that solve your problem?")
    response = input("Please enter yes or no: ")
    if response == "yes":
        print("Thank you! Have a good day.")
    elif response == "no":
        print("Would you rather talk to a live representative or schedule a home visit?")
        response = input(
            "Please enter 1 to speak to a live representative, or 2 to schedule a home visit: ")
        if response == "1":
            live_rep("support")
        elif response == "2":
            home_visit("support")
        else:
            print("Sorry, we didn't understand your selection.")
            did_that_help()
    else:
        print("Sorry, we didn't understand your selection.")
        did_that_help()

def sign_up():
    print("Great choice, friend! We're excited to have you join the DNS family! Please select the package you are interested in signing up for.")
    print("[1] Bundle Deal (Internet + Cable)")
    print("[2] Internet")
    print("[3] Cable")
    response = input("Please enter the corresponding number to your choice: ")
    if response == "1":
        print("You've selected the Bundle Package! Please schedule a home visit and our technician will come and set up your new service.")
        home_visit("new_install")
    elif response == "2":
        print("You've selected the Internet Only Package! Please schedule a home visit and our technician will come and set up your new service.")
        home_visit("new_install")
    elif response == "3":
        print("You've selected the Cable Only Package! Please schedule a home visit and our technician will come and set up your new servie.")
        home_visit("new_install")
    else:
        print("Sorry, we didn't understand your selection.")
        sign_up()

def home_visit(purpose="none"):
    if purpose == "none":
        print("What is the purpose of the home visit?")
        print("[1] New service installation.")
        print("[2] Existing service repair.")
        print("[3] Location scouting for unserviced region.")
        response = input("Please select the corresponding number to your choice.")
        if response == "1":
            home_visit("new_install")
        elif response == "2":
            home_visit("support")
        elif response == "3":
            home_visit("scout")
        else:
            print("I'm sorry, we didn't understand your selection")
            home_visit()
    else:
        visit_date = input(
            "Please enter a date below when you are available for a technician to come to your home and " + purpose)
        print("Wonderful! A technician will come visit you on " + visit_date +
              ". Please be available between the hours of 1:00am and 11:00pm.")

def live_rep(purpose):
    if purpose == "sales":
        print("Please hold while we connect you with a live sales representative. The wait time will be between two minutes and six hours. We thank you for your patience.")
    elif purpose == "support":
        print("Please hold while we connect you with a live support representative. The wait time will be between two minutes and six hours. We thank you for your patience.")

cs_service_bot()
