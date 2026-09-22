#candidates list
candidates = ["Pranta", "Fuad", "Nafis"] 
#vote counter
vote_count = {"Pranta": 0, "Fuad": 0, "Nafis": 0} 

age = int(input("\n****** Welcome to Voting System ******\n\nEnter you age: "))

if age < 18:
    print("\nYou are not eligible.\n")
elif age >= 18:
    print("\nChoose your candidate by their id: \n0: Pranta \n1: Fuad \n2: Nafis")

    vote = int(input("\nEnter vote: "))

    if vote == 0:
        print("\nVote casted for: ",candidates[0])
        vote_count["Pranta"] += 1
        print("\n",vote_count,"\n")

    elif vote == 1:
        print("\nVote casted for: ",candidates[1])
        vote_count["Fuad"] += 1
        print("\n",vote_count,"\n")
    elif vote == 2:
        print("\nVote casted for: ",candidates[2])
        vote_count["Nafis"] += 1
        print("\n",vote_count,"\n")
    else:
        print("Error!")
    
   