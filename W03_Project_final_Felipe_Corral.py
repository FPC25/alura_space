"""
Program: Adventure Game
Authors: Felipe Proença Corral

Also contains the stretch goal
"""

def printInventory(inventory):
    print("\n# Inventory #")
    for key in inventory.keys():
        print(f"{key}: {inventory[key]}")
    print()

def startGame():
    
    print("--------------------------------")
    print("- Quest for the Ancient Relic! -")
    print("--------------------------------")


    print("\n\n# Introduction #\n\n")
    
    print("You are a renowned swordsman, celebrated for your skill and valor. Today, you find yourself at the threshold of the mystical land of Meleeth, a realm steeped in legend and mystery. Here, tales whisper of an ancient relic, hidden away and fiercely guarded by untold dangers. This relic is said to bestow unimaginable power upon its wielder. Will you rise to the challenge and claim it for yourself? Your journey begins now.\n\n")

    inventory = {"Armor": "Old Armor", "Weapon": "Old Sword", "Shield": "Old Shield", "Gold": 150, "Misc": ["2x Healing Potion", "Stamina Potion"]}

    printInventory(inventory)
    
    levelOne(inventory)
    
    
def levelOne(inventory):
    
    print("#############")
    print("# Level One #")
    print("#############")

    print("\n\n# The Village of Dawn #\n\n")
    
    print("You arrive at the peaceful Village of Dawn, where the locals whisper about the relic and the dangers surrounding it. To proceed, you need information and supplies and maybe new equipment. But where to begin? You can SPEAK to the village Elder to try to learn more about the relic's location, or I can VISIT the blacksmith to buy weapons and armor, or even SEARCH the Tavern for rumors about this ancient relic.\n\n")

    times_visited_square = 1
    times_visited_elder = 0
    times_visited_blacksmith = 0
    times_visited_tavern = 0
    side_quest_status = "Not started"

    choice = input("What will you do first? ")
    villageSquareDecisions(choice, times_visited_square, times_visited_elder, times_visited_blacksmith, times_visited_tavern, inventory, side_quest_status)

def messageLevelOne(times_visited_elder, times_visited_blacksmith, times_visited_tavern, side_quest_status):
    message = "You decide to visit the village square again. You see the villagers going about their daily lives."
    if times_visited_elder >= 1:
        elder_times = "You can SPEAK again to the village Elder to see if he has anymore thing to say,"
    else:
        elder_times = "You can SPEAK to the village Elder to try to learn more about the relic's location,"
        
    if times_visited_blacksmith >= 1:
        blacksmith_times = "VISIT the blacksmith again,"        
    else:
        blacksmith_times = "VISIT the blacksmith to buy weapons and armor,"
    
    if times_visited_tavern >= 1:
        tavern_times = "SEARCH for the Tavern for any other rumors about this ancient relic"
    else:
        tavern_times = "SEARCH for the Tavern for rumors about this ancient relic and its location"
    
    if not side_quest_status == "Accepted" and (times_visited_elder >=1 or times_visited_tavern >= 1):
        leaving = "You can now GO and begin your journey to the tomb"
        message = f"{message} {elder_times} {blacksmith_times} {tavern_times} {leaving}"
    else:
        message = f"{message} {elder_times} {blacksmith_times} {tavern_times}"
    
    return message
 
def villageSquare(times_visited_square, times_visited_elder, times_visited_blacksmith, times_visited_tavern, inventory, side_quest_status):
    
    print("\n# The Village of Dawn #")
    times_visited_square += 1
    if times_visited_square == 1:
        message = messageLevelOne(times_visited_elder, times_visited_blacksmith, times_visited_tavern, side_quest_status)
        print(message)
        choice = input("What will you do?: ").upper()
        levelOne(choice, times_visited_square, times_visited_elder, times_visited_blacksmith, times_visited_tavern, inventory, side_quest_status)
            
    else:
        if side_quest_status == "Accepted":
            message = messageLevelOne(times_visited_elder, times_visited_blacksmith, times_visited_tavern, side_quest_status)   
            print(f"{message} or go to the forest to LOCATE the rare ore.\n")                 
            choice = input("What will you do?: ").upper()
            levelOne(choice, times_visited_square, times_visited_elder, times_visited_blacksmith, times_visited_tavern, inventory, side_quest_status)
               
        else:
            message = messageLevelOne(times_visited_elder, times_visited_blacksmith, times_visited_tavern, side_quest_status)               
            print(f"{message}.\n")                 
            choice = input("What will you do?: ").upper()
            levelOne(choice, times_visited_square, times_visited_elder, times_visited_blacksmith, times_visited_tavern, inventory, side_quest_status)

def villageSquareDecisions(choice, times_visited_square, times_visited_elder, times_visited_blacksmith, times_visited_tavern, inventory, side_quest_status):
    
    choice = choice.upper()
    if choice == "SPEAK":
        elderHouse(times_visited_square, times_visited_elder, times_visited_blacksmith, times_visited_tavern, inventory, side_quest_status)
    
    elif choice == "VISIT":
        blacksmith(times_visited_square, times_visited_elder, times_visited_blacksmith, times_visited_tavern, inventory, side_quest_status)
    
    elif side_quest_status.upper() == "ACCEPTED" and choice == "LOCATE":
        forest(times_visited_square, times_visited_elder, times_visited_blacksmith, times_visited_tavern, inventory, side_quest_status)

    elif choice == "SEARCH":
        tavern(times_visited_square, times_visited_elder, times_visited_blacksmith, times_visited_tavern, inventory, side_quest_status)
        
    elif (not side_quest_status == "Accepted" and (times_visited_elder >=1 or times_visited_tavern >= 1)) and choice == "GO":
        levelTwo(inventory)
        
    else:
        print("You seem frustrated with you indecision, but you think a bit harder. You can SPEAK to the village Elder to try to learn more about the relic's location, or I can VISIT the blacksmith to buy weapons and armor, or even SEARCH the Tavern for rumors about this ancient relic.")
        choice = input("So, what will you do? ")
        villageSquareDecisions(choice, times_visited_square, times_visited_elder, times_visited_blacksmith, times_visited_tavern, inventory, side_quest_status)

def elderHouse(times_visited_square, times_visited, times_visited_blacksmith, times_visited_tavern, inventory, side_quest_status):
    
    print("\n# The Elder House #")
    
    if times_visited == 0:
        times_visited += 1
        print("You decide to speak with the village Elder. He tells you that the local legends tells that the relic is hidden in Migner's Tomb, north to the village, and, although no one know where really is its entrance, tales says its location is somewhere near the craggy hill and it is full of traps and that I must prepare myself to it. Knowing about my previous adventures the Elder go to a chest and pick a map of the region, mark the Tombs position. Now I have a **Map** of the region and a destination. What will you do? Will you GO to Migner's Tomb or keep SEARCHING for more clues in the village?")
        inventory["Misc"].append("Map")
        printInventory(inventory)
        choice = input("What will you do?: ").upper()
        
        
        if choice == "GO":
            print("You decide to go to Migner's Tomb. You leave the village and head north. After a few hours of walking, you arrive at the Tomb. You feel and ominous feeling and try to find the entrance to the tomb.")
            levelTwo(inventory)
            
        elif choice == "SEARCHING":
            print("You decide to stay in the village to search for more clues. You leave the Elder's house to the village square.")
            villageSquare(times_visited_square, times_visited, times_visited_blacksmith, times_visited_tavern, inventory, side_quest_status)
            
        else:
            print("You stay a bit longer in the Elder's House chatting about the village and your adventures. Eventually you decide to leave to the village square, saying goodbye to the Elder.")
            villageSquare(times_visited_square, times_visited, times_visited_blacksmith, times_visited_tavern, inventory, side_quest_status)
    else:
        print("You decide to speak again with the village Elder. But he seems to be busy and tells you that he has nothing new to say. You decide to leave the house to the village square.")
        villageSquare(times_visited_square, times_visited, times_visited_blacksmith, times_visited_tavern, inventory, side_quest_status)
        
    return choice, times_visited, inventory 
        
def blacksmith(times_visited_square, times_visited_elder, times_visited_blacksmith, times_visited_tavern, inventory, side_quest_status):
    
    print("\n# The Blacksmith #")
    times_visited_blacksmith += 1
    if times_visited_blacksmith == 0 or (side_quest_status == "Not started" and times_visited_blacksmith <= 3):
        times_visited_blacksmith += 1
        print("You decide to visit the blacksmith. The blacksmith greets you with a warm but wary smile as you step into his cluttered workshop. Tools dangle from hooks on the walls, and the air smells of molten metal and soot. You know that your gear and weapons have seeing better days, so you decide to get new ones. After arriving the blacksmith forge, you greet the blacksmith, who leans over the counter, wiping his hands on a stained cloth. After quick a chat with her about your mission, she shows you some good but common gear, weapons and shield that costs 75 gold. Knowing your fame, she shows his finest weapons and armor as well, but they are too expensive, costing 225 gold. Seeing that and her expression you think to yourself:\n\n'As it seems people often confuse fame with wealth.'\n\nYour ask if you can help her in any way to get an discount and she says:\n\n'You look like the kind of adventurer who isn't afraid to get their hands dirty,' She says. 'There is a rare ore I need for a project — Shadowiron. It is only found deep in the Whispering Forest, where few dare to tread. If you bring it back, I'll give you a 100 gold off from my finest gear. Deal?'.\n\nYou can ACCEPT the quest, BUY the common equipment and refuse the quest or just LEAVE the blacksmith. If you BUY the common equipment or complete the quest the blacksmith will pay 35 gold for your present set.")
        choice = input("What will you do?: ").upper()
        if choice == "ACCEPT":
            side_quest_status = "Accepted"
            print("You happily accept the quest saying 'Deal! I will bring you the **Shadowiron ore**. She happily hands you a **Pickaxe** wishing you good luck")
            inventory['Misc'].append("Pickaxe")
            printInventory(inventory)
            villageSquare(times_visited_square, times_visited_elder, times_visited_blacksmith, times_visited_tavern, inventory, side_quest_status)
            
        elif choice == "BUY":
            print("You think about it, but thinks that the **Common Equipment** is good enough for the task. You buy the common equipment and sell your old equipment. You leave the blacksmith to the village square while the blacksmith goes to forest gather the materials. (You cannot get the side quest anymore)")
            side_quest_status = "Refused"
            inventory["Gold"] -= 75
            inventory["Gold"] += 35
            inventory["Armor"] = "Common Armor"
            inventory["Weapon"] = "Common Sword"
            inventory["Shield"] = "Common Shield"
            printInventory(inventory)
            villageSquare(times_visited_square, times_visited_elder, times_visited_blacksmith, times_visited_tavern, inventory, side_quest_status)
            
        else:
            print("You asked for more time to think about the quest and left the blacksmith to the village square.")
            villageSquare(times_visited_square, times_visited_elder, times_visited_blacksmith, times_visited_tavern, inventory, side_quest_status)
            
    elif times_visited_blacksmith > 4 and side_quest_status == "Not started":
        times_visited_blacksmith += 1
        print("The blacksmith says that you are taking too long to decide about the quest. She sells you the **Common Equipment** and buy your old equipment. You leave the blacksmith to the village square while the blacksmith goes to forest gather the materials. (You cannot get the side quest anymore).")
        side_quest_status = "Refused"
        inventory["Gold"] -= 75
        inventory["Gold"] += 35
        inventory["Armor"] = "Common Armor"
        inventory["Weapon"] = "Common Sword"
        inventory["Shield"] = "Common Shield"
        printInventory(inventory)
        villageSquare(times_visited_square, times_visited_elder, times_visited_blacksmith, times_visited_tavern, inventory, side_quest_status)
    
    elif times_visited_blacksmith >= 1 and side_quest_status == "Accepted":
        times_visited_blacksmith += 1
        if "Shadowiron ore" in inventory["Misc"]:
            if not inventory["Armor"] == "Old Armor":
                print("You give the blacksmith the **Shadowiron Ore** and return the **Pickaxe**. She is very happy and gives you the discount of 100 gold. You pay 125 gold for the finest equipment and she gives you 20 gold for your old equipment, seeing that you lost your Armor. You acquired the **Finest Equipment** from the blacksmith.")
                side_quest_status = "Completed"
                inventory["Misc"].remove("Shadowiron ore")
                inventory["Misc"].remove("Pickaxe")
                inventory["Gold"] += 20
                inventory["Gold"] -= 125 
                inventory["Armor"] = "Finest Armor"
                inventory["Weapon"] = "Finest Sword"
                inventory["Shield"] = "Finest Shield"
                printInventory(inventory)
                villageSquare(times_visited_square, times_visited_elder, times_visited_blacksmith, times_visited_tavern, inventory, side_quest_status)
            else:              
                print("You give the blacksmith the **Shadowiron Ore** and return the **Pickaxe**. She is very happy and gives you the discount of 100 gold. You pay 125 gold for the finest equipment and she gives you 35 gold for your old equipment. You acquired the **Finest Equipment** from the blacksmith.")
                
                side_quest_status = "Completed"
                inventory["Misc"].remove("Shadowiron ore")
                inventory["Misc"].remove("Pickaxe")
                inventory["Gold"] += 35
                inventory["Gold"] -= 125 
                inventory["Armor"] = "Finest Armor"
                inventory["Weapon"] = "Finest Sword"
                inventory["Shield"] = "Finest Shield"
                printInventory(inventory)
                
                villageSquare(times_visited_square, times_visited_elder, times_visited_blacksmith, times_visited_tavern, inventory, side_quest_status)
        elif "Shadowiron ore" not in inventory["Misc"]:
            if times_visited_blacksmith < 7:
                print("You return to the blacksmith without the **Shadowiron Ore**. She reminds you that you need to bring the **Shadowiron Ore** from the forest to get the discount. You leave the blacksmith to the village square.")
                villageSquare(times_visited_square, times_visited_elder, times_visited_blacksmith, times_visited_tavern, inventory, side_quest_status)
            else:
                print("You return to the blacksmith without the **Shadowiron Ore**. She says that you are taking too long to gather the ore. She sells you the **Common Equipment** and buy your old equipment. You leave the blacksmith to the village square while the blacksmith goes to forest gather the materials. (You cannot get the side quest anymore).")
                side_quest_status = "Failed"
                inventory["Misc"].remove("Pickaxe")
                inventory["Gold"] -= 75
                inventory["Gold"] += 35
                inventory["Armor"] = "Common Armor"
                inventory["Weapon"] = "Common Sword"
                inventory["Shield"] = "Common Shield"
                printInventory(inventory)
                villageSquare(times_visited_square, times_visited_elder, times_visited_blacksmith, times_visited_tavern, inventory, side_quest_status)
    
    else:
        print("You decide to visit the blacksmith again, but it seems she is not back yet. You go back to the village square")
        villageSquare(times_visited_square, times_visited_elder, times_visited_blacksmith, times_visited_tavern, inventory, side_quest_status)
        
def tavern(times_visited_square, times_visited_elder, times_visited_blacksmith, times_visited, inventory, side_quest_status):
    
    print("\n# Tavern #")
    
    if times_visited == 0:
        times_visited += 1
        print("You decide to search the tavern for rumors. After ordering some food and a beverage from the waiter, you find a seat and discreetly listen for any useful information. After some time, you overhear a story about a group of adventurers who claimed to have found the tomb's entrance at the base of a craggy hill—but they never returned. The locals say they investigated the area afterward but found nothing. \n\nAs the night goes on, one of the drinkers begins sharing tales about the tomb, warning that it's cursed and that the relic is guarded by the spirits of the dead. You also hear whispers that the tomb's main entrance collapsed a few years ago, meaning anyone who wishes to retrieve the relic will face significant challenges.\n\nYou stay late at the tavern, hoping to catch more rumors, but luck isn't on your side. 'Can I find the entrance to the tomb?' you wonder to yourself. But this is a matter for tomorrow.\n\nAfter spending so long at the tavern, you finally head to bed. After a good night's sleep and gathering some **Supplies**, you get up and leave the tavern.")

        inventory["Misc"].append("Supplies")
        printInventory(inventory)
        
        print("What will you do next? Will you GO to Migner's Tomb, or keep LOOKING around for more clues? ")
        choice = input("What will you do?: ").upper()

        if choice == "GO":
            print("You decide to go to Migner's Tomb. You leave the village and head north. After a few hours of walking, you arrive at the Tomb. You feel and ominous feeling and try to find the entrance to the tomb.")
            
            return choice
        elif choice == "LOOKING":
            print("You decide to stay in the village to search for more clues. You leave the tavern to the village square.")
            villageSquare(times_visited_square, times_visited_elder, times_visited_blacksmith, times_visited, inventory, side_quest_status)
        else:
            print("You decide to see if anyone has anymore rumors, but it seems you run out of luck, so you decide to go take a walk around the village, leaving the tavern in direction to the village square.")
            villageSquare(times_visited_square, times_visited_elder, times_visited_blacksmith, times_visited, inventory, side_quest_status)
    else:
        times_visited += 1
        print("You decide to visit the tavern again, but the locals have nothing new about the Tomb. You just hear conversation about village's daily life. You decide to leave the tavern.")
        villageSquare(times_visited_square, times_visited_elder, times_visited_blacksmith, times_visited, inventory, side_quest_status)

def forest(times_visited_square, times_visited_elder, times_visited_blacksmith, times_visited_tavern, inventory, side_quest_status):
    
    print("\n# The Whispering Forest #")
    
    if not "Shadowiron ore" in inventory["Misc"]:
        print("The Whispering Forest lives up to its name. The trees stand tall and gnarled, their twisted branches creaking in the breeze like voices whispering secrets. Shafts of sunlight barely pierce the dense canopy above, casting the forest floor in an eerie twilight.\nYou tread carefully, following the blacksmith1s directions toward the rocky outcrop where the Shadowiron vein is said to be. Along the way, strange sights catch your eye—a deer with glowing antlers bounds across your path, and shimmering lights dance in the distance, vanishing when you draw near.\n\nAfter a while, you reach the outcrop. The black stone juts out from the earth like the rib of a forgotten giant. In the rock, faint silver veins gleam, reflecting a cold, unearthly light. This must be the Shadowiron.\n\nYou swing the pickaxe, and the ore chips away with a satisfying crack. As you work, the air grows colder, and the forest falls unnervingly silent. Then you feel it—a presence watching from the shadows.\n\nA low growl rumbles behind you. Turning slowly, you see a pair of glowing yellow eyes emerge from the darkness. A massive wolf, its fur as black as the ore you1re mining, steps into the clearing. Its lips curl into a snarl, revealing fangs that glint like polished obsidian.")
        
        if "Supplies" in inventory["Misc"]:
            
            print("You grip your **{}** tightly, preparing for a fight, but the wolf hesitates. Its ears twitch, and it sniffs the air as if sensing something unfamiliar. Slowly, you lower the **{}** and pull a piece of dried meat from your pack.\nYou toss the meat toward the wolf, and it snatches it mid-air with a snap of its jaws. It lingers for a moment, then slinks back into the shadows, its glowing eyes watching you until it disappears completely.\nBreathing a sigh of relief, you finish gathering the **Shadowiron Ore** and head back to the village.".format(inventory["Weapon"], inventory["Weapon"]))
        else:
            print("You turn slowly, gripping the **{}** tightly as glowing yellow eyes emerge from the shadows. A massive wolf, its fur black as night and fangs sharp as blades, steps into the clearing. It growls low, the sound vibrating in your chest.\nThe wolf lunges, and you sidestep just in time, swinging the **{}** in desperation. The sharp edge scrapes the creature's shoulder, and it howls in pain, retreating a few paces. Its yellow eyes burn brighter, now filled with rage.\nThe battle is fierce, with the wolf darting in and out of the shadows. You manage to land a few solid blows, but it's your determination—and a bit of luck—that turn the tide. With a final, desperate swing, the **{}** strikes true, and the wolf collapses. It lets out a final, mournful growl before falling silent.\nPanting and bloodied, you take a **Healing Potion**, pick up the **Pickaxe** and collect the Shadowiron ore. Before you make your way back to the village you skin the beast acquiring **Beast Pelt**. You notice that your **{}** is worst than ever making impossible to keep using it.".format(inventory["Weapon"], inventory["Weapon"], inventory["Weapon"], inventory["Armor"]))
            inventory["Misc"].remove("2x Healing Potion")
            inventory["Misc"].append("Healing Potion")
            inventory["Misc"].append("Beast Pelt")
            inventory["Armor"] = "Common Clothes"
            
        inventory["Misc"].append("Shadowiron ore")
        printInventory(inventory)
    
    else:
        print("You already gathered the Shadowiron ore. You don't need to go back to there for now.")
        
    villageSquare(times_visited_square, times_visited_elder, times_visited_blacksmith, times_visited_tavern, inventory, side_quest_status)


def levelTwo(inventory, side_quest_status):
    
    print("##############")
    print("# Level Two #")
    print("##############")
    
    print("\n\n# Migners Tomb Outskirts #\n\n")
    
    if 'Map' in inventory['Misc']:
        print("Following the elder's directions, you travel north until you arrive at the base of a craggy hill where the secret path is rumored to begin. The entrance is hidden, and you need to find a way in. The hill is covered in thick vines, jagged rocks, and eerie silence, broken only by the occasional rustle of leaves.\n\n")
    else:
        print("Relying only on rumors overheard at the tavern, you set out to find the tomb at the base of a craggy hill. With no clear directions, the search becomes arduous. You trek through dense forests and climb rocky inclines, the eerie silence around you broken only by the occasional rustle of leaves.\n\nHours pass, and frustration sets in. You find yourself wandering in circles, uncertain if you've already passed the same twisted tree or stumbled over the same loose stones. The sun sinks lower, and your supplies dwindle. Each sip of water and bite of rations feels heavier with the weight of uncertainty.\n\nJust as you begin to question whether the rumors were even true, you catch sight of an unusual outcrop of rock partially obscured by thick vines. You breathe a sigh of relief and take the Stamina Potion so you can continue your journey.\n\n")
        
        inventory['Misc'].remove("Supplies")
        inventory['Misc'].remove("Stamina Potion")
        printInventory(inventory)
        
    print("The entrance is hidden, and you need to find a way in. The hill is covered in thick vines, jagged rocks, and eerie silence, broken only by the occasional rustle of leaves. As you search, you stumble upon a crumpled body—a fallen adventurer clad in rusted armor. A faint trail of blood leads to a mossy rock wall. Scrawled in dried red across the wall are the words:\n\n'ONLY THE LIGHT SHALL REVEAL THE WAY.'\n\nNearby, you spot a torch bracket on the wall, but no torch to light it. The ground is littered with scraps of paper, strange etchings, and a broken sword. A faint glint catches your eye—a chest buried beneath some rubble. Now you have to find the secret entrance.\n\n")
    times_investigated += 1
    chest_status = False
    fallen_status = False
    choice = input("Do you want to OPEN the chest, SEARCH the fallen adventure or INVESTIGATE the mossy wall more closely").upper()
    
    tombsOutskirtDecisions(choice, inventory, chest_status, fallen_status, side_quest_status)
         
def tombsOutskirt(inventory, chest_status, fallen_status, side_quest_status):
    
    print("\n\n# Migners Tomb Outskirts #\n\n")
    
    print("You come back from your investigation and you have to decide what to do now. You still need to lit the **Torch**.\n\n")
    
    choice = input("Do you want to OPEN the chest, SEARCH the fallen adventure or INVESTIGATE the mossy wall more closely").upper()
    
    tombsOutskirtDecisions(choice, inventory, chest_status, fallen_status, side_quest_status)

def tombsOutskirtDecisions(choice, inventory, chest_status, fallen_status, side_quest_status):
    
    if not "Torch" in inventory["Misc"] and not "Flint" in inventory["Misc"] and not "Strange Sap" in inventory["Misc"]:
        if choice == "OPEN":
            if not chest_status:
                print("You approach the chest cautiously, its ancient wood cracked and reinforced with tarnished iron bands.")
                
                if fallen_status:
                    print("The chest seems much older than the fallen adventurer remains.") 
                    
                print("The lock crumbles under a little force, and the lid creaks as it opens. Inside, you find a small pile of **10 gold coins**, a **Torch** and a **Strange Medallion** with peculiar carvings. You pocket the items quickly, feeling a chill in the air as if the chest's contents were watching you. Gaining confidence, you prepare to move forward.")
                
                inventory["Gold"] += 10
                inventory["Misc"].append("Torch")
                inventory["Misc"].append("Strange Medallion")
                printInventory(inventory)
                
                chest_status = True
            else:
                if not fallen_status:
                    print("The chest sits empty, its contents gone. The lid hangs open, creaking softly as the wind passes by. There's nothing left to find here.")
                else:
                    print("The chest sits empty, its contents gone. The lid hangs open, creaking softly as the wind passes by. There's nothing left to find here. But you now notices that the chest seems much older than the fallen adventurer remains")
                
            tombsOutskirt(inventory, times_investigated, chest_status, fallen_status)
            
        elif choice == "SEARCH":
            if not fallen_status:
                print("You examine the body of the fallen adventurer, their rusted armor barely holding together. A tattered pack rests at their side. Inside, you find a **Flint** and a **Rag**, likely used to light torches.\n")
                
                if side_quest_status != "Completed":
                    print("As you collect these items, you notice strange claw marks on their armor and wonder what fate they met.")
                else:
                    print("As you collect these items, you notice claw marks on their armor and recall the encounter you had with a beast while you were collecting Shadowiron ore.\n")
                    
                print("The eerie silence of the path presses in around you. You make a mental note to bury him after finish you quest if you make it alive.")
                                  
                inventory["Misc"].append("Flint")
                inventory["Misc"].append("Rag")
                printInventory(inventory)
                
                fallen_status = True
            else:
                print("The fallen adventurer lies as you left them, their tattered belongings already taken. There's nothing more to find here, though the sight of the body lingers in your mind. You make a mental note to bury him after finish you quest if you make it alive.")
                
            if chest_status:
                print("While you contemplate the finitude of life, you then notice the that the fallen adventurer remains seems newer than the chest you've found earlier")
                
            tombsOutskirt(inventory, times_investigated, chest_status, fallen_status)
                
        elif choice == "INVESTIGATE":
            print("You take time to survey the area. The ground is uneven,marked by faint footprints leading in multiple directions. After carefully examining the overgrown vines and weathered rocks, you notice faint carvings on the hillside—a clue to the hidden entrance. The marks are ancient, perhaps directions or warnings, though their meaning eludes you. Your persistence is rewarded as you uncover an **Strange Sap** in a nearby tree, it seems flammable.")
            
            inventory["Misc"].append("Strange Sap")
            printInventory(inventory)
            
            tombsOutskirt(inventory, times_investigated, chest_status, fallen_status)
    else:
        print("Now that ou retrieved every component to lit the **Torch** you do it and out put it on the bracket. The ground start to tremble and you worry if you made anything wrong. Then a gust of air pass you caring an strange smell, a mixture of earth and decay. Following the smell, you see besides the vines an narrow entrance wide enough to squeeze through. You notice that strangely the path is illuminated. Despite your exhaustion, the faint hope of discovering the relic drives you forward. You take a deep breath and step inside, leaving the forest and the fading daylight behind.")
        
        inventory["Misc"].remove("Torch")
        inventory["Misc"].remove("Rag")
        inventory["Misc"].remove("Strange Sap") 
        printInventory(inventory)
        
        secretPath(inventory)
      
def secretPath(inventory, side_quest_status):
    
    print("After you enter, the entrance closes, locking you inside. With only the path ahead, you asses the situation. The tunnel is dimly illuminated, damp, and unnervingly quiet. The air feels heavy, and your footsteps echo off the narrow stone walls. As you move deeper, you hear faint scuttling noises from ahead.\n\nSuddenly, the scuttling grows louder, and a swarm of large, glowing Sacred Scarab bursts from the shadows! Their pincers gleam like steel, and their eerie green glow makes them even more unsettling.\n\n")
    
    if "Old" in inventory["Weapon"]:
        print("You raise your {} as the scarabs swarm, but it splinters under their relentless strikes. Your {} is dull and chips and shatters as you try to fight them off. Outnumbered and defenseless, you succumb to the overwhelming swarm. The Sacred Scarabs destroy your {} and then consume you, leaving no trace of your presence behind.\n\n".format(inventory["Shield"], inventory["Weapon"], inventory["Armor"]))
        
        print("Unfortunately, you died, next time try get better equipment. Try Again.")
        exit()

    elif "Common" in inventory["Weapon"]:
        print("You brace yourself, raising your {} just in time to block the first wave. The scarabs' pincers crack your shield, and your {} blade dulls as it strikes their hardened shells. The battle is grueling, with the swarm attacking from all directions, but you fight valiantly.\n\nAfter a desperate struggle, you manage to defeat the swarm, collapsing to the ground in exhaustion. Your {} now suffered a lot, but it still holds. Drinking a **Healing Potion** restores your strength, allowing you to continue your journey.".format(inventory["Shield"], inventory["Weapon"], inventory["Armor"]))
        
        inventory["Misc"].remove("Healing Potion")
        inventory["Armor"] = "Damaged Common Armor"
        inventory["Weapon"] = "Dull Common Sword"
        inventory["Shield"] = "Damaged Common Shield"
        printInventory(inventory)
        
    else:
        print("With a steady hand, you raise your {}, which deflects the scarabs' strikes effortlessly. Their pincers glance harmlessly off your reinforced {}. Wielding your expertly sharpened {}, you cut through the swarm with precision and ease.\n\nThe battle is over almost as quickly as it began, and you stand victorious among the glowing remains. Your superior equipment has served you well, leaving you unscathed and ready to press onward.".format(inventory["Shield"], inventory["Armor"], inventory["Weapon"]))

    trapCorridor(inventory, side_quest_status)
    
def trapCorridor(inventory, side_quest_status):
    print("As you continue, the tunnel widens into a long corridor. The floor is covered in dust, and strange carvings line the walls. In a distance you see another fallen adventurer. From where you are, you cannot see what may have taken her. Her equipment seem unscathed making you feel nervous about the path in front of you.\n")
    
    choice = input("How to do you want to proceed? Do you want to carefully INVESTIGATE the floor and wall nearby or simply WALK towards the fallen Adventurer?").upper()
    
    if choice == "INVESTIGATE":
        print("Looking around you very carefully you notice in front of you a series of pressure plates and rows of small holes in the walls on either side. The holes are unnervingly aligned at chest height, and you quickly realize their purpose: they're meant for firing arrows.")
    elif choice == "WALK":
        print("Without warning, a stone beneath your foot sinks slightly, and the sound of grinding mechanisms fills the air.\n\nClick. Click.\n\nArrows shoot out of the walls, narrowly missing you. You dive forward, landing hard but avoiding injury. The arrows stop, but the danger isn't over. Ahead, you see pressure plates scattered across the floor. On the wall, there's a faint carving of a path—a possible solution to avoid triggering the traps.")
    else:
        print("Nervously, you begin to look around, trying to make sense of your situation. Your heart pounds as you scan the corridor, searching for clues. But in a moment of cruel irony, you lose your balance and stumble forward and fall landing squarely on a pressure plate.\n\n A sharp click echoes through the air, followed by the unmistakable sound of something slicing through the darkness. You instinctively duck as arrows whistle past, narrowly missing your head. Your breath catches in your throat as you realize the deadly nature of the trap you're facing.\n\nEventually, the arrows stop, and the corridor falls silent once more. Shaken but alive, you take a cautious step back and notice the other pressure plates stretching ahead. Your eyes drift to the carvings on the wall—intricate patterns and faint symbols etched into the stone. Could they be a clue? A way to navigate this deadly puzzle? You can't be sure, but it's clear you'll need to rely on them if you hope to survive.")
    
    print("You take a deep breath and focus on the carvings on the wall. The symbols depict a series of footprints crossing the corridor, with certain pressure plates marked by faint, glowing runes. The path looks deceptively simple, but one wrong step could spell disaster.\n\nAs you study the carvings more closely, you notice something peculiar. The strange medallion in your pack begins to emit a faint, warm glow. Curious, you take it out and hold it up to the wall. To your amazement, the carvings react—the glowing runes brighten, and the correct path through the pressure plates becomes much clearer.\n\nCarefully, you place your foot on the first marked plate. Nothing happens. Emboldened, you follow the pattern indicated by the carvings, using the medallion's glow as your guide. Each step feels like an eternity, the sound of your boots against the dusty floor echoing ominously through the corridor.\n\nHalfway across, you hesitate. The carvings show two possible steps forward, but only one is marked with a rune. You glance at the medallion, which grows warmer in your hand, and trust its guidance. Choosing the marked plate, you proceed without incident. \n\nFinally, you step onto the last plate and exhale a shaky breath. The medallion's glow fades, and the corridor ahead stretches out, free of traps. Behind you, the intricate carvings dim as if the path has been sealed for anyone else. You've solved the puzzle and can now continue deeper into the tomb. At distance you see a lever nearby.")
    choice = input("Do you PULL the lever?").upper()
    
    if choice == "PULL":
        print("You decide to pull the lever, and the faint, almost imperceptible clicking sound that had filled the corridor suddenly stops. It's only now, in the silence, that you realize the noise had been there all along—an ominous backdrop you hadn't noticed until the tension eased after passing the traps.\n\nWith the mechanism seemingly disarmed, the path ahead feels safer. You turn your attention to the fallen adventurer's remains. Now it seems safe to SEARCH for anything useful in her remains, or you can CONTINUE your way.")
        side_choice = input("What will you do?").upper()
        
        if side_choice == "SEARCH":
            print("Now that you are able to approach safely you notice a couple of arrows in the adventurers armor and shield. Besides that, her equipment seems almost unscathed. It seems he was a swordsman as yourself and his equipment is very similar to the common one the blacksmith tried to sell to you in the village.")
            
            if "Damage" in inventory["Armor"]:
                print("Not knowing what kind of dangers lay ahead you have to make a choice. If you want you can change you equipment for his or respect the fallen and continue your way.")             
                side_choice2 = input("Will you TAKE his equipment?").upper()
                
                if side_choice2 == "TAKE":
                    print("You decide that is wiser to take his equipment, so you take the arrows out, change your equipment with the fallen. When you were standing you decide, not only take the equipment but you also take a **Token**, promising to honor him after you get out of this tomb. Afterwards you continue your way towards the next room.")
                    
                    inventory["Armor"] = "Common Armor"
                    inventory["Weapon"] = "Common Sword"
                    inventory["Shield"] = "Common Shield"
                else:
                    print("You prefer to take a **Token** from the remains promising that you will honor the fallen after you get out of this tomb, but do not take his equipment. Now you make your way towards the next room.")
            else:
                print("You short your distance to the fallen and take a **Token** from the remains promising that you will honor the fallen after you get out of this tomb. Now you make your way towards the next room.")
                
            inventory["Misc"].append("Token from the Fallen")
            printInventory(inventory)
            
            bossAntechamber(inventory, side_quest_status)
        
        elif side_choice == "CONTINUE": 
            print("Thinking this room may still have another surprise, you decide that is wiser to just make your way to the next room. Simply leaving a prayer for the fallen.")
            
            bossAntechamber(inventory, side_quest_status)
            
        else:
            print("You seem a bit undecided for a while, but you finally choose to keep going your way to the next room, thinking it may be wiser, leaving the fallen with a prayer.")
            
            bossAntechamber(inventory, side_quest_status)
        
    else:
        print("Afraid of what kind of new hell this lever could release, you chose to just continue your way towards the other room, leaving the fallen with a prayer.")

        bossAntechamber(inventory, side_quest_status)

def antechamberDecisions(choice, inventory, side_quest_status, times_dragged = 0, door_opened = False, wall_read = False, right_check = False, dragged = False):

    if choice == "LEFT":
        if not dragged:
            print("You are able to resist the whispers and go in direction to the left wall.")
        if not wall_read:
            print("As you approach the wall, you notice it is completely covered in intricate carvings, telling a story through vivid images and symbols. The tale begins to take shape as you study it: a mighty ruler, long forgotten by time, who sought immortality. This tomb was not meant as a resting place, but as a ritual chamber to achieve his wicked ambition.\n\nThe carvings depict the ruler's rise to power and their growing obsession with eternal life. At the center of this obsession was the creation of a diadem — a vessel designed to hoard the remaining years of their subjects' lives. The ruler's goal was to prolong their own life indefinitely by stealing the life force of others.\n\nHowever, the gods, witnessing such evil, intervened. They twisted the ritual, ensuring its completion would not grant the ruler the immortality they had craved. Instead, it transformed them into an undead being—immortal but mindless, stripped of intelligence and agency. Yet the gods' punishment was not without risk. They feared that over centuries, as the balance of their interference waned, the ruler might gradually regain their mind and with it, the power to seek vengeance upon the world for thwarting their ambitions.\n\n To forestall this terrifying possibility, the gods took extreme measures. They summoned their priests to construct this tomb, not as a sanctuary but as an inescapable prison. But mere stone walls could not bind a being of such forbidden might forever. The gods devised a grim justice for the atrocity committed against the ruler's subjects: the very souls of those who had been drained of their remaining years were called forth, tethered to the tomb itself. Once freed from their mortal prisons, these stolen souls were bound by divine will to guard the tomb, ensuring the ruler could never reclaim the cursed diadem or escape to wreak havoc on the living. The carvings show their spectral forms, mournful and vigilant, their unearthly faces etched in every detail upon the walls. Eyes like empty voids gaze at all who dare enter, a warning to trespassers and a tribute to their stolen lives.\n\nThe final panels portray a dire prophecy: should the ruler's intellect return before the last of the stolen years is spent, their wrath will be unthinkable. The gods foresaw that should the ruler emerge, freed of their prison and brimming with knowledge gained through eons of unending existence, they would unleash a dark age from which the world might not recover. Justice must take its course, and the price of the ruler's ambition must be paid in full. Until that time comes, the tomb must hold them, and the souls of the wronged will remain vigilant, trapped themselves but driven by divine compulsion to serve their tormentor's eternal punishment.\n\n")
            
            if dragged:
                print("Knowing the history behind this tomb, you think the whispers that you heard are the souls that guard this place, and that if they are so eager for you to open this door, the time must have come to free them from their role.\n\n")
            else:
                print("Now that you know the story behind this relic, you feel sorry for them but if the time wasn't right the gods would never allow him to get so far...\n\n")
            
            if door_opened:
                print("Knowing the history behind this tomb, you realize the spirits have expressed their gratitude to you. You whisper a prayer to the gods, hoping that these souls may finally find the rest they deserve.")
            
            side_choice = input("Now do you want to STRAIGHT to the door or go to the LEFT to breath a bit of fresh air").upper()
            
            wall_read = True
            antechamberDecisions(side_choice, inventory, side_quest_status, times_dragged, door_opened, wall_read, right_check, dragged)
        
        else:
            print("You come back to the wall, but you cannot get new information from it. Looking to this wall and the history it tells you makes you think what will you do with the relic afterwards...")
            side_choice = input("Now do you want to STRAIGHT to the door or go to the LEFT to breath a bit of fresh air").upper()
            
            antechamberDecisions(side_choice, inventory, side_quest_status, times_dragged, door_opened, wall_read, right_check, dragged)
            
    elif choice == "RIGHT":
        if not door_opened:
            if not dragged:
                print("You are able to resist the whispers and head toward the right wall..\n\n")
            else:
                print("This time, you manage to resist the whispers and move toward the right wall.\n\n") 
        
        print("In the dim tomb with no windows or ventilation, the faint sunlight and gentle breeze touching your face remind you how grateful you are to breathe fresh air and glimpse the sky once more.\n\nWhile you are there, savoring this brief moment of solace, a glimmer catches your eye, reflecting faintly beneath the fallen boulders. Upon closer inspection, you see the crushed remains of two adventurers, their armor still glinting faintly bellow the boulders fallen after the ceiling's collapse. Struck by the tragedy of their fate, you carefully retrieve a small **Token** from both adventurers, resolving to give them a proper burial once you escape this tomb. Before moving on, you close your eyes and offer a solemn prayer to the gods for their souls, hoping they may find peace in the afterlife.\n\n")
        
        inventory["Misc"].remove("Token from the Fallen")
        inventory["Misc"].append("3x Token from the Fallen")
        
        printInventory(inventory)
        
        if side_quest_status == "Completed":
            if not "Beast Pelt" in inventory["Misc"]:
                print("While standing there, you notice a shadow passing overhead, reminding you of the wolf you helped earlier.\n\n") 
            
            if door_opened:
                side_choice = input("You decide you've had enough and need to choose: will you head STRAIGHT to the door, or go LEFT to inspect the carving in the opposite wall? ").upper()
                
            else:
                side_choice = input("The whispers grow louder and more insistent. You need to choose: will you head STRAIGHT to the door, or go to the LEFT to inspect the carving in the opposite wall?").upper()
                
            antechamberDecisions(side_choice, inventory, side_quest_status, times_dragged, door_opened, wall_read, right_check, dragged)
        else:
            print("While standing there, you notice a shadow passing overhead, and an ominous thought crosses your mind — what if the creature that killed the adventurer outside the tomb entrance is still lurking in the forest\n\n")
            
            if door_opened:
                side_choice = input("You decide you've had enough and need to choose: will you head STRAIGHT to the door, or go LEFT to inspect the carving in the opposite wall? ").upper()
                
            else:
                side_choice = input("The whispers grow louder and more insistent. You need to choose: will you head STRAIGHT to the door, or go to the LEFT to inspect the carving in the opposite wall?").upper()
                
            antechamberDecisions(side_choice, inventory, side_quest_status, times_dragged, door_opened, wall_read, right_check, dragged)
        
    elif choice == "STRAIGHT":
        if not door_opened:
            if dragged:
                print("This time, you purposely walk toward the door, determined to maintain control over your body and actions.\n\nStanding before the massive stone door, you take in its intricate carvings and glowing runes. At its center lies a circular indentation, faintly pulsing with light. You suspect it's meant for the **Strange Medallion**, the whispers that once urged you to take it from your bag now growing louder and more insistent. Their presence is unnerving, as if the door itself is alive and calling to you.\n\nThe **Strange Medallion* in your hand begins to glow brighter, almost as though it's begging to be placed in the indentation. Your hands twitch involuntarily, moving toward the groove of their own accord. But with great effort, you resist, pulling your hands back and forcing yourself to act on your terms. Slowly, deliberately, you press the **Strange Medallion** into the groove\n\n.The moment it clicks into place, you regain control of your body, staggering back a few steps. A sudden blue glow bursts forth, racing along the carved runes, illuminating the entire door with an otherworldly brilliance. For a second — a second that feels like an eternity — everything is still. Then, with a deep rumble, the massive door begins to shift and grind open, revealing a cavern beyond.\n\nAs the door opens, the whispers that had plagued your mind fade into silence. But just before they vanish entirely, you hear one last whisper, softer than the others, almost like a sigh. 'Thank you.'\n\nThe sudden quiet feels strange, almost hollow, as though a presence has left you. You step forward into the cavern, its vast expanse stretching into shadow. The air feels ancient, thick with the weight of time and secrets yet uncovered. Whatever lies ahead, you know this is only the beginning of what awaits.\n\n")
                
            else:
                print("Standing before a massive stone door, you take in its surface, covered in intricate carvings and glowing runes. At the center is a circular indentation, faintly pulsing with light, as though waiting for something. The whispers you've been hearing grow louder and more insistent, echoing in your mind.\n\nThe Strange Medallion in your hand begins to glow brighter, almost as if it's urging you to place it in the groove. Before you can stop yourself, your hands move on their own, picking up the Strange Medallion and pressing it into the indentation.\n\nThe moment it clicks into place, you regain control of your body and take a few cautious steps back. A faint blue glow spreads across the carvings on the door, illuminating the intricate patterns with an otherworldly light. For a second that feels like an eternity, nothing happens. Then, with a deep rumble, the giant stone door begins to shift and grind open, revealing a much larger cavern beyond.\n\nAs the door opens, the whispers suddenly fall silent. Just before they fade completely, a single soft whisper lingers in your mind, almost like a sigh. 'Thank you.'\n\n")  
            
            if wall_read:
               print("Knowing the history behind this tomb, you realize the spirits have expressed their gratitude to you. You whisper a prayer to the gods, hoping that these souls may finally find the rest they deserve.\n\n")     
            
            side_choice = input("What will you do now? See the RIGHT wall, go to the LEFT to breath a bit of fresh air, or GO straight ahead to the cave? ").upper()
            
            inventory["Misc"].remove("Strange Medallion")
            door_opened = True
            
            if side_choice == "GO":
                print("You decided to go straight to the cave, to finally fulfill your mission.\n\n")
                levelThree(inventory, side_quest_status)
            else:
                antechamberDecisions(side_choice, inventory, side_quest_status, times_dragged, door_opened, wall_read, right_check, dragged)
        else:
            side_choice = input("Now the door its opened, allowing you to see the cave ahead, do you want to GO straight ahead, or do you want to LOOK around a bit more? ").upper()
            
            if side_choice == "GO":
                print("You decided to go straight to the cave, to finally fulfill your mission.\n\n")
                levelThree(inventory, side_quest_status)
            
            elif side_choice == "LOOK":
                print("You don't think you are ready to proceed, so you decide to look around the antechamber a bit more.\n\n")
                side_choice = input("Do you want to the RIGHT wall, go to the LEFT to breath a bit of fresh air. ").upper()
                antechamberDecisions(side_choice, inventory, side_quest_status, times_dragged, door_opened, wall_read, right_check, dragged)
                
            else:
                print("You really don't feel ready to proceed so you decide to look around the antechamber a bit more.\n\n")
                side_choice = input("Do you want to the RIGHT wall, go to the LEFT to breath a bit of fresh air. ").upper()
                antechamberDecisions(side_choice, inventory, side_quest_status, times_dragged, door_opened, wall_read, right_check, dragged)
    
    else:
        times_dragged += 1
        if times_dragged == 0:
            print("While you were there trying to decide what to do next, while trying to ignore the insisting whispers. With time them seem to became louder, clearer, more insistent, you almost can't think clearly... Suddenly you notice that you are standing next to the door... It don't make any sense you have no memory of moving this direction. While you think about it, you notice that you've taken the **Strange Medallion** from your backpack noticing it as well the door glowing brightly every inch closer to the door.\n\nYour swordsman's instincts take control of your body, put the **Strange Medallion** back into the backpack and run to the entrance of the room. You are more cautious of the whispering and your actions.\n\n")
            dragged = True
            side_choice = input("What will you do now? See the RIGHT wall, go to the LEFT to breath a bit of fresh air, or STRAIGHT ahead to inspect the door? ")

        else: 
            print("You feel the whispering start to grow louder again, but you are now cautious about and run again directly to the entrance. You have to act purposely.\n\n")
            side_choice = input("What will you do now? See the RIGHT wall, go to the LEFT to breath a bit of fresh air, or STRAIGHT ahead to inspect the door? ")
        
        antechamberDecisions(side_choice, inventory, side_quest_status, times_dragged, door_opened, wall_read, right_check, dragged)                               

def bossAntechamber(inventory, side_quest_status):
            
        print("As you proceed deeper into the tunnel, you find yourself in what seems an antechamber. A magnificent room, at your left you see a carved wall that may have more information about this tomb and the relic, at the center there is a massive door, that seems that is whispering your name trying to attract you, finally, at your left seems that had another entrance to the chamber, but is blocked by boulder from the ceiling that have collapsed leaving a pile of jagged rocks. The opening above reveals the outside world — a small patch of sky painted in hues of orange and purple as the sun begins to set. A cool breeze flows into the chamber, carrying with it the faint scent of earth and trees.")
        choice = input("What will do? Go to the LEFT and inspect the wall, STRAIGHT to the door or to the RIGHT to breath a fresher air").upper()
        
        antechamberDecisions(choice, inventory, side_quest_status)  


def levelThree(inventory, side_quest_status):
    
    print("###############")
    print("# Level Three #")
    print("###############")
    
    print("\n\n# Migners Prison #\n\n")
    
    print("At last, you enter the cavern, it as well dimly lit with an outwardly blue light, looking around mesmerized by the size of it, the ceiling full of stalactites hanging there ominously on the ceiling, but the apparent lack of life, makes you wonder how well sealed this cavern was. But that thought only last a minute, as you pass the door and look around making sure the door will no imprison you for the eternity you notice you see claw marks, the oldest ones very small, the ones that seems more recent, very, very big. You ready yourself for the fight, scanning the cave for any movement or sound. You notice nothing nothing for a while, unexpectedly and without any other clues you hear a low growl before a huge pawn hits you throwing you far away. A monstrous creature — a cross between a lizard and a wolf—emerges from the shadows. Its scales shimmer faintly, and its eyes glow red.\n\n")
    
    if side_quest_status == "Completed" and not "Beast Pelt" in inventory["Misc"]:
        pass
          
          


if __name__ == "__main__":
    """
        Disclaimer: The text, and only text, was improved using ChatGPT 4o mini to correct spelling and grammar mistakes helping with immersion in the game. 
    """
    
    startGame()


