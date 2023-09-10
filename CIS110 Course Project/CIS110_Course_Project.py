#Greeting
import time
def slow_print(text, delay=.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()   

slow_print("\nHey there!, I need your help advising a wildcatter.\nA wildcatter is an adventurer who finds a profitable piece of land to produce oil.") 
slow_print("He needs help deciding when to extract, sell or just leave his commodity in the ground")
slow_print("---------------                 Press enter after every response!")

#TimetoPlay
acceptResponses = ["yes", "ok", "yep", "yeah", "yea", "yup"]
letsPlay = input("\nAre you ready to help him out?   ").lower()
while letsPlay not in acceptResponses:
    if len(letsPlay) == 0:
        letsPlay = input("Let's play!...say yes, ok or yep!:      ")
    else:
        letsPlay = input("Please respond with 'ok', 'yes' or 'yep':  ") 
        
slow_print("-" * 15)   
slow_print("\n                   Yehawww!!!")

keepGoing = "yes"
while keepGoing.lower() == "yes":

    #Questions
    #1
    catterName = input("\nWhat's the wildcatter's name:   ").lower().capitalize()
    while len(catterName) == 0:
        catterName = input("Please enter a name:  ").lower().capitalize()
    #2
    oilStates = ["alaska", "north Dakota", "texas", "colorado", "new Mexico"]
    usState = input("\nIn What state is he drilling?     ").lower().strip()
    while usState not in oilStates:
        if len(usState) == 0:
            usState = input("Input cannot be blank. Please enter a valid US State:  ").lower().strip()
        else:
            usState = input("Please enter an oil producing State (Alaska, North Dakota, Texas, Colorado or New Mexico):   ").lower().strip()
    usState = usState.capitalize() 
    
    #3
    barrelsProduced = input("\nHow many thousands of barrels has he produced? Enter no more than 10: ")
    while True:
        if not barrelsProduced.isdigit():
           barrelsProduced = input("Please enter a numeric value:  ")
        elif 1 <= int(barrelsProduced) <= 10:  # If it's a digit and between 1 to 10
           barrelsProduced = int(barrelsProduced) * 1000
           print(f"                   {catterName} has produced {barrelsProduced} barrels!!")
           break
        else:
            barrelsProduced = input("Please enter a value between 1 and 10:  ")

    
    #4
    costPbarrel = input("\nHow much does it cost him to produce one barrel? $  ")
    while True:
        if costPbarrel.strip() and costPbarrel.isdigit():
           costPbarrel = int(costPbarrel)
           if 10 <= costPbarrel <= 100:
              break    
           else: 
               costPbarrel = input("Cost per barrel must be between 10 and 100. Please try again:  ")
        else:
            costPbarrel = input("Enter a whole number between 1 and 100. Try again: ")
    #5
    while True:
        currentOprice = input("\nWhat is a barrel selling for today? $")
        if currentOprice.strip() and currentOprice.isdigit():
            currentOprice= int(currentOprice)
            if currentOprice >= costPbarrel + 20:
               break
            else:
                print("The current oil price must $20 higher than cost per barrel")
        else:
            print("Please enter a digit at least $20 higher than cost per barrel")


    print("\nReady? here we go!!")
     
    #Calculations
    wcRevenue = barrelsProduced * currentOprice
    wctotalCost = barrelsProduced * costPbarrel
    wcProfit = wcRevenue - wctotalCost
    dcurrentOprice = currentOprice * 2

    #Story Starts
    slow_print(f"\nOnce upon a time, there was a wildcatter by the name of {catterName} in the state of {usState}.") 
    slow_print(f"He extracted and produced {barrelsProduced} thousand barrels of Oil from his field. It costs him ${costPbarrel}") 
    slow_print(f"per barrel to take out of the ground & he can sell it right now for ${currentOprice}.")
    slow_print(f"That is a total production cost of ${wctotalCost} and a profit of ${wcProfit} if he decides to sell right now")
    slow_print(f"Keep in mind that production takes at least six months, when you help him make a decision.")
      

    #Decision 1
    print(f"\nThe price of oil is selling at ${currentOprice} and the {catterName} has some oil")
    print(f"above ground that can be sold now or sometime in the future")
    print(f"\nHere is a question for you. If you were {catterName}.") 
    sellDecis1 = input(f"\nWould you sell your {barrelsProduced} thousand barrels of oil, or hold on to it. Yes or no?:   ")
    while sellDecis1.lower() not in ["yes", "no"]:
        sellDecis1 = input(" Please type yes or no:  ")

    if sellDecis1 == "yes":
        print(f"\n{catterName} the wildcatter from {usState} sells his {barrelsProduced} of Oil at ${currentOprice},")
        print(f"remembering his cost of production was ${costPbarrel} per barrel. His bottom line is ${wcProfit}. {catterName} risks") 
        print(f"losing profit if price of oil goes up, between now and the next six months because he has no oil above ground to sell right now.")
        print("Let's see what happens next.")
    else:
        print(f"\nOk, {catterName} has spent money to produce and risks losing profit if oil goes down from here, but he decides to hold on hoping")
        print(f"for higher prices later. {catterName} from {usState} decides not to sell at the current price and hold out for higher prices in")
        print(f"the future. Remember it cost him ${costPbarrel} to extract {barrelsProduced} barrels of oil, and he risks losing profit if the price goes down,")
        print(f"plus it costs money to store the oil on a monthly basis, but we have not accounted for that here.")   

    print("Not only is wildcatting for oil hardwork, one risks losing $ if one sells at the wrong time.")
    print("At any rate, let's go on to the next question.")
    print("\nOk, Ready!!!!")

     
    #Decision 2
    print(f"\nIt's been 3 months since your last decision, and the price of oil has doubled to ${dcurrentOprice}. Did you sell? cause if you did")
    print(f"you can't sell right now and  can't produce from one day to the next. So, here goes the next") 
    prodDecis2 = input(f"question. Should you produce? yes or no:   ")
    while prodDecis2.lower() not in ["yes", "no"]:
        prodDecis2 = input("Please type yes or no")
    
    if prodDecis2 == "yes":
        print(f"\nIt is costing {catterName} money to produce right now, and even though the price of oil is at ${dcurrentOprice}. {catterName} risks the price going down")
        print(f"never know what's going to happen. Historically when prices double in 3 months they tend to crash, due to oversupply or a recession")
    else:
        print(f"You will be missing out on profit if prices continue to rise")
    
    #Alternate Endings
    if sellDecis1 == "yes" and prodDecis2 == "yes":
        print(f"{catterName} sold his oil at ${currentOprice} a barrel missing out on ${dcurrentOprice} which would have doubled his profits")
    elif sellDecis1 == "no" and prodDecis2 == "no":
        print(f"{catterName} did not sell his inventory at ${currentOprice} and decided not to produce at ${dcurrentOprice}")
    else:
        print(f"oil goes negative cause nuclear fusion replaces fossil fuels an {catterName} goes broke")
    print("THE END!!!")

    keepGoing = input("\nDo you want to play again? yes or no  ")
    while keepGoing.lower() not in ["yes", "no"]:
        keepGoing = input("Invalid value. please enter yes or no: ")
