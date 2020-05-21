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
            y "Tu crois aux âmes soeurs toi ?"
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
    outline "A bit later, in the tavern..."
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
    nar "{i}{color=#f2de5c}Ingrid est une jeune femme célibataire à la recherche de l’amour.{/i}{/color}"
    nar "{i}{color=#f2de5c}Tiraillée entre la beauté du corps et la beauté du cœur, \n Ingrid devra choisir entre deux Germains presque charmants.{/i}{/color}"
    show char_beaudrik normal left :
        xalign 0.5 yalign 0.8
        zoom 0.8 xpos 1.0 ypos 0.8
        linear 0.4 xpos 0.86
    pause 0.4
    show char_ingrid love at notSpeakingAnim(0.18, 1.115, 1.14, 0.25)
    nar "{i}{color=#f2de5c}D'un coté, Beaudrik, parangon de virilité.{/i}{/color}"
    show char_ingrid degout at notSpeakingAnim(0.18, 1.115, 1.14, 0.25)
    show char_beaudrik mepris2 left at notSpeakingAnim(0.86, 0.85, 0.88, 0.8)
    nar "{i}{color=#f2de5c}De l'autre, Gaufrid, maigre et moche.{/i}{/color}"
    show char_ingrid degout at notSpeakingAnim(0.18, 1.115, 1.14, 0.25)
    show char_beaudrik mepris2 left at notSpeakingAnim(0.86, 0.85, 0.88, 0.8)
    play sound "sfx/Voices/Player/Char_Player_Non_03.ogg"
    y "Quelqu’un peut m’expliquer ce qu’il se passe ?"
    show char_ingrid degout at speakingAnim(0.18, 1.15, 1.17, 0.25)
    play sound "sfx/Voices/Ingrid/Char_Ingrid_Degout_02.ogg"
    i "Laisse le présentateur parler, Gaufrid !"
    #nar "{i}{color=#f2de5c}Ingrid est une jeune femme célibataire à la recherche de l’amour.{/color}{/i}"
    #nar "{i}{color=#f2de5c}Tiraillée entre la beauté du corps et la beauté du cœur, Ingrid devra choisir entre deux Germains presque charmants."
    #nar "{i}{color=#f2de5c}D'un coté, Beaudrik, parangon de virilité.{/color}{/i}"
    #nar "{i}{color=#f2de5c}De l'autre, Gaufrid, maigre et moche.{/color}{/i}"

    jump taverne_Concours_Part2_2_Manual
    
# -----------------------------------------#   

label taverne_Concours_Part2_1_Intro_choice:
    
    menu:
        "T’es moche toi-même":
            y "Euh ! Comment oses-tu ?"
            outline "Tais-toi quand je parle."
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
    nar "{i}{color=#f2de5c}Il est maintenant l’heure de l’ultime épreuve qui départagera Beaudrik et Gaufrid !{/i}{/color}"
    nar "{i}{b}{color=#f2de5c}« Le Procès de l’Amour ! »{/i}{/b}{/color}"
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
    
    nar "{i}{color=#f2de5c}Je vous explique les règles !{/i}{/color}"
    show char_ingrid normal at notSpeakingAnim(0.18, 1.2, 1.14, 0.25)
    show char_beaudrik normal left at notSpeakingAnim(0.86, 0.85, 0.88, 0.8)
    nar "{i}{color=#f2de5c}Pour ce dernier test, {b}Beaudrik{/b}, Champion en Titre, sera acclamé par les habitants du village pour ses qualités.{/i}{/color}"
    show char_ingrid degout at notSpeakingAnim(0.18, 1.2, 1.14, 0.25)
    show char_beaudrik mepris2 left at notSpeakingAnim(0.86, 0.85, 0.88, 0.8)
    nar "{i}{color=#f2de5c}{b}Gaufrid{/b}, Challengeur de cet épisode, devra faire preuve d’humilité et se taire, car de toute façon il ne vaut rien.{/i}{/color}"
    nar "{i}{color=#f2de5c}Ceci dit, il pourra {i}{b}{color=#f2de5c}faire objection{/color}{/b}{/i} aux nombreux compliments faits à Beaudrik, s’il le souhaitera.{/i}{/color}"
    show char_ingrid normal at notSpeakingAnim(0.18, 1.2, 1.14, 0.25)
    show char_beaudrik normal left at notSpeakingAnim(0.86, 0.85, 0.88, 0.8)
    nar "{i}{color=#f2de5c}Nous pouvons passer aux {b}interviews{/b}, ou {b}commencer le jeu{/b}.{/i}{/color}"
    show char_ingrid normal at notSpeakingAnim(0.18, 1.2, 1.14, 0.25):
        zoom 1.0 xpos 0.18 ypos 1.2
        linear 1.0 xpos -0.3
    show char_beaudrik normal left at notSpeakingAnim(0.86, 0.85, 0.88, 0.8):
        zoom 0.8 xpos 0.86 ypos 0.85
        linear 1.0 xpos 1.5
    nar "{i}{color=#f2de5c}Que souhaitez-vous faire, Gaufrid ?{/i}{/color}"
    
    jump taverne_Concours_Part2_4_Hub

# -----------------------------------------#

label taverne_Concours_Part2_4_Hub:
    
    menu:
        nar "{cps=0}{i}{color=#f2de5c}Que souhaitez-vous faire, Gaufrid ?{/i}{/color}{/cps}"
        "{color=#FFFFFF}Interview d'Ingrid{/color}":
            y "Je voudrais voir l’interview de Ingrid."
            nar "{i}{color=#f2de5c}Excellent choix !{/i}{/color}"
            nar "{i}{color=#f2de5c}Messieurs-dames : Ingrid, 22 ans, belle du village et prix à gagner !{/i}{/color}"
            show char_ingrid love:
                xalign 0.5 yalign 0.8
                xpos -0.5 ypos 1.5 zoom 0.25 rotate 30
                linear 0.5 xpos 0.05 ypos 1.15
            #show char_ingrid normal at notSpeakingAnim(0.5, 0.95, 0.92, 0.22) with Dissolve(0.5)
            pause 0.5
            #show char_ingrid normal at speakingAnim(0.50, 1.0, 0.98, 0.22)
            play sound "sfx/Voices/Ingrid/Char_Ingrid_Love_01.ogg"
            i "Bonjour ! Merci, merci !"
            show char_ingrid love:
                xalign 0.5 yalign 0.8
                xpos 0.05 ypos 1.15 zoom 0.25 rotate 30
                #linear 0.5 xpos 0.8 ypos 1.15
                parallel:
                    linear 0.5 xpos 0.5
                parallel:
                    linear 0.3 rotate 0
            nar "{i}{color=#f2de5c}Ingrid, décrivez-nous votre homme idéal.{/i}{/color}"
            show char_ingrid normal at speakingAnim(0.5, 1.15, 1.17, 0.25)
            play sound "sfx/Voices/Ingrid/Char_Ingrid_Normal_03.ogg"
            i "J’ai besoin d’un homme fort qui sait monter les meubles."
            i "Je trouve que c’est vachement important un mec qui sait monter des meubles car… moi c’est pas du tout mon truc et…"
            show char_ingrid degout at speakingAnim(0.5, 1.15, 1.17, 0.25)
            play sound "sfx/Voices/Ingrid/Char_Ingrid_Degout_02.ogg"
            i "...voilà, s’il ne sait pas monter des meubles je ne sais pas comment on va faire."
            show char_ingrid love at speakingAnim(0.5, 1.15, 1.17, 0.25)
            play sound "sfx/Voices/Ingrid/Char_Ingrid_Love_02.ogg"
            i "Sinon j’aime bien les hommes courageux, honnêtes et sans anormalités physiques."
            show char_ingrid love at speakingAnim(0.5, 1.35, 1.17, 0.25):
                    zoom 1.0 xpos 0.5 ypos 1.35
                    linear 2.0 xpos 1.5
            nar "{i}{color=#f2de5c}Merci Ingrid ! A bientôt !{/i}{/color}"
            jump taverne_Concours_Part2_4_Hub
            
        "{color=#FFFFFF}Interview de Beaudrik{/color}":
            y "Je voudrais voir l’interview de Beaudrik."
            nar "{i}{color=#f2de5c}Excellent choix !{/i}{/color}"
            nar "{i}{color=#f2de5c}Messieurs-dames : Beaudrik, Champion en titre !{/i}{/color}"
            show char_beaudrik drague right at notSpeakingAnim(0.86, 0.85, 0.88, 1.0):
                xalign 0.45 yalign 0.8
                zoom 0.88 xpos 1.5 ypos 0.77
                linear 0.7 xpos 0.7
            play sound "sfx/Voices/Beaudrik/Char_Beaudrik_Drague_03.ogg"
            bg "Merci les gars !"
            nar "{i}{color=#f2de5c}Beaudrik, vous sentez-vous prêt ?{/i}{/color}"
            show char_beaudrik normal left at speakingAnim(0.8, 0.85, 0.86, 0.8)
            play sound "sfx/Voices/Beaudrik/Char_Beaudrik_Normal_02.ogg"
            bg "Je suis à fond ! Moi, les compétitions, c'est mon truc."
            show char_beaudrik mepris2 left at speakingAnim(0.8, 0.85, 0.86, 0.8)
            play sound "sfx/Voices/Beaudrik/Char_Beaudrik_Normal_08.ogg"
            bg "Sinon je suis un peu nerveux car Josiane, mon ex-fiancée, est dans le public."
            show char_beaudrik mepris left at speakingAnim(0.8, 0.85, 0.86, 0.8)
            bg "J’espère qu'Ingrid ne découvrira pas que ce n’est pas fini-fini entre Josiane et moi."
            show char_beaudrik mepris left at notSpeakingAnim(0.8, 0.85, 0.86, 0.8)
            nar "{i}{color=#f2de5c}Beaudrik, je vous rappelle que Gaufrid, votre adversaire, est juste devant vous.{/i}{/color}"
            show char_beaudrik choque left at speakingAnim(0.8, 0.85, 0.86, 0.8)
            play sound "sfx/Voices/Beaudrik/Char_Beaudrik_Doute_04.ogg"
            bg "Ah ! Euh..."
            show char_beaudrik choque left at speakingAnim(0.8, 0.85, 0.86, 1.0):
                zoom 0.8 xpos 0.8 ypos 1.0
                linear 1.0 xpos 1.5
            nar "{i}{color=#f2de5c}Merci Beaudrik !{/i}{/color}"
            hide char_beaudrik normal left
            jump taverne_Concours_Part2_4_Hub
            
        "{color=#FFFFFF}Mon interview{/color}":
            y "Je voudrais m’interviewer moi-même."
            nar "{i}{color=#f2de5c}Gaufrid... déjà qu'on ne vous donne pas favori.{/i}{/color}"
            nar "{i}{color=#f2de5c}Ne vous tirez pas une balle dans le pied !{/i}{/color}"
            jump taverne_Concours_Part2_4_Hub
            
        "On peut commencer !":
            play sound "sfx/Voices/Player/Char_Player_Sarcastic_01.ogg"
            y "C’est bon, je suis prêt !"
            jump taverne_Concours_Part3_Brutalmund

# -----------------------------------------#
label taverne_Concours_Part3_Brutalmund:
    
    nar "{i}{color=#f2de5c}Très bien, nous appelons le premier témoin : le père de Beaudrik !{/i}{/color}"
    play sound "sfx/SFX_Stairs_02.ogg"
    show char_brutal normal:
        zoom 0.35 xpos 1.5 ypos 0.07
        linear 1.5 xpos 0.27
    pause 1.5
    play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere1_02.ogg"

    show char_brutal colere at speakingAnim(0.52, 0.95, 0.95, 0.35)
    play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere1_01.ogg"
    brut "Moi, je ne voulais pas venir. On m’a obligé ! Obligé, je vous dis !"
    show char_brutal normal at speakingAnim(0.52, 0.95, 0.95, 0.35)
    brut "Mais vous savez comment c’est. Je n’en peux plus de mon fils, là, Beaudrik."
    show char_brutal heureux at speakingAnim(0.52, 0.95, 0.95, 0.35)
    play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Normal_05.ogg"
    brut "Alors, j’ai envie qu’il gagne. Histoire qu’il se marie et qu’il se casse."
    show char_brutal normal at notSpeakingAnim(0.52, 0.95, 0.95, 0.35)
    nar "{i}{color=#f2de5c}Que pensez-vous de votre fils, Monsieur Brutalmund ?{/i}{/color}"
    show char_brutal normal at speakingAnim(0.52, 0.95, 0.95, 0.35)
    play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere2_04.ogg"
    brut "C’est une vraie mauviett…"
    show char_brutal surpris at speakingAnim(0.52, 0.95, 0.95, 0.35)
    play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Choc_01.ogg"
    brut "Euh, attendez, il faut que je dise des trucs bien pour qu’il gagne ?"
    show char_brutal surpris at notSpeakingAnim(0.52, 0.95, 0.95, 0.35)
    nar "{i}{color=#f2de5c}C’est l’idée.{/i}{/color}"
    show char_brutal normal at speakingAnim(0.52, 0.95, 0.95, 0.35)
    play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Normal_05.ogg"
    brut "Ah… euh… il est fort et courageux."
    play sound "sfx/SFX_Stairs_02.ogg"
    show char_brutal normal at speakingAnim(0.52, 0.95, 0.95, 0.35):
        zoom 1.0 xpos 0.52 ypos 1.15
        linear 1.5 xpos -0.5
    jump taverne_Concours_Part3_Brutalmund_Choice

# -----------------------------------------#

label taverne_Concours_Part3_Brutalmund_Choice:

    menu:
        brut "{cps=0}Ah… euh… il est fort et courageux.{/cps}"
        "Objection !":
            play sound "sfx/Voices/Player/Char_Player_Non_03.ogg"
            
            
            pause 0.4
            y "Objection ! Beaudrik est un lâche !"

            jump taverne_Concours_Part3_Brutalmund_Choice_Subchoice
            
        "C'est pas faux":
            show char_beaudrik normal left :
                zoom 0.8 xpos 1.0 ypos 0.8
                linear 0.4 xpos 0.85
            play sound "sfx/Voices/Player/Char_Player_Heureux_04.ogg"
            y "J’aimerais bien être comme lui."
            hide char_brutal normal
            nar "{i}{color=#f2de5c}Mais c’est le cas, Gaufrid.{/i}{/color}"
            play sound "sfx/Voices/Beaudrik/Char_Beaudrik_Doute_03.ogg"
            show char_beaudrik choque left at notSpeakingAnim(0.75, 0.8, 0.82, 0.8)
            play sound "sfx/Voices/Beaudrik/Char_Beaudrik_Choc_01.ogg"
            nar "{i}{color=#f2de5c}Vous ne saviez pas que Beaudrik dort avec un nounours car il peur du noir ?{/i}{/color}"
            jump taverne_Concours_Part3_Ingrid

# -----------------------------------------#

label taverne_Concours_Part3_Brutalmund_Choice_Subchoice:
    
    hide char_brutal normal
    show char_beaudrik normal left at notSpeakingAnim(0.85, 0.8, 0.86, 0.8) with Dissolve (0.5)
    
    play sound "sfx/Voices/Beaudrik/Char_Beaudrik_Mepris_03.ogg"
            
    bg "Tsk ! Tu ne peux pas le prouver !"
    menu:
        bg "{cps=0}Tsk ! Tu ne peux pas le prouver !{/cps}"
        "Il a peur du noir":
            show char_beaudrik choque left at notSpeakingAnim(0.75, 0.8, 0.82, 0.8)
            play sound "sfx/Voices/Player/Char_Player_Non_04.ogg"
            pause 0.5
            play sound "sfx/Voices/Beaudrik/Char_Beaudrik_Choc_01.ogg"
            y "Brutalmund est un menteur ! Il sait très bien que son fils a peur du noir !"

        "Il a peur des buffles":
            play sound "sfx/Voices/Player/Char_Player_Hesitation_02.ogg"
            y "Les buffles le terrifient !"
            nar "{i}{color=#f2de5c}Non, ça, c'est Crossfitrichernvald.{/i}{/color}"
            show char_beaudrik mepris left at speakingAnim(0.8, 0.85, 0.86, 0.8)
            play sound "sfx/Voices/Beaudrik/Char_Beaudrik_Mepris_02.ogg"
            bg "Comment tu peux dire ça ?!"
            show char_beaudrik normal left at speakingAnim(0.8, 0.85, 0.86, 0.8)
            play sound "sfx/Voices/Beaudrik/Char_Beaudrik_Mepris_04.ogg"
            bg "Les buffles, c’est délicieux."
            show char_beaudrik mepris2 left at notSpeakingAnim(0.8, 0.85, 0.86, 0.8)
            play sound "sfx/Voices/Beaudrik/Char_Beaudrik_Choc_01.ogg"
            nar "{i}{color=#f2de5c}Mauvaise réponse, Gaufrid ! La bonne réponse était qu’il a peur du noir.{/i}{/color}"
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
    i "Tu as peur du noir ?!"
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
    
    i "Tiens, moi aussi !"
    show char_ingrid degout at speakingAnim(0.2, 1.15, 1.17, 0.25)
    show char_beaudrik insulte right at notSpeakingAnim(0.8, 0.8, 0.82, 0.8) # A FLIPPER
    play sound "sfx/Voices/Ingrid/Char_Ingrid_Degout_04.ogg"
    pause 0.7
    play sound "sfx/Voices/Beaudrik/Char_Beaudrik_Insult_01.ogg"
    i "Mais les hommes sensibles, c’est pas trop mon truc."
    
    $ loveGauge(ingrid_char, +10, 0.23, 0.15)
    
    show char_ingrid degout at notSpeakingAnim(0.2, 1.15, 1.17, 0.25)
    nar "{i}{color=#f2de5c}Silence ! J’appelle le deuxième témoin : Ingrid elle-même !{/i}{/color}"
    nar "{i}{color=#f2de5c}Ingrid, que pensez-vous de Beaudrik ?{/i}{/color}"
    show char_ingrid normal at speakingAnim(0.2, 1.15, 1.17, 0.25)
    play sound "sfx/Voices/Ingrid/Char_Ingrid_Normal_04.ogg"
    i "Bon, ce n’est pas le plus intelligent, mais Gaufrid n’est pas un génie non plus !"
    show char_ingrid love at speakingAnim(0.2, 1.15, 1.17, 0.25)
    show char_beaudrik normal left at notSpeakingAnim(0.8, 0.8, 0.82, 0.8)
    play sound "sfx/Voices/Ingrid/Char_Ingrid_Love_01.ogg"
    i "Au moins, Beaudrik n'a pas d'imperfections physiques."
    show char_ingrid love at notSpeakingAnim(0.2, 1.15, 1.17, 0.25)

    jump taverne_Concours_Part3_Ingrid_Choice
    
# -----------------------------------------#   
  
label taverne_Concours_Part3_Ingrid_Choice:

    menu:
        i "{cps=0}Au moins Beaudrik n'a pas d'imperfections phyisiques.{/cps}"
        "Objection ! Il est imparfait !":
            play sound "sfx/Voices/Player/Char_Player_Non_03.ogg"
            y "Objection ! Beaudrik est moche !"
            show char_ingrid normal at speakingAnim(0.2, 1.15, 1.17, 0.25)
            show char_beaudrik mepris2 left at notSpeakingAnim(0.8, 0.8, 0.82, 0.8)
            play sound "sfx/Voices/Ingrid/Char_Ingrid_Normal_01.ogg"
            i "Tu n’aurais pas bu un coup en trop, Gaufrid ?"
            show char_ingrid normal at notSpeakingAnim(0.2, 1.15, 1.17, 0.25)
            show char_beaudrik mepris left at speakingAnim(0.8, 0.8, 0.82, 0.8)
            play sound "sfx/Voices/Beaudrik/Char_Beaudrik_Mepris_06.ogg"
            bg "Comment ça, je suis moche ?"
            show char_beaudrik mepris2 left at notSpeakingAnim(0.8, 0.8, 0.82, 0.8)
            jump taverne_Concours_Part3_Ingrid_Choice_Subchoice
            
        "En effet":
            play sound "sfx/Voices/Player/Char_Player_Heureux_02.ogg"
            y "C’est un joli garçon, en effet."
            show char_beaudrik drague right at speakingAnim(0.70, 0.85, 0.86, 0.88)
            play sound "sfx/Voices/Beaudrik/Char_Beaudrik_Doute_03.ogg"
            bg "Oh, c’est gentil !"
            show char_beaudrik normal left at speakingAnim(0.8, 0.8, 0.82, 0.8)
            play sound "sfx/Voices/Beaudrik/Char_Beaudrik_Drague_02.ogg"
            bg "J’ai beau être un homme, j’aime bien prendre soin de mon corps !"
            show char_beaudrik normal left at notSpeakingAnim(0.8, 0.8, 0.82, 0.8)
            nar "{i}{color=#f2de5c}Même de votre troisième téton ?{/i}{/color}"
            show char_beaudrik choque left at notSpeakingAnim(0.75, 0.85, 0.82, 0.8)
            jump taverne_Concours_Part4_Final

# -----------------------------------------#  

label taverne_Concours_Part3_Ingrid_Choice_Subchoice:
    
    menu:
        bg "{cps=0}Comment ça je suis moche ?{/cps}"
        "Il a un gros nez !":
            play sound "sfx/Voices/Player/Char_Player_Non_01.ogg"
            y "Vous avez vu son nez ? C’est une péninsule !"
            show char_ingrid love at speakingAnim(0.2, 1.15, 1.17, 0.25)
            play sound "sfx/Voices/Ingrid/Char_Ingrid_Love_02.ogg"
            $ loveGauge(ingrid_char, -5, 0.23, 0.15)
            i "Je sais pas... moi, je trouve ça sécurisant."
            show char_ingrid normal at notSpeakingAnim(0.2, 1.15, 1.17, 0.25)
            nar "{i}{color=#f2de5c}Vous changerez d'avis quand vous verrez son troisième téton.{/i}{/color}"

        "Il a 3 tétons !":
            play sound "sfx/Voices/Player/Char_Player_Non_03.ogg"
            $ loveGauge(ingrid_char, +10, 0.23, 0.15)
            show char_ingrid choc at notSpeakingAnim(0.2, 1.15, 1.17, 0.25)
            y "Toutes les jeunes femmes du village le savent ! Il a un troisième téton !"

        "{color=#FFFFFF}Il est maigre et moche !{/color}":
            play sound "sfx/Voices/Player/Char_Player_Hesitation_01.ogg"
            y "Euh… il est maigre et moche !"
            show char_ingrid degout at notSpeakingAnim(0.2, 1.15, 1.17, 0.25)
            show char_beaudrik mepris2 left at notSpeakingAnim(0.8, 0.8, 0.82, 0.8)
            nar "{i}{color=#f2de5c}Non Gaufrid, ça, c’est vous.{/i}{/color}"
            play sound "sfx/Voices/Player/Char_Player_Normal_04.ogg"
            y "Ah oui, c’est vrai. Désolé."
            
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
    i "Un troisième téton ?! Mais c’est une imperfection physique complètement discrète et négligeable !"
    show char_ingrid choc at speakingAnim(0.2, 1.15, 1.17, 0.25)
    show char_beaudrik insulte right at notSpeakingAnim(0.8, 0.8, 0.82, 0.8)
    play sound "sfx/Voices/Ingrid/Char_Ingrid_Degout_04.ogg"
    play sound "sfx/Voices/Beaudrik/Char_Beaudrik_Insult_03.ogg"
    i "Ça me dégoûte !"
    show char_ingrid degout at speakingAnim(0.2, 1.15, 1.17, 0.25)
    i "Beaudrik, je suis très déçue."
    i "Ce n’est pas le téton, hein. C’est le principe."
    show char_ingrid choc at speakingAnim(0.2, 1.15, 1.17, 0.25)
    play sound "sfx/Voices/Ingrid/Char_Ingrid_Degout_02.ogg"
    i "Tu m’avais promis que tu n’avais que deux tétons !"
    show char_ingrid degout at notSpeakingAnim(0.2, 1.15, 1.17, 0.25)
    nar "{i}{color=#f2de5c}Bon. En parlant de confiance, Ingrid, pensez-vous que Beaudrik est un gars honnête ?{/i}{/color}"
    show char_ingrid degout at speakingAnim(0.2, 1.15, 1.17, 0.25)
    i "Hormis le téton N°3 ?"
    show char_ingrid degout at notSpeakingAnim(0.2, 1.15, 1.17, 0.25)
    nar "{i}{color=#f2de5c}Oui.{/i}{/color}"
    show char_ingrid love at speakingAnim(0.2, 1.15, 1.17, 0.25)
    play sound "sfx/Voices/Ingrid/Char_Ingrid_Love_02.ogg"
    i "Je pense qu’il serait un époux fidèle et loyal."
    show char_ingrid love at notSpeakingAnim(0.2, 1.15, 1.17, 0.25)
    show char_beaudrik normal left at notSpeakingAnim(0.8, 0.8, 0.82, 0.8)

    jump taverne_Concours_Part4_Final_Choice

# -----------------------------------------#

label taverne_Concours_Part4_Final_Choice:
    
    menu:
        i "Je pense qu’il serait un époux fidèle et loyal."
        "Objection !":
            show char_ingrid degout at notSpeakingAnim(0.2, 1.15, 1.17, 0.25)
            show char_beaudrik mepris2 left at notSpeakingAnim(0.8, 0.8, 0.82, 0.8)
            play sound "sfx/Voices/Player/Char_Player_Non_02.ogg"
            y "Objection ! Beaudrik a déjà une fiancée !"
            show char_ingrid choc at speakingAnim(0.2, 1.15, 1.17, 0.25)
            play sound "sfx/Voices/Ingrid/Char_Ingrid_Choc_01.ogg"
            i "Comment ça, il a une fiancée ?!"
            i "Comment elle s’appelle, cette vache ?!"
            show char_ingrid degout at notSpeakingAnim(0.2, 1.15, 1.17, 0.25)
            jump taverne_Concours_Part4_Final_Choice_Subchoice
            
        "Elle a raison...":
            play sound "sfx/Voices/Player/Char_Player_Heureux_03.ogg"
            y "C’est vraiment un mec bien."
            show char_ingrid love at speakingAnim(0.2, 1.15, 1.17, 0.25)
            play sound "sfx/Voices/Ingrid/Char_Ingrid_Love_03.ogg"
            i "N’est-ce pas ?"
            show char_ingrid love at notSpeakingAnim(0.2, 1.15, 1.17, 0.25)
            nar "{i}{color=#f2de5c}Dommage qu’il soit déjà pris. Votre ami a déjà une fiancée.{/i}{/color}"
            show char_ingrid choc at notSpeakingAnim(0.2, 1.15, 1.17, 0.25)
            show char_beaudrik choque at notSpeakingAnim(0.8, 0.8, 0.82, 0.8)
            nar "{i}{color=#f2de5c}Elle s’appelle Josiane.{/i}{/color}"
            jump taverne_Concours_Part5_Ending
            
# -----------------------------------------#

label taverne_Concours_Part4_Final_Choice_Subchoice:

    menu:
        i "{cps=0}Comment elle s’appelle cette vache ?!{/cps}"
        "Johanne":
            show char_ingrid degout at notSpeakingAnim(0.2, 1.15, 1.17, 0.25)
            show char_beaudrik mepris2 left at notSpeakingAnim(0.8, 0.8, 0.82, 0.8)
            play sound "sfx/Voices/Player/Char_Player_Hesitation_04.ogg"
            y "Euh… Johanne ?"
            $ loveGauge(ingrid_char, -5, 0.23, 0.15)
            nar "{i}{color=#f2de5c}Vous y étiez presque, Gaufrid.{/i}{/color}"
            show char_ingrid choc at notSpeakingAnim(0.2, 1.15, 1.17, 0.25)
            show char_beaudrik choque at notSpeakingAnim(0.8, 0.8, 0.82, 0.8)
            nar "{i}{color=#f2de5c}Elle s’appelle Josiane.{/i}{/color}"
            jump taverne_Concours_Part5_Ending

        "Josiane":
            show char_ingrid choc at notSpeakingAnim(0.2, 1.15, 1.17, 0.25)
            show char_beaudrik choque at notSpeakingAnim(0.8, 0.8, 0.82, 0.8)
            play sound "sfx/Voices/Player/Char_Player_Non_03.ogg"
            $ loveGauge(ingrid_char, +10, 0.23, 0.15)
            y "Josiane ! Elle s’appelle Josiane !"
            jump taverne_Concours_Part5_Ending

        "Jovanne":
            show char_ingrid degout at notSpeakingAnim(0.2, 1.15, 1.17, 0.25)
            show char_beaudrik mepris2 left at notSpeakingAnim(0.8, 0.8, 0.82, 0.8)
            play sound "sfx/Voices/Player/Char_Player_Hesitation_04.ogg"
            y "Euh… Jovanne ?"
            $ loveGauge(ingrid_char, -5, 0.23, 0.15)
            nar "{i}{color=#f2de5c}Vous y étiez presque, Gaufrid.{/i}{/color}"
            show char_ingrid choc at notSpeakingAnim(0.2, 1.15, 1.17, 0.25)
            show char_beaudrik choque at notSpeakingAnim(0.8, 0.8, 0.82, 0.8)
            nar "{i}{color=#f2de5c}Elle s’appelle Josiane.{/i}{/color}"
            jump taverne_Concours_Part5_Ending

        "{color=#FFFFFF}Ernust{/color}":
            play sound "sfx/Voices/Player/Char_Player_Non_03.ogg"
            y "Ernust !"
            show char_ernust love2 :
                xpos 0.5 ypos 1.5 zoom 0.8 #rotate 30
                linear 0.5 xpos 0.15 ypos 0.2
            play sound "sfx/Voices/Ernust/Char_Ernust_Joyeux_03.ogg"
            e "Gaufrid ! Tu m’as appelé ?"
            y "Oui, comment elle s’appelle, la copine de Beaudrik, déjà ?"
            show char_ernust inquiet at speakingAnim(0.5, 1.3, 1.32, 0.8)
            play sound "sfx/Voices/Ernust/Char_Ernust_Inquiet_04.ogg"
            e "Ça commence avec un J, je crois."
            play sound "sfx/Voices/Player/Char_Player_Non_05.ogg"
            y "Ça m’aide beaucoup."
            show char_ernust love2 at speakingAnim(0.5, 1.2, 1.22, 0.8)
            play sound "sfx/Voices/Ernust/Char_Ernust_Joyeux_01.ogg"
            e "On est vraiment un duo dynamique !"
            show char_ernust love2 :
                xpos 0.5 ypos 1.2 zoom 0.8 #rotate 30
                linear 1.0 xpos 0.5 ypos 2.0
            play sound "sfx/Voices/Player/Char_Player_Sarcastic_01.ogg"
            y "Dégage ! Hop !"
            hide char_ernust
            show char_ingrid degout at speakingAnim(0.2, 1.15, 1.17, 0.25)
            i "Alors ?!"
            i "Comment elle s’appelle, cette vache ?!"
            show char_ingrid degout at notSpeakingAnim(0.2, 1.15, 1.17, 0.25)
            jump taverne_Concours_Part4_Final_Choice_Subchoice

# -----------------------------------------#

label taverne_Concours_Part5_Ending:

    stop music1 fadeout 1.5
    $ renpy.pause(2.0, hard = True)
    play sound "sfx/Voices/Ingrid/Char_Ingrid_Choc_01.ogg"
    
    hide screen datingSim
    
    i "JOSIANE ?!"
    play sound "sfx/SFX_Drama_01.ogg"
    i "LA CHÈVRE !?!"
    $ renpy.pause(2.0, hard = True)
    show char_goat choc:
        xalign 0.5 yalign 0.8
        zoom 0.35 xpos 0.5 ypos 1.5
        easein 0.8 ypos 0.73
    play sound "sfx/Voices/Chevre/Char_Chevre_Choc2_01.ogg"
    goat "Bêêêh !"
    show char_beaudrik insulte right at notSpeakingAnim(0.8, 0.8, 0.82, 0.8)
    play sound "sfx/Voices/Beaudrik/Char_Beaudrik_Humilie_01.ogg"
    show char_beaudrik insulte right at speakingAnim(0.8, 0.8, 0.82, 0.8)
    show char_ingrid degout at notSpeakingAnim(0.2, 1.15, 1.17, 0.25)
    bg "C’est platonique, Ingrid ! Crois-moi !"
    show char_beaudrik insulte right at notSpeakingAnim(0.8, 0.8, 0.82, 0.8)
    show char_goat normal:
    nar "{i}{color=#f2de5c}Beaudrik, vous êtes disqualifié.{/i}{/color}"
    show char_beaudrik mepris left at speakingAnim(0.8, 0.8, 0.82, 0.8)
    play sound "sfx/Voices/Beaudrik/Char_Beaudrik_Mepris_01.ogg"
    bg "Tu vas me le payer, Gaufrid !"
    bg "Allons-y, Josiane."
    play sound "sfx/Voices/Chevre/Char_Chevre_Love_01.ogg"
    show char_goat love
    goat "Bêêêh !"
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
    i "Euh…"
    play sound "sfx/Voices/Ingrid/Char_Ingrid_Degout_03.ogg"
    i "Bon Gaufrid, il ne reste plus que toi. On va devoir se marier."
    play sound "sfx/Voices/Player/Char_Player_Heureux_04.ogg"
    show char_ingrid degout at notSpeakingAnim(0.2, 1.15, 1.17, 0.25)
    y "Ah ! Bien, bien !"
    y "C’est bon ? Je te fais la demande ?"

    jump taverne_Concours_Part6_Conclusion

# ------------GOOD ENDING----------------#

label taverne_Concours_Part5_Ending_GoodEnding:

    show char_ingrid love at speakingAnim(0.2, 1.15, 1.17, 0.25)
    i "Gaufrid ! On va pouvoir se marier !"
    show char_ingrid love at notSpeakingAnim(0.2, 1.15, 1.17, 0.25)
    y "Du coup, je dois te faire la demande ?" 
    
    jump taverne_Concours_Part6_Conclusion
    
# -----------------------------------------#

label taverne_Concours_Part6_Conclusion:

    play sound "sfx/Voices/Ingrid/Char_Ingrid_Normal_04.ogg"
    show char_ingrid normal at speakingAnim(0.2, 1.15, 1.17, 0.25)
    i "Oh, non merci, ça ira !"
    i "On peut se marier directement, ça ira plus vite !"
    i "Il nous reste plus qu’à demander la bénédiction de Véléda !"
    play sound "sfx/Voices/Player/Char_Player_Hesitation_04.ogg"
    show char_ingrid normal at notSpeakingAnim(0.2, 1.15, 1.17, 0.25)
    y "Ah oui… c’est vrai qu’il y a cette tradition."
    show char_ingrid normal at speakingAnim(0.2, 1.15, 1.17, 0.25)
    play sound "sfx/Voices/Ingrid/Char_Ingrid_Normal_01.ogg"
    i "Bon ! C'est décidé ! On se voit dans dix minutes à la Tour de Véléda !"
    play sound "sfx/Voices/Ingrid/Char_Ingrid_Love_01.ogg"
    i "Sois ponctuel, ma Gaufrette !"
    
    stop music1 fadeout 1.0
    stop music2 fadeout 1.0
    stop ambiance fadeout 0.5
    jump taverne_Concours_Part6_FadeToBlack

# -----------------------------------------#

label taverne_Concours_Part6_FadeToBlack:

    scene black with Dissolve(0.5)
    y "Comment je vais faire maintenant ?"
    pause 2.0
    outline "{i}Dix minutes plus tard...{/i}"

label taverne_MarryingIngridPart1:

# -----------------------------------------#

    jump tourVeleda_MarryingIngridPart2
    
# -----------------------------------------#
