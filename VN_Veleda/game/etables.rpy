#####################################################
# Ici figurent les scènes se déroulant aux étables. #
#####################################################
init:
    define buf = Character("Buffles : ",
        what_suffix=" ",
        ctc=anim.Blink("gui/ctc.png"))
    $  _testCrossfitTalk = 0
    $  _testEtable = 0
    $  _testRomainsTalk = 0
    
label etables_PeurDesBufflesPart1:
    scene bg_etablesBuffles:
        zoom 0.70
    show char_crossfit inquietG right at notSpeakingAnim(0.7, 0.77, 0.8, 0.27)
    $ _testTrompette = 1
    if _testTrompette == 1:
        if _testCrossfitTalk == 1:
            $ _testEtable = 1
    if _testEtable == 1:
        $ _return = renpy.call_screen("action_choice_EtableTrumpet")
        if _return == "trompette":
            jump etables_PeurDesBufflesPart2
        elif _return == "buffles":
            buf "Meuuuuuuuh !"
            y "A vos souhaits"
            jump etables_PeurDesBufflesPart1
        elif _return == "crossfit":
            scene bg_etablesBuffles:
                zoom 0.7
                linear 0.5 zoom 0.75 xpos -0.1
            pause 0.5
            if _testCrossfitTalk == 0:
                jump etables_PeurDesBufflesPart1bis
            else:
                jump etables_PeurDesBufflesPart1boucle
        elif _return == "sortir":
            y "Retournons au village..."
            jump PlaceDuVillageDefault

    else:
        $ _return = renpy.call_screen("action_choice_Etable")
        if _return == "buffles":
            buf "Meuuuuuuuh !"
            y "A vos souhaits"
            jump etables_PeurDesBufflesPart1
        elif _return == "crossfit":
            scene bg_etablesBuffles:
                zoom 0.7
                linear 0.5 zoom 0.75 xpos -0.1
            show char_crossfit inquietG right:
                xalign 0.5 yalign 0.8 zoom 0.27
                xpos 0.7 ypos 0.77
                linear 0.5 zoom 0.28 xpos 0.65 ypos 0.76
            pause 0.5
            if _testCrossfitTalk == 0:
                jump etables_PeurDesBufflesPart1bis
            else:
                jump etables_PeurDesBufflesPart1boucle
        elif _return == "sortir":
            y "Retournons au village..."
            jump PlaceDuVillageDefault

# -----------------------------------------#

label etables_PeurDesBufflesPart1bis:
    y "Bonjour ! Alors ces Buffles ?"
    show char_crossfit inquietG right at speakingAnim(0.65, 0.84, 0.82, 0.28)
    cross "..."
    show char_crossfit inquietG right at notSpeakingAnim(0.65, 0.84, 0.82, 0.28)

    show char_crossfit inquietG right at notSpeakingAnim(0.65, 0.84, 0.82, 0.28)
    y "... ?"
    show char_crossfit inquietG right at speakingAnim(0.65, 0.84, 0.82, 0.28)
    cross "..."
    cross "....................."
    show char_crossfit inquietG right at notSpeakingAnim(0.65, 0.84, 0.82, 0.28)
    menu:
        cross "{cps=0}.....................{/cps}"
        "Ca a pas l'air d'aller fort dites moi !":
            y "Ca a pas l'air d'aller fort dites moi !"
            show char_crossfit inquietG right at speakingAnim(0.65, 0.84, 0.82, 0.28)
            cross "Ils...Ils sont toujours là !"
        "Satisfait de vos buffles ?" if Acte1_Tour_CoupableJugement=="Brutalmund":
            y "Alors, satisfait de vos buffles ?"
            show char_crossfit inquietG right at speakingAnim(0.65, 0.84, 0.82, 0.28)
            cross "Ils...Ils sont toujours là !"
        "Vous avez livrés vos buffles à Brutalmund ?" if Acte1_Tour_CoupableJugement=="Crossfit":
            y "... Du coup, vous avez livrés vos buffles à Brutalmund ?"
            show char_crossfit inquietG right at speakingAnim(0.65, 0.84, 0.82, 0.28)
            cross "Ils...Ils sont toujours là !"
        "Vous êtiez plus bavard avec la prophétesse...":
            y "Ben dis donc, vous êtiez plus bavard avec la prophétesse..."
            show char_crossfit inquietG right at speakingAnim(0.65, 0.84, 0.82, 0.28)
            cross "Ca n'a rien à voir ! C'est juste que..."
            cross "Ils...Ils sont toujours là !"
    show char_crossfit inquietG right at notSpeakingAnim(0.65, 0.84, 0.82, 0.28)
    y "Je vous demande pardon ?"
    show char_crossfit inquietG right at speakingAnim(0.65, 0.84, 0.82, 0.28)
    cross "Les buffles crétin ! Ils sont toujours là !"
    show char_crossfit inquietG right at notSpeakingAnim(0.65, 0.84, 0.82, 0.28)
    menu:
        cross "{cps=0}Les buffles crétin ! Ils sont toujours là !{/cps}"
        "Les buffles ont une espérance de vie élevée vous savez ?":
            y "Les buffles ont une espérance de vie assez élevée vous savez ?"
            y "20 ans environ !"
            y "Du coup ils risquent d'être là encore un moment !"
            show char_crossfit inquietG right at speakingAnim(0.65, 0.84, 0.82, 0.28)
            cross "C'EST PAS CA LE PROBLEME !"
            cross "Regardez comme ils m'observent, les yeux imbibés de sang... Brrrr..."
            show char_crossfit inquietG right at notSpeakingAnim(0.65, 0.84, 0.82, 0.28)
            y "Attendez. Quoi ?"
        "Ils étaient censés partir ?":
            y "Mais ils étaient censés partir ?"
            show char_crossfit inquietG right at speakingAnim(0.65, 0.84, 0.82, 0.28)
            cross "Evidemment !"
            cross "Ca fait 12 heures que la porte est ouverte, et ces imbéciles de bovins ne bougent pas d'un poil !"
            cross "Je sais plus quoi faire moi !"
            show char_crossfit inquietG right at notSpeakingAnim(0.65, 0.84, 0.82, 0.28)            
            y "Attendez. Quoi ?"
    show char_crossfit pleursG right at speakingAnim(0.65, 0.84, 0.82, 0.28)
    cross "Chuuuuuuuuuut ! Ils vont vous entendre !"
    show char_crossfit pleursG right at notSpeakingAnim(0.65, 0.84, 0.82, 0.28)
    y "... Mais vous avez peur des buffles ?"
    show char_crossfit inquietG right at speakingAnim(0.65, 0.84, 0.82, 0.28)
    cross "Répète ça et je t'écrase !"
    show char_crossfit inquietG right at notSpeakingAnim(0.65, 0.84, 0.82, 0.28)
    "bruit meuglement meuuuuuuuh"
    show char_crossfit pleursG:
        zoom 0.28 ypos 0.84
        linear 0.4 xpos 0.79 rotate 15 ypos 0.95
    cross "AAAAAAAAAAH !"
    show char_crossfit pleursG right:
        zoom 0.28 ypos 0.95 xpos 0.79
        linear 0.8 rotate 0 ypos 0.84
    pause 0.8
    show char_crossfit inquietG right at speakingAnim(0.79, 0.84, 0.82, 0.28)
    cross "..."
    cross "Bon OK, je trouve les buffles absolument terrifiants, heureux ?!"
    show char_crossfit inquietG right at notSpeakingAnim(0.79, 0.84, 0.82, 0.28)
    show char_crossfit inquietG right:
        xalign 0.5 yalign 0.8
        zoom 0.28 xpos 0.79 ypos 0.84
        parallel:
            linear 1.5 xpos -0.5 ypos 0.86
        parallel:
            linear 0.5 rotate -16 
    pause 1.6
    outline "Il y a forcèment quelquechose à faire pour aider ce pauvre homme..."
    outline "Et qui sait... ça pourrait peut-être t'aider dans ta quête..."
    scene bg_etablesBuffles:
        zoom 0.75 xpos -0.1
        linear 0.5 zoom 0.7 xpos 0.0
    pause .5
    show char_crossfit inquietG right:
        xalign 0.5 yalign 0.8 zoom 0.28
        xpos 0.7 ypos 1.5
        linear 0.5 zoom 0.27 xpos 0.7 ypos 0.77
    pause .5
    $ _testCrossfitTalk = 1
    jump etables_PeurDesBufflesPart1
    
    
# -----------------------------------------#

label etables_PeurDesBufflesPart1boucle:
    y "Alors, tout baigne ?"
    show char_crossfit inquietG right at speakingAnim(0.65, 0.84, 0.82, 0.28)
    cross "... Les... les buffles... Ils me regardent..."
    show char_crossfit inquietG right at notSpeakingAnim(0.65, 0.84, 0.82, 0.28)
    y "Je vais vous laisser hein ?"
    scene bg_etablesBuffles:
        zoom 0.75 xpos -0.1
        linear 0.5 zoom 0.7 xpos 0.0
    show char_crossfit inquietG right:
        xalign 0.5 yalign 0.8 zoom 0.28
        xpos 0.65 ypos 0.76
        linear 0.5 zoom 0.27 xpos 0.7 ypos 0.77
    pause .5
    jump etables_PeurDesBufflesPart1
    
# -----------------------------------------#    
label etables_PeurDesBufflesPart2:
    show char_ernust normal right:
        xalign 0.5 yalign 0.8
        xpos -0.5 zoom 0.75 ypos 0.94
        linear 1.0 xpos 0.15
    pause 1.0
    show char_ernust normal right at speakingAnim(0.15, 0.94, 0.92, 0.75)
    e "Euh... Gaufrid, t'es sur que c'est une bonne idée ?"
    show char_ernust normal right at notSpeakingAnim(0.15, 0.94, 0.92, 0.75)
    y "Il faut bien utiliser cette trompette quelque part non ?"
    nar "J'aurais jamais cru dire ça mais je suis de l'avis d'Ernust sur le coup..."
    y "Trop tard."
    show screen inventory_screen(obj = "trompette")
    "*PFIOUUUUUUU* Bruit de trompette"
    hide screen inventory_screen
    "Scène Clé"
    show char_crossfit colere:
        xalign 0.5 yalign 0.8
        zoom 0.27 xpos 1.5 ypos 0.82
        parallel:
            linear 0.5 xpos 0.56
        parallel:
            linear 0.2 rotate -20
            block:
                linear 0.5 rotate 10
                linear 0.4
                repeat
    cross "AU SECOUUUUUUUUUURS ! LES BUFFLES M'ATTAQUENT !"
    show char_crossfit colere:
        xalign 0.5 yalign 0.8
        zoom 0.27 xpos 0.56 ypos 0.82
        parallel:
            linear 0.7 xpos -0.5
        parallel:
            linear 0.6 rotate -30    
    scene black with Dissolve(1.0)
    outline "Et c'est ainsi que le brave Crossfitrichernvald pris la fuite devant les trois buffles fonçant sur lui"
    scene bg_etables with Dissolve(1.0)
    show char_ernust normal right at speakingAnim(0.15, 0.94, 0.92, 0.75)
    e "Ah ben tiens, il a fait tomber ses lunettes en courant."
    
    show char_ernust normal right at notSpeakingAnim(0.15, 0.94, 0.92, 0.75)
    
    $ inventory.add(lunettes)
    $ _testLunettes = 1
    show img_lunettes at center:
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
    pause 3.0
    e "On devrais ptêtre les lui rendre ?"
    jump PlaceDuVillageDefault
    
# -----------------------------------------#
