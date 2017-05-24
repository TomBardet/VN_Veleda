#####################################################
# Ici figurent les scènes se déroulant aux étables. #
#####################################################
init:
    define buf = Character("Buffles : ",
        what_suffix=" ",
        ctc=anim.Blink("gui/ctc.png"))
    $  _testCrossfitTalk = 0
    $  _testBrutalmundTalk = 0
    $  _testRomainsTalk = 0
    
label etables_PeurDesBufflesPart1:
    scene bg_etables
    show char_crossfit colere at notSpeakingAnim(0.56, 0.80, 0.8, 0.27)
    "Choix d'action"
    #$ _testTrompette = 1
    if _testTrompette == 1:
        menu:
            " "
            "Jouer de la trompette":
                jump etables_PeurDesBufflesPart2
            "Parler aux Buffles":
                buf "Meuuuuuuuh !"
                y "A vos souhaits"
                jump etables_PeurDesBufflesPart1
            "Parler à Crossfitrichernvald":
                jump etables_PeurDesBufflesPart1bis
            "Sortir de l'étable":
                "Gaufrid sort de l'étable"
                jump PlaceDuVillageDefault
    else:
        menu:
            " "
            "Parler aux Buffles":
                buf "Meuuuuuuuh !"
                y "A vos souhaits"
                jump etables_PeurDesBufflesPart1
            "Parler à Crossfitrichernvald":
                if _testCrossfitTalk == 0:
                    jump etables_PeurDesBufflesPart1bis
                else:
                    jump etables_PeurDesBufflesPart1boucle
            "Sortir de l'étable":
                "Gaufrid sort de l'étable"
                jump PlaceDuVillageDefault

# -----------------------------------------#

label etables_PeurDesBufflesPart1bis:
    show char_crossfit colere at speakingAnim(0.56, 0.82, 0.8, 0.27)
    cross "..."
    show char_crossfit colere at notSpeakingAnim(0.56, 0.82, 0.8, 0.27)
    show char_ernust normal right:
        xalign 0.5 yalign 0.8
        xpos -0.5 zoom 0.75 ypos 0.94
        linear 1.0 xpos 0.15
    pause 1.0
    show char_ernust normal right at speakingAnim(0.15, 0.94, 0.92, 0.75)
    e "..."
    show char_ernust normal right at notSpeakingAnim(0.15, 0.94, 0.92, 0.75)
    menu:
        cross "..."
        "Bonjour M.Crossfitrichmsze-machin":
            y "Bonjour M.Crossfitrichmsze-machin"
        "Bonjour M.Brossfitrirenlavd":
            y "Bonjour M.Brossfitrirenlavd"
        "Bonjour M.Crossfitricheval":
            y "Bonjour M.Crossfitricheval"
    show char_crossfit colere at speakingAnim(0.56, 0.82, 0.8, 0.27)
    cross "..."
    cross "............."
    cross "................................................"
    show char_crossfit colere at notSpeakingAnim(0.56, 0.82, 0.8, 0.27)
    y "... ?"
    y "Vous m'entendez ?"
    show char_crossfit colere at speakingAnim(0.56, 0.82, 0.8, 0.27)
    cross "C'est Crossfitrichernvald. Comme ça se prononce."
    show char_crossfit colere at notSpeakingAnim(0.56, 0.82, 0.8, 0.27)
    show char_ernust normal right at speakingAnim(0.15, 0.94, 0.92, 0.75)
    e "Comment ça se prononce ?"
    show char_ernust normal right at notSpeakingAnim(0.15, 0.94, 0.92, 0.75)
    show char_crossfit colere at speakingAnim(0.56, 0.82, 0.8, 0.27)
    cross "..."
    cross "............."
    show char_crossfit colere at notSpeakingAnim(0.56, 0.82, 0.8, 0.27)
    menu:
        cross "............."
        "Ca a pas l'air d'aller fort dites moi !":
            y "Ca a pas l'air d'aller fort dites moi !"
            show char_crossfit colere at speakingAnim(0.56, 0.82, 0.8, 0.27)
            cross "Ils...Ils sont toujours là !"
        "Satisfait de vos buffles ?":
            y "Alors, satisfait de vos buffles ?"
            show char_crossfit colere at speakingAnim(0.56, 0.82, 0.8, 0.27)
            cross "Ils...Ils sont toujours là !"
        "Vous êtiez plus bavard avec la prophétesse...":
            y "Ben dis donc, vous êtiez plus bavard avec la prophétesse..."
            show char_crossfit colere at speakingAnim(0.56, 0.82, 0.8, 0.27)
            cross "Ca n'a rien à voir ! C'est juste que..."
            cross "Ils...Ils sont toujours là !"
    show char_crossfit colere at notSpeakingAnim(0.56, 0.82, 0.8, 0.27)
    y "Je vous demande pardon ?"
    show char_crossfit colere at speakingAnim(0.56, 0.82, 0.8, 0.27)
    cross "Les buffles crétin ! Ils sont toujours là !"
    show char_crossfit colere at notSpeakingAnim(0.56, 0.82, 0.8, 0.27)
    menu:
        cross "{cps=0}Les buffles crétin ! Ils sont toujours là !{/cps}"
        "Les buffles ont une espérance de vie élevée vous savez ?":
            y "Les buffles ont une espérance de vie assez élevée vous savez ?"
            y "20 ans environ !"
            y "Du coup ils risquent d'être là encore un moment !"
            show char_ernust normal right at speakingAnim(0.15, 0.94, 0.92, 0.75)
            e "Sauf si tu veux les manger ! Haha !"
            show char_ernust normal right at notSpeakingAnim(0.15, 0.94, 0.92, 0.75)
            show char_crossfit colere at speakingAnim(0.56, 0.82, 0.8, 0.27)
            cross "C'EST PAS CA LE PROBLEME !"
            cross "Regardez comme ils m'observent, les yeux imbibés de sang... Brrrr..."
            show char_crossfit colere at notSpeakingAnim(0.56, 0.82, 0.8, 0.27)
            y "Attendez. Quoi ?"
        "Ils étaient censés partir ?":
            y "Mais ils étaient censés partir ?"
            show char_crossfit colere at speakingAnim(0.56, 0.82, 0.8, 0.27)
            cross "Evidemment !"
            cross "Ca fait 12 heures que la porte est ouverte, et ces imbéciles de bovins ne bougent pas d'un poil !"
            show char_crossfit colere at notSpeakingAnim(0.56, 0.82, 0.8, 0.27)
            cross "Je sais plus quoi faire moi !"
            y "Attendez. Quoi ?"
    show char_crossfit colere at speakingAnim(0.56, 0.82, 0.8, 0.27)
    cross "Chuuuuuuuuuut ! Ils vont vous entendre !"
    show char_crossfit colere at notSpeakingAnim(0.56, 0.82, 0.8, 0.27)
    show char_ernust normal right at speakingAnim(0.15, 0.94, 0.92, 0.75)
    e "... T'as peur des buffles ?"
    show char_ernust normal right at notSpeakingAnim(0.15, 0.94, 0.92, 0.75)
    show char_crossfit colere at speakingAnim(0.56, 0.82, 0.8, 0.27)
    cross "Répète ça et je t'écrase !"
    show char_crossfit colere at notSpeakingAnim(0.56, 0.82, 0.8, 0.27)
    "bruit meuglement meuuuuuuuh"
    show char_crossfit colere at speakingAnim(0.56, 0.82, 0.8, 0.27)
    cross "AAAAAAAAAAH !"
    show char_crossfit colere at notSpeakingAnim(0.56, 0.82, 0.8, 0.27)
    pause 2.0
    show char_crossfit colere at speakingAnim(0.56, 0.82, 0.8, 0.27)
    cross "..."
    cross "Bon OK, je trouve les buffles absolument terrifiants, heureux ?!"
    show char_crossfit colere:
        xalign 0.5 yalign 0.8
        zoom 0.27 xpos 0.56 ypos 0.82
        parallel:
            linear 1.5 xpos -0.5
        parallel:
            linear 0.5 rotate -20
    "crossfit part en pleurant"
    nar "Il y a forcèment quelquechose à faire pour aider ce pauvre homme..."
    nar "Et qui sait... ça pourrait peut-être t'aider dans ta quête..."
    $ _testCrossfitTalk = 1
    jump etables_PeurDesBufflesPart1
    
    
# -----------------------------------------#

label etables_PeurDesBufflesPart1boucle:
    y "Alors, tout baigne ?"
    show char_crossfit colere at speakingAnim(0.56, 0.82, 0.8, 0.27)
    cross "... Les... les buffles... Ils me regardent..."
    show char_crossfit colere at notSpeakingAnim(0.56, 0.82, 0.8, 0.27)
    y "Je vais vous laisser hein ?"
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
    "*PFIOUUUUUUU* Bruit de trompette"
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
    e "On devrais ptêtre les lui rendre ?"
    show char_ernust normal right at notSpeakingAnim(0.15, 0.94, 0.92, 0.75)
    
    $ inventory.add(lunettes)
    $ _testLunettes = 1
    
    "Lunettes récupérées + anim lunettes qui vont vers l'inventaire"
    
    jump PlaceDuVillageDefault
    
# -----------------------------------------#
