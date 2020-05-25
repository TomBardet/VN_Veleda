####################################################
# Ici figurent les scènes se déroulant à la Forge. #
####################################################

label forge_BrutalmundEtBeaudrik:
    
    stop music1 fadeout 1
    stop ambiance fadeout 0.5
    
    $ renpy.music.play("ambiances/AMB_Lieu_Forge_01.ogg", channel = "ambiance", loop = True, fadein = 1)
    $ renpy.music.set_volume(0.4, delay=0.4, channel='music1')
    $ renpy.music.set_volume(0, delay=0.4, channel='music2')
    $ renpy.music.set_volume(0.4, delay=0.4, channel='ambiance')

    $ interlocuteur = "brut_char"
    $ interlocuteur = "beau_char"

    if Acte2_Forge_FirstVisit == 0:
        $ forge_cannotpay_check = 0 # Check si on a déjà dit à Brutalmund qu'on ne peut pas payer
        jump forge_Intro
    if Acte2_Forge_FirstVisit == 1:
        jump forge_Brutalmund_Tampon_HUB
        
# ----------------------------------------- #

label forge_Brutalmund_Tampon_HUB:

    scene bg_forge with Dissolve(1.5)
    pause 0.5
    $ renpy.music.play("music/MUSIC_Forge.ogg", channel = "music1", loop = True, fadein = 1)
    show char_brutal normal :
        zoom 0.35 xpos -0.5 ypos 0.05
        linear 0.7 xpos 0.2
    brut "Wafflid !"
    show char_brutal heureux at speakingAnim(0.52, 0.93, 0.91, 0.35)
    play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Heureux_02.ogg"
    brut "So, ya tempted by a brand spanking new {b}Original Captain Germania™ Shield{/b}?"
    show screen datingSim(brut_char, 0.57, 0.15)
    jump forge_Brutalmund_06_Hub

# -----------------------------------------#

label forge_Intro:
    
    scene bg_forge with Dissolve(1.5)
    #play sound "sfx/Voices/Player/Char_Player_Hesitation_01.ogg"
    #y "Hm... anyone there?"
    
    jump forge_Beaudrik_01

# -----------------------------------------#

label forge_Beaudrik_01:
    $ _window_during_transitions = False
    $ Acte2_Forge_FirstVisit = 1
    show char_beaudrik normal left :
        xalign 0.5 yalign 0.8
        zoom 0.8 xpos 1.5 ypos 0.78
        linear 0.4 xpos 0.8

jump forge_Beaudrik_02
    
# -----------------------------------------#

label forge_Beaudrik_02:
    
    pause 0.5
    show char_beaudrik normal left at speakingAnim(0.8, 0.9, 0.88, 0.8)
    play sound "sfx/Voices/Beaudrik/Char_Beaudrik_Normal_02.ogg"
    bg "Would you look at that! It's the shorty, Wafflid."
    show screen datingSim(beau_char, 0.75, 0.10)
    
    $ renpy.music.play("music/MUSIC_Forge.ogg", channel = "music1", loop = True, fadein = 1)
    
    #bg "Y'know, I was thinking about yoo."
    #show char_beaudrik normal left at notSpeakingAnim(0.8, 0.9, 0.88, 0.2)
    #play sound "sfx/Voices/Player/Char_Player_Heureux_01.ogg"
    #y "Wow, I'm flattered Beaudrik."
    
    show char_beaudrik mepris left at speakingAnim(0.8, 0.9, 0.88, 0.8)
    $ loveGauge(beau_char, -5, 0.85, 0.10)
    play sound "sfx/Voices/Beaudrik/Char_Beaudrik_Mepris_02.ogg"
    bg "I heard rumours. So you want to marry Ingrid?"
    show char_beaudrik drague right at speakingAnim(0.7, 0.9, 0.88, 0.88)
        #zoom 0.22 xpos 0.4 ypos 0.09
    play sound "sfx/Voices/Beaudrik/Char_Beaudrik_Drague_04.ogg"
    bg "That's hilarious! Ahahahaha."
    show char_beaudrik normal left at speakingAnim(0.8, 0.9, 0.88, 0.8)
        #zoom 0.2 xpos 0.6 ypos 0.09

jump forge_Beaudrik_03_EpouserIngrid
    
#------------------------------------------#

label forge_Beaudrik_03_EpouserIngrid:
    
    #show char_beaudrik normal left at notSpeakingAnim(0.8, 0.9, 0.88, 0.2)
    #menu:
    #    bg "You really hear some hilarious things in the tavern."
    #    "Yeah... really funny" :
    #        y "Well, thankfully they are just rumours."
    #        show char_beaudrik normal left at speakingAnim(0.8, 0.9, 0.88, 0.2)
    #        bg "I know right? I would hate to have to beat your tiny face up."
    #        jump forge_Beaudrik_04
    #    "That's none of your business" :
    #        y "Hey! Whatever happens between Ingrid and I is none of your business!"
    #        show char_beaudrik normal left at speakingAnim(0.8, 0.9, 0.88, 0.2)
    #        bg "Ahahahaha!"
    #        bg "You're really killing me man. You're right, I should play along."
    #        bg "Good thing it's just a rumour."
    #        bg "I would hate to have to beat your tiny face up."
    #        jump forge_Beaudrik_04
    #    "We're getting married for real!" :
    #        y "Hey! Ingrid and I are really going to get married!"
    #        show char_beaudrik normal left at speakingAnim(0.8, 0.9, 0.88, 0.2)
    #        bg "Ahahahaha!"
    #        bg "You're really killing me man. You're right, I should play along."
    #        bg "Good thing it's just a rumour."
    #        bg "I would hate to have to beat your tiny face up."
    #        jump forge_Beaudrik_04
            
    jump forge_Beaudrik_04
        
#------------------------------------------#

label forge_Beaudrik_04:

    show char_beaudrik mepris left at speakingAnim(0.8, 0.9, 0.88, 0.8)
    bg "I'm the one who is going to marry Ingrid, y'know. I have a dowry and everything."
    show char_beaudrik mepris left at speakingAnim(0.8, 0.9, 0.88, 0.8)
    bg "I want to settle down. Have someone to do the dishes for me and give me back massages."
    show char_beaudrik mepris left at speakingAnim(0.8, 0.9, 0.88, 0.8)
    
    play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere1_01.ogg"
    show char_brutal colere:
        xalign 0.5 yalign 0.8
        xpos -0.55 ypos 1.5 zoom 0.2 rotate 45
        linear 0.7 xpos 0.045 ypos 0.7
    pause 1
    brut "{i}Hey, Beaudrik! Ya lazy bum! Come 'ere!{/i}"    
    show char_beaudrik choque left at speakingAnim(0.8, 0.9, 0.88, 0.8)

    show char_brutal colere:
        xalign 0.5 yalign 0.8
        xpos 0.1 ypos 0.6 zoom 0.2 rotate 45
        linear 2.5 xpos -1.0 ypos 1.5

    $ renpy.pause(0.5, hard = True)
    
    show char_beaudrik choque left at speakingAnim(0.8, 0.9, 0.88, 0.8)
    hide char_brutal
    play sound "sfx/Voices/Beaudrik/Char_Beaudrik_Insult_02.ogg"
    bg "Oh no, Dad's calling me! I'm out of here!"
    show char_beaudrik mepris left at speakingAnim(0.8, 0.9, 0.88, 0.8)
    bg "Anyway, I have to take care of something with Josiane... my other fiancée."

jump forge_Beaudrik_06_leaving

#------------------------------------------#

label forge_Beaudrik_05_Josiane:
    
    show char_beaudrik normal left at notSpeakingAnim(0.8, 0.9, 0.88, 0.8)
    menu:
        bg "{cps=0}Anyway, I have to take care of something with Josiane... my other fiancée.{/cps}"
        "Two fiancées? That's messed up!" :
            play sound "sfx/Voices/Player/Char_Player_Non_04.ogg"
            y "Wait a minute... I have to drag Ernust around, and you're picking up girls left and right?"
            show char_beaudrik mepris left at speakingAnim(0.8, 0.9, 0.88, 0.8)
            $ loveGauge(beau_char, -5, 0.85, 0.10)
            play sound "sfx/Voices/Beaudrik/Char_Beaudrik_Mepris_02.ogg"
            bg "I know, I know... it's complicated."
        "You would do that to Ingrid?" :
            play sound "sfx/Voices/Player/Char_Player_Non_04.ogg"
            y "Two girlfriends? That's, like, not cool man, and sort of mean."
            y "Aren't you going to break Ingrid's heart?"
            play sound "sfx/Voices/Beaudrik/Char_Beaudrik_Mepris_02.ogg"
            show char_beaudrik mepris left at speakingAnim(0.8, 0.9, 0.88, 0.8)
            $ loveGauge(beau_char, -5, 0.85, 0.10)
            bg "Erm, well... it's complicated."
        "Brutalmund looks really angry" :
            y "Your father looks like he's going to smack you."
            play sound "sfx/Voices/Player/Char_Player_Normal_03.ogg"
            show char_beaudrik normal left at speakingAnim(0.8, 0.9, 0.88, 0.8)
            play sound "sfx/Voices/Beaudrik/Char_Beaudrik_Mepris_06.ogg"
            bg "Yeah, he got this idea somewhere that I should get a job to earn a living."
            show char_beaudrik mepris left at speakingAnim(0.8, 0.9, 0.88, 0.8)
            bg "But I have girlfriends to take care of."

jump forge_Beaudrik_06_leaving

#------------------------------------------#

label forge_Beaudrik_06_leaving:
    
    show char_beaudrik mepris left at speakingAnim(0.8, 0.9, 0.88, 0.8)
    bg "You're lucky man, you don't have any girl problems like that. I envy you."
    show char_beaudrik normal left at speakingAnim(0.8, 0.9, 0.88, 0.8)
    bg "Well, I'm going. Before my dad gets here."
    show char_beaudrik drague right at speakingAnim(0.7, 0.9, 0.88, 0.88)
        #zoom 0.23 xpos 0.4 ypos 0.09
    hide screen datingSim
    play sound "sfx/Voices/Beaudrik/Char_Beaudrik_Normal_04.ogg"
    bg "See ya!"
    show char_beaudrik drague right :
        zoom 0.88 xpos 0.7 ypos 0.9
        linear 1.0 xpos 1.5
    pause 1
    hide char_beaudrik drague right
    pause 1.0
    play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere1_03.ogg"
    brut "Beaudrik!"
    
    jump forge_Brutalmund_01
    
#------------------------------------------#

label forge_Brutalmund_01:
    
    show char_brutal colere :
        xalign 0.5 yalign 0.8
        zoom 0.35 xpos -0.5 ypos 0.77
        linear 0.7 xpos 0.52
    pause 0.9
    show char_brutal colere at speakingAnim(0.52, 0.93, 0.91, 0.35)
    pause 0.3
    show char_brutal colere at notSpeakingAnim(0.52, 0.93, 0.91, 0.35)
    brut "..."
    show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.35)
    play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere1_02.ogg"
    brut "Well then! I'm looking for one donkey brained muppet and I find another!"
    show char_brutal heureux at speakingAnim(0.52, 0.93, 0.91, 0.35)
    show screen datingSim(brut_char, 0.57, 0.15)
    play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Heureux_02.ogg"
    brut "Ahahahahahahaha!"
    show char_brutal normal
    brut "You seen my son?"

    jump forge_Brutalmund_02
    
#------------------------------------------#

label forge_Brutalmund_02:
    
    show char_brutal normal at notSpeakingAnim(0.52, 0.93, 0.91, 0.35)
    menu:
        brut "{cps=0}You seen my son?{/cps}"
        "Not really, no" :
            y "No, I didn't see him. Why?"
            play sound "sfx/Voices/Player/Char_Player_Non_01.ogg"
            show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.35)
            if Acte1_Tour_CoupableJugement == "Crossfit":
                show char_brutal colere at speakingAnim(0.52, 0.93, 0.91, 0.35)
                play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere1_03.ogg"
                brut "He should be keeping an eye on the {b}shields{/b} while I go pick up the buffalos!"
                show char_brutal colere at speakingAnim(0.52, 0.93, 0.91, 0.35)
                brut "He deserves a punch in the throat, I can tell ya that!"
            if Acte1_Tour_CoupableJugement == "Brutalmund":
                show char_brutal colere at speakingAnim(0.52, 0.93, 0.91, 0.35)
                $ loveGauge(brut_char, -5, 0.57, 0.15)
                play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere1_01.ogg"
                brut "Because of your friend, there, that prophetess, we don't have a single buffalo left!"
                show char_brutal colere at speakingAnim(0.52, 0.93, 0.91, 0.35)
                brut "And all these {b}shields{/b} won't get sold all on their own!"
            #show char_brutal colere at notSpeakingAnim(0.52, 0.93, 0.91, 0.35)
            #play sound "sfx/Voices/Player/Char_Player_Sarcastic_03.ogg"
            #y "You should go look for him, right?"
            #show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.35)
            #play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere1_04.ogg"
            #brut "And leave you here, alone, with my precious {b}shields{/b}?"
            #show char_brutal colere at speakingAnim(0.52, 0.93, 0.91, 0.35)
            #play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere1_03.ogg"
            #brut "No way!"
        "He's at the tavern" :
            play sound "sfx/Voices/Player/Char_Player_Sarcastic_03.ogg"
            y "He was going to tavern, you should be able to catch up."
            show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.35)
            play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere1_04.ogg"
            brut "And leave you here, alone, with my precious {b}shields{/b}??"
            show char_brutal colere at speakingAnim(0.52, 0.93, 0.91, 0.35)
            play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere1_03.ogg"
            brut "No way!"
            #if Acte1_Tour_CoupableJugement == "Crossfit":
                #jump forge_Brutalmund_03
            #if Acte1_Tour_CoupableJugement == "Brutalmund":
                #$ loveGauge(brut_char, -5, 0.57, 0.15)
                #play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere1_02.ogg"
                #brut "Ya alreay robbed me once with that buffalo business! Ha!"

jump forge_Brutalmund_03

#------------------------------------------#

label forge_Brutalmund_03:
    
    show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.35)
    play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere2_02.ogg"
    brut "There's no point anyway. Beaudrik, he's a lost cause."
    show char_brutal colere at speakingAnim(0.52, 0.93, 0.91, 0.35)
    brut "I shoulda thrown him off that cliff when he was born!"
    show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.35)
    brut "That third nipple of his, not a good sign."
    show char_brutal normal at notSpeakingAnim(0.52, 0.93, 0.91, 0.35)
    menu:
        brut "{cps=0}Le troisième téton, c’était pas bon signe.{/cps}"
        "Having three nipples is not a big deal" :
            play sound "sfx/Voices/Player/Char_Player_Non_05.ogg"
            y "It's not his fault if he was born that way."
            y "Deformed children like that need even more love than normal ones."
            show char_brutal colere at speakingAnim(0.52, 0.93, 0.91, 0.35)
            play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere1_02.ogg"
            brut "That's what his mother used to say! It destroyed her!"
        #"How is that a bad sign?" :
            #play sound "sfx/Voices/Player/Char_Player_Normal_01.ogg"
            #y "Really? A third nipple is a bad omen?"
            #show char_brutal colere at speakingAnim(0.52, 0.93, 0.91, 0.35)
            #$ loveGauge(brut_char, -5, 0.57, 0.152)
            #play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere1_02.ogg"
            #brut "Didn't Veleda put anything in that empty gourd you call a head?"
            #show char_brutal colere at notSpeakingAnim(0.52, 0.93, 0.91, 0.35)
            #y "We do prophecies. Extra nipples are not our specialty."
            #show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.35)
            #play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Normal_05.ogg"
            #brut "Alright then, let me explain..."
            #show char_brutal colere at speakingAnim(0.52, 0.93, 0.91, 0.35)
            #play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere1_01.ogg"
            #brut "A third nipple, it's a sign of weakness!"
        "People like that are monsters!" :
            play sound "sfx/Voices/Player/Char_Player_Sarcastic_03.ogg"
            y "Maybe it's not too late. Should I help you find the closest cliff?"
            show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.35)
            $ loveGauge(brut_char, +5, 0.57, 0.15)
            play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere2_04.ogg"
            brut "It's too late now, it had to be done a long time ago."
            brut "I tried dumping him on the other side of the Lippe but he keeps coming back."
        "Does he have any other weird secrets?":
            play sound "sfx/Voices/Player/Char_Player_Sarcastic_03.ogg"
            y "Does your son have any other weird secets?"
            show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.35)
            play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Normal_05.ogg"
            brut "Ha! You want to know his other secrets?"
            
    jump forge_Brutalmund_04

#------------------------------------------#

label forge_Brutalmund_04:
    
    show char_brutal colere at speakingAnim(0.52, 0.93, 0.91, 0.35)
    play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere1_04.ogg"
    brut "We spoiled him, that idiot Beaudrik!"
    brut "He sleeps with a stuffed animal, cuz he's scared of the dark!"
    show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.35)
    play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Normal_05.ogg"
    brut "But, y'know...."
    show char_brutal heureux at speakingAnim(0.52, 0.93, 0.91, 0.35)
    play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Heureux_03.ogg"
    brut "I imagine you need an {b}Original Captain Germania™ Shield{/b}, right?"
    show char_brutal normal at notSpeakingAnim(0.52, 0.93, 0.91, 0.35)
    jump forge_Brutalmund_04_choice
    
#-------------------------------------------#

label forge_Brutalmund_04_choice:
    
    menu:
        brut "{cps=0}I imagine you need an {b}Original Captain Germania™ Shield{/b}, right?{/cps}"
        "{color=#FFFFFF}Is it possible to have a normal shield?{/color}":
            play sound "sfx/Voices/Player/Char_Player_Sarcastic_02.ogg"
            y "Do you have any off-brand ones? I'm trying to stay frugal."
            show char_brutal colere at speakingAnim(0.52, 0.93, 0.91, 0.35)
            if Forge_LeaderPrice_check == 0:  
                $ loveGauge(brut_char, -5, 0.57, 0.15)
                $ Forge_LeaderPrice_check = 1
            play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere1_01.ogg"
            brut "Where d'ya think ya are, little Wafflid. A thrift store?"
            show char_brutal normal at notSpeakingAnim(0.52, 0.93, 0.91, 0.35)
            jump forge_Brutalmund_04_choice
        "Can I try one out first?":
            play sound "sfx/Voices/Player/Char_Player_Sarcastic_03.ogg"
            y "I'm interested, but how do I know if they are any good? What about a test run?"
            show char_brutal surpris at speakingAnim(0.52, 0.93, 0.91, 0.35)
            $ loveGauge(brut_char, -5, 0.57, 0.15)
            play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Choc_01.ogg"
            brut "Ya're breaking my heart there, Wafflid my friend"
            play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Heureux_02.ogg"
            show char_brutal colere at speakingAnim(0.52, 0.93, 0.91, 0.35)
            brut "My {b}Original Captain Germania™ Shields{/b}, they're the bees knees!"
            show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.35)
            brut "Trials are forbidden."
            jump forge_Brutalmund_04_01_Branche_EssaiRoutier
        "I can't pay...":
            jump forge_Brutalmund_05_CannotPay
            
    jump forge_Brutalmund_05_CannotPay

#-----------------------------------------#

label forge_Brutalmund_04_01_Branche_EssaiRoutier:
    
    show char_brutal normal at notSpeakingAnim(0.52, 0.93, 0.91, 0.35)
    menu:
        brut "{cps=0}I can promise you these shields are the best.{/cps}"
        "{color=#FFFFFF}Looks like a scam...{/color}":
            play sound "sfx/Voices/Player/Char_Player_Non_03.ogg"
            y "TAre you trying to scam me?"
            show char_brutal surpris at speakingAnim(0.52, 0.93, 0.91, 0.35)
            if Forge_reply_arnaque == 0:
                $ loveGauge(brut_char, -5, 0.57, 0.15)
                $ Forge_reply_arnaque = 1
            play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Choc_01.ogg"
            brut "Who?! Me?!"
            show char_brutal heureux at speakingAnim(0.52, 0.93, 0.91, 0.35)
            play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Heureux_01.ogg"
            brut "Why waste your time with a trial buddy, when you can just buy them?"
            jump forge_Brutalmund_04_01_Branche_EssaiRoutier
        "I'll buy one from Crossfitrichernvald then.":
            play sound "sfx/Voices/Player/Char_Player_Sarcastic_01.ogg"
            y "I think I'll just buy from Crossfitrichernvald, then!"
            show char_brutal surpris at speakingAnim(0.52, 0.93, 0.91, 0.35)
            play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Choc_01.ogg"
            brut "What? That dirty Batave accuses me of theft, AND he's stealing my customers?!"
            show char_brutal colere at speakingAnim(0.52, 0.93, 0.91, 0.35)
            play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere1_02.ogg"
            brut "Ha! That's enough Wafflid, I tell ya. I'm done with this!"
            brut "I'm gonna tell him what's on my mind."
            show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.35)
            hide screen datingSim
            brut "Don't move, I'll be right back."
            show char_brutal normal :
                zoom 0.35 xpos 0.5 ypos 0.9
                linear 3.0 xpos -1.5
            pause 0.7
            show char_brutal colere:
                xalign 0.5 yalign 0.8
                xpos -0.5 ypos 2.0 zoom 0.35 rotate 30
                linear 0.7 xpos 0.1 ypos 1.1
            pause 0.5
            play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere1_03.ogg"
            brut "Don't touch anything!"
            show char_brutal colere:
                xalign 0.5 yalign 0.8
                xpos 0.1 ypos 1.1 zoom 0.35 rotate 30
                linear 1.0 xpos -1.0 ypos 2.0
            pause 1.5
            hide char_brutal
            jump forge_Brutalmund_07_Bouclier
            
        "I can't pay…":
            jump forge_Brutalmund_05_CannotPay
        

#------------------------------------------#

label forge_Brutalmund_05_CannotPay:

    show char_brutal normal at notSpeakingAnim(0.52, 0.93, 0.91, 0.35)
    play sound "sfx/Voices/Player/Char_Player_Hesitation_02.ogg"
    y "I don't have a penny."
    show char_brutal surpris at speakingAnim(0.52, 0.93, 0.91, 0.35)
    play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Normal_05.ogg"
    brut "No money at all? C'mon Wafflid, I haven't sold anything in two months!"

    $ Acte2_Forge_FirstVisit = 1

jump forge_Brutalmund_06_Hub

#------------------------------------------#

label forge_Brutalmund_06_Hub:
    show char_brutal normal at notSpeakingAnim(0.52, 0.93, 0.91, 0.35)
    
    menu:
        brut "{cps=0}No money at all? C'mon Wafflid, I haven't sold anything in two months!{/cps}"
        
        "{color=#FFFFFF}What do you want in exchage?{/color}":
            play sound "sfx/Voices/Player/Char_Player_Normal_03.ogg"
            y "I don't have any money, but maybe we can trade?"
            show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.35)
            if Acte1_Tour_CoupableJugement == "Brutalmund":
                play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Normal_06.ogg"
                brut "Well, if you can find two buffalos for me... I've lost mine ya know…"
                show char_brutal normal at notSpeakingAnim(0.52, 0.93, 0.91, 0.35)
                y "Do you really think I have extra buffalos lying around?"
                show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.35)
                brut "They don't exactly have to be your own buffalos, eh!"
                brut "C'mon Wafflid. You're a bit dense but I'm sure you can figure it out..."
            if Acte1_Tour_CoupableJugement == "Crossfit":
                show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.35)
                play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Normal_06.ogg"
                brut "Crossfitman hasn't brought me my buffalos yet."
                brut "If you can accelerate things... maybe we can make a deal."
                show char_brutal heureux at speakingAnim(0.52, 0.93, 0.91, 0.35)
            play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Heureux_03.ogg"
            brut "Bring me my buffalos and you can have an {b}Original Captain Germania™ shield{/b} !"
            jump forge_Brutalmund_06_Hub
        
        "Your buffalos are free" if _testLunettes == 1:
            play sound "sfx/Voices/Player/Char_Player_Heureux_01.ogg"
            y "I got your buffalos back."
            show char_brutal heureux at speakingAnim(0.52, 0.93, 0.91, 0.35)
            $ loveGauge(brut_char, +10, 0.57, 0.15)
            play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Heureux_01.ogg"
            brut "Aha, you finally make yourself useful!"
            #show char_brutal normal at notSpeakingAnim(0.52, 0.93, 0.91, 0.4)
            #y "Well, sort of..."
            #show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.4)
            #brut "What does that mean?"
            #show char_brutal normal at notSpeakingAnim(0.52, 0.93, 0.91, 0.4)
            play sound "sfx/Voices/Player/Char_Player_Sarcastic_02.ogg"
            y "I freed them from the stables, you have to go get them now... Wherever they are."
            show char_brutal heureux at notSpeakingAnim(0.52, 0.93, 0.91, 0.35)
            pause 1.0
            show char_brutal surpris at notSpeakingAnim(0.52, 0.93, 0.91, 0.35)
            pause 1.0
            show char_brutal colere at speakingAnim(0.52, 0.93, 0.91, 0.35)
            $ loveGauge(brut_char, -15, 0.57, 0.15)
            play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere1_04.ogg"
            brut "You're really not any good are ya?"
            hide screen datingSim
            brut "Don't move, I'll go and look for them!"
            show char_brutal normal :
                zoom 0.35 xpos 0.5 ypos 0.9
                linear 3.0 xpos -1.5
            pause 0.7
            show char_brutal colere:
                xalign 0.5 yalign 0.8
                xpos -0.5 ypos 2.0 zoom 0.35 rotate 30
                linear 0.7 xpos 0.1 ypos 1.1
            pause 0.5
            play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere1_02.ogg"
            brut "And don't touch anything! No shield for you as long as I haven't got my buffalos!"
            show char_brutal colere:
                xalign 0.5 yalign 0.8
                xpos 0.1 ypos 1.1 zoom 0.35 rotate 30
                linear 1.0 xpos -1.0 ypos 2.0
            pause 1.5
            hide char_brutal
            jump forge_Brutalmund_07_Bouclier
            
        "I'll be back when I can pay." if _testLunettes == 0:
            play sound "sfx/Voices/Player/Char_Player_Non_01.ogg"
            y "I have nothing to give you..."
            show char_brutal colere at speakingAnim(0.52, 0.93, 0.91, 0.35)
            if forge_cannotpay_check == 0:
                $ loveGauge(brut_char, -5, 0.57, 0.15)
                $ forge_cannotpay_check = 1
            play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere1_01.ogg"
            brut "Get out then, I've got work to do."
            hide screen datingSim

            stop music1 fadeout 1.5
            stop ambiance fadeout 0.5

            jump PlaceDuVillageDefault

#---------------------------------------------------#

label forge_Brutalmund_07_Bouclier:

    stop music1 fadeout 1.5
    
    hide  char_brutal
    outline "And so, Brutalmund left his station." 
    outline "Using this time to steal a {b}shield{/b} would be completely despicable!"
    play sound "sfx/Voices/Player/Char_Player_Heureux_03.ogg"
    y "Hey, you're right! Great idea."
    $ inventory.add(bouclier)
    $ _testBouclier = 1
    show img_bouclier at center:
        xalign 0.7 yalign 0.9 zoom 0.3
        linear 0.5 yalign 0.7 zoom 0.7
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
        
    $renpy.pause(0.5, hard = True)
    
    play sound "sfx/SFX_UI_Bouclier_01.ogg"
    $renpy.pause(1.8, hard = True)
    play sound "sfx/SFX_UI_Inventory_Bag_01.ogg"
    $renpy.pause(0.2, hard = True)
    
    stop ambiance fadeout 0.5

    if _testGlaive == 1 & _testBouclier == 1:
        jump PlaceDuVillageAllObjects
    else:
        jump PlaceDuVillageDefault
    
#--------Backup Conditions et Variables-------------#

#    if _testBlague == 1:
#        menu:
#            "Back to village":
#                jump PlaceDuVillageDefault
#            "Give the joke":
#                jump forge_BrutalMundBlaguePart2
#    else:
#        "No joke..."
#        jump PlaceDuVillageDefault

# -----------------------------------------#

#label forge_BrutalMundBlaguePart2:
#    "Entrée forge_BrutalMundBlaguePart2"
#    
#    $ inventory.add(bouclier)
#    $ _testBouclier = 1
#    
#    "Shield get"
#    
#    if _testGlaive == 1 & _testBouclier == 1:
#        jump PlaceDuVillageAllObjects
#    else:
#        jump PlaceDuVillageDefault
    
jump PlaceDuVillageDefault   