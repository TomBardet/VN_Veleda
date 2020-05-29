################################################################################
# Ici figurent les scènes se déroulant à l'aurée du village, chez les romains. #
################################################################################
init python:
    _testA = 0
    _testB = 0
label romains_PremiereRencontre:
    if Acte2_Romains_FirstVisit == 1:
        scene bg_romains with Dissolve(1.5):
                zoom 1.15 xpos -0.15
    else:
        scene bg_romains with Dissolve(1.5)
    jump romains_Part1

# -----------------------------------------#

label romains_Part1:
    
    stop music1 fadeout 1.0
    
    $ renpy.music.play("music/MUSIC_Tente_Romain.ogg", channel = "music1", loop = True, fadein = 1)
    $ renpy.music.play("ambiances/AMB_Lieu_Sentier_01.ogg", channel = "ambiance", loop = True, fadein = 1)
    
    $ renpy.music.set_volume(0.4 , delay=0, channel='music1')
    $ renpy.music.set_volume(0, delay=0, channel='music2')
    $ renpy.music.set_volume(0.4, delay=0.4, channel='ambiance')
    
    
    $ interlocuteur = "num_char"
    
    window hide
    if Acte2_Romains_FirstVisit == 1:
        scene bg_romains:
            zoom 1.15 xpos -0.15
        $ _return = renpy.call_screen("action_choice_Tente1")
        
        if _return == "tente":

            pause 0.6
            window show
            jump romains_Part5
        elif _return == "sortir":
            hide screen datingSim
            stop music1 fadeout 1.0
            jump PlaceDuVillageDefault
    
        jump romains_Part5
    else :
        scene bg_romains
        $ _return = renpy.call_screen("action_choice_Tente")
        
        if _return == "tente":
            scene bg_romains:
                linear 0.4 zoom 1.15 xpos -0.15
            pause 0.6
            window show
            y "It looks like there is nobody here..."
            jump romains_Part2
        elif _return == "sortir":
            hide screen datingSim
            stop music1 fadeout 1.0
            jump PlaceDuVillageDefault
            
            
                     
# -----------------------------------------#

label romains_Part2:
    
    show char_digitimus normal right :
        xalign 0.5 yalign 0.8 zoom 1
        xpos 1.2 ypos 0.78
        linear 1 xpos 0.5
    
    
    show char_numerimus normal:
        xalign 0.5 yalign 0.8 zoom 1
        xpos 1.3 ypos 0.82
        linear 0.7 xpos 0.2
    pause 4
   
    show char_numerimus normal at speakingAnim(0.2, 0.82, 0.8, 1)
    show char_digitimus normal right at notSpeakingAnim(0.5, 0.8, 0.815, 1)
    
   
    
    play sound "sfx/Voices/Num/Char_Num_Normal_03.ogg"
    num "{i}Ave{/i}, barbarian!"
    show char_numerimus normal at notSpeakingAnim(0.2, 0.82, 0.8, 1)
    play sound "sfx/Voices/Player/Char_Player_Hesitation_03.ogg"
    y "Erm...{i}Ave{/i} to you... I guess?"
    show screen datingSim(num_char, 0.28, 0.3)
    $ loveGauge(num_char, +10, 0.36, 0.28)
    y "Do I know you?"
    jump romains_Part3

        
# -----------------------------------------#

label romains_Part3:
    
    show char_numerimus heureux at speakingAnim(0.2, 0.82, 0.8, 1)
    show char_digitimus normal right at speakingAnim(0.5, 0.8, 0.815, 1)
    
    play sound "sfx/Voices/Num et Dig/Char_Num_Dig_Heureux_04.ogg"
    num "Haha! Looks like you're a comedian, Germani. I'm Numerimus and that guy there is Digitimus!"
    dig "{i}Ave{/i}..."
    show char_digitimus normal at notSpeakingAnim(0.5, 0.8, 0.815, 1)
    show char_numerimus normal at notSpeakingAnim(0.2, 0.82, 0.8, 1)
     
    play sound "sfx/Voices/Num/Char_Num_Normal_03.ogg"
    show char_numerimus normal at speakingAnim(0.2, 0.82, 0.8, 1)
    num "We are on shore leave, so we're going for a tour around the region."
    num "And we thought: \"Hey, why not go and mock the local customs?\""
    num "So, here we are."
    show char_numerimus normal at notSpeakingAnim(0.2, 0.82, 0.8, 1)
    jump romains_Part4

# -----------------------------------------#

label romains_Part4:
    $ Acte2_Romains_FirstVisit = 1

    play sound "sfx/Voices/Num et Dig/Char_Num_Dig_Normal_01.ogg"
    
    show char_numerimus normal at speakingAnim(0.2, 0.82, 0.8, 1)
    show char_digitimus normal right at speakingAnim(0.5, 0.8, 0.815, 1)
    dig "We're a bit bored to be honest..."
    show char_digitimus normal right at notSpeakingAnim(0.5, 0.8, 0.815, 1)
    num "Yeah, we're really bored..."
    show char_numerimus normal at notSpeakingAnim(0.2, 0.82, 0.8, 1)
    menu :
        num "{cps=0}Yeah, we're really bored...{/cps}"
        "Should I give you a tour?" if _testGlaive == 0:
            play sound "sfx/Voices/Player/Char_Player_Normal_01.ogg"
            y "There's some beautiful sights around here."
            y "Let me give you a tour of our beautiful country."
            jump romains_VisitePart1
            
        "I have an excellent joke for you!" if _testTrompette == 0:
            play sound "sfx/Voices/Player/Char_Player_Sarcastic_02.ogg"
            y "Hold on to your helmets, I have an amazing joke here!"
            show char_numerimus dubitatif at notSpeakingAnim(0.2, 0.82, 0.8, 1)
            show char_digitimus normal right at notSpeakingAnim(0.5, 0.8, 0.815, 1)
            jump romains_Blague

# -----------------------------------------#

label romains_Part5:
    $ Acte2_Romains_FirstVisit = 1
    show screen datingSim(num_char, 0.28, 0.3)
    
    show char_digitimus normal right :
        xalign 0.5 yalign 0.8 zoom 1
        xpos 1.2 ypos 0.78
        linear 1 xpos 0.5
    
    
    show char_numerimus normal:
        xalign 0.5 yalign 0.8 zoom 1
        xpos 1.3 ypos 0.82
        linear 0.7 xpos 0.2
    pause 1.2
    show char_digitimus normal right at notSpeakingAnim(0.5, 0.8, 0.815, 1)
    show char_numerimus normal at speakingAnim(0.2, 0.82, 0.8, 1)
    
    play sound "sfx/Voices/Num/Char_Num_Normal_02.ogg"
    num "We're really bored"
    show char_numerimus normal at notSpeakingAnim(0.2, 0.82, 0.8, 1)
    menu :
        num "{cps=0}We're really bored{/cps}"
        "Look at that, I found some glasses!" if _testLunettes == 1:
            play sound "sfx/Voices/Player/Char_Player_Normal_02.ogg"
            y "Long story short, I found some glasses!"
            jump romains_VisitePart2
            
        "Should I give you a tour?" if _testGlaive == 0:
            play sound "sfx/Voices/Player/Char_Player_Normal_01.ogg"
            y "There's some beautiful sights around here."
            y "Let me give you a tour of our beautiful country."
            jump romains_VisitePart1
            
        "I have an excellent joke for you!" if _testTrompette == 0:
            play sound "sfx/Voices/Player/Char_Player_Sarcastic_02.ogg"
            y "Someone gave me an amazing joke just yesterday!"
            show char_numerimus dubitatif at notSpeakingAnim(0.2, 0.82, 0.8, 1)
            show char_digitimus normal right at notSpeakingAnim(0.5, 0.8, 0.815, 1)
            jump romains_Blague
           
# -----------------------------------------#
                #VISITE
# -----------------------------------------#
label romains_VisitePart1:
    

    show char_numerimus normal at speakingAnim(0.2, 0.82, 0.8, 1)
    play sound "sfx/Voices/Num/Char_Num_Doute_03.ogg"
    num "Forget about sight-seeing. This genius of an assistant here forgot my {b}glasses{/b} in Rome."
    num "I have no sight to see the sights with, see? The world's a blur."
    show char_numerimus normal at notSpeakingAnim(0.2, 0.82, 0.8, 1)
    
    if _testLunettes == 1:
        play sound "sfx/Voices/Player/Char_Player_Heureux_03.ogg"
        y "You're lucky, I just so happen to have a pair right here."
        y "What a happy coincidence!"
        show screen inventory_screen(obj = "lunettes")
        jump romains_VisitePart2
        
    else:
        menu :
            num "{cps=0}This genius of an assistant here forgot my {b}glasses{/b} in Rome.{/cps}"
            "Oh jiminy... don't you have a spare?":
                play sound "sfx/Voices/Player/Char_Player_Normal_01.ogg"
                y "Don't you have a spare?"
                
                show char_numerimus normal at speakingAnim(0.2, 0.82, 0.8, 1)
                
                play sound "sfx/Voices/Num/Char_Num_Doute_02.ogg"
                num "No. We forgot that too"
                num "It would help a lot if you could find one, German."
                
            "Go back to Rome and get them.":
                play sound "sfx/Voices/Player/Char_Player_Sarcastic_02.ogg"
                y "Why don't you go pick them up in Rome."
                y "Pretty convenient that all roads lead there."
                play sound "sfx/Voices/Num/Char_Num_Normal_02.ogg"
                show char_numerimus normal at speakingAnim(0.2, 0.82, 0.8, 1)
                num "A real comedian aren't you..."
                $ loveGauge(num_char, -10, 0.36, 0.28)
        
        show char_numerimus normal at notSpeakingAnim(0.2, 0.82, 0.8, 1)
        show char_digitimus normal right at speakingAnim(0.5, 0.8, 0.815, 1)
        dig "Tell us if you find any {b}glasses{/b} !"
        show char_digitimus normal at notSpeakingAnim(0.5, 0.8, 0.815, 1)
        hide screen datingSim
     #   scene bg_romains:
      #      linear 0.4 zoom 1.0 xpos 0
        show char_numerimus normal at notSpeakingAnim(0.2, 0.82, 0.8, 1)
        show char_digitimus normal right at notSpeakingAnim(0.5, 0.8, 0.815, 1)
        
        if _testTrompette == 0:
                jump romains_Part5
        else :
            show char_numerimus normal at notSpeakingAnim(0.2, 0.82, 0.8, 1) :
                linear 1.5 xpos -1.0
            show char_digitimus normal right at notSpeakingAnim(0.5, 0.8, 0.815, 1) :
                linear 1.5 xpos -1.0
            pause 2.0
            jump romains_Part1
# -----------------------------------------#

label romains_VisitePart2:
    
    play sound "sfx/Voices/Num/Char_Num_Heureux_02.ogg"
    show char_numerimus heureux at speakingAnim(0.2, 0.82, 0.8, 1)
    num "Would you look at that!"
    $ loveGauge(num_char, +35, 0.36, 0.28)
    hide screen inventory_screen
    show char_numerimus normal at notSpeakingAnim(0.2, 0.82, 0.8, 1)
    hide char_numerimus normal
    
    show char_numerimus heureux lunette at speakingAnim(0.2, 0.82, 0.8, 1)
    num "Look at me German! I'm really rocking the hell out of them!"
    show char_numerimus heureux lunette at notSpeakingAnim(0.2, 0.82, 0.8, 1)
    
    jump romains_VisitePart3

# -----------------------------------------#
label romains_VisitePart3:
        
    play sound "sfx/Voices/Num/Char_Num_Normal_02.ogg"
    show char_numerimus normal lunette at speakingAnim(0.2, 0.82, 0.8, 1)
    num "What's there to see around here?"
    show char_numerimus normal lunette at notSpeakingAnim(0.2, 0.82, 0.8, 1)
            
    menu :
        num "{cps=0}What's there to see around here?{/cps}"
        "The fresh vivifying air of the Bructeri land" if _testA == 0:
            $ _testA = 1
            play sound "sfx/Voices/Player/Char_Player_Heureux_03.ogg"
            y "The Lippe, the fresh grass, the fresh air of our beautiful countryside!"
            
            play sound "sfx/Voices/Num et Dig/Char_Num_Dig_Doute_04.ogg"
            show char_digitimus normal right at speakingAnim(0.5, 0.8, 0.815, 1)
            show char_numerimus normal lunette lunette at speakingAnim(0.2, 0.82, 0.8, 1)
            dig "Yeah..."
            show char_digitimus normal right at notSpeakingAnim(0.5, 0.8, 0.815, 1)
            num "What else?"
            show char_numerimus normal lunette at notSpeakingAnim(0.2, 0.82, 0.8, 1)
            jump romains_VisitePart3
            
        "Two big idiots."if _testB == 0:
            play sound "sfx/Voices/Player/Char_Player_Sarcastic_01.ogg"
            y "Two big idiots."
            $ _testB = 1
            play sound "sfx/Voices/Num/Char_Num_Heureux_02.ogg"
            show char_numerimus normal lunette at speakingAnim(0.2, 0.82, 0.8, 1)
            num "Oh, we wouldn't be able to tell all of you look the same to us..."
            show char_numerimus normal lunette at notSpeakingAnim(0.2, 0.82, 0.8, 1)
            jump romains_VisitePart3
            
        "Veleda?":
            play sound "sfx/Voices/Player/Char_Player_Normal_03.ogg"
            y "There is the prophetess Veleda, but..."
            
            play sound "sfx/Voices/Num et Dig/Char_Num_Dig_Heureux_03.ogg"
            show char_numerimus heureux lunette at speakingAnim(0.2, 0.82, 0.8, 1)
            show char_digitimus rire at speakingAnim(0.5, 0.8, 0.815, 1)
            dig "Of course! We've always wanted to see her!"
            show char_digitimus rire at notSpeakingAnim(0.5, 0.8, 0.815, 1)
            num "Yeah! Great idea, german!"
            show char_numerimus heureux lunette at notSpeakingAnim(0.2, 0.82, 0.8, 1)
            
            
            play sound "sfx/Voices/Player/Char_Player_Hesitation_04.ogg"
            y "Well, no right now she's not..."
            
            play sound "sfx/Voices/Num/Char_Num_Heureux_01.ogg"
            show char_numerimus heureux lunette at speakingAnim(0.2, 0.82, 0.8, 1)
            num "Sold! Let's go right now!"
            show char_numerimus heureux lunette at notSpeakingAnim(0.2, 0.82, 0.8, 1)
            
            stop music1 fadeout 1.5
            stop ambiance fadeout 1.0
            
            hide screen datingSim
            scene black with Dissolve (2.0)
            
            y "What did I just do...?"
            

            jump romains_VisitePart4
            
           
    
# -----------------------------------------#
                #VISITE (A LA TOUR)
# -----------------------------------------#
    
# -----------------------------------------#

label romains_VisitePart4:
    

    $ renpy.music.play("music/MUSIC_Tour_Antichambre.ogg", channel = "music1", loop = True, fadein = 1)
    $ renpy.music.play("music/MUSIC_Tour_Chambre_Jour.ogg", channel = "music2", loop = True, fadein = 1)
    $ renpy.music.play("ambiances/AMB_Lieu_Tour_Chambre_01.ogg", channel = "ambiance", loop = True, fadein = 1)
    
    $ renpy.music.set_volume(0.4, delay=0.4, channel='music1')
    $ renpy.music.set_volume(0, delay=0, channel='music2')
    $ renpy.music.set_volume(0.4, delay=0.4, channel='ambiance')
    
    scene bg_tour with Dissolve (1) :
        xpos 0 ypos -960
    show char_ernust normal right at notSpeakingAnim (0.3, 0.92, 0.9, 0.6)  with Dissolve(1.5)
    jump romains_VisitePart5
    
# -----------------------------------------#

label romains_VisitePart5:
    
  
    play sound "sfx/Voices/Player/Char_Player_Non_04.ogg"
    y "Ernust! We have a problem!"
    y "There's two Romans there that want to see Veleda!"
    
    play sound "sfx/Voices/Ernust/Char_Ernust_Inquiet_03.ogg"
    show char_ernust normal right at speakingAnim(0.3, 0.99, 0.97, 0.6) 
    e "Oh! It's too bad she's dead!"
    show char_ernust normal right at notSpeakingAnim(0.3, 0.99, 0.97, 0.6) 
    
    play sound "sfx/SFX_Knock_01.ogg"
    num "Hey, can we come in? It's cold out there!"
    
    play sound "sfx/Voices/Player/Char_Player_Non_02.ogg"
    y "Ahhhhh! There they are!"
    
    play sound "sfx/Voices/Ernust/Char_Ernust_Normal_07.ogg"
    show char_ernust normal right at speakingAnim(0.3, 0.99, 0.97, 0.6) 
    e "Don't worry, Wafflid, I have a great idea! Trust me!"
    show char_ernust normal right at notSpeakingAnim(0.3, 0.99, 0.97, 0.6) 
    menu :
        e "{cps=0}Don't worry, Wafflid, I have a great idea! Trust me!{/cps}"
        "I don't trust you.":
            play sound "sfx/Voices/Player/Char_Player_Non_01.ogg"
            y "There's no way I can trust you."
            y "You'd be able to re-kill her."
            y "But I don't really have a choice..."
            jump romains_VisitePart7           
        "I really don't trust you!":
            play sound "sfx/Voices/Player/Char_Player_Non_01.ogg"
            y "There's no way I can trust you."
            y "You'd be able to re-kill her."
            y "But I don't really have a choice..."
            jump romains_VisitePart7
        "No words can describe how little I trust you.":
            play sound "sfx/Voices/Player/Char_Player_Non_02.ogg"
            y "There's no way I can trust you."
            y "You'd be able to re-kill her."
            y "But I don't really have a choice..."
            jump romains_VisitePart7
            
# -----------------------------------------#
label romains_VisitePart7:
   
    show char_ernust normal right at speakingAnim(0.3, 0.99, 0.97, 0.6) 
    play sound "sfx/Voices/Ernust/Char_Ernust_Love_03.ogg"
    e"I won't disappoint you Wafflid!"
    show char_ernust normal right at notSpeakingAnim(0.3, 0.99, 0.97, 0.6) 
    show char_ernust normal right:
        linear 1.5 xpos -0.5 rotate 10
    pause 0.5
 
    play sound "sfx/Voices/Player/Char_Player_Heureux_01.ogg"
    y "Come in!"
    play sound "sfx/SFX_Entrance_01.ogg"
    show char_numerimus dubitatif lunette:
        xalign 0.5 yalign 0.8 zoom 1
        xpos 1.3 ypos 0.90
        linear 1.0 xpos 0.475
    pause 1.0
    show char_numerimus dubitatif lunette at speakingAnim(0.475, 0.92, 0.9, 1)
    play sound "sfx/Voices/Num/Char_Num_Doute_03.ogg"
    num "Finally!"
    show screen datingSim(num_char, 0.55, 0.35)
    show char_numerimus dubitatif lunette at notSpeakingAnim(0.475, 0.92, 0.9, 1)
    play sound "sfx/Voices/Player/Char_Player_Normal_03.ogg"
    y "Where's your bannerman?"
    show char_numerimus normal lunette at speakingAnim(0.475, 0.92, 0.9, 1)
    play sound "sfx/Voices/Num/Char_Num_Normal_01.ogg"
    num "He's grounded."
    num "He made fun of my sandals."
    num "So, where's that Veleda, eh?"
    show char_numerimus normal lunette at notSpeakingAnim(0.475, 0.92, 0.9, 1)
    
    jump romains_VisitePart8

            
# -----------------------------------------#

label romains_VisitePart8:
    
 #   play sound "sfx/SFX_Char_Player_Ok_01.ogg"
    
    y "Upstairs, she's getting ready..."
    play sound "sfx/Voices/Player/Char_Player_Hesitation_01.ogg"
    y "It should be ok now, I think?"
    y "Follow me."
    jump romains_VisitePart9

# -----------------------------------------#

label romains_VisitePart9:
    
    stop music1 fadeout 1.0
    hide screen datingSim
    scene bg_tour :
        xpos 0 ypos -960
        linear 2.0 xpos 0 ypos 0
        
    play sound "sfx/SFX_Stairs_01.ogg"   
    pause 3.0
    scene vel mario zorder 1 :
        xpos 0 ypos 0
    play sound "sfx/SFX_Stairs_01.ogg"
    jump romains_VisitePart10

# -----------------------------------------#
label romains_VisitePart10:
    
    
    $ renpy.music.play("music/MUSIC_Tour_Chambre_Jour.ogg", channel = "music1", loop = True, fadein = 2)
    show char_numerimus normal lunette at speakingAnim(0.2, 0.92, 0.9, 1) zorder 3:
    show char_veledaernust 02 at notSpeakingAnim(0.8, 0.72, 0.70, 0.3) zorder 3:
    show screen datingSim(num_char, 0.25, 0.35)
    
    play sound "sfx/Voices/Num/Char_Num_Normal_01.ogg"
    num "Wow. So this is the famous Veleda..."    
    play sound "sfx/Voices/Ernust/Char_Ernust_Marionnette_02.ogg"
    show char_veledaernust 01 at speakingAnim(0.8, 0.80, 0.82, 0.3) zorder 3:
        
    ve "Heeeeellooooooo, stranger!"
    ve "I will tell youuuu... a prophecy!!!"
    scene vel mario2 zorder 1:
        xpos 0 ypos 0

    show char_numerimus normal lunette at notSpeakingAnim(0.2, 0.84, 0.82, 1) zorder 3:
        
    show char_veledaernust 02 at speakingAnim(0.8, 0.80, 0.82, 0.3) zorder 3:
    ve "Under the sun, the pebble-colored stone!!!!!!"
    scene vel mario zorder 1 :
        xpos 0 ypos 0
    show char_veledaernust 01 at notSpeakingAnim(0.8, 0.72, 0.70, 0.3) zorder 3:
 
        
 #   play sound "sfx/SFX_Char_Numerimus_Normal_01.ogg"
    show char_numerimus normal lunette at speakingAnim(0.2, 0.92, 0.9, 1) zorder 3:
    play sound "sfx/Voices/Num/Char_Num_Normal_02.ogg"
    num "Fascinating... What does it mean?"
    show char_numerimus normal lunette at notSpeakingAnim(0.2, 0.84, 0.82, 1) zorder 3:
    
 #   play sound "sfx/SFX_Char_Player_Ok_01.ogg"
    play sound "sfx/Voices/Player/Char_Player_Hesitation_04.ogg"
    y "Errr that means uh... when you return... the people of Rome will... be very happy to see you."
    
 #   play sound "sfx/Voices/Player/Char_Player_Hesitation_04.ogg"    show char_numerimus normal at speakingAnim(0.2, 0.92, 0.9, 1.25)
    play sound "sfx/Voices/Num/Char_Num_Heureux_02.ogg"
    $ loveGauge(num_char, +15, 0.34, 0.28)
    num "Ahah! That's true!"
    show char_numerimus normal lunette at notSpeakingAnim(0.2, 0.84, 0.82, 1) zorder 3:
    
    jump romains_VisiteProphetie
    
# -----------------------------------------#
label romains_VisiteProphetie:
    
    play sound "sfx/Voices/Ernust/Char_Ernust_Marionnette_01.ogg"
    scene vel mario2 zorder 1 :
        xpos 0 ypos 0
    show char_numerimus normal lunette at notSpeakingAnim(0.2, 0.84, 0.82, 1) zorder 3:
    show char_veledaernust 01 at speakingAnim(0.8, 0.80, 0.82, 0.3) zorder 3:
    ve  "The biiiiiiiirds siiiing! They sound like crows!" 
    show char_veledaernust 02 at notSpeakingAnim(0.8, 0.72, 0.70, 0.3) zorder 3:
    
    show char_numerimus normal lunette at speakingAnim(0.2, 0.92, 0.9, 1) zorder 3:
    play sound "sfx/Voices/Num/Char_Num_Normal_01.ogg"
    num "... translation please?"
    show char_numerimus normal lunette at notSpeakingAnim(0.2, 0.84, 0.82, 1) zorder 3:
    
    play sound "sfx/Voices/Player/Char_Player_Hesitation_01.ogg"
    y "Well, this obviously means..."
    
 #   play sound "sfx/SFX_Char_Player_Ok_01.ogg"
    menu :
        y "{cps=0}Well, this obviously means...{/cps}"
        "Death is near!" :
            y "A dark omen is upon you!"
            show char_numerimus dubitatif lunette at speakingAnim(0.2, 0.92, 0.9, 1) zorder 3:
            play sound "sfx/Voices/Num/Char_Num_Normal_04.ogg"
            $ loveGauge(num_char, -15, 0.34, 0.28)
            num "Erm... Thanks I guess? "
            show char_numerimus normal lunette at notSpeakingAnim(0.2, 0.84, 0.82, 1) zorder 3:
        "There are... crows?" :
            y "The birds must be crows."
            show char_numerimus normal lunette at speakingAnim(0.2, 0.92, 0.9, 1) zorder 3:
            play sound "sfx/Voices/Num/Char_Num_Normal_04.ogg"
            $ loveGauge(num_char, +1, 0.34, 0.28)
            num "Humm..."
            show char_numerimus normal lunette at notSpeakingAnim(0.2, 0.84, 0.82, 1) zorder 3:
        "The birds will soon enjoy spring." : 
            y "The birds will enjoy the coming of spring."
            show char_numerimus heureux lunette at speakingAnim(0.2, 0.92, 0.9, 1) zorder 3:
            play sound "sfx/Voices/Num/Char_Num_Heureux_02.ogg"
            $ loveGauge(num_char, +15, 0.34, 0.28)
            num "Of course! Everyone loves springtime."
            show char_numerimus normal lunette at notSpeakingAnim(0.2, 0.84, 0.82, 1) zorder 3:
            
    
    
    #Proph 03#
    
    play sound "sfx/Voices/Ernust/Char_Ernust_Marionnette_03.ogg"
    scene vel mario zorder 1 :
        xpos 0 ypos 0
    show char_numerimus normal lunette at notSpeakingAnim(0.2, 0.84, 0.82, 1) zorder 3:    
    show char_veledaernust 01 at speakingAnim(0.8, 0.80, 0.82, 0.3) zorder 3:
   
    ve  "Hot waaaateerrrr... should not mix with.... coooooold waaateeeer!" 

    show char_veledaernust 02 at notSpeakingAnim(0.8, 0.72, 0.70, 0.3) zorder 3:
    play sound "sfx/Voices/Player/Char_Player_Hesitation_02.ogg"
    y "And this one means..."
 #   play sound "sfx/SFX_Char_Player_Ok_01.ogg"
    menu :
        y "{cps=0}And this one means...{/cps}"
        "There is a traitor in your midst!" :
            y "There is a traitor in your midst!"
            show char_numerimus dubitatif lunette at speakingAnim(0.2, 0.92, 0.9, 1) zorder 3:
            play sound "sfx/Voices/Num/Char_Num_Doute_02.ogg"
            $ loveGauge(num_char, -15, 0.34, 0.28)
            num "I hope it's not Digitimus!"
            show char_numerimus normal lunette at notSpeakingAnim(0.2, 0.84, 0.82, 1) zorder 3:
        "You will find glory." :
            y "You will be recognized as a powerful Centurion."
            show char_numerimus heureux lunette at speakingAnim(0.2, 0.92, 0.9, 1) zorder 3:
            play sound "sfx/Voices/Num/Char_Num_Heureux_03.ogg"
            $ loveGauge(num_char, +15, 0.34, 0.28)
            num "I knew it!"
            show char_numerimus normal lunette at notSpeakingAnim(0.2, 0.84, 0.82, 1) zorder 3:
        "Lukewarm water is not cool." :
            y "Mixing cold and hot water is wrong. " 
            show char_numerimus normal lunette at speakingAnim(0.2, 0.92, 0.9, 1) zorder 3:
            play sound "sfx/Voices/Num/Char_Num_Normal_04.ogg"
            $ loveGauge(num_char, +1, 0.34, 0.28)
            num "Humm... yes."
            show char_numerimus normal lunette at notSpeakingAnim(0.2, 0.84, 0.82, 1) zorder 3:
            
    play sound "sfx/Voices/Ernust/Char_Ernust_Marionnette_04.ogg"
    scene vel mario2 zorder 1 :
        xpos 0 ypos 0
    show char_numerimus normal lunette at notSpeakingAnim(0.2, 0.84, 0.82, 1) zorder 3:
    show char_veledaernust 02 at speakingAnim(0.8, 0.80, 0.82, 0.3) zorder 3:
    ve  " Ah.... my arm is getting sore..."
    show char_veledaernust 01 at notSpeakingAnim(0.8, 0.72, 0.70, 0.3) zorder 3:
    
 #   play sound "sfx/SFX_Char_Numerimus_Normal_01.ogg"
    show char_numerimus normal lunette at speakingAnim(0.2, 0.92, 0.9, 1) zorder 3:
    play sound "sfx/Voices/Num/Char_Num_Normal_04.ogg"
    num "Huh?"
    show char_numerimus normal lunette at notSpeakingAnim(0.2, 0.84, 0.82, 1) zorder 3:
    play sound "sfx/Voices/Player/Char_Player_Hesitation_04.ogg"
    y "Errrr... what she means is... that..."
#    play sound "sfx/SFX_Char_Player_Ok_01.ogg"
    menu :
        y "{cps=0}Errrr... what she means is... that...{/cps}"
        "You are getting old." :
            y "Old age is getting near"
            show char_numerimus dubitatif lunette at speakingAnim(0.2, 0.92, 0.9, 1)
            play sound "sfx/Voices/Num/Char_Num_Normal_03.ogg"
            $ loveGauge(num_char, -15, 0.34, 0.28)
            num "Hey, I already know that!"
            show char_numerimus normal lunette at notSpeakingAnim(0.2, 0.84, 0.82, 1)
            jump romains_FinDeLaVisite80
        "Your arm looks strong." :
            y "Your right arm looks much stronger than your left arm. "
            show char_numerimus heureux lunette at speakingAnim(0.2, 0.92, 0.9, 1)
            play sound "sfx/Voices/Num/Char_Num_Heureux_03.ogg"
            $ loveGauge(num_char, +15, 0.34, 0.28)
            num "Extraordinary! She's right!"
            show char_numerimus normal lunette at notSpeakingAnim(0.2, 0.84, 0.82, 1)
            jump romains_FinDeLaVisite80
        "You will be very successful!" :
            y "Your praise will be sung across the entire empire."
            show char_numerimus heureux lunette at speakingAnim(0.2, 0.92, 0.9, 1)
            play sound "sfx/Voices/Num/Char_Num_Heureux_02.ogg"
            $ loveGauge(num_char, +20, 0.34, 0.28)
            num "Haha, no surprise there!"
            show char_numerimus normal lunette at notSpeakingAnim(0.2, 0.84, 0.82, 1)
            jump romains_FinDeLaVisite80

# -----------------------------------------#
label romains_FinDeLaVisite80:
    
 
    
    play sound "sfx/Voices/Ernust/Char_Ernust_Marionnette_01.ogg"
    scene vel mario zorder 1 :
        xpos 0 ypos 0
    show char_veledaernust 02 at speakingAnim(0.8, 0.80, 0.82, 0.3) zorder 3:
    show char_numerimus normal lunette at notSpeakingAnim(0.2, 0.84, 0.82, 1) zorder 3:
    ve  "... It's over."
    show char_veledaernust 01 at notSpeakingAnim(0.8, 0.72, 0.70, 0.3) zorder 3:
    show char_numerimus normal lunette at speakingAnim(0.2, 0.92, 0.9, 1) zorder 3:
    play sound "sfx/Voices/Num/Char_Num_Normal_01.ogg"
    num "What?"
    show char_numerimus normal lunette at notSpeakingAnim(0.2, 0.84, 0.82, 1) zorder 3:
    play sound "sfx/Voices/Player/Char_Player_Normal_02.ogg"
    y "Show's over! Hippity hoppity, off you go!"
    hide screen datingSim
    scene bg_tour :
        xpos 0 ypos 0
        linear 2.0 xpos 0 ypos -960
    play sound "sfx/SFX_Stairs_01.ogg"   
    pause 2.0
    
    show char_numerimus heureux lunette at speakingAnim(0.5, 0.92, 0.9, 1)
    show screen datingSim(num_char, 0.55, 0.35)

 
    
    play sound "sfx/Voices/Num/Char_Num_Heureux_02.ogg"
    num "These prophecies really touched my heart!"
    num "I will leave the army and join the Red Cross! I can't stay indiferent to such a revelation."
    num "I won't need this anymore, take it!"
    show char_numerimus heureux lunette at notSpeakingAnim(0.5, 0.92, 0.9, 1)
    $ inventory.add(glaive)
    $ _testGlaive = 1
    play sound "sfx/SFX_UI_Inventory_Glaive_01.ogg"
    show img_glaive at center:
        xalign 0.7 yalign 0.9 zoom 0.3
        linear 0.5 yalign 0.7 zoom 0.4
        easein 0.5 zoom 0.45
        easeout 0.5 zoom 0.4
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
    pause 2.5
    play sound "sfx/SFX_UI_Inventory_Bag_01.ogg"
    pause 0.5
        
    hide screen datingSim
    hide char_numerimus normal lunette with Dissolve(1.5)
    hide screen datingSim
    pause 3.0
    y "Hey! That's a {b}glaive{/b}! Thanks!"
    
    if _testGlaive == 1 & _testBouclier == 1:
        stop music1 fadeout 1.0
        hide screen datingSim
        jump PlaceDuVillageAllObjects
        
    else:
        stop music1 fadeout 1.0
        hide screen datingSim
        jump PlaceDuVillageDefault
    
# -----------------------------------------#
                #BLAGUE
# -----------------------------------------#

label romains_Blague:
    
    if _testBlague == 1:
        y "There you go, read this..."
        show screen inventory_screen(obj = "blague")
        
        play sound "sfx/SFX_UI_Inventory_Glaive_01.ogg"

        pause 3.0
        
        hide screen inventory_screen
        play sound "sfx/Voices/Num et Dig/Char_Num_Dig_Rire_01.ogg"
        show char_numerimus heureux at speakingAnim(0.2, 0.82, 0.8, 1)
        show char_digitimus rire right at speakingAnim(0.5, 0.8, 0.815, 1)
        num "Hahahaha!"
        $ loveGauge(num_char, +10, 0.36, 0.28)
        show char_numerimus normal at notSpeakingAnim(0.2, 0.82, 0.8, 1)
        dig "Haahahahaha... haahaha!"
        $ loveGauge(num_char, +25, 0.36, 0.28)
        dig "It's the best joke I heard in my life! I almost died!"
        show char_digitimus normal right at notSpeakingAnim(0.5, 0.8, 0.815, 1)
        dig "Well, thanks! What can I do to thank you? Take this... my {b}trumpet{b}."
        
        $ inventory.add(trompette)
        $ _testTrompette = 1
        
        play sound "sfx/SFX_UI_Inventory_Trumpet_01.ogg"
        
        show img_trompette at center:
            xalign 0.7 yalign 0.9 zoom 0.3
            linear 0.5 yalign 0.7 zoom 0.4
            easein 0.5 zoom 0.55
            easeout 0.5 zoom 0.4
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
        pause 2.5
        play sound "sfx/SFX_UI_Inventory_Bag_01.ogg"
        pause 0.5
        y "... What in the world am I going to do with a {b}trumpet{/b}?"
        show char_ernust normal left:
            xalign 0.5 yalign 0.8
            xpos 0.999 ypos 1.9 zoom 0.8 rotate -30
            linear 0.3 xpos 0.9 ypos 1.3
        #pause 1.5
        
        play sound "sfx/Voices/Ernust/Char_Ernust_Normal_03.ogg"
        e "We can use it to scare animals!"
        y "... What are you talking about?"
        show char_ernust normal left:
            xalign 0.5 yalign 0.8
            xpos 0.9 ypos 1.3 zoom 0.8 rotate -30
            linear 0.3 xpos 0.999 ypos 1.9
        pause 1.0
        jump romains_Part5