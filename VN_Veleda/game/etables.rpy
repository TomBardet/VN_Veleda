#####################################################
# Ici figurent les scènes se déroulant aux étables. #
#####################################################
init:
    define buf = Character("Buffles : ",
        what_suffix=" ",
        ctc=anim.Blink("gui/ctc.png"))
    $  _testCrossfitTalk = 0
    $  _etableDone = 0
    $  _testEtable = 0
    $  _testRomainsTalk = 0
    $  _testBuffaloTalk = 0
label etable_fromPlace:
            
    $ renpy.music.play("music/MUSIC_Etable_Normale.ogg", channel = "music1", loop = True, fadein = 1)
    $ renpy.music.play("music/MUSIC_Etable_Panique.ogg", channel = "music2", loop = True, fadein = 1)
    $ renpy.music.play("ambiances/AMB_Lieu_Etable_Normal_01.ogg", channel = "ambiance", loop = True, fadein = 1)
    
    $ renpy.music.set_volume(0.4, delay=0, channel='music1')
    $ renpy.music.set_volume(0, delay=0, channel='music2')
    $ renpy.music.set_volume(0.4, delay=0, channel='ambiance')
    
    scene bg_etables with Dissolve(1.5):
        zoom 0.70
    jump etables_PeurDesBufflesPart1
label etables_PeurDesBufflesPart1:
    $ _window_during_transitions = False
    scene bg_etables:
        zoom 0.70
    show char_crossfit inquiet right at notSpeakingAnim(0.7, 0.77, 0.8, 0.27)
    #$ _testTrompette = 1
    if _testTrompette == 1:
        if _testCrossfitTalk == 1:
            $ _testEtable = 1
    window show
    if _testEtable == 1:
        $ _return = renpy.call_screen("action_choice_EtableTrumpet")
        if _return == "trompette":
            jump etables_PeurDesBufflesPart2
        elif _return == "buffles":
            play sound "sfx/SFX_Buffle_Dialogue.ogg"
            if _testBuffaloTalk <= 6:
                 buf "Moooooo!"
                 y "That's right!"
                 $ _testBuffaloTalk += 1
                 jump etables_PeurDesBufflesPart1
            else:
                 buf "Moomoomoo!"
                 buf "Moooooooooooo!"
                 y "Let's just agree to disagree."
                 play sound "sfx/SFX_Buffle_Dialogue.ogg"
                 buf "Moo!"
                 $ _testBuffaloTalk = 0
                 jump etables_PeurDesBufflesPart1
        elif _return == "crossfit":
            scene bg_etables:
                zoom 0.7
                linear 0.5 zoom 0.75 xpos -0.1
            show char_crossfit inquiet right:
                xalign 0.5 yalign 0.8 zoom 0.27
                xpos 0.7 ypos 0.77
                linear 0.5 zoom 0.28 xpos 0.65 ypos 0.76
            pause 0.5
            if _testCrossfitTalk == 0:
                jump etables_PeurDesBufflesPart1bis
            else:
                jump etables_PeurDesBufflesPart1boucle
        elif _return == "sortir":
            y "Let's go back to the village..."
            jump PlaceDuVillageDefault

    else:
        $ _return = renpy.call_screen("action_choice_Etable")
        if _return == "buffles":
            play sound "sfx/SFX_Buffle_Dialogue.ogg"
            if _testBuffaloTalk <= 6:
                 buf "Moooooo!"
                 y "That's right!"
                 $ _testBuffaloTalk += 1
                 jump etables_PeurDesBufflesPart1
            else:
                 buf "Moomoomoo!"
                 buf "Moooooooooooo!"
                 y "Let's just agree to disagree."
                 play sound "sfx/SFX_Buffle_Dialogue.ogg"
                 buf "Moo!"
                 $ _testBuffaloTalk = 0
                 jump etables_PeurDesBufflesPart1
        elif _return == "crossfit":
            scene bg_etables:
                zoom 0.7
                linear 0.5 zoom 0.75 xpos -0.1
            show char_crossfit inquiet right:
                xalign 0.5 yalign 0.8 zoom 0.27
                xpos 0.7 ypos 0.77
                linear 0.5 zoom 0.28 xpos 0.65 ypos 0.76
            pause 0.5
            if _testCrossfitTalk == 0:
                jump etables_PeurDesBufflesPart1bis
            else:
                jump etables_PeurDesBufflesPart1boucle
        elif _return == "sortir":
            y "Let's go back to the village..."
            jump PlaceDuVillageDefault

# -----------------------------------------#

label etables_PeurDesBufflesPart1bis:
    
    show screen datingSim(cross_char, 0.45, .27)
    play sound "sfx/Voices/Player/Char_Player_Normal_01.ogg"
    y "Hello there! So, how are the buffalos doing?"
    show char_crossfit inquiet right at speakingAnim(0.65, 0.84, 0.82, 0.28)
    cross "..."
    show char_crossfit inquiet right at notSpeakingAnim(0.65, 0.84, 0.82, 0.28)

    show char_crossfit inquiet right at notSpeakingAnim(0.65, 0.84, 0.82, 0.28)
    y "... ?"
    show char_crossfit inquiet right at speakingAnim(0.65, 0.84, 0.82, 0.28)
    cross "..."
    show char_crossfit inquiet right at notSpeakingAnim(0.65, 0.84, 0.82, 0.28)
    menu:
        cross "{cps=0}...{/cps}"
        "You're not looking too good, you know?":
            play sound "sfx/Voices/Player/Char_Player_Sarcastic_02.ogg"
            y "You're not looking too good, you know?"
            $ loveGauge(cross_char, -4, 0.44, 0.27)
            show char_crossfit inquiet right at speakingAnim(0.65, 0.84, 0.82, 0.28)
            play sound "sfx/Voices/Crossfit/Char_Crossfit_Inquiet_01.ogg"
            cross "They... they are still here!"
        "Happy with your buffalos?" if Acte1_Tour_CoupableJugement=="Brutalmund":
            play sound "sfx/Voices/Player/Char_Player_Normal_03.ogg"
            y "Happy with your buffalos?"
            $ loveGauge(cross_char, -4, 0.44, 0.27)
            show char_crossfit inquiet right at speakingAnim(0.65, 0.84, 0.82, 0.28)
            play sound "sfx/Voices/Crossfit/Char_Crossfit_Inquiet_01.ogg"
            cross "They... they are still here!"
        "Did you deliver the buffalos to Brutalmund?" if Acte1_Tour_CoupableJugement=="Crossfit":
            play sound "sfx/Voices/Player/Char_Player_Normal_03.ogg"
            y "... so, did you deliver the buffalos to Brutalmund?"
            $ loveGauge(cross_char, -4, 0.44, 0.27)
            show char_crossfit inquiet right at speakingAnim(0.65, 0.84, 0.82, 0.28)
            play sound "sfx/Voices/Crossfit/Char_Crossfit_Inquiet_01.ogg"
            cross "They... they are still here!"
        "You were a lot more talkative back in the tower":
            play sound "sfx/Voices/Player/Char_Player_Sarcastic_01.ogg"
            y "You know, you had a lot more to say to the prophetess..."
            $ loveGauge(cross_char, -4, 0.44, 0.27)
            show char_crossfit inquiet right at speakingAnim(0.65, 0.84, 0.82, 0.28)
            play sound "sfx/Voices/Crossfit/Char_Crossfit_Inquiet_01.ogg"
            cross "It's... it's just that..."
            cross "They are still here!"
    show char_crossfit inquiet right at notSpeakingAnim(0.65, 0.84, 0.82, 0.28)
    play sound "sfx/Voices/Player/Char_Player_Normal_01.ogg"
    y "I beg your pardon?"
    $ loveGauge(cross_char, -6, 0.44, 0.27)
    show char_crossfit inquiet right at speakingAnim(0.65, 0.84, 0.82, 0.28)
    play sound "sfx/Voices/Crossfit/Char_Crossfit_Inquiet_03.ogg"
    cross "The buffalos, you dimwit! They are still here!"
    $ loveGauge(cross_char, -4, 0.44, 0.27)
    show char_crossfit inquiet right at speakingAnim(0.65, 0.84, 0.82, 0.28)
    cross "I opened the door 12 hours ago, and these stupid beasts have not left yet!"
    play sound "sfx/Voices/Player/Char_Player_Normal_01.ogg"
    y "Wait... what do you mean?"
    show char_crossfit pleurs right at speakingAnim(0.65, 0.84, 0.82, 0.28)
    play sound "sfx/Voices/Crossfit/Char_Crossfit_inquiet_02.ogg"
    cross "Shhhhhhhh! They are going to hear you!"
    show char_crossfit pleurs right at notSpeakingAnim(0.65, 0.84, 0.82, 0.28)
    play sound "sfx/Voices/Player/Char_Player_Sarcastic_02.ogg"
    y "Wait, are you afraid of buffalos?"
    $ loveGauge(cross_char, -20, 0.44, 0.27)
    show char_crossfit inquiet right at speakingAnim(0.65, 0.84, 0.82, 0.28)
    play sound "sfx/Voices/Crossfit/Char_Crossfit_Colere_03.ogg"
    cross "What? I dare you to say that again!"
    show char_crossfit inquiet right at notSpeakingAnim(0.65, 0.84, 0.82, 0.28)
    play sound "sfx/SFX_Buffle_Dialogue.ogg"
    buf "Moooooooooo!"
    hide screen datingSim
    show char_crossfit pleurs:
        zoom 0.28 ypos 0.84
        linear 0.4 xpos 0.79 rotate 15 ypos 0.95
    play sound "sfx/Voices/Crossfit/Char_Crossfit_Pleurs_01.ogg"
    cross "Aaaaaaaaaah!"
    show char_crossfit pleurs:
        zoom 0.28 ypos 0.95 xpos 0.79
        linear 0.8 rotate 0 ypos 0.84
    pause 1.2
    show char_crossfit inquiet right at speakingAnim(0.79, 0.84, 0.82, 0.28)
    play sound "sfx/Voices/Crossfit/Char_Crossfit_Colere_02.ogg"
    cross "..."
    cross "Alright, alright! I find buffalos terrifying... Happy now?!"
    show char_crossfit inquiet right at notSpeakingAnim(0.79, 0.84, 0.82, 0.28)
    show char_crossfit inquiet right:
        xalign 0.5 yalign 0.8
        zoom 0.28 xpos 0.79 ypos 0.84
        parallel:
            linear 1.5 xpos -0.5 ypos 0.86
        parallel:
            linear 0.5 rotate -16 
    pause 1.6
    nar "{i}There must be something you can do to help this poor soul...{/i}"
    nar "{i}And it might even help you in your quest...{/i}"
    scene bg_etables:
        zoom 0.75 xpos -0.1
        linear 0.5 zoom 0.7 xpos 0.0
    pause .5
    show char_crossfit inquiet right:
        xalign 0.5 yalign 0.8 zoom 0.28
        xpos 0.7 ypos 1.5
        linear 0.5 zoom 0.27 xpos 0.7 ypos 0.77
    pause .5
    $ _testCrossfitTalk = 1
    jump etables_PeurDesBufflesPart1
    
    
# -----------------------------------------#

label etables_PeurDesBufflesPart1boucle:
    show screen datingSim(cross_char, 0.45, .27)
    play sound "sfx/Voices/Player/Char_Player_Normal_01.ogg"
    y "How's it hanging?"
    show char_crossfit inquiet right at speakingAnim(0.65, 0.84, 0.82, 0.28)
    play sound "sfx/Voices/Crossfit/Char_Crossfit_Inquiet_01.ogg"
    cross "The... the buffalos. They're looking at me..."
    show char_crossfit inquiet right at notSpeakingAnim(0.65, 0.84, 0.82, 0.28)
    y "I'll just leave you to it, alright?"
    hide screen datingSim
    scene bg_etables:
        zoom 0.75 xpos -0.1
        linear 0.5 zoom 0.7 xpos 0.0
    show char_crossfit inquiet right:
        xalign 0.5 yalign 0.8 zoom 0.28
        xpos 0.65 ypos 0.76
        linear 0.5 zoom 0.27 xpos 0.7 ypos 0.77
    pause 0.5
    jump etables_PeurDesBufflesPart1
    
# -----------------------------------------#    
label etables_PeurDesBufflesPart2:
    scene bg_etables:
        zoom 0.7 
        linear 1.0 zoom 0.85 xpos -0.07 ypos -0.02
    show char_crossfit inquiet right:
        xalign 0.5 yalign 0.8 zoom 0.27
        xpos 0.7 ypos 0.77
        linear 0.8 xpos 1.2 
    pause 1.0
    
    $ renpy.music.set_volume(0.3, delay=1, channel='music1')
    $ renpy.music.set_volume(0, delay=0, channel='music2')
    $ renpy.music.set_volume(0.3, delay=1, channel='ambiance')
    
    show char_ernust inquiet left:
        xalign 0.5 yalign 0.8
        xpos 0.65 zoom 0.65 ypos 1.6
        linear 0.4 ypos 0.94
    pause 1.0
    

    show char_ernust inquiet left at speakingAnim(0.65, 1.02, 1.0, 0.65)
    play sound "sfx/Voices/Ernust/Char_Ernust_Inquiet_04.ogg"
    e "Erm... Wafflid, are you sure this is a good idea?"
    show char_ernust inquiet left at notSpeakingAnim(0.65, 1.02, 1.0, 0.65)
    play sound "sfx/Voices/Player/Char_Player_Normal_04.ogg"
    y "I have to use this trumpet somewhere, right?"
    y "I wouldn't just have one for no reason."
    nar "I would be careful if I were you..."
    play sound "sfx/Voices/Player/Char_Player_Normal_02.ogg"
    y "Too late."
    scene black with Dissolve (1.0)
    show screen inventory_screen(obj = "trompette")
    pause 4.0
    
    $ renpy.music.play("ambiances/AMB_Lieu_Etable_Panic_01.ogg", channel = "ambiance", loop = True, fadein = 0.5)
    
    $ renpy.music.set_volume(0.5, delay=0.5, channel='music1')
    $ renpy.music.set_volume(0.5, delay=0.5, channel='music2')
    $ renpy.music.set_volume(0.5, delay=0.5, channel='ambiance')
    
    play sound "sfx/SFX_Trumpet_01.ogg"
    
    pause 1.5
    
    play sound "sfx/SFX_Buffle_Peur.ogg"
    pause 1.0
    hide screen inventory_screen
    window hide
    scene bg_buffles with hpunch:
        zoom 0.7
    pause 1.5
    window show
    show char_crossfit pleursG right:
        zoom 0.3 xalign 0.5 yalign 0.8
        xpos 1.2 ypos 0.84
        linear 1.8 xpos -0.5 rotate -15
    
    play sound "sfx/Voices/Crossfit/Char_Crossfit_Pleurs_01.ogg"
    cross "Heeeeeelp! The buffalos are attacking meeeee!" 
    #scene black with Dissolve(1.0)
    outline "And so the brave sir Crossfitricheridoo ran away, his tail between his legs"
    scene bg_etables2 with Dissolve(1.0):
        zoom 0.7
    show char_ernust normal right:
        xalign 0.5 yalign 0.8
        xpos 0.65 zoom 0.65 ypos 1.6
        linear 0.3 ypos 0.94
    pause 0.3
    show char_ernust normal right at speakingAnim(0.65, 1.02, 1.0, 0.65)
    play sound "sfx/Voices/Ernust/Char_Ernust_Joyeux_03.ogg"
    e "Hey, he dropped his glasses, would you look at that."
    
    show char_ernust normal right at notSpeakingAnim(0.65, 1.02, 1.0, 0.65)
    
    $ inventory.add(lunettes)
    $ _testLunettes = 1
    show img_lunettes at center:
        xalign 0.7 yalign 0.9 zoom 0.3
        linear 0.5 yalign 0.7 zoom 0.4
        easein 0.5 zoom 0.55
        easeout 0.5 zoom 0.4
        pause 0.5
        parallel :
            linear 0.8 yalign 0.05 xalign 0.95 zoom 0.3
        parallel :
            linear 0.9 alpha 0
    pause 0.5
    play sound "sfx/SFX_UI_Lunettes_01.ogg"
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
    pause 0.5
    show char_ernust normal right at speakingAnim(0.65, 1.02, 1.0, 0.65)
    play sound "sfx/Voices/Ernust/Char_Ernust_Normal_07.ogg"
    e "Should we give them back?"
    show char_ernust normal right at notSpeakingAnim(0.65, 1.02, 1.0, 0.65)
    $ _etableDone = 1
    $ renpy.music.play("ambiances/AMB_Lieu_Etable_Panic_01.ogg", channel = "ambiance", loop = True, fadein = 0.5)
    
    stop music1 fadeout 1.5
    stop music2 fadeout 1.5
    stop ambiance fadeout 0.5
    
    pause 0.5
    
    jump PlaceDuVillageDefault
    
# -----------------------------------------#
