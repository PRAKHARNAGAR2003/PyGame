degree = input("What type of degree you have: Masters, Bachelors or Phd??")
experience = input("The number of years you have experience??")

if degree == "Masters" or "masters" or" Phd" or "phd":
    if int(experience) >=2:
        print("You are accepted for the interview")
    else:
        print("You don't have enough experience")
else:
    print("You dont have required experience")