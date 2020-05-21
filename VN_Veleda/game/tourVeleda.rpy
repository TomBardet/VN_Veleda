##########################################################
# Ici figurent les scènes se déroulant à la Tour Véléda. #
##########################################################

label tourVeleda_ErnustEtVeleda :
    
    scene bg_tour with Dissolve (2.5) :
        xpos 0 ypos 0
        
    $ renpy.music.play("music/MUSIC_Tour_Antichambre.ogg", channel = "music1", loop = True, fadein = 1)
    $ renpy.music.play("music/MUSIC_Tour_Chambre_Jour.ogg", channel = "music2", loop = True, fadein = 1)
    $ renpy.music.play("ambiances/AMB_Lieu_Tour_Chambre_01.ogg", channel = "ambiance", loop = True, fadein = 1)
    
    $ renpy.music.set_volume(0.4, delay=0.4, channel='music1')
    $ renpy.music.set_volume(0.4, delay=0.4, channel='music2')
    $ renpy.music.set_volume(0.4, delay=0.4, channel='ambiance')
    
    
    
    show vel normal with Dissolve (2.5) :
        xpos 0 ypos 0
    
    $ interlocuteur = "vel_char"
    
    show screen datingSim(vel_char, 0.625, 0.33)
    
    play sound "sfx/Voices/Veleda/Char_Veleda_Normal_04.ogg"
    
    show vel normal2 :
        xpos 0 ypos 0
        
    v "There you are Wafflid! Hurry it up, we are waiting for some very important guests."
    
    play sound "sfx/Voices/Player/Char_Player_Normal_02.ogg"
    y "What?... the numbers are still here? Have I lost my marbles?"
    
    play sound "sfx/Voices/Veleda/Char_Veleda_rage_01.ogg"
    $ loveGauge(vel_char, -3, 0.75, 0.4)
    
    show vel normal :
        xpos 0 ypos 0

    v "Numbers? What ARE you talking about?"
    
    $ loveGauge(vel_char, -3, 0.75, 0.4)
    
    v "Go prepare the room, Mister Wafflid. Your shenanigans are no business of ours."
    

    play sound "sfx/Voices/Veleda/Char_Veleda_Normal_02.ogg"
    
    show vel normal2 :
        xpos 0 ypos 0
    
    v "We are expecting a noteworthy guest! My Lord Crossfrit... croshfritsh... crosrustr..."
    
    
    v "My Lord Crossfrenchfry, the noble chief of our Batavian neighbours."
    
    show vel normal :
        xpos 0 ypos 0
        
    y "Do you mean Crossfitrichernvald?" 
    
    menu :
        y "{cps=0}Do you mean Crossfitrichernvald?{/cps}"
        "Is he coming for advice, O honourable Veleda? ":
            play sound "sfx/Voices/Player/Char_Player_Normal_04.ogg"
            
            y "Will he listen to your legendary prophecies, O divine Veleda?"
            
            play sound "sfx/Voices/Veleda/Char_Veleda_Normal_03.ogg"
            
            $ loveGauge(vel_char, -3, 0.5, 0.25)
            
            show vel normal2 :
                xpos 0 ypos 0
            
            v "You will not trick me with your simpering, Mister Wafflid."
            
            $ loveGauge(vel_char, -3, 0.75, 0.4)
    
            v "Flattery is but a refuge for the incompetent."
            
            
        "What does this brute want?":

            play sound "sfx/Voices/Player/Char_Player_Sarcastic_04.ogg"
            y "What's this animal's problem this time?"
            
            play sound "sfx/Voices/Veleda/Char_Veleda_Normal_03.ogg"
            
            show vel normal2 :
                xpos 0 ypos 0
            
            $ loveGauge(vel_char, -3, 0.5, 0.25)
            v "Oh! How vulgar Mister Wafflid!"
            
            $ loveGauge(vel_char, -3, 0.5, 0.25)
            v "What kind of uncivilized language is that?"

            
    play sound "sfx/Voices/Veleda/Char_Veleda_Normal_01.ogg"
    
    show vel normal :
        xpos 0 ypos 0
    
    v "My lord Crossfritrichierich accuses our village's blacksmith, Mister Brutalmund, of unjustly appropriating his property!"
    
    v "Mister Brutalmund denies the allegation! We shall therefore render justice with..."
    
    $ renpy.music.set_volume(0, delay = 0, channel='music1')
    $ renpy.music.set_volume(0, delay = 0, channel='music2')
    $ renpy.music.set_volume(0, delay=0, channel='ambiance')
    
    show vel normal2 :
        xpos 0 ypos 0
        
    play sound "sfx/SFX_Drama_01.ogg"
    show vel normal2 :
        xpos 0 ypos 0
        easein 0.8 xpos -300 zoom 1.2
    $ renpy.pause(2.0, hard = True)
    v "A prophecy!"
    show vel normal2 with Dissolve(0.5):
        xpos 0 ypos 0 zoom 1.0
    $ renpy.music.set_volume(0.4, delay=0.4, channel='music1')
    $ renpy.music.set_volume(0.4, delay=0.4, channel='music2')
    $ renpy.music.set_volume(0.4, delay=0.4, channel='ambiance')
    
 
    play sound "sfx/Voices/Player/Char_Player_Hesitation_01.ogg"
    y "Erm... why doesn't he just file a complaint?"
    
    show vel normal :
        xpos 0 ypos 0
    
    play sound "sfx/Voices/Veleda/Char_Veleda_Rage_01.ogg"

    
    $ loveGauge(vel_char, -3, 0.8, 0.25)
    v "You dare doubt the wisdom of our prophecies, Mister Wafflid?"
    
    v "Where is your cousin by the way? The dopey Mister Ernust?"
    
    play sound "sfx/Voices/Veleda/Char_Veleda_Normal_04.ogg"
    v "He should have brought us sustenance hours ago!"
    
    show vel normal2 :
        xpos 0 ypos 0
    
    play sound "sfx/SFX_Entrance_01.ogg"
    
    pause 0.8
    
    v "Aha! That must be him!"
    
    play sound "sfx/SFX_Stairs_02.ogg"
    show char_ernust normal right :
        xalign 0.5 yalign 0.8
        xpos -0.2 ypos 2.0 zoom 0.6
        linear 1.2 xpos 0.20 ypos 0.94
        
    $ renpy.pause (1.7, hard=True)
    
    $ interlocuteur = "ern_char"
    show screen datingSim(ern_char, 0.15, 0.17)
    
    pause 0.5

    show char_ernust joyeux right at speakingAnim(0.21,1.025,1.0,0.6)
   
    
 #   play sound "sfx/SFX_Char_Ernust_Normal_01.ogg"
    
    
    play sound "sfx/Voices/Ernust/Char_Ernust_Joyeux_03.ogg"
    e "Oh, hello there Wafflid!"
    $ loveGauge(ern_char, 1, 0.26, 0.14)
    show char_ernust normal right at notSpeakingAnim(0.193,1.02,1.0,0.6)
    show vel normal :
        xpos 0 ypos 0
    menu :
        e "{cps=0}Oh, hello there Wafflid!{/cps}"
        "Hello Ernust!" :
            play sound "sfx/Voices/Player/Char_Player_Normal_01.ogg"
            y "Hello Ernust, how are you?"
            
            show char_ernust love1 at speakingAnim(0.23,1.025,1.0,0.6)
            play sound "sfx/Voices/Ernust/Char_Ernust_Normal_05.ogg"
            $ loveGauge(ern_char, 3, 0.26, 0.14)            
            e "I'm doing very well!"
            $ loveGauge(ern_char, 3, 0.26, 0.14)
            e "It is so nice of you to ask Wafflid!"
            
        "90 affection points?" :
            play sound "sfx/Voices/Player/Char_Player_Hesitation_04.ogg"
            y "90 love points? Is he in love with me?"

            show char_ernust love1 at speakingAnim(0.23,1.025,1.0,0.6)
            play sound "sfx/Voices/Ernust/Char_Ernust_Normal_05.ogg"
            $ loveGauge(ern_char, 3, 0.26, 0.14)            
            e "You're my bestest best friend Wafflid!"
            $ loveGauge(ern_char, 3, 0.26, 0.14)
            e "I like you!"

            
        "Ah... you're here too?" :
            play sound "sfx/Voices/Player/Char_Player_Sarcastic_01.ogg"
            y "Oh... you're here? Pfff..."

            show char_ernust joyeux right at speakingAnim(0.20,1.02,1.0,0.6)

            play sound "sfx/Voices/Ernust/Char_Ernust_Normal_05.ogg"
            $ loveGauge(ern_char, 3, 0.26, 0.14)            
            e "Yes, I am here!"
            $ loveGauge(ern_char, 3, 0.26, 0.14)
            show char_ernust love1 at speakingAnim(0.23,1.025,1.0,0.6)
            e "I'm so glad to see you too Wafflid!"


            
    play sound "sfx/Voices/Veleda/Char_Veleda_Normal_03.ogg"
    
    pause 0.1 
    
    show char_ernust inquiet right :
            xpos 0.195 ypos 1.02 zoom 0.6
            linear 0.15 xpos 0.185 ypos 1.03 rotate -5
    
    $ interlocuteur = "vel_char"
    show screen datingSim(vel_char, 0.625, 0.33)
    
    show vel normal2 :
        xpos 0 ypos 0
    $ loveGauge(vel_char, -1, 0.75, 0.4)
    v "Bring us our food, mister Ernust! We are perishing from hunger."

    play sound "sfx/Voices/Ernust/Char_Ernust_Normal_06.ogg"
    show char_ernust joyeux right at speakingAnim(0.20,1.02,1.0,0.6)
    show vel normal :
        xpos 0 ypos 0
    e "Oh yes, Your Excelency My Lady Veleda!"
    e "I was in the forest hunting boars."
    play sound "sfx/Voices/Ernust/Char_Ernust_Normal_03.ogg"
    show char_ernust normal right at speakingAnim(0.19,1.02,1.0,0.6)
    e "I was thinking: a nice grilled boar, that's hearty and it will fill you right up!"
    show char_ernust joyeux right at speakingAnim(0.20,1.02,1.0,0.6)
    e "With a bit of thyme, and a couple of potatoes..."
    show char_ernust normal right at notSpeakingAnim(0.193,1.02,1.0,0.6)
    menu :
        e "{cps=0}With a bit of thyme, and a couple of potatoes...{/cps}"
        "That sounds delicious!" :
            
            $ interlocuteur = "ern_char"
            show screen datingSim(ern_char, 0.15, 0.17)
            
            play sound "sfx/Voices/Player/Char_Player_Heureux_03.ogg"
            y "That really sounds great Ernust, I can't wait to see it!"
            
            show char_ernust joyeux right at speakingAnim(0.20,1.02,1.0,0.6)
            
            play sound "sfx/Voices/Ernust/Char_Ernust_Joyeux_01.ogg"
            $ loveGauge(ern_char, 3, 0.26, 0.14)
            e "You're so nice Wafflid!"
            $ loveGauge(ern_char, 2, 0.26, 0.14)
            
            e "I was thinking about you you know. I was thinking: Wafflid must be so sad!"
            $ loveGauge(ern_char, 2, 0.26, 0.14)
            
            show char_ernust normal right at speakingAnim(0.19,1.02,1.0,0.6)
            play sound "sfx/Voices/Ernust/Char_Ernust_Inquiet_02.ogg"
            e "Ingrid is so mean to you!"
            $ loveGauge(ern_char, 5, 0.26, 0.14)
            
            show char_ernust love1 at speakingAnim(0.23,1.025,1.0,0.6)
            
            e "But I think you are a really special guy Wafflid."

            
        "Hurry it up Ernust." :
            
            $ interlocuteur = "ern_char"
            show screen datingSim(ern_char, 0.15, 0.17)
            
            play sound "sfx/Voices/Player/Char_Player_Non_04.ogg"
            y "Hurry up Ernust, we're waiting for customers."
            
            play sound "sfx/Voices/Ernust/Char_Ernust_Inquiet_02.ogg"
            show char_ernust joyeux right at speakingAnim(0.20,1.02,1.0,0.6)
            e "You're right Wafflid, I'm talking too much again!"
            
            show char_ernust love1 at speakingAnim(0.23,1.025,1.0,0.6)
            
            $ loveGauge(ern_char, 3, 0.26, 0.14)
            e "You always tell me when I mess up."
            
            play sound "sfx/Voices/Ernust/Char_Ernust_Normal_02.ogg"
            $ loveGauge(ern_char, 2, 0.26, 0.14)
            e "It really helps you know, I feel so much smarter when I'm with you!"
            
                
    play sound "sfx/Voices/Veleda/Char_Veleda_Normal_01.ogg"
    
    pause 0.1 
    
    show char_ernust inquiet right :
            xpos 0.195 ypos 1.02 zoom 0.6
            linear 0.15 xpos 0.185 ypos 1.03 rotate -5
    
    #show char_veleda normal at speakingAnim(0.48,0.82,0.80,0.7)
    show vel normal2 :
        xpos 0 ypos 0
    
    $ interlocuteur = "vel_char"
    show screen datingSim(vel_char, 0.625, 0.33)
    
    v "That is enough! Serve us our boar!"
    #show char_veleda normal at notSpeakingAnim(0.48,0.82,0.80,0.7)
    play sound "sfx/Voices/Ernust/Char_Ernust_Normal_06.ogg"
    show char_ernust joyeux right at speakingAnim(0.20,1.02,1.0,0.6)
    show vel normal :
        xpos 0 ypos 0
    e "Oh no, I don't have a boar!"
    e "I saw one in the forest but... I don't have a weapon!"
    e "You can't hunt boars with your bare hands, oh no."
    
    play sound "sfx/Voices/Ernust/Char_Ernust_Joyeux_03.ogg"
    e "But I did find mushrooms, so I made a soup! A nice mushroom soup!"
    show char_ernust normal right at notSpeakingAnim(0.193,1.02,1.0,0.6)
    #show char_veleda normal at speakingAnim(0.48,0.82,0.80,0.7)
    play sound "sfx/Voices/Veleda/Char_Veleda_Normal_03.ogg"
    show vel normal2 :
        xpos 0 ypos 0
    v "It shall be enough! You, Mister Wafflid, go meet our guests. We are prophecisizing that they will knock on the door soon!"
    
    play sound "sfx/SFX_Knock_01.ogg"
    pause 1.0
    v "Aha, see? Go on then, mister Wafflid."
    #show char_veleda normal at notSpeakingAnim(0.48,0.82,0.80,0.7)
    play sound "sfx/Voices/Player/Char_Player_Normal_04.ogg"
    show vel normal :
        xpos 0 ypos 0
    y "Alright, I'm going, I'm going..."
    
    hide screen datingSim
    
    window hide 
    
    $ renpy.music.set_volume(0, delay=1, channel='music2')
    
    stop ambiance fadeout 1.5
    
    scene bg_tour :
        xpos 0 ypos 0
        linear 2.0 xpos 0 ypos -960
    show vel normal :
        xpos 0 ypos 0
        linear 2.0 xpos 0 ypos -960
    show char_ernust normal right :
        xalign 0.5 yalign 0.8
        xpos 0.20 ypos 1.02 zoom 0.6
        linear 2.0 xpos 0.24 ypos -0.55
    show char_crossfit colere right :
        xalign 0.5 yalign 0.8
        xpos 0.20 ypos 3.0 zoom 0.32
        linear 2.0 xpos 0.26 ypos 0.84
    show char_brutal normal:
        xalign 0.5 yalign 0.8
        xpos 0.81 ypos 3.0 zoom 0.32
        linear 2.0 xpos 0.75 ypos 0.92
        
    play sound "sfx/SFX_Stairs_01.ogg"   
    $ renpy.pause(2.5, hard = True)
             
    
    jump tourVeleda_HistoireBrevetPart1

        
# -----------------------------------------#

label tourVeleda_HistoireBrevetPart1:

    $ renpy.music.play("ambiances/AMB_Lieu_Antichambre_01.ogg", channel = "ambiance", loop = True, fadein = 1)
    

    #show char_brutal normal at notSpeakingAnim(0.75, 0.92,0.92,0.32) with Dissolve(1)

    
    play sound "sfx/Voices/Crossfit/Char_Crossfit_Colere_01.ogg"
    show char_crossfit colere right at speakingAnim(0.26,0.94,0.92,0.32)
    cross "There you are! I will finally have justice, Brutalmund !"
    
    show char_crossfit colere right at notSpeakingAnim(0.26,0.94,0.92,0.32)
    show char_brutal colere at speakingAnim(0.75, 1.05, 1.02, 0.32)
    play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere1_01.ogg"
    brut "I told ya I didn' steal a thing!"
    
    show char_brutal normal at notSpeakingAnim(0.75, 1.05,1.2,0.32)
    show char_crossfit serieux at speakingAnim(0.26,0.94,0.92,0.32)
    play sound "sfx/Voices/Crossfit/Char_Crossfit_Colere_03.ogg"
    cross "You, assistant, go and get the prophetess!"
    
    show char_crossfit colere right at notSpeakingAnim(0.26,0.94,0.92,0.32)
    play sound "sfx/Voices/Player/Char_Player_Non_04.ogg"
    y "Ah no! The prophetess does not see visitors directly."
    y "You tell me the problem, and I'll bring it to her. I'll come back down and tell you the result of the prophecy."
    

    show char_crossfit serieux at speakingAnim(0.26,0.94,0.92,0.32)
    play sound "sfx/Voices/Crossfit/Char_Crossfit_Serieux_02.ogg"
    cross "Very well, servant! If you don't transmit my exact words, I will gut you like a fish."
    
    $ interlocuteur = "cross_char"
    
    show screen datingSim(cross_char, 0.35, 0.27)
    
    show char_crossfit colere right at notSpeakingAnim(0.26,0.94,0.92,0.32)
    menu :
        cross "{cps=0}Very well, servant! If you don't transmit my exact words, I will gut you like a fish.{/cps}"
        "Yes, My Lord" :
            
            $ loveGauge(cross_char, 5, 0.45, 0.27)
            play sound "sfx/Voices/Player/Char_Player_Normal_01.ogg"
            y "Of course, My Lord Crossfritrichernvald, I will be very careful."
            
        "I know how to do my job, you know" :
            $ loveGauge(cross_char, -5, 0.45, 0.27)
            play sound "sfx/Voices/Player/Char_Player_Sarcastic_04.ogg"
            y "Hey, I know what I'm doing! You don't need to threaten me."
    
    y "Tell me everything, what is the issue?"
    
    play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Heureux_01.ogg"
    show char_brutal normal at speakingAnim(0.75, 1.05,1.02,0.32)
    
    $ interlocuteur = "brut_char"
    
    show screen datingSim(brut_char, 0.63, 0.29)
    
    brut "Imma tell you right there buddy, my friend Wafflid!"
    brut "Y'see, the other day, Crossfitrichernvald, he's walking by my shop y'know."
    show char_brutal heureux at speakingAnim(0.75, 1.05,1.02,0.32)
    
    play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Normal_05.ogg"
    brut "And he sees that shield, right? Looks just like his!"
    show char_brutal colere at speakingAnim(0.75, 1.05,1.02,0.32)
    
    play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere1_03.ogg"
    brut "But I didn' steal no shield I can tell y'a that buddy!"
    brut "I made it m'self. With ma'own hands! I swear, Wafflid, pal, y'a gotta believe me!"
    show char_brutal normal at notSpeakingAnim(0.75, 1.05,1.02,0.32)
    
    $ interlocuteur = "cross_char"
    
    show screen datingSim(cross_char, 0.35, 0.27)
    
    play sound "sfx/Voices/Crossfit/Char_Crossfit_Choc_01.ogg"
    show char_crossfit choc right at speakingAnim(0.26,0.94,0.92,0.32)
    cross "Hey! You know very well that that is not the problem, crook!"
    show char_crossfit colere right at notSpeakingAnim(0.26,0.94,0.92,0.32)

    play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Choc_01.ogg"
    show char_brutal surpris at speakingAnim(0.75, 1.05,1.02,0.32)
    brut "Me? A crook?"
    show char_brutal normal at notSpeakingAnim(0.75, 1.05,0.92,0.32)
    
    play sound "sfx/Voices/Crossfit/Char_Crossfit_Inquiet_01.ogg"
    show char_crossfit serieux at speakingAnim(0.26,0.94,0.92,0.32)
    cross "Yes, a crook! This shield is the same as mine, you copied it!"
    cross "It's {b}copyright infringement{/b}!"
    show char_crossfit colere right at notSpeakingAnim(0.26,0.94,0.92,0.32)        

    play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere1_02.ogg"
    show char_brutal colere at speakingAnim(0.75, 1.05,1.02,0.32)
    brut "Oh wow, usin' fancy words there I see!"
    show char_brutal normal at notSpeakingAnim(0.75, 1.05,1.0,0.32)
    
    play sound "sfx/Voices/Crossfit/Char_Crossfit_Serieux_01.ogg"
    show char_crossfit serieux at speakingAnim(0.26,0.94,0.92,0.32)
    cross "Copyright law is a fundamental aspect of first century Germanic society!"
    show char_crossfit colere right at notSpeakingAnim(0.26,0.94,0.92,0.32)
    menu :
        cross "{cps=0}Copyright law is a fundamental aspect of first century Germanic society{/cps}"
        "That's very serious!" :
            play sound "sfx/Voices/Player/Char_Player_Non_03.ogg"
            y "You're right, this is a big deal!"
            $ interlocuteur = "brut_char"
    
            show screen datingSim(brut_char, 0.63, 0.29)
            
            
            
            play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Choc_01.ogg"
            show char_brutal surpris at speakingAnim(0.75, 1.05,1.02,0.32)
            brut "You too! Wafflid, my brother from another mother, turning against me!"
            show char_brutal normal at notSpeakingAnim(0.75, 1.05,1.02,0.32)
            
            $ loveGauge(brut_char, -5, 0.55, 0.27)
            
            play sound "sfx/Voices/Player/Char_Player_Normal_01.ogg"
            y "Well, let me see what the prophetess thinks."
        
        "Who cares?" :
            play sound "sfx/Voices/Player/Char_Player_Non_03.ogg"
            y "No reason to get all worked up over it, right?"
            
            $ loveGauge(cross_char, -5, 0.45, 0.27)
            
            play sound "sfx/Voices/Crossfit/Char_Crossfit_Choc_01.ogg"
            show char_crossfit choc right at speakingAnim(0.26,0.94,0.92,0.32)
            cross "How dare you, lackey?"
            show char_crossfit serieux at speakingAnim(0.26,0.94,0.92,0.32)
            play sound "sfx/Voices/Crossfit/Char_Crossfit_Serieux_03.ogg"
            cross "Our laws are clear! Go and see the prophetess, now!"
            show char_crossfit colere right at notSpeakingAnim(0.26,0.94,0.92,0.32)
            
            play sound "sfx/Voices/Player/Char_Player_Normal_01.ogg"
            y "Alright! Alright! I'm going! No need to get angry!"
            
    hide screen datingSim        
    
    window hide 
    
    stop ambiance fadeout 1.5

    scene bg_tour :
        xpos 0 ypos -960
        linear 2.0 xpos 0 ypos 0
    show vel morte :
        xpos 0 ypos -960
        linear 2.0 xpos 0 ypos 0
    show char_ernust normal right :
        xalign 0.5 yalign 0.8
        xpos 0.24 ypos -0.55 zoom 0.6
        linear 2.0 xpos 0.193 ypos 0.92
    show char_crossfit colere right :
        xalign 0.5 yalign 0.8
        xpos 0.26 ypos 0.84 zoom 0.32
        linear 2.0 xpos 0.20 ypos 3.0
    show char_brutal normal:
        xalign 0.5 yalign 0.8
        xpos 0.75 ypos 1.05 zoom 0.32
        linear 2.0 xpos 0.81 ypos 3.0
        
    play sound "sfx/SFX_Stairs_02.ogg"   
    $ renpy.pause(2.5, hard = True)
    
    jump tourVeleda_MortVeleda
    
# -----------------------------------------#
    
label tourVeleda_MortVeleda:
    
    $ renpy.music.set_volume(0.4, delay=1, channel='music2')
    $ renpy.music.play("ambiances/AMB_Lieu_Tour_Chambre_01.ogg", channel = "ambiance", loop = True, fadein = 1)
    
    pause 0.5
    
    show char_ernust joyeux right at speakingAnim(0.20,1.02,1.0,0.6)
    
    play sound "sfx/Voices/Ernust/Char_Ernust_Normal_07.ogg"
    
    e "Oh, Wafflid! How did it go?"
    e "Veleda's having a quick nap!"
    
    show char_ernust normal right  at notSpeakingAnim(0.185,1.01,1.0,0.6)
   
    play sound "sfx/Voices/Player/Char_Player_Normal_04.ogg"
    y "A nap? What do you mean"
    
    show char_ernust joyeux right at speakingAnim(0.20,1.02,1.0,0.6)
    
    play sound "sfx/Voices/Ernust/Char_Ernust_Joyeux_03.ogg"
    
    e "Well yeah, she ate my soup and then she made some weird sounds."
    e "She was gagging and choking, it was pretty scary."
    e "But now she's sleaping peacefully!"
    
    show char_ernust normal right  at notSpeakingAnim(0.185,1.01,1.0,0.6)
    play sound "sfx/Voices/Player/Char_Player_Normal_03.ogg"
    y "What? What kind of mushrooms were they?"
    y "Check on her right now!"
    
    play sound "sfx/Voices/Ernust/Char_Ernust_Normal_02.ogg"
    show char_ernust joyeux right :
        xalign 0.5 yalign 0.8
        xpos 0.185 ypos 1.01 zoom 0.6
        linear 1 xpos 0.35 ypos 1.05 zoom 0.55 rotate 5
        
    $ renpy.pause (1.1, hard = True)
    
    show char_ernust normal right :
        linear 0.15 rotate 25
    
    $ renpy.pause (0.6, hard = True)
    play sound "sfx/Voices/Ernust/Char_Ernust_Normal_01.ogg"
    e "Hmm..."
    
    play sound "sfx/Voices/Ernust/Char_Ernust_Trahi_02.ogg"
    show char_ernust inquiet right :
        linear 0.15 rotate -3
        linear 0.15 rotate 3
        linear 0.15 rotate 0
        
    $ renpy.pause (0.8, hard = True)
    
    show char_ernust inquiet right at speakingAnim(0.35,1.05,1.0,0.55)

    e "Shes' not ok, Wafflid!"
    e "I can't feel her pulse!"
    
    show char_ernust inquiet right at notSpeakingAnim(0.35,1.04,1.0,0.55)
    play sound "sfx/Voices/Player/Char_Player_Non_02.ogg"
    y "What? You... you killed Veleda, Ernust !"
    y "The most famous and legendary prophetess in history!"
    
    show char_ernust inquiet right at speakingAnim(0.35,1.05,1.0,0.55)
    
    e "Oh, I'm so sorry Wafflid!"
    e "What are we going to do?"
    
    show char_ernust inquiet right at notSpeakingAnim(0.35,1.04,1.0,0.55)
    play sound "sfx/Voices/Player/Char_Player_Normal_02.ogg"
    y "You know what... I'll just make up a prophecy!"
    y "They will never be able to tell the difference!"
    y "Don't move from here!"
    
    hide screen datingSim
    
    window hide 
    
    $ renpy.music.set_volume(0, delay=1, channel='music2')
    stop ambiance fadeout 1.5
    
    scene bg_tour :
        xpos 0 ypos 0
        linear 1.75 xpos 0 ypos -960
    show vel morte :
        xpos 0 ypos 0
        linear 1.75 xpos 0 ypos -960
    show char_ernust inquiet right :
        xalign 0.5 yalign 0.8
        xpos 0.35 ypos 0.94 zoom 0.55
        linear 2.0 xpos 0.36 ypos -0.59
    show char_crossfit colere right :
        xalign 0.5 yalign 0.8
        xpos 0.20 ypos 3.0 zoom 0.32
        linear 1.75 xpos 0.26 ypos 0.84
    show char_brutal normal:
        xalign 0.5 yalign 0.8
        xpos 0.81 ypos 3.0 zoom 0.32
        linear 1.75 xpos 0.75 ypos 0.92
        
    play sound "sfx/SFX_Stairs_02.ogg"   
    $ renpy.pause(2, hard = True)
    
    jump tourVeleda_HistoireBrevetPart2
    
# -----------------------------------------#
    
label tourVeleda_HistoireBrevetPart2:


    $ renpy.music.play("ambiances/AMB_Lieu_Antichambre_01.ogg", channel = "ambiance", loop = True, fadein = 1)
    
    show char_brutal normal at notSpeakingAnim(0.75, 0.92,1.02,0.32)

    
    show char_crossfit colere right at speakingAnim(0.26,0.94,0.92,0.32)
    
    play sound "sfx/Voices/Crossfit/Char_Crossfit_Colere_02.ogg"
    cross "Ah, finally! Talk, servant."
    
    show char_crossfit colere right at notSpeakingAnim(0.26,0.94,0.92,0.32)
    y "Gentlemen! The divine Veleda has consulted the gods, and passed onto me the prophecy!"
    
    menu :
        y "{cps=0}Gentlemen! The divine Veleda has consulted the gods, and passed onto me the prophecy!{/cps}"
        "Crossfitrichernvald has suffered injustice!" :
            $ Acte1_Tour_CoupableJugement = "Brutalmund"
            $ interlocuteur = "cross_char"
    
            show screen datingSim(cross_char, 0.35, 0.27)
            
            y "Brutalmund must pay reparations!"
            
            $ loveGauge(cross_char, 5, 0.45, 0.27)
            
            play sound "sfx/Voices/Crossfit/Char_Crossfit_Serieux_02.ogg"
            show char_crossfit serieux at speakingAnim(0.26,0.94,0.92,0.32)   
            cross "Aha! Justice is sweet!"
            show char_crossfit colere right at notSpeakingAnim(0.26,0.94,0.92,0.32)
            
            $ interlocuteur = "brut_char"
    
            show screen datingSim(brut_char, 0.63, 0.29)
            
            
            show char_brutal colere at speakingAnim(0.75, 1.05,1.02,0.32)
            play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere1_03.ogg"
            brut "What kinda story is that?"
            show char_brutal normal at notSpeakingAnim(0.75, 1.05,1.02,0.32)
            
            y "Brutlamund must give Crossfritrichernvald two buffalos!"
            
            $ loveGauge(brut_char, -5, 0.73, 0.29)
            
            show char_brutal surpris at speakingAnim(0.75, 1.05,1.02,0.32)
            play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Choc_01.ogg"
            brut "Two whole buffalos? There something wrong with ya' head?"
            show char_brutal normal at notSpeakingAnim(0.75, 1.05,1.02,0.32)
            
            play sound "sfx/Voices/Crossfit/Char_Crossfit_Inquiet_03.ogg"
            show char_crossfit inquiet at speakingAnim(0.26,0.94,0.92,0.32)
            cross "Buff... buffalos?"
            
        "Brutalmund has been unjustly accused!":
            $ Acte1_Tour_CoupableJugement = "Crossfit"
            
            $ interlocuteur = "brut_char"
    
            show screen datingSim(brut_char, 0.63, 0.29)
            
            y "The gods are insulted by this baseless accusation!"
            
            $ loveGauge(brut_char, 5, 0.73, 0.29)
            
            show char_brutal heureux at speakingAnim(0.75, 1.05,1.02,0.32)
            play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Heureux_02.ogg"
            brut "Haha! I knew it!"
            show char_brutal normal at notSpeakingAnim(0.75, 1.05,1.02,0.32)
            
            $ interlocuteur = "cross_char"
    
            show screen datingSim(cross_char, 0.35, 0.27)
            
            play sound "sfx/Voices/Crossfit/Char_Crossfit_Choc_01.ogg"
            show char_crossfit choc right at speakingAnim(0.26,0.94,0.92,0.32) 
            cross "What a scandal!"
            show char_crossfit colere right at notSpeakingAnim(0.26,0.94,0.92,0.32)
            $ loveGauge(cross_char, -5, 0.45, 0.27)
            y "Crossfitrichernvald must give Brutalmund two buffalos, as a booking fee!"
            show char_brutal normal at speakingAnim(0.75, 1.05,1.02,0.32)
            play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere2_03.ogg"
            brut "Buffalos? Bah ! I got's tons of 'em already."
            show char_brutal normal at notSpeakingAnim(0.75, 1.05,1.02,0.32)
            
            play sound "sfx/Voices/Crossfit/Char_Crossfit_Inquiet_03.ogg"
            show char_crossfit inquiet at speakingAnim(0.26,0.94,0.92,0.32)
            cross "Buff... buffalos?"
    
    
    show char_crossfit inquiet at notSpeakingAnim(0.26,0.94,0.92,0.32)
    y "The prophetess has spoken, gentlemen!"
    
    hide screen datingSim
    
    y "Pray, now, gentlemen, get yourselves out of here!"
    
 #   play sound "sfx/SFX_Walk_02.ogg"
 
    show char_crossfit inquiet :
        xalign 0.5 yalign 0.8
        xpos 0.26 ypos 0.94 zoom 0.32 rotate -12
        linear 1.8 xpos 2.0 ypos 0.94
    show char_brutal normal:
        xalign 0.5 yalign 0.8
        xpos 0.75 ypos 1.05 zoom 0.32 rotate 8
        linear 2.0 xpos 2.0 ypos 1.05
    
    
    y "Come on, hop hop hop!"
    
    pause 0.5

    y "Well then. Let's go to the tavern! All this excitement made me thirsty!"
    y "And I can see Ingrid again!"
    
    stop music1 fadeout 1.5
    stop music2 fadeout 1.5
    stop ambiance fadeout 0.5
    
    jump narration_ellipse02
    #jump tourVeleda_MarryingIngridPart2
    
# -----------------------------------------#

label tourVeleda_MarryingIngridPart2:
    scene bg_place:
        zoom 1 xanchor 0.0 yanchor 0.0
        easein 2.0 xpos -2000 ypos -150 zoom 2.5
    
    $ renpy.music.play("music/MUSIC_Main_CarteVillage.ogg", channel = "music1", loop = True, fadein = 1)
    $ renpy.music.play("ambiances/AMB_Lieu_CarteVillage_01.ogg", channel = "ambiance", loop = True, fadein = 1)
    pause 2.0
    show char_ernust normal right :
        xalign 0.5 yalign 0.8
        zoom 0.7 xpos 0.2 ypos 1.5
        easein 0.8 xpos 0.4 ypos 0.94 
    pause 0.8
    play sound "sfx/Voices/Player/Char_Player_Hesitation_02.ogg"
    y "Quick Ernust! Go ahead and prepare the Veledapuppet!"
    show char_ernust normal right at speakingAnim(0.4, 1.03, 1.01, 0.7)
    play sound "sfx/Voices/Ernust/Char_Ernust_Joyeux_03.ogg"
    e "Sir, yes, sir, Wafflid!"
    show char_ernust normal right :
        xalign 0.5 yalign 0.8
        zoom 0.7 xpos 0.4 ypos 1.03
        easeout 0.8 xpos 1.5
    pause 0.8
    hide char_ernust
    
    show char_ingrid normal right :
        xalign 0.5 yalign 0.8
        zoom 0.25 xpos 0.2 ypos 1.5
        easein 0.8 xpos 0.4 ypos 1.06
    pause 0.8
    show char_ingrid love at speakingAnim(0.4, 1.16, 1.14, 0.25)
    play sound "sfx/Voices/Ingrid/Char_Ingrid_Love_02.ogg"
    i "Oh my dear Wafflid! We can finally get married!"
    i "Veleda must be waiting to give us her blessing."
    show char_ingrid love:
        xalign 0.5 yalign 0.8
        zoom 0.25 xpos 0.4 ypos 1.18
        easeout 0.8 xpos 1.5
    pause 0.8

    
    stop music1 fadeout 1.5
    stop ambiance fadeout 0.5
    
    scene vel mario2 with Dissolve(1.5) 
    $ renpy.music.play("music/MUSIC_Tour_Antichambre.ogg", channel = "music1", loop = True, fadein = 1)
    $ renpy.music.play("ambiances/AMB_Lieu_Antichambre_01.ogg", channel = "ambiance", loop = True, fadein = 1)

    show char_veledaernust 01 at speakingAnim(0.8, 0.78, 0.76, 0.3) zorder 2:

    show char_ingrid normal zorder 2:
        xalign 0.5 yalign 0.8 zoom 0.25
        xpos 0.0 ypos 1.5
        linear 1.5 xpos 0.15 ypos 1.16
    pause 2.0
    play sound "sfx/Voices/Ernust/Char_Ernust_Marionnette_04.ogg"
    ve "We are gathered together on this blessed day to celebrate..."
    show vel mario zorder 1 with Dissolve(0.5) 
    pause 0.5
    show vel mario2 zorder 1 with Dissolve(0.5) 
    show char_veledaernust 02 at speakingAnim(0.8, 0.78, 0.76, 0.3) zorder 2:
    play sound "sfx/Voices/Ernust/Char_Ernust_Trahi_02.ogg"
    e "Hey! She won't stop moving!"
    play sound "sfx/Voices/Player/Char_Player_Hesitation_02.ogg"
    y "Moving?!"
    
    show vel normal zorder 1 with hpunch
    show char_veledaernust 02:
        xalign 0.5 yalign 0.8
        zoom 0.3 xpos 0.8 ypos 0.78
        linear 0.6 xpos 2.0 ypos 1.0
    play sound "sfx/Voices/Veleda/Char_Veleda_rage_01.ogg"
    v "Ernust! What are you doing?!"
    v "Release us immediately!"
    
    show char_ingrid choc at speakingAnim(0.15, 1.22, 1.20, 0.25)
    play sound "sfx/Voices/Ingrid/Char_Ingrid_Choc_01.ogg"
    i "Ernust! Were you pretending to be Veleda ?"
    i "How shocking! You have disrespected our most valued traditions!"
    
    show char_ingrid choc at notSpeakingAnim(0.15, 1.22, 1.20, 0.25)
    show vel normal2 zorder 1
    show char_ernust inquiet left zorder 2:
            xalign 0.5 yalign 0.8
            xpos 1.0 ypos 1.9 zoom 0.7 rotate -15
            linear 0.8 xpos 0.9 ypos 1.13
    pause 1.2
    
    
    play sound "sfx/Voices/Ernust/Char_Ernust_Inquiet_01.ogg"
    e "Oh snap Wafflid, we got caught!"
    show char_ingrid choc at speakingAnim(0.15, 1.22, 1.20, 0.25)
    i "Wafflid?! You knew about this?!"
    show char_ingrid choc at notSpeakingAnim(0.15, 1.22, 1.20, 0.25)
    y "Ernust! You told me she was dead!"
    jump ending_AskErnust

# -----------------------------------------#

label ending_AskErnust:

    show char_ernust inquiet left at speakingAnim(0.9, 1.18, 1.16, 0.7)
    e "Yeah! I really focused but I couldn't feel her pulse."
    e "There was a weird dried onion smell but that's it."
    show char_ernust inquiet left at notSpeakingAnim(0.9, 1.18, 1.16, 0.7)
    show char_ingrid choc at speakingAnim(0.15, 1.22, 1.20, 0.25)
    i "Wafflid, tell me what's going on!"
    show char_ingrid choc at notSpeakingAnim(0.15, 1.22, 1.20, 0.25)
    menu :
        i "{cps=0}Wafflid, tell me what's going on!{/cps}"
        "It wasn't me! It was all Ernust!":
            jump ending_ErnustPart1
        "Ingrid, I have to tell you the truth..." :
            jump ending_Admit
        "The real culprit here is... the goat!" :
            jump ending_ChevrePart1

# -----------------------------------------#
label ending_ChevrePart1 :
    
    play sound "sfx/Voices/Player/Char_Player_Non_02.ogg"
    y "Don't listen to him Ingrid!"
    y "The only criminal here is Josiane, the goat. I'm sure of it!"
    show char_goat normal zorder 2:
        xalign 0.5 yalign 0.8
        zoom 0.45 xpos 0.5 ypos 1.5
        easein 0.8 ypos 0.85
    play sound "sfx/Voices/Chevre/Char_Chevre_Choc1_01.ogg"
    goat "Bêêêêêêêêêêêêh !"
    show char_ingrid choc at speakingAnim(0.15, 1.22, 1.20, 0.25)
    i "Josiane?! Really?!"
    show char_ingrid choc at notSpeakingAnim(0.15, 1.22, 1.20, 0.25)
    show char_beaudrik choque right zorder 2:
        xalign 0.5 yalign 0.8 zoom 0.8
        xpos -0.2 ypos 0.88
        easein 0.8 xpos 0.2
    show char_ingrid choc:
        linear 0.8 xpos 0.1
    show char_goat normal:
        xpos 0.5
        linear 0.8 xpos 0.6
    play sound "sfx/Voices/Beaudrik/Char_Beaudrik_Choc_01.ogg"
    bg "Josiane?! How could you?!"
    bg "After everything we've been through!"
    play sound "sfx/Voices/Chevre/Char_Chevre_Love_03.ogg"
    show char_goat choc at speakingAnim(0.6, 0.88, 0.86, 0.45)
    goat "Bêêêêêêêêh..."
    show char_goat choc at notSpeakingAnim(0.6, 0.88, 0.86, 0.45)
    play sound "sfx/Voices/Veleda/Char_Veleda_Normal_02.ogg"
    v "Josiane, the facts are clear."
    v "I have no other choice than condemn you to exile..."
    play sound "sfx/Voices/Chevre/Char_Chevre_Normal_01.ogg"
    show char_goat choc at speakingAnim(0.6, 0.88, 0.86, 0.45)
    goat "Bêêêêêêêêêêh !"
    show char_goat normal at notSpeakingAnim(0.6, 0.88, 0.86, 0.45)
    play sound "sfx/Voices/Beaudrik/Char_Beaudrik_Humilie_01.ogg"
    show char_beaudrik insulte at speakingAnim(0.18, 0.98, 0.96, 0.8)
    bg "Goodbye, Josiane..."
    bg "My dear..."

    stop music1 fadeout 1.5
    stop ambiance fadeout 0.5

jump ending_ChevreTrahie
# -----------------------------------------#
label ending_Admit :
    
    y "Ingrid, I have to tell you the truth..."
    y "Ernust and I are guilty!"
    play sound "sfx/Voices/Ingrid/Char_Ingrid_Choc_01.ogg"
    show char_ingrid choc at speakingAnim(0.15, 1.22, 1.20, 0.25)
    i "Oh! My brand new fiancé!"
    i "How could you? What sadness!"
    i "I had gotten so attached to you since you gave me a {b}glaive{/b} and a {b}shield{/b} !"
    show char_ingrid normal at notSpeakingAnim(0.15, 1.22, 1.20, 0.25)
    play sound "sfx/Voices/Veleda/Char_Veleda_Normal_04.ogg"
    v "Wafflid! How dare you spit on our traditions this way?"
    v "Your punishment shall be..."
    play sound "sfx/SFX_Drama_01.ogg"
    pause 0.5
    v "Exile!"
    
    stop music1 fadeout 1.5
    stop ambiance fadeout 0.5
    
jump ending_ExilPart1
# -----------------------------------------#
label ending_ErnustPart1 :
    
    play sound "sfx/Voices/Player/Char_Player_Non_02.ogg"
    y "I didn't do anything! It was Ernust, he is guilty!"
    play sound "sfx/Voices/Ernust/Char_Ernust_Trahi_01.ogg"
    show char_ernust inquiet left at speakingAnim(0.9, 1.18, 1.16, 0.7)
    e "Oh bah... but... Wafflid!"
    show char_ernust inquiet left at notSpeakingAnim(0.9, 1.18, 1.16, 0.7)
    show char_ingrid degout at speakingAnim(0.15, 1.22, 1.20, 0.25)
    i "Ernust... he seemed so innocent..."
    show char_ingrid degout at notSpeakingAnim(0.15, 1.22, 1.20, 0.25)
    play sound "sfx/Voices/Veleda/Char_Veleda_Normal_03.ogg"
    v "Ernust, you have ridiculed our traditions."

    v "It is with great pleasure that we condemn you to..."
    play sound "sfx/SFX_Drama_01.ogg"
    v "Exile!"
    play sound "sfx/Voices/Ernust/Char_Ernust_Trahi_02.ogg"
    show char_ernust inquiet left at speakingAnim(0.9, 1.18, 1.16, 0.7)
    e "Oh no! Where am I going to go?"
    show char_ernust inquiet left at notSpeakingAnim(0.9, 1.18, 1.16, 0.7)
    
    
    scene black with Dissolve(1.5)
    
    stop music1 fadeout 1.5
    stop ambiance fadeout 0.5
    play sound "sfx/Voices/Ernust/Char_Ernust_Normal_06.ogg"
    e "Wafflid... why?"


jump ending_ErnustTrahi
# -----------------------------------------#

label ending_ExilPart1 :
    
    y "Exile!?"
    y "If I must leave, I will go with my best friend!"
    show char_ernust love2:
        xalign 0.5 yalign 0.8 zoom 0.7
        xpos 0.88 ypos 1.16
        easeout 0.8 xpos 0.5 zoom 0.72
    pause 0.8
    show char_ernust love2 at speakingAnim(0.5, 1.16, 1.14, 0.72)
    play sound "sfx/Voices/Ernust/Char_Ernust_Joyeux_04.ogg"
    e "Really?"
    show char_ernust love2 at notSpeakingAnim(0.5, 1.16, 1.14, 0.72)
    menu:
        e "{cps=0}Really?{/cps}"
        "Yes Ernust, let's go!":
            y "Yes Ernust, let's go!"
            show char_ernust love2 at speakingAnim(0.5, 1.18, 1.16, 0.72)
            e "Oh, Wafflid... you're making me so happy!"
            show char_ernust love2 at notSpeakingAnim(0.5, 1.18, 1.16, 0.72)
            stop music1 fadeout 1.5
            stop ambiance fadeout 0.5
            
            jump ending_ExilAvecErnust
            
        "Come on Josiane, we're leaving!":
            y "Let's )go Josiane, we will discover the world together!"
            show char_goat choc zorder 2:
                xalign 0.5 yalign 0.8
                zoom 0.45 xpos 0.75 ypos 1.5
                easein 0.8 ypos 0.85
            pause 0.8
            show char_goat choc at speakingAnim(0.75, 0.88, 0.86, 0.45)
            play sound "sfx/Voices/Chevre/Char_Chevre_Heureux_03.ogg"
            goat "Bêêêêêêêêêêh ?"
            show char_goat choc at notSpeakingAnim(0.75, 0.88, 0.86, 0.45)
            stop music1 fadeout 1.5
            stop ambiance fadeout 0.5
            show char_ernust inquiet left at speakingAnim(0.5, 1.18, 1.16, 0.7)
            play sound "sfx/Voices/Ernust/Char_Ernust_Inquiet_04.ogg"
            e "But... Wafflid?"
            show char_ernust inquiet left at notSpeakingAnim(0.5, 1.18, 1.16, 0.7)
            jump ending_ExilAvecChevre