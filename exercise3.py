def degree(degree,experience):
    if degree == "Master" or "master" or "Phd" or "phd":
        if experience >=2:
            print("You are selected for the intrview")
        else:
            print("You don not have the enough experience")
    else:
        print("You dont have the required experience")

degree("Master",3)