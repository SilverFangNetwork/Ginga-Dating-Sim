# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define player = Character("[playername]")
define mystery = Character("???")

define akakabuto = Character("Akakabuto")
define ben = Character("Ben")
define cross = Character("Cross")
define riki = Character("Riki")
define smith = Character("Smith")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    riki "Welcome to the Ohu army! We're always happy to see young dogs like yourself willing to fight."
    
    $ playername = renpy.input("What is your name?")
    $ playername = playername.strip()

    if not playername:
         $ playername = "Recruit"
         
    riki "Nice to meet you, [playername]! We don't have a platoon to assign you to yet. Feel free to talk to the other dogs for now."

menu:
    
    "Go hunting":
        jump gohunting
        
    "Akakabuto arc":
        jump akakabutoarc
    
label gohunting:
    
    cross "While hunting you run into Cross"
    
    jump end
    
label akakabutoarc:
    
    riki "Well [playername], you have created more trouble for everyone than good... to the point that every platoon leader has brought up the same topic."
    
    riki "Banishment."
    
    riki "Either leave now or you will be forced out."
    
menu:
    
    "I guess I can't argue with everyone...":
        jump akakabutoarc2
        
    "THIS IS UNJUST! I DEMAND FAIR TRIAL!":
        jump akakabutoarc3
        
label akakabutoarc2:
    
    riki "Ohu just isn't the right place for you. Farewell, [playername]."
    
    jump akakabutoarc4
    
label akakabutoarc3:
    
    riki "Of course. Jury, what do you say?"
    
    ben "Guilty!"
    
    smith "Guilty!"
    
    player "And with that, my scruff was grabbed and I was kicked out of the Ohu territory."
    
    jump akakabutarc4
    
label akakabutarc4:

    player "Dejected, I stumbled through the wilderness around Futago Pass for what felt like hours, turning tail whenever I caught the familiar scent of the Ohu army until..."
    
    player "What's that scent?"
    
    mystery "Gyoooooouugghhhh!"
    
    player "What?!"
    
    mystery "GYYOOOOUUUGGHHHHH!"
    
    player "What the hell is this?!"
    
    akakabuto "You stupid dog, what the HELL do you think you're doing in my territory?!"
    
    player "I'm... I'm a character in a dating game. But everyone hates me."
    
    player "Is this the bad ending? You're not going to eat me are you?"
    
    akakabuto "A dating game?"
    
    akakabuto "AND I WASN'T INVITED?"
    
    player "Kabuto-san... It's okay, if you're in the game, then you WERE invited!"
    
    akakabuto "Y-you're right! I'm here and that means..."
    
    akakabuto "Well..."
    
menu:
    
    "I love you... Akakabuto...":
        jump akakabutoarc5
        
    "Ai shiteru... Akakabut-san...":
        jump akakabutoarc5
        
    "Jag älskar dig... Akakabuto...":
        jump akakabutoarc5
        
label akakabutoarc5:
    
    player "At first I was scared but he was so gentle with me, his huge paws softly taking hold of me and holding me near his nose, letting me lean in on my own will."
    
    player "When we embraced, Akakabuto's coarse fur was warm past his frightening exterior, making me lean in closer."
    
    player "Unlike with the dogs of Ohu, I felt safe, protected. We spent a lot of time together after that."
    
    player "In fact, I think that if me and your father never met, the dogs and bears would have waged war with each other. Who knows what would have happened after that!"
    
    akakabuto "Well, I would be ruling over Futago pass unchallenged!"
    
    player "No doubt about it!"
    
    jump end
    
label end:
        
    # This ends the game.

    return

