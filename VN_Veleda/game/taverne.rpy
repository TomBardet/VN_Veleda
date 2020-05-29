######################################################
# Ici figurent les scènes se déroulant à la Taverne. #
######################################################

label taverne_DatingIngrid:
    

    scene bg_taverneJ with Dissolve (2.5) :
        xpos 20 ypos 70 zoom 0.7
        linear 1 xpos -100 ypos -50 zoom 0.85
    $ renpy.pause(0.25, hard = True)
    
    $ renpy.music.play("ambiances/AMB_Lieu_Taverne_02.ogg", channel = "ambiance", loop = True, fadein = 1)
    $ renpy.music.play("music/MUSIC_Taverne.ogg", channel = "music1", loop = True, fadein = 1)
    
    $ renpy.music.set_volume(0.4, delay=0, channel='music1')
    $ renpy.music.set_volume(0.4, delay=0, channel='music2')
    $ renpy.music.set_volume(0.4, delay=0, channel='ambiance')
    
    show char_ingrid normal at notSpeakingAnim(0.5, 1.11, 1.09, 0.25) with Dissolve (1.5)

    $ _window_during_transitions = True
    
    $ lieu = "Taverne"
    $ interlocuteur = "ingrid_char"
    
    play sound "sfx/Voices/Narrateur/Narrateur_Intro_07.ogg"
    
    nar "{cps=2} {/cps}{cps=40}What's that?{cps=2} {/cps}{cps=20}It looks like he is trying to hit on Ingrid!{/cps}"
    
    play sound "sfx/Voices/Player/Char_Player_Normal_01.ogg"
    
    y "Who are you calling 'he'? Are you talking about me?"
    
    play sound "sfx/Voices/Narrateur/Narrateur_Intro_08.ogg"
    
    nar "{cps=2} {/cps}Hey,{cps=4} {/cps}{cps=28}Wake up now!{/cps}{cps=2} {/cps}{cps=25}It's going to be your turn.{/cps}"
    
    show char_ingrid love at speakingAnim(0.5, 1.16, 1.14, 0.25)
    
    play sound "sfx/Voices/Ingrid/Char_Ingrid_Normal_01.ogg"
    
    i "Hihi! Wafflid, you're so cute!"

    show char_ingrid love at notSpeakingAnim(0.5, 1.16, 1.14, 0.25)
    
    menu:
        i "{cps=0}Hihi! Wafflid, you're so cute!{/cps}"
        
        "Let's go look at the stars together, Ingrid!":
            play sound "sfx/Voices/Player/Char_Player_Normal_03.ogg"
            y "Ingrid, follow me!"
            y "We shall admire how the stars illuminate your moonlit beauty!"
        "That's true, I am pretty handsome.":
            play sound "sfx/Voices/Player/Char_Player_Normal_03.ogg"
            y "I am often told that I am quite attractive, yes..."
            y "I just take good care of myself!"
        "Ingrid, marry me!":
            play sound "sfx/Voices/Player/Char_Player_Normal_03.ogg"
            y "Marry me Ingrid!"
            y "I have been madly in love with you for the past 8 days."
    
    show char_ingrid degout at speakingAnim(0.5, 1.16, 1.14, 0.25)
    
    play sound "sfx/Voices/Ingrid/Char_Ingrid_Degout_04.ogg"
    
    i "Hum... I mean... you're like a little brother to me."
    
    show char_ingrid degout at notSpeakingAnim(0.5, 1.16, 1.14, 0.25)
    
    play sound "sfx/Voices/Player/Char_Player_Normal_04.ogg"
    y "A little brother... Hehe I knew I had a shot!"
    nar "What ?! What do you mean 'a shot'?!"
    nar "Fine. I'll give you a hand."
    
    show screen datingSim(ingrid_char, 0.57, 0.33)
    pause 1.0
    $ loveGauge(ingrid_char, -10, 0.67, 0.33)

    menu:
        nar "{cps=0}Fine. I'll give you a hand.{/cps}"
        
        "Huh? What are those numbers supposed to be?!":
            play sound "sfx/Voices/Player/Char_Player_Normal_01.ogg"
            y "Huh? What are those numbers supposed to be?!"
            
        "Hey! Why did I lose 10 points?!":
            play sound "sfx/Voices/Player/Char_Player_Normal_01.ogg"
            y "Hey! Why did I lose 10 points?!"

    nar "These numbers show the affection of the person you are talking to."
    nar "The higher the number, the better the person likes you."
    nar "This kind of mechanic is very common in dating sims..."
    
    play sound "sfx/Voices/Player/Char_Player_Normal_02.ogg"        
    y "Dating whats?"
    $ loveGauge(ingrid_char, -5, 0.67, 0.33)
    show char_ingrid degout at speakingAnim(0.5, 1.16, 1.14, 0.25)
    
    play sound "sfx/Voices/Ingrid/Char_Ingrid_Normal_04.ogg"
    
    i "... Wafflid? Who are you talking to? You worry me..."
    
    show char_ingrid degout at notSpeakingAnim(0.5, 1.16, 1.14, 0.25)
    
    play sound "sfx/Voices/Player/Char_Player_Normal_04.ogg"
    y "I'm just talking to the narrator. He made a bunch of numbers appear above your head."
    show char_ingrid degout at speakingAnim(0.5, 1.16, 1.14, 0.25)
    
    play sound "sfx/Voices/Ingrid/Char_Ingrid_Degout_02.ogg"
    
    i "..........."
    i "Listen... I have to go. Bye!"
    
    play sound "sfx/SFX_Run_01.ogg"
    hide screen datingSim
    show char_ingrid degout:
        xalign 0.5 yalign 0.8
        xpos 0.5 ypos 1.16 zoom 0.25
        parallel:
            linear 1.6 xpos 1.5
        parallel:
            linear 0.1 rotate 10
    $ renpy.pause (1.5, hard = True)
            
    play sound "sfx/Voices/Player/Char_Player_Heureux_03.ogg"    
    y "Hehe, this date was perfect!"
    y "Alright, let's head to bed."
    y "If I'm late to work tomorrow, Veleda will get mad at me."
    
    stop ambiance fadeout 1    
    stop music1 fadeout 1.5

            
    jump narration_ellipse01
 
# -----------------------------------------# 
 
label taverne_PresentationDot:
    $ _window_during_transitions = False
    scene bg_taverneJ with Dissolve (2.5) :
        xpos 20 ypos 70 zoom 0.7
        linear 1 xpos -100 ypos -50 zoom 0.81
    $ renpy.pause(0.25, hard = True)
    show char_ingrid normal at speakingAnim(0.5, 1.16, 1.14, 0.25) with Dissolve(1.5)
    
   
    $ renpy.music.play("ambiances/AMB_Lieu_Taverne_02.ogg", channel = "ambiance", loop = True, fadein = 1)
    $ renpy.music.play("music/MUSIC_Taverne.ogg", channel = "music1", loop = True, fadein = 1)
    
    $ renpy.music.set_volume(0.4, delay=0, channel='music1')
    $ renpy.music.set_volume(0.4, delay=0, channel='music2')
    $ renpy.music.set_volume(0.4, delay=0, channel='ambiance')
    
    $ lieu = "Taverne"
    $ interlocuteur = "ingrid_char"
    
    show screen datingSim(ingrid_char, 0.57, 0.30)
    play sound "sfx/Voices/Ingrid/Char_Ingrid_Normal_01.ogg"
    i "Wafflid?!"
    i "Hm... listen, I'm sorry I ran away last time."
    i "It's just... you were being very weird!"
    
    show char_ingrid normal at notSpeakingAnim(0.5, 1.16, 1.14, 0.25)
    menu:
        i "{cps=0}It's just... you were being very weird!{/cps}"
        
        "That's how I am, Baby. Take it or leave it.":
            play sound "sfx/Voices/Player/Char_Player_Sarcastic_02.ogg"
            y "That's how I am, Baby. Take it or leave it."
            $ loveGauge(ingrid_char, -2, 0.65, 0.3)
            show char_ingrid degout at speakingAnim(0.5, 1.16, 1.14, 0.25)
            play sound "sfx/Voices/Ingrid/Char_Ingrid_Degout_04.ogg"
            i "Uuh..."
        "It was all because of the numbers!":
            play sound "sfx/Voices/Player/Char_Player_Normal_03.ogg"
            y "Have you never seen numbers above people's heads?"
            $ loveGauge(ingrid_char, -1, 0.65, 0.3)
            show char_ingrid degout at speakingAnim(0.5, 1.16, 1.14, 0.25)
            play sound "sfx/Voices/Ingrid/Char_Ingrid_Degout_04.ogg"
            i "Uuh..."
        "I want to marry you, Ingrid!":
            y "Marry me, Ingrid!"
            $ loveGauge(ingrid_char, -4, 0.65, 0.3)
            show char_ingrid degout at speakingAnim(0.5, 1.16, 1.14, 0.25)
            play sound "sfx/Voices/Ingrid/Char_Ingrid_Degout_04.ogg"
            i "Uuh..."
        
    i "Why don't I just go and get you a drink, Wafflid?"
    show char_ingrid degout at notSpeakingAnim(0.5, 1.16, 1.14, 0.25)
    play sound "sfx/Voices/Player/Char_Player_Heureux_01.ogg"
    y "Yes please!"
    hide screen datingSim
    $ renpy.music.set_volume(0, delay = 0.4, channel='music1')
    $ renpy.music.set_volume(0, delay = 0.4, channel='music2')
    $ renpy.music.set_volume(0, delay=0.4, channel='ambiance')
    scene black with Dissolve(1.5)
    play sound "sfx/Voices/Player/Char_Player_Boire_03.ogg"
    pause 2.5
    $ renpy.music.set_volume(0.4, delay = 1, channel='music1')
    $ renpy.music.set_volume(0.4, delay= 1, channel='ambiance')
    scene bg_taverneJ with Dissolve (1.0):
        xpos -100 ypos -50 zoom 0.81
    show screen datingSim(ingrid_char, 0.57, 0.30)
    show char_ingrid normal at notSpeakingAnim(0.5, 1.11, 1.14, 0.25)   
    y "Ingrid, I..."
    y "I love you! Let's get married!"
    $ loveGauge(ingrid_char, 2, 0.65, 0.3)
    show char_ingrid normal at speakingAnim(0.5, 1.16, 1.14, 0.25)
    play sound "sfx/Voices/Ingrid/Char_Ingrid_Normal_03.ogg"
    i "Listen Wafflid, it's not that simple you know."
    i "Love is not a game."
    i "I will only fall in love with you if you bring me a dowry."
    show char_ingrid normal at notSpeakingAnim(0.5, 1.16, 1.14, 0.25)
    play sound "sfx/Voices/Player/Char_Player_Hesitation_01.ogg"
    y "A dowry?"
    show char_ingrid normal at speakingAnim(0.5, 1.16, 1.14, 0.25)
    i "It's tradition, you know that! You need a {b}glaive{/b} and a {b}shield{/b} to marry me."
    show char_ingrid normal at notSpeakingAnim(0.5, 1.16, 1.14, 0.25)
    y "What... why?"
    show char_ingrid normal at speakingAnim(0.5, 1.16, 1.14, 0.25)
    play sound "sfx/Voices/Ingrid/Char_Ingrid_Love_03.ogg"
    i "Don't say anymore Wafflid! None can understand love!"
    hide screen datingSim
    show char_ingrid normal:
        xalign 0.5 yalign 0.8
        xpos 0.5 ypos 1.15 zoom 0.25
        parallel:
            linear 3.0 xpos -0.5
        parallel:
            linear 0.1 rotate 10
    i "Don't forget! A {b}glaive{/b} and a {b}shield{/b} !"
    show char_ingrid normal:
        xalign 0.5 yalign 0.8
        xpos -0.5 ypos 1.5 zoom 0.25 rotate 30
        linear 1.0 xpos 0.05 ypos 1.15
    pause 1.5
    play sound "sfx/Voices/Ingrid/Char_Ingrid_Normal_03.ogg"
    i "Another drink?"
    play sound "sfx/Voices/Player/Char_Player_Normal_04.ogg"
    y "... Yes."
    show char_ingrid normal:
        xalign 0.5 yalign 0.8
        xpos 0.05 ypos 1.15 zoom 0.25 rotate 30
        linear 1.0 xpos -0.5 ypos 1.5
    pause 1.0
    
    $ renpy.music.set_volume(0, delay = 0.2, channel='music1')
    $ renpy.music.set_volume(0, delay = 0.2, channel='music2')
    $ renpy.music.set_volume(0, delay=0.2, channel='ambiance')
    
    scene black with Dissolve(2.0)
    
    play sound "sfx/Voices/Player/Char_Player_Boire_03.ogg"
    pause 2.8
    
    outline "A few drinks later..."
     
    jump taverne_AbusAlcoolPart1
     
# -----------------------------------------#

label taverne_AbusAlcoolPart1:
    
    $ renpy.music.set_volume(0.4, delay = 0.5, channel='music1')
    $ renpy.music.set_volume(0.4, delay= 0.5, channel='ambiance')
    
    scene bg_taverneFull with Dissolve(0.8):
        zoom 0.65 xpos -0.5
        easein 2.0 zoom 0.73 xpos -1.15
    $ renpy.pause(2.0, hard = True)
    $ _window_during_transitions = True

    show char_goat normal:
        xalign 0.5 yalign 0.8
        zoom 0.35 xpos 0.5 ypos 1.5
        easein 0.8 ypos 0.73
    pause 1.2
    $ lieu = "Taverne2"
    $ interlocuteur = "goat_char"
    
    y "And then, she tells me: "
    y "Bring me back a {b}shield{/b} and a {b}glaive{/b}!"
    show char_goat choc at speakingAnim(0.5, 0.73, 0.71, 0.35)
    show screen datingSim(goat_char, 0.28, 0.42)
    play sound "sfx/Voices/Chevre/Char_Chevre_Normal_01.ogg"
    goat "Bêêêêêêêêêêêêh."
    show char_goat choc at notSpeakingAnim(0.5, 0.73, 0.71, 0.35)
    play sound "sfx/Voices/Player/Char_Player_Sarcastic_04.ogg"
    y "Can you believe it?"
    show char_goat normal at speakingAnim(0.5, 0.73, 0.71, 0.35)
    play sound "sfx/Voices/Chevre/Char_Chevre_Normal_02.ogg"
    goat "Bêêêêêêêêêêh."
    show char_goat normal at notSpeakingAnim(0.5, 0.73, 0.71, 0.35)
    menu:
        goat "{cps=0}Bêêêêêêêêêêêh.{/cps}"
        "That's right!":
            y "Nah, yeah, you're just so right!"
            play sound "sfx/Voices/Player/Char_Player_Heureux_03.ogg"
            $ loveGauge(goat_char, 15, 0.25, 0.41)
            y "Baby here's not some kinda lackey!"
            $ loveGauge(goat_char, 10, 0.25, 0.41)
            y "I'm not some kind of sheep!."
            $ loveGauge(goat_char, -4, 0.25, 0.41)
            show char_goat choc at speakingAnim(0.5, 0.73, 0.71, 0.35)
            play sound "sfx/Voices/Chevre/Char_Chevre_Choc1_01.ogg"
            goat "BÊÊÊÊÊÊH !"
            show char_goat choc at notSpeakingAnim(0.5, 0.73, 0.71, 0.35)
            play sound "sfx/Voices/Player/Char_Player_Sarcastic_03.ogg"
            y "Oh sorry! No offense."
        "That's a bit harsh...":
            play sound "sfx/Voices/Player/Char_Player_Non_01.ogg"
            y "You're sorta going too far there."
            $ loveGauge(goat_char, -1, 0.25, 0.41)
            y "She didn't say it in a mean way, really."
            $ loveGauge(goat_char, -1, 0.25, 0.41)
            y "She looked a bit sheepish I think."
            $ loveGauge(goat_char, -2, 0.25, 0.41)
            show char_goat choc at speakingAnim(0.5, 0.73, 0.71, 0.35)
            play sound "sfx/Voices/Chevre/Char_Chevre_Choc1_01.ogg"
            goat "BÊÊÊÊÊÊÊÊÊÊÊÊÊÊH !"
            show char_goat choc at notSpeakingAnim(0.5, 0.73, 0.71, 0.35)
            play sound "sfx/Voices/Player/Char_Player_Sarcastic_03.ogg"
            y "Oh sorry! No offense."
        "Bêêêêêêêêêêêh.":
            y "Bêêêêêêêêêêêêh."
            $ loveGauge(goat_char, 22, 0.25, 0.41)
    show char_goat love at speakingAnim(0.5, 0.73, 0.71, 0.35)
    play sound "sfx/Voices/Chevre/Char_Chevre_Love_01.ogg"
    goat "Bêêêêêêêêêêêêêêêh."
    show char_goat love at notSpeakingAnim(0.5, 0.73, 0.71, 0.35)
    menu:
        goat "{cps=0}Bêêêêêêêêêêêêêêêh.{/cps}"
        "Phew, I'm so happy you can forgive me.":
            play sound "sfx/Voices/Player/Char_Player_Heureux_04.ogg"
            y "Phew, I'm so happy you can forgive me."
            $ loveGauge(goat_char, 16, 0.25, 0.41)
            y "For a moment there, I... I thought I had ruined it all between us!"
            $ loveGauge(goat_char, 11, 0.25, 0.41)
            y "Thank god you are so understanding."
            $ loveGauge(goat_char, 13, 0.25, 0.41)
        "Really? You won't hold it against me?":
            play sound "sfx/Voices/Player/Char_Player_Heureux_04.ogg"
            y "Really? You won't hold it against me?"
            $ loveGauge(goat_char, 10, 0.25, 0.41)
            y "I'm so relieved."
            $ loveGauge(goat_char, 11, 0.25, 0.41)
            y "For a moment there, I... I thought I had ruined it all between us!"
            $ loveGauge(goat_char, 10, 0.25, 0.41)
            y "Thank god you are so understanding."
            $ loveGauge(goat_char, 5, 0.25, 0.41)
        "Bêêêêêêêêêêêêêêêêêêêêêêêh":
            y "Bêêêêêêêêêêêêêêêêêêêh." 
            $ loveGauge(goat_char, 22, 0.25, 0.41)
    show char_goat love at speakingAnim(0.5, 0.73, 0.71, 0.35)
    play sound "sfx/Voices/Chevre/Char_Chevre_Love_02.ogg"
    goat "Bêêêêêêêêêêêêêêêh."
    show char_goat love at notSpeakingAnim(0.5, 0.73, 0.71, 0.35)
    menu:
        goat "{cps=0}Bêêêêêêêêêêêêêêêh{/cps}"
        "You have beautiful eyes.":
            play sound "sfx/Voices/Player/Char_Player_Heureux_03.ogg"
            y "Hey... you know... you have the prettiest eyes."
            $ loveGauge(goat_char, 21, 0.25, 0.41)
            y "I'm serious. When you look at me like this, I feel..."
            y "I feel like you are staring straight into my soul."
            $ loveGauge(goat_char, 19, 0.25, 0.41)
            y "Do you believe in soulmates?"
        "Woooow! Your wool is so soft!":
            play sound "sfx/Voices/Player/Char_Player_Heureux_03.ogg"
            y "Woooow! Your wool is so soft!"
            $ loveGauge(goat_char, 15, 0.25, 0.41)
            y "Such silky hair... you have got to tell me what brand of shampoo you use."
            $ loveGauge(goat_char, 10, 0.25, 0.41)
            y "I've always been obsessed by personal hygiene."
            y "You too, apparently..."
            $ loveGauge(goat_char, 13, 0.25, 0.41)
            y "Do you believe in soulmates?"
        "Bêêêêêêêêêêêêêêêêêêêêêêêêêêêh": 
            y "Bêêêêêêêêêêêêêêêêêêêêêêêh."  
            $ loveGauge(goat_char, 25, 0.25, 0.41)
    show char_goat love at speakingAnim(0.5, 0.73, 0.71, 0.35)
    play sound "sfx/Voices/Chevre/Char_Chevre_Heureux_01.ogg"
    goat "Bêêêêêêêêêêêêêêêh." 
    goat "Bêêêêhêêêhêê- *cough*"
    goat "F-F-Faaaalfliiid !"
    show char_goat love at notSpeakingAnim(0.5, 0.73, 0.71, 0.35)
    play sound "sfx/Voices/Player/Char_Player_Non_04.ogg"
    y "Wafflid."
    show char_goat normal at speakingAnim(0.5, 0.73, 0.71, 0.35)
    play sound "sfx/Voices/Chevre/Char_Chevre_Heureux_02.ogg"
    goat "Sorry. W-W-Waaaaaaaffliiiid."
    goat "You broke the curse by speaking to me with love."
    goat "You are an extraordinary person, Wafflid. Really."
    goat "As a sign of my gratitude, please accept this {b}joke{/b}."
    $ inventory.add(blague)
    $ _testBlague = 1
    show img_blague at center:
        xalign 0.7 yalign 0.9 zoom 0.3
        linear 0.5 yalign 0.7 zoom 0.4
        easein 0.5 zoom 0.55
        easeout 0.5 zoom 0.38
        pause 0.5
        parallel :
            linear 0.8 yalign 0.05 xalign 0.95 zoom 0.3
        parallel :
            linear 0.9 alpha 0
    show img_bag:
        xpos 1.0 yalign 0.05 zoom 1.0
        linear 0.5 xpos 0.87 yalign 0.05
        pause 2.3
        easein 0.3 zoom 1.1
        easeout 0.3 zoom 1.0 
        pause 0.5
        linear 0.3 xpos 1.0
        pause 2.0
    play sound "sfx/SFX_UI_Inventory_Bag_01.ogg"
    pause 1.0
    play sound "sfx/Voices/Chevre/Char_Chevre_Heureux_03.ogg"
    goat "It can make anyone laugh, and will help you climp to the highest rungs of society."
    goat "I must go now."
    goat "Goodbye, Wafflid!"
    hide screen datingSim
    show char_goat normal:
        xalign 0.5 yalign 0.8
        zoom 0.35 xpos 0.5 ypos 0.7
        parallel :
            linear 3.5 zoom 0.8
        parallel :
            linear 3.5 alpha 0.3
        parallel :
            easeout 3.5 ypos -0.5
        parallel :
            block:
                easein 0.2 rotate 2
                easein 0.2 rotate -2
                repeat
    pause 1.5
    play sound "sfx/Voices/Player/Char_Player_Non_02.ogg"
    y "Nooo! Come back!"
    y "..."
    y "She's gone..."
    y "I'm drunk..."
    stop music1 fadeout 1.5
    stop music2 fadeout 1.5
    stop ambiance fadeout 1.0
    scene black with Dissolve (2.0)
    jump narration_ellipseCuite

#######################################################
#               CONCOURS BACHELORS, intro            ##
#######################################################
# ----------------------------------------- #

label Act2_transition_alldone:

    scene black with Dissolve(0.5)
    outline "A while later, in the tavern..."
    jump taverne_ConcoursPart1
    
#------------------------------------------#

label placeDuVillage_Concours_Placeholder:

    outline "The player clicks on the tavern"
       
# -----------------------------------------#

label taverne_ConcoursPart1:
    
    $ renpy.music.play("ambiances/AMB_Lieu_Taverne_02.ogg", channel = "ambiance", loop = True, fadein = 0.5)
    
    scene bg_taverne2N with Dissolve(0.5):
        zoom 0.70
    show char_ingrid normal:
        xalign 0.5 yalign 0.8
        xpos -0.5 ypos 1.5 zoom 0.25 rotate 30
        linear 0.5 xpos 0.05 ypos 1.15
    #show char_ingrid normal at notSpeakingAnim(0.5, 0.95, 0.92, 0.22) with Dissolve(0.5)
    pause 0.5
    #show char_ingrid normal at speakingAnim(0.50, 1.0, 0.98, 0.22)
    play sound "sfx/Voices/Ingrid/Char_Ingrid_Normal_01.ogg"
    i "Wafflid! You are finally here, we were waiting for you!"
    show char_ingrid normal:
        xalign 0.5 yalign 0.8
        xpos 0.05 ypos 1.15 zoom 0.25 rotate 30
        #linear 0.5 xpos 0.8 ypos 1.15
        parallel:
            linear 0.5 xpos 0.5
        parallel:
            linear 0.3 rotate 0
    pause 1.0
    
    show screen datingSim(ingrid_char, 0.50, 0.13)
    
    play sound "sfx/Voices/Player/Char_Player_Heureux_01.ogg"
    y "I have the dowry, my dear pancake!"
    show char_ingrid normal at speakingAnim(0.50, 1.15, 1.12, 0.25)
    play sound "sfx/Voices/Ingrid/Char_Ingrid_Love_02.ogg"
    
    $ loveGauge(ingrid_char, +10, 0.50, 0.13)
    
    i "Good! We can start the contest!"
    show char_ingrid normal at notSpeakingAnim(0.50, 1.15, 1.12, 0.25)
    play sound "sfx/Voices/Player/Char_Player_Normal_01.ogg"
    y "Of course! …wait, what?"
    show char_ingrid normal at speakingAnim(0.50, 1.15, 1.12, 0.25)
    
    hide screen datingSim
    
    i "Shh! It's starting!"
    
    jump taverne_Concours_Part2_0_Transition

# --------------DESACTIVé--------------#

label taverne_ConcoursPart1_choice:

    menu:
        i "{cps=0}Gaufrid ! Enfin tu es là ! On t’attendait !{/cps}"
        "J'étais attendu ?":
            y "Ah bon ? Vous m’attendiez ?"
            i "Tout le village est là pour toi Gaufrid !"
            y "Ah bah tiens ! Ça fait plaisir !"
            y "On va pouvoir se marier !" 
        "Toi et...?":
            y "Vous m’attendiez ? Toi et qui d’autre ?"
            i "Moi, Brutalmund, Beaudrik… "
            i "Tout le village est là pour toi Gaufrid !"
            y "Ah bah tiens ! Ça fait plaisir !"
            y "On va pouvoir se marier !"
        "J'ai la dot !":
            y "Ingrid ! J’ai le bouclier et le glaive !"
            y "On va pouvoir se marier !"
        "Je suis là ma belle":
            y "Je suis là pour toi, ma pupuce."
            y "On peut enfin se marier !"
            
    i "Oh t’es mignon, Gaufrid ! Mais ce n’est pas si simple que ça."
    i "Maintenant que tu es là, nous pouvons enfin commencer le concours !"
    y "Oui bien sûr ! …attends, quoi ?"
    i "Shh ! ça commence !"

    jump taverne_Concours_Part2_0_Transition
    
# -----------------------------------------#

    
label taverne_Concours_Part2_0_Transition:
    scene black with Dissolve(0.5)
    play sound "sfx/SFX_TVShow_01.ogg"
    $ renpy.pause(1.5, hard = True)
    outline "Once upon a time, in Germania…"
    outline "...Beaudrik and Wafflid, two eligible Germani bachelors."
    $ renpy.pause(2.0, hard = True)
    jump taverne_Concours_Part2_1_Intro
    
# -----------------------------------------#
    
label taverne_Concours_Part2_1_Intro:
    
    
    #NARRATEUR--------------> nar "{i}{color=#f2de5c}{/color}{/i}"
    scene bg_taverneN with Dissolve (0.5):
        zoom 0.70
    pause 1.0
    outline "Welcome to the first century edition of: \n « Bructeri Bachelor », on air every friday in the village tavern!"
    #nar "{i}{color=#f2de5c}Welcome to the first century edition of: \n « Bructeri Bachelor », on air every friday in the village tavern!{/color}{/i}"
    show char_ingrid normal at notSpeakingAnim(0.5, 1.16, 1.14, 0.25):
        zoom 1.0 xpos 0.0 ypos 1.115
        linear 0.4 xpos 0.18
    $ renpy.music.play("music/MUSIC_Etable_Normale.ogg", channel = "music1", loop = True, fadein = 4)
    nar "{i}{color=#f2de5c}Ingrid is a beautiful, single young lady, looking for love.{/i}{/color}"
    nar "{i}{color=#f2de5c}Torn between the beauty of the body and the beauty of the heart, \n Ingrid must chose between two charming enough Germans.{/i}{/color}"
    show char_beaudrik normal left :
        xalign 0.5 yalign 0.8
        zoom 0.8 xpos 1.0 ypos 0.8
        linear 0.4 xpos 0.86
    pause 0.4
    show char_ingrid love at notSpeakingAnim(0.18, 1.115, 1.14, 0.25)
    nar "{i}{color=#f2de5c}On one side, Beaudrik, a paragon on manliness.{/i}{/color}"
    show char_ingrid degout at notSpeakingAnim(0.18, 1.115, 1.14, 0.25)
    show char_beaudrik mepris2 left at notSpeakingAnim(0.86, 0.85, 0.88, 0.8)
    nar "{i}{color=#f2de5c}On the other, Wafflid, ugly and skinny.{/i}{/color}"
    show char_ingrid degout at notSpeakingAnim(0.18, 1.115, 1.14, 0.25)
    show char_beaudrik mepris2 left at notSpeakingAnim(0.86, 0.85, 0.88, 0.8)
    play sound "sfx/Voices/Player/Char_Player_Non_03.ogg"
    y "Can someone please tell me what's going on?"
    show char_ingrid degout at speakingAnim(0.18, 1.15, 1.17, 0.25)
    play sound "sfx/Voices/Ingrid/Char_Ingrid_Degout_02.ogg"
    i "Don't interrupt the host, Wafflid!"
    #nar "{i}{color=#f2de5c}Ingrid is a beautiful, single young lady, looking for love.{/color}{/i}"
    #nar "{i}{color=#f2de5c}Torn between the beauty of the body and the beauty of the heart, \n Ingrid must chose between two charming enough Germans."
    #nar "{i}{color=#f2de5c}On one side, Beaudrik, a paragon on manliness.{/color}{/i}"
    #nar "{i}{color=#f2de5c}On the other, Wafflid, ugly and skinny.{/color}{/i}"

    jump taverne_Concours_Part2_2_Manual
    
# -----------------------------------------#   

label taverne_Concours_Part2_1_Intro_choice:
    
    menu:
        "Hey, I'm not ugly!":
            y "How dare you?"
            outline "Shut up. I'm talking."
            outline "Et n’oublie pas que je \n peux lire tes \n choix de dialogue."
            outline "Je disais…"
        "Qu’est-ce qu’il se passe ?":
            y "Quelqu’un peut m’expliquer ce qu’il se passe ?"
            i "Laisse le présentateur parler, Gaufrid !"
            outline "Je disais…"
        "Laissez-moi tranquil !":
            y "Mais... Pourquoi toujours sur moi les trucs comme ça ?!"
            i "Laisse le présentateur parler, Gaufrid !"
            outline "Je disais…"

    hide char_ingrid normal
    hide char_beaudrik normal left

    jump taverne_Concours_Part2_2_Manual

# -----------------------------------------#

label taverne_Concours_Part2_2_Manual:

    show char_ingrid normal at notSpeakingAnim(0.18, 1.2, 1.14, 0.25)
    show char_beaudrik normal left at notSpeakingAnim(0.86, 0.85, 0.88, 0.8)
    nar "{i}{color=#f2de5c}It is time for the ultimate test of love!{/i}{/color}"
    nar "{i}{b}{color=#f2de5c}« The Love Tribunal! »{/i}{/b}{/color}"
    jump taverne_Concours_Part2_3_Rules
    
    nar "{i}{color=#f2de5c}Gaufrid, avez-vous lu le manuel, ou faut-il que je vous explique les règles ?{/i}{/color}"

    menu:
        nar "{cps=0}{i}{color=#f2de5c}Gaufrid, avez-vous lu le manuel, ou faut-il que je vous explique les règles ?{/i}{/color}{/cps}"
        "Quel manuel ?":
            show char_ingrid degout at notSpeakingAnim(0.18, 1.2, 1.14, 0.25)
            show char_beaudrik mepris2 left at notSpeakingAnim(0.86, 0.85, 0.88, 0.8)
            play sound "sfx/Voices/Player/Char_Player_Hesitation_02.ogg"
            y "Euh ?"
            nar "{i}{color=#f2de5c}Celui à votre gauche, Gaufrid. Juste à côté de l’ordi.{/i}{/color}"
            pause 1.5
            nar "{i}{color=#f2de5c}...{/i}{/color}"
            nar "{i}{color=#f2de5c}C'est bon ou pas ?{/i}{/color}"
            jump taverne_Concours_Part2_2_Manual_Extra
        "Bien sûr que oui":
            play sound "sfx/Voices/Player/Char_Player_Hesitation_03.ogg"
            y "Je l’ai appris par cœur."
            show char_ingrid degout at notSpeakingAnim(0.18, 1.2, 1.14, 0.25)
            show char_beaudrik mepris2 left at notSpeakingAnim(0.86, 0.85, 0.88, 0.8)
            nar "{i}{color=#f2de5c}Maigre, moche et menteur.{/i}{/color}"
            nar "{i}{color=#f2de5c}Ça va surement bien se passer pour vous.{/i}{/color}"
            jump taverne_Concours_Part2_3_Rules
        "J’ai oublié règles":
            show char_ingrid degout at notSpeakingAnim(0.18, 1.2, 1.14, 0.25)
            show char_beaudrik mepris2 left at notSpeakingAnim(0.86, 0.85, 0.88, 0.8)
            play sound "sfx/Voices/Player/Char_Player_Hesitation_02.ogg"
            y "Euh… j’ai un trou de mémoire."
            nar "{i}{color=#f2de5c}Maigre, moche et amnésique.{/i}{/color}"
            nar "{i}{color=#f2de5c}Ça va surement bien se passer pour vous.{/i}{/color}"
            jump taverne_Concours_Part2_3_Rules

# -----------------------------------------#

label taverne_Concours_Part2_2_Manual_Extra:
    
    menu:
        nar "{cps=0}{i}{color=#f2de5c}C'est bon ou pas ?{/i}{/color}{/cps}"
        "Toujours pas":
            play sound "sfx/Voices/Player/Char_Player_Normal_03.ogg"
            y "Je ne vois pas de manuels."
            nar "{i}{color=#f2de5c}Maigre, moche et aveugle.{/i}{/color}"
            nar "{i}{color=#f2de5c}Ça va surement bien se passer pour vous.{/i}{/color}"
        "J’ai trouvé":
            play sound "sfx/Voices/Player/Char_Player_Hesitation_04.ogg"
            y "Euh… c’est bon !"
            nar "{i}{color=#f2de5c}Maigre, moche et menteur.{/i}{/color}"
            nar "{i}{color=#f2de5c}Ça va surement bien se passer pour vous.{/i}{/color}"
        "Un manuel de jeu en 2017 ?":
            play sound "sfx/Voices/Player/Char_Player_Non_03.ogg"
            y "Ça fait 10 ans que les jeux-vidéo n’ont plus de manuels."
            nar "{i}{color=#f2de5c}Ne faits pas le type moderne, Gaufride{/i}{/color}"
            nar "{i}{color=#f2de5c}Après tout, c'est vous le germain du premier siècle qui joue à une Visual Novel.{/i}{/color}"
    
    jump taverne_Concours_Part2_3_Rules

# -----------------------------------------#

label taverne_Concours_Part2_3_Rules:
    
    nar "{i}{color=#f2de5c}I will explain the rules!{/i}{/color}"
    show char_ingrid normal at notSpeakingAnim(0.18, 1.2, 1.14, 0.25)
    show char_beaudrik normal left at notSpeakingAnim(0.86, 0.85, 0.88, 0.8)
    nar "{i}{color=#f2de5c}For this final test, {b}Beaudrik{/b}, the defending Champion, will be praised by the whole village for his strength and beauty.{/i}{/color}"
    show char_ingrid degout at notSpeakingAnim(0.18, 1.2, 1.14, 0.25)
    show char_beaudrik mepris2 left at notSpeakingAnim(0.86, 0.85, 0.88, 0.8)
    nar "{i}{color=#f2de5c}{b}Wafflid{/b}, the Challenger, must be humble and stay silent. He is worthless anyway.{/i}{/color}"
    nar "{i}{color=#f2de5c}He can still {i}{b}{color=#f2de5c}Object{/color}{/b}{/i} to the compliments Beaudrik receives, if he so desires.{/i}{/color}"
    show char_ingrid normal at notSpeakingAnim(0.18, 1.2, 1.14, 0.25)
    show char_beaudrik normal left at notSpeakingAnim(0.86, 0.85, 0.88, 0.8)
    nar "{i}{color=#f2de5c}Shall we move on to the {b}interviews{/b}, or shall we {b}start the game{/b}.{/i}{/color}"
    show char_ingrid normal at notSpeakingAnim(0.18, 1.2, 1.14, 0.25):
        zoom 1.0 xpos 0.18 ypos 1.2
        linear 1.0 xpos -0.3
    show char_beaudrik normal left at notSpeakingAnim(0.86, 0.85, 0.88, 0.8):
        zoom 0.8 xpos 0.86 ypos 0.85
        linear 1.0 xpos 1.5
    nar "{i}{color=#f2de5c}What do you wish to do Wafflid?{/i}{/color}"
    
    jump taverne_Concours_Part2_4_Hub

# -----------------------------------------#

label taverne_Concours_Part2_4_Hub:
    
    menu:
        nar "{cps=0}{i}{color=#f2de5c}What do you wish to do Wafflid?{/i}{/color}{/cps}"
        "{color=#FFFFFF}Ingrid's Interview{/color}":
            y "I want to interview Ingrid."
            nar "{i}{color=#f2de5c}Excellent choice!{/i}{/color}"
            nar "{i}{color=#f2de5c}Ladies and gentlemen: Ingrid, 22 years old, the village beauty, and the grand prize of this contest!{/i}{/color}"
            show char_ingrid love:
                xalign 0.5 yalign 0.8
                xpos -0.5 ypos 1.5 zoom 0.25 rotate 30
                linear 0.5 xpos 0.05 ypos 1.15
            #show char_ingrid normal at notSpeakingAnim(0.5, 0.95, 0.92, 0.22) with Dissolve(0.5)
            pause 0.5
            #show char_ingrid normal at speakingAnim(0.50, 1.0, 0.98, 0.22)
            play sound "sfx/Voices/Ingrid/Char_Ingrid_Love_01.ogg"
            i "Hello! Thank you, thank you..."
            show char_ingrid love:
                xalign 0.5 yalign 0.8
                xpos 0.05 ypos 1.15 zoom 0.25 rotate 30
                #linear 0.5 xpos 0.8 ypos 1.15
                parallel:
                    linear 0.5 xpos 0.5
                parallel:
                    linear 0.3 rotate 0
            nar "{i}{color=#f2de5c}Ingrid, describe your ideal man{/i}{/color}"
            show char_ingrid normal at speakingAnim(0.5, 1.15, 1.17, 0.25)
            play sound "sfx/Voices/Ingrid/Char_Ingrid_Normal_03.ogg"
            i "I need a strong man who can assemble my furniture."
            i "It's really important for me that my man can assemble furniture… I really don't want to do it myself…"
            show char_ingrid degout at speakingAnim(0.5, 1.15, 1.17, 0.25)
            play sound "sfx/Voices/Ingrid/Char_Ingrid_Degout_02.ogg"
            i "...so if he can't do it, I don't know how we can make it work."
            show char_ingrid love at speakingAnim(0.5, 1.15, 1.17, 0.25)
            play sound "sfx/Voices/Ingrid/Char_Ingrid_Love_02.ogg"
            i "I also like men that are brave, honnest and without any physical abnormalities."
            show char_ingrid love at speakingAnim(0.5, 1.35, 1.17, 0.25):
                    zoom 1.0 xpos 0.5 ypos 1.35
                    linear 2.0 xpos 1.5
            nar "{i}{color=#f2de5c}Thank you Ingrid!{/i}{/color}"
            jump taverne_Concours_Part2_4_Hub
            
        "{color=#FFFFFF}Beaudrik's Interview{/color}":
            y "Let's hear Beaudrik's interview."
            nar "{i}{color=#f2de5c}Excellent choice!{/i}{/color}"
            nar "{i}{color=#f2de5c}Ladies and gentlemen: Beaudrik, our Champion!{/i}{/color}"
            show char_beaudrik drague right at notSpeakingAnim(0.86, 0.85, 0.88, 1.0):
                xalign 0.45 yalign 0.8
                zoom 0.88 xpos 1.5 ypos 0.77
                linear 0.7 xpos 0.7
            play sound "sfx/Voices/Beaudrik/Char_Beaudrik_Drague_03.ogg"
            bg "Thanks so much guys!"
            nar "{i}{color=#f2de5c}Beaudrik, are you ready?{/i}{/color}"
            show char_beaudrik normal left at speakingAnim(0.8, 0.85, 0.86, 0.8)
            play sound "sfx/Voices/Beaudrik/Char_Beaudrik_Normal_02.ogg"
            bg "Oh yeah, I'm in the zone. I love competitions."
            show char_beaudrik mepris2 left at speakingAnim(0.8, 0.85, 0.86, 0.8)
            play sound "sfx/Voices/Beaudrik/Char_Beaudrik_Normal_08.ogg"
            bg "I'm just a bit nervous because Josiane, my ex-fiancée, is watching from the stands."
            show char_beaudrik mepris left at speakingAnim(0.8, 0.85, 0.86, 0.8)
            bg "I hope Ingrid won't find out I still have a thing going on with her."
            show char_beaudrik mepris left at notSpeakingAnim(0.8, 0.85, 0.86, 0.8)
            nar "{i}{color=#f2de5c}Beaudrik, please remember that your opponent Wafflid is right in front of you.{/i}{/color}"
            show char_beaudrik choque left at speakingAnim(0.8, 0.85, 0.86, 0.8)
            play sound "sfx/Voices/Beaudrik/Char_Beaudrik_Doute_04.ogg"
            bg "Ah! Errrr..."
            show char_beaudrik choque left at speakingAnim(0.8, 0.85, 0.86, 1.0):
                zoom 0.8 xpos 0.8 ypos 1.0
                linear 1.0 xpos 1.5
            nar "{i}{color=#f2de5c}Thank you Beaudrik!{/i}{/color}"
            hide char_beaudrik normal left
            jump taverne_Concours_Part2_4_Hub
            
        "{color=#FFFFFF}My interview{/color}":
            y "I would like to interview myself."
            nar "{i}{color=#f2de5c}Wafflid... chance is not on your side.{/i}{/color}"
            nar "{i}{color=#f2de5c}Don't make it worse for yourself!{/i}{/color}"
            jump taverne_Concours_Part2_4_Hub
            
        "Let's begin!":
            play sound "sfx/Voices/Player/Char_Player_Sarcastic_01.ogg"
            y "Ok, I'm ready!"
            jump taverne_Concours_Part3_Brutalmund

# -----------------------------------------#
label taverne_Concours_Part3_Brutalmund:
    
    nar "{i}{color=#f2de5c}Let's call the first witness forward: Beaudrik's father!{/i}{/color}"
    play sound "sfx/SFX_Stairs_02.ogg"
    show char_brutal normal:
        zoom 0.35 xpos 1.5 ypos 0.07
        linear 1.5 xpos 0.27
    pause 1.5
    play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere1_02.ogg"

    show char_brutal colere at speakingAnim(0.52, 0.95, 0.95, 0.35)
    play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere1_01.ogg"
    brut "I didn't want to come y'know, I was brought here by force! By force, I tell ya!"
    show char_brutal normal at speakingAnim(0.52, 0.95, 0.95, 0.35)
    brut "But ya know how it is, right. I'm so tired of my son, there, Beaudrik."
    show char_brutal heureux at speakingAnim(0.52, 0.95, 0.95, 0.35)
    play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Normal_05.ogg"
    brut "So, I want him to win! So he gets married and goes away."
    show char_brutal normal at notSpeakingAnim(0.52, 0.95, 0.95, 0.35)
    nar "{i}{color=#f2de5c}What are your thoughts about your son, Mister Brutalmund?{/i}{/color}"
    show char_brutal normal at speakingAnim(0.52, 0.95, 0.95, 0.35)
    play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere2_04.ogg"
    brut "He's a real wimp…"
    show char_brutal surpris at speakingAnim(0.52, 0.95, 0.95, 0.35)
    play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Choc_01.ogg"
    brut "Wait, wait... I have ta' say good things about him so he can win, right?"
    show char_brutal surpris at notSpeakingAnim(0.52, 0.95, 0.95, 0.35)
    nar "{i}{color=#f2de5c}That's the idea, yes.{/i}{/color}"
    show char_brutal normal at speakingAnim(0.52, 0.95, 0.95, 0.35)
    play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Normal_05.ogg"
    brut "Ok... so... he's strong and brave!."
    play sound "sfx/SFX_Stairs_02.ogg"
    show char_brutal normal at speakingAnim(0.52, 0.95, 0.95, 0.35):
        zoom 1.0 xpos 0.52 ypos 1.15
        linear 1.5 xpos -0.5
    jump taverne_Concours_Part3_Brutalmund_Choice

# -----------------------------------------#

label taverne_Concours_Part3_Brutalmund_Choice:

    menu:
        brut "{cps=0}Ok... so... he's strong and brave!{/cps}"
        "Objection!":
            play sound "sfx/Voices/Player/Char_Player_Non_03.ogg"
            
            
            pause 0.4
            y "Objection! Beaudrik is a coward!"

            jump taverne_Concours_Part3_Brutalmund_Choice_Subchoice
            
        "That's true":
            show char_beaudrik normal left :
                zoom 0.8 xpos 1.0 ypos 0.8
                linear 0.4 xpos 0.85
            play sound "sfx/Voices/Player/Char_Player_Heureux_04.ogg"
            y "I'd love to be more like him."
            hide char_brutal normal
            nar "{i}{color=#f2de5c}But you are Wafflid.{/i}{/color}"
            play sound "sfx/Voices/Beaudrik/Char_Beaudrik_Doute_03.ogg"
            show char_beaudrik choque left at notSpeakingAnim(0.75, 0.8, 0.82, 0.8)
            play sound "sfx/Voices/Beaudrik/Char_Beaudrik_Choc_01.ogg"
            nar "{i}{color=#f2de5c}Didn't you know he sleeps with a teddy bear, since he's afraid of the dark?{/i}{/color}"
            jump taverne_Concours_Part3_Ingrid

# -----------------------------------------#

label taverne_Concours_Part3_Brutalmund_Choice_Subchoice:
    
    hide char_brutal normal
    show char_beaudrik normal left at notSpeakingAnim(0.85, 0.8, 0.86, 0.8) with Dissolve (0.5)
    
    play sound "sfx/Voices/Beaudrik/Char_Beaudrik_Mepris_03.ogg"
            
    bg "Tsk! You can't prove that!"
    menu:
        bg "{cps=0}Tsk! You can't prove that!{/cps}"
        "He's afraid of the dark":
            show char_beaudrik choque left at notSpeakingAnim(0.75, 0.8, 0.82, 0.8)
            play sound "sfx/Voices/Player/Char_Player_Non_04.ogg"
            pause 0.5
            play sound "sfx/Voices/Beaudrik/Char_Beaudrik_Choc_01.ogg"
            y "Brutalmund is lying! He knows his son is afraid of the dark!"

        "Buffalos scare the hell out of him":
            play sound "sfx/Voices/Player/Char_Player_Hesitation_02.ogg"
            y "He is terrified of buffalos!"
            nar "{i}{color=#f2de5c}No, no, that's Crossfitrichernvald.{/i}{/color}"
            show char_beaudrik mepris left at speakingAnim(0.8, 0.85, 0.86, 0.8)
            play sound "sfx/Voices/Beaudrik/Char_Beaudrik_Mepris_02.ogg"
            bg "How can you say that?!"
            show char_beaudrik normal left at speakingAnim(0.8, 0.85, 0.86, 0.8)
            play sound "sfx/Voices/Beaudrik/Char_Beaudrik_Mepris_04.ogg"
            bg "Buffalos are delicious."
            show char_beaudrik mepris2 left at notSpeakingAnim(0.8, 0.85, 0.86, 0.8)
            play sound "sfx/Voices/Beaudrik/Char_Beaudrik_Choc_01.ogg"
            nar "{i}{color=#f2de5c}Wrong answer, Wafflid! The right answer is that he is afraid of the dark.{/i}{/color}"
            show char_beaudrik choque left at notSpeakingAnim(0.75, 0.85, 0.82, 0.8)

    jump taverne_Concours_Part3_Ingrid

            
# -----------------------------------------#

label taverne_Concours_Part3_Ingrid:

    show char_ingrid choc:
        xalign 0.5 yalign 0.8
        xpos -0.5 ypos 1.5 zoom 0.25 rotate 30
        linear 0.5 xpos 0.05 ypos 1.15
            #show char_ingrid normal at notSpeakingAnim(0.5, 0.95, 0.92, 0.22) with Dissolve(0.5)
    pause 0.5
            #show char_ingrid normal at speakingAnim(0.50, 1.0, 0.98, 0.22)
    play sound "sfx/Voices/Ingrid/Char_Ingrid_Choc_01.ogg"
    i "You are afraid of the dark?!"
    show char_ingrid love:
        xalign 0.5 yalign 0.8
        xpos 0.05 ypos 1.15 zoom 0.25 rotate 30
                #linear 0.5 xpos 0.8 ypos 1.15
        parallel:
            linear 1.5 xpos 0.2
        parallel:
            linear 1.5 rotate 0
    show char_ingrid love at speakingAnim(0.2, 1.15, 1.17, 0.25)
    
    show char_beaudrik mepris2 left at notSpeakingAnim(0.8, 0.8, 0.82, 0.8)
    play sound "sfx/Voices/Ingrid/Char_Ingrid_Normal_03.ogg"
    
    show screen datingSim(ingrid_char, 0.23, 0.15)
    
    i "Hey, me too!"
    show char_ingrid degout at speakingAnim(0.2, 1.15, 1.17, 0.25)
    show char_beaudrik insulte right at notSpeakingAnim(0.8, 0.8, 0.82, 0.8) # A FLIPPER
    play sound "sfx/Voices/Ingrid/Char_Ingrid_Degout_04.ogg"
    pause 0.7
    play sound "sfx/Voices/Beaudrik/Char_Beaudrik_Insult_01.ogg"
    i "But sensitive men are really not my thing."
    
    $ loveGauge(ingrid_char, +10, 0.23, 0.15)
    
    show char_ingrid degout at notSpeakingAnim(0.2, 1.15, 1.17, 0.25)
    nar "{i}{color=#f2de5c}Silence! Time for the second witness: Ingrid herself!{/i}{/color}"
    nar "{i}{color=#f2de5c}Ingrid, what do you think of Beaudrik?{/i}{/color}"
    show char_ingrid normal at speakingAnim(0.2, 1.15, 1.17, 0.25)
    play sound "sfx/Voices/Ingrid/Char_Ingrid_Normal_04.ogg"
    i "Well, he's not very smart, but Wafflid isn't that bright either!"
    show char_ingrid love at speakingAnim(0.2, 1.15, 1.17, 0.25)
    show char_beaudrik normal left at notSpeakingAnim(0.8, 0.8, 0.82, 0.8)
    play sound "sfx/Voices/Ingrid/Char_Ingrid_Love_01.ogg"
    i "At least Beaudrik doesn't have any physical imperfections."
    show char_ingrid love at notSpeakingAnim(0.2, 1.15, 1.17, 0.25)

    jump taverne_Concours_Part3_Ingrid_Choice
    
# -----------------------------------------#   
  
label taverne_Concours_Part3_Ingrid_Choice:

    menu:
        i "{cps=0}At least Beaudrik doesn't have any physical imperfections.{/cps}"
        "Objection! Beaudrik is imperfect!":
            play sound "sfx/Voices/Player/Char_Player_Non_03.ogg"
            y "Objection! Beaudrik is ugly!"
            show char_ingrid normal at speakingAnim(0.2, 1.15, 1.17, 0.25)
            show char_beaudrik mepris2 left at notSpeakingAnim(0.8, 0.8, 0.82, 0.8)
            play sound "sfx/Voices/Ingrid/Char_Ingrid_Normal_01.ogg"
            i "Did you have too much to drink Wafflid?"
            show char_ingrid normal at notSpeakingAnim(0.2, 1.15, 1.17, 0.25)
            show char_beaudrik mepris left at speakingAnim(0.8, 0.8, 0.82, 0.8)
            play sound "sfx/Voices/Beaudrik/Char_Beaudrik_Mepris_06.ogg"
            bg "What do you mean, I'm ugly?"
            show char_beaudrik mepris2 left at notSpeakingAnim(0.8, 0.8, 0.82, 0.8)
            jump taverne_Concours_Part3_Ingrid_Choice_Subchoice
            
        "Indeed":
            play sound "sfx/Voices/Player/Char_Player_Heureux_02.ogg"
            y "He is a very handsome man indeed."
            show char_beaudrik drague right at speakingAnim(0.70, 0.85, 0.86, 0.88)
            play sound "sfx/Voices/Beaudrik/Char_Beaudrik_Doute_03.ogg"
            bg "Oh, that's nice!"
            show char_beaudrik normal left at speakingAnim(0.8, 0.8, 0.82, 0.8)
            play sound "sfx/Voices/Beaudrik/Char_Beaudrik_Drague_02.ogg"
            bg "I might be a man, but I like taking care of my body!"
            show char_beaudrik normal left at notSpeakingAnim(0.8, 0.8, 0.82, 0.8)
            nar "{i}{color=#f2de5c}Including your third nipple?{/i}{/color}"
            show char_beaudrik choque left at notSpeakingAnim(0.75, 0.85, 0.82, 0.8)
            jump taverne_Concours_Part4_Final

# -----------------------------------------#  

label taverne_Concours_Part3_Ingrid_Choice_Subchoice:
    
    menu:
        bg "{cps=0}What do you mean, I'm ugly?{/cps}"
        "He has a very large nose!":
            play sound "sfx/Voices/Player/Char_Player_Non_01.ogg"
            y "Have you seen his nose? It's a peninsula!"
            show char_ingrid love at speakingAnim(0.2, 1.15, 1.17, 0.25)
            play sound "sfx/Voices/Ingrid/Char_Ingrid_Love_02.ogg"
            $ loveGauge(ingrid_char, -5, 0.23, 0.15)
            i "I like it. It makes me feel safe."
            show char_ingrid normal at notSpeakingAnim(0.2, 1.15, 1.17, 0.25)
            nar "{i}{color=#f2de5c}You'll change your mind when you see his third nipple.{/i}{/color}"

        "He has three nipples!":
            play sound "sfx/Voices/Player/Char_Player_Non_03.ogg"
            $ loveGauge(ingrid_char, +10, 0.23, 0.15)
            show char_ingrid choc at notSpeakingAnim(0.2, 1.15, 1.17, 0.25)
            y "All the young ladies know it! He has a third nipple!"

        "{color=#FFFFFF}He's ugly and skinny!{/color}":
            play sound "sfx/Voices/Player/Char_Player_Hesitation_01.ogg"
            y "Erm... He's skinny and ugly!"
            show char_ingrid degout at notSpeakingAnim(0.2, 1.15, 1.17, 0.25)
            show char_beaudrik mepris2 left at notSpeakingAnim(0.8, 0.8, 0.82, 0.8)
            nar "{i}{color=#f2de5c}No Wafflid, you are thinking about yourself.{/i}{/color}"
            play sound "sfx/Voices/Player/Char_Player_Normal_04.ogg"
            y "Ah yes, you're right. Sorry about that"
            
            jump taverne_Concours_Part3_Ingrid_Choice_Subchoice
            
            nar "{i}{color=#f2de5c}Non, non, c’est moi. Excusez-moi.{/i}{/color}"
            nar "{i}{color=#f2de5c}Je n’ai peut-être pas assez insisté là-dessus.{/i}{/color}"
            y "C’était pas super clair en effet."
            nar "{i}{color=#f2de5c}Alors écoutez-moi bien :{/i}{/color}"
            show char_ingrid normal at notSpeakingAnim(0.2, 1.15, 1.17, 0.25)
            show char_beaudrik normal left at notSpeakingAnim(0.8, 0.8, 0.82, 0.8)
            nar "{i}{color=#f2de5c}{b}VOUS ETES MAIGRE ET MOCHE.{/b}{/i}{/color}"
            nar "{i}{color=#f2de5c}C’est mieux comme ça ?{/i}{/color}"
            y "Beaucoup mieux, merci."
            nar "{i}{color=#f2de5c}De rien. Hésitez pas s’il y a autre chose qui vous échappe.{/i}{/color}"
            y "Merci bien."
            nar "{i}{color=#f2de5c}Je vous remets dans la boucle.{/i}{/color}"
            y "C’est gentil."
            

    jump taverne_Concours_Part4_Final

# -----------------------------------------# 

label taverne_Concours_Part4_Final:
    
    show char_ingrid normal at speakingAnim(0.2, 1.15, 1.17, 0.25)
    show char_beaudrik choque at notSpeakingAnim(0.8, 0.8, 0.82, 0.8)
    play sound "sfx/Voices/Ingrid/Char_Ingrid_Degout_02.ogg"
    i "A third nipple?! That's a completely negligible and unimportant physical flaw!"
    show char_ingrid choc at speakingAnim(0.2, 1.15, 1.17, 0.25)
    show char_beaudrik insulte right at notSpeakingAnim(0.8, 0.8, 0.82, 0.8)
    play sound "sfx/Voices/Ingrid/Char_Ingrid_Degout_04.ogg"
    play sound "sfx/Voices/Beaudrik/Char_Beaudrik_Insult_03.ogg"
    i "It's disgusting!"
    show char_ingrid degout at speakingAnim(0.2, 1.15, 1.17, 0.25)
    i "Beaudrik, I am very disappointed."
    i "It's not about the nipple, it's a matter of principle."
    show char_ingrid choc at speakingAnim(0.2, 1.15, 1.17, 0.25)
    play sound "sfx/Voices/Ingrid/Char_Ingrid_Degout_02.ogg"
    i "You promised you had only two nipples!"
    show char_ingrid degout at notSpeakingAnim(0.2, 1.15, 1.17, 0.25)
    nar "{i}{color=#f2de5c}Well. On the subject of trust, Ingrid, do you think Beaudrik is an honest man?{/i}{/color}"
    show char_ingrid degout at speakingAnim(0.2, 1.15, 1.17, 0.25)
    i "Outside of nipple number three?"
    show char_ingrid degout at notSpeakingAnim(0.2, 1.15, 1.17, 0.25)
    nar "{i}{color=#f2de5c}Yes.{/i}{/color}"
    show char_ingrid love at speakingAnim(0.2, 1.15, 1.17, 0.25)
    play sound "sfx/Voices/Ingrid/Char_Ingrid_Love_02.ogg"
    i "I believe he will be a loyal and faithful husband."
    show char_ingrid love at notSpeakingAnim(0.2, 1.15, 1.17, 0.25)
    show char_beaudrik normal left at notSpeakingAnim(0.8, 0.8, 0.82, 0.8)

    jump taverne_Concours_Part4_Final_Choice

# -----------------------------------------#

label taverne_Concours_Part4_Final_Choice:
    
    menu:
        i "I believe he will be a loyal and faithful husband."
        "Objection!":
            show char_ingrid degout at notSpeakingAnim(0.2, 1.15, 1.17, 0.25)
            show char_beaudrik mepris2 left at notSpeakingAnim(0.8, 0.8, 0.82, 0.8)
            play sound "sfx/Voices/Player/Char_Player_Non_02.ogg"
            y "Objection! Beaudrik already has a fiancée."
            show char_ingrid choc at speakingAnim(0.2, 1.15, 1.17, 0.25)
            play sound "sfx/Voices/Ingrid/Char_Ingrid_Choc_01.ogg"
            i "What do you mean he has a fiancée?!"
            i "What's her name, that fat cow?!"
            show char_ingrid degout at notSpeakingAnim(0.2, 1.15, 1.17, 0.25)
            jump taverne_Concours_Part4_Final_Choice_Subchoice
            
        "She's right...":
            play sound "sfx/Voices/Player/Char_Player_Heureux_03.ogg"
            y "He's really a good guy."
            show char_ingrid love at speakingAnim(0.2, 1.15, 1.17, 0.25)
            play sound "sfx/Voices/Ingrid/Char_Ingrid_Love_03.ogg"
            i "Isn't he?"
            show char_ingrid love at notSpeakingAnim(0.2, 1.15, 1.17, 0.25)
            nar "{i}{color=#f2de5c}Too bad he's already taken. Your friend already has a fiancée{/i}{/color}"
            show char_ingrid choc at notSpeakingAnim(0.2, 1.15, 1.17, 0.25)
            show char_beaudrik choque at notSpeakingAnim(0.8, 0.8, 0.82, 0.8)
            nar "{i}{color=#f2de5c}Her name is Josiane.{/i}{/color}"
            jump taverne_Concours_Part5_Ending
            
# -----------------------------------------#

label taverne_Concours_Part4_Final_Choice_Subchoice:

    menu:
        i "{cps=0}What's her name, that fat, ugly cow?!{/cps}"
        "Johanne":
            show char_ingrid degout at notSpeakingAnim(0.2, 1.15, 1.17, 0.25)
            show char_beaudrik mepris2 left at notSpeakingAnim(0.8, 0.8, 0.82, 0.8)
            play sound "sfx/Voices/Player/Char_Player_Hesitation_04.ogg"
            y "Erm... Johanne?"
            $ loveGauge(ingrid_char, -5, 0.23, 0.15)
            nar "{i}{color=#f2de5c}So close, Wafflid.{/i}{/color}"
            show char_ingrid choc at notSpeakingAnim(0.2, 1.15, 1.17, 0.25)
            show char_beaudrik choque at notSpeakingAnim(0.8, 0.8, 0.82, 0.8)
            nar "{i}{color=#f2de5c}Her name is Josiane.{/i}{/color}"
            jump taverne_Concours_Part5_Ending

        "Josiane":
            show char_ingrid choc at notSpeakingAnim(0.2, 1.15, 1.17, 0.25)
            show char_beaudrik choque at notSpeakingAnim(0.8, 0.8, 0.82, 0.8)
            play sound "sfx/Voices/Player/Char_Player_Non_03.ogg"
            $ loveGauge(ingrid_char, +10, 0.23, 0.15)
            y "Josiane! She's called Josiane!"
            jump taverne_Concours_Part5_Ending

        "Jovanne":
            show char_ingrid degout at notSpeakingAnim(0.2, 1.15, 1.17, 0.25)
            show char_beaudrik mepris2 left at notSpeakingAnim(0.8, 0.8, 0.82, 0.8)
            play sound "sfx/Voices/Player/Char_Player_Hesitation_04.ogg"
            y "Erm… Jovanne?"
            $ loveGauge(ingrid_char, -5, 0.23, 0.15)
            nar "{i}{color=#f2de5c}So close, Wafflid.{/i}{/color}"
            show char_ingrid choc at notSpeakingAnim(0.2, 1.15, 1.17, 0.25)
            show char_beaudrik choque at notSpeakingAnim(0.8, 0.8, 0.82, 0.8)
            nar "{i}{color=#f2de5c}Her name is Josiane.{/i}{/color}"
            jump taverne_Concours_Part5_Ending

        "{color=#FFFFFF}Ernust{/color}":
            play sound "sfx/Voices/Player/Char_Player_Non_03.ogg"
            y "Ernust!"
            show char_ernust love2 :
                xpos 0.5 ypos 1.5 zoom 0.8 #rotate 30
                linear 0.5 xpos 0.15 ypos 0.2
            play sound "sfx/Voices/Ernust/Char_Ernust_Joyeux_03.ogg"
            e "Wafflid! Did you call me?"
            y "Yes! What's Beaudrik's girlfriend's name?"
            show char_ernust inquiet at speakingAnim(0.5, 1.3, 1.32, 0.8)
            play sound "sfx/Voices/Ernust/Char_Ernust_Inquiet_04.ogg"
            e "It starts with a 'J' I think."
            play sound "sfx/Voices/Player/Char_Player_Non_05.ogg"
            y "That's... very helpful...."
            show char_ernust love2 at speakingAnim(0.5, 1.2, 1.22, 0.8)
            play sound "sfx/Voices/Ernust/Char_Ernust_Joyeux_01.ogg"
            e "We're such a cool duo!"
            show char_ernust love2 :
                xpos 0.5 ypos 1.2 zoom 0.8 #rotate 30
                linear 1.0 xpos 0.5 ypos 2.0
            play sound "sfx/Voices/Player/Char_Player_Sarcastic_01.ogg"
            y "Go away! Come on!"
            hide char_ernust
            show char_ingrid degout at speakingAnim(0.2, 1.15, 1.17, 0.25)
            i "So?!"
            i "What's her name?!"
            show char_ingrid degout at notSpeakingAnim(0.2, 1.15, 1.17, 0.25)
            jump taverne_Concours_Part4_Final_Choice_Subchoice

# -----------------------------------------#

label taverne_Concours_Part5_Ending:

    stop music1 fadeout 1.5
    $ renpy.pause(2.0, hard = True)
    play sound "sfx/Voices/Ingrid/Char_Ingrid_Choc_01.ogg"
    
    hide screen datingSim
    
    i "JOSIANE?!"
    play sound "sfx/SFX_Drama_01.ogg"
    i "THE GOAT!?!"
    $ renpy.pause(2.0, hard = True)
    show char_goat choc:
        xalign 0.5 yalign 0.8
        zoom 0.35 xpos 0.5 ypos 1.5
        easein 0.8 ypos 0.73
    play sound "sfx/Voices/Chevre/Char_Chevre_Choc2_01.ogg"
    goat "Bêêêh!"
    show char_beaudrik insulte right at notSpeakingAnim(0.8, 0.8, 0.82, 0.8)
    play sound "sfx/Voices/Beaudrik/Char_Beaudrik_Humilie_01.ogg"
    show char_beaudrik insulte right at speakingAnim(0.8, 0.8, 0.82, 0.8)
    show char_ingrid degout at notSpeakingAnim(0.2, 1.15, 1.17, 0.25)
    bg "It's platonic, Ingrid! Believe me!"
    show char_beaudrik insulte right at notSpeakingAnim(0.8, 0.8, 0.82, 0.8)
    show char_goat normal:
    nar "{i}{color=#f2de5c}Beaudrik, you are disqualified.{/i}{/color}"
    show char_beaudrik mepris left at speakingAnim(0.8, 0.8, 0.82, 0.8)
    play sound "sfx/Voices/Beaudrik/Char_Beaudrik_Mepris_01.ogg"
    bg "You will pay for this, Wafflid!"
    bg "Let's go, Josiane."
    play sound "sfx/Voices/Chevre/Char_Chevre_Love_01.ogg"
    show char_goat love
    goat "Bêêêh!"
    show char_goat choc:
        xalign 0.5 yalign 0.8
        zoom 0.35 xpos 0.5 ypos 0.73
        linear 2.5 xpos 1.5
    show char_beaudrik mepris right:
        zoom 0.8 xpos 0.8 ypos 0.8
        linear 2.0 xpos 1.5
    play sound "sfx/SFX_Stairs_02.ogg"
    
    if ingrid_char.love >= 60:
        jump taverne_Concours_Part5_Ending_GoodEnding
    else:
        jump taverne_Concours_Part5_Ending_BadEnding
    
# ------------BAD ENDING----------------#

label taverne_Concours_Part5_Ending_BadEnding:
    
    pause 2.0
    show char_ingrid degout at speakingAnim(0.2, 1.15, 1.17, 0.25)
    i "Errm…"
    play sound "sfx/Voices/Ingrid/Char_Ingrid_Degout_03.ogg"
    i "Well Wafflid, looks like you're the only one left. Let's get married."
    play sound "sfx/Voices/Player/Char_Player_Heureux_04.ogg"
    show char_ingrid degout at notSpeakingAnim(0.2, 1.15, 1.17, 0.25)
    y "Ah! Good, good!"
    y "Is it ok? Can I propose now?"

    jump taverne_Concours_Part6_Conclusion

# ------------GOOD ENDING----------------#

label taverne_Concours_Part5_Ending_GoodEnding:

    show char_ingrid love at speakingAnim(0.2, 1.15, 1.17, 0.25)
    i "Wafflid! We can get married!"
    show char_ingrid love at notSpeakingAnim(0.2, 1.15, 1.17, 0.25)
    y "Really? Should I propose then?" 
    
    jump taverne_Concours_Part6_Conclusion
    
# -----------------------------------------#

label taverne_Concours_Part6_Conclusion:

    play sound "sfx/Voices/Ingrid/Char_Ingrid_Normal_04.ogg"
    show char_ingrid normal at speakingAnim(0.2, 1.15, 1.17, 0.25)
    i "Oh, no thanks, it's ok!"
    i "Let's get married right away, it will be quicker!"
    i "We just need to ask Veleda's benediction!"
    play sound "sfx/Voices/Player/Char_Player_Hesitation_04.ogg"
    show char_ingrid normal at notSpeakingAnim(0.2, 1.15, 1.17, 0.25)
    y "Oh right... there's a tradition like that."
    show char_ingrid normal at speakingAnim(0.2, 1.15, 1.17, 0.25)
    play sound "sfx/Voices/Ingrid/Char_Ingrid_Normal_01.ogg"
    i "Ok! We'll meet at Veleda's tower in ten minutes!"
    play sound "sfx/Voices/Ingrid/Char_Ingrid_Love_01.ogg"
    i "Be on time, my little waffle!"
    
    stop music1 fadeout 1.0
    stop music2 fadeout 1.0
    stop ambiance fadeout 0.5
    jump taverne_Concours_Part6_FadeToBlack

# -----------------------------------------#

label taverne_Concours_Part6_FadeToBlack:

    scene black with Dissolve(0.5)
    y "What am I going to do now?"
    pause 2.0
    outline "{i}Ten minutes later...{/i}"

label taverne_MarryingIngridPart1:

# -----------------------------------------#

    jump tourVeleda_MarryingIngridPart2
    
# -----------------------------------------#
