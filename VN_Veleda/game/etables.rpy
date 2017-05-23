#####################################################
# Ici figurent les scènes se déroulant aux étables. #
#####################################################
init:
    define buf = Character("Buffles : ",
        what_suffix=" ",
        ctc=anim.Blink("gui/ctc.png"))
    
label etables_PeurDesBufflesPart1:
    scene bg_etables
    show char_crossfit colere at notSpeakingAnim(0.56, 0.82, 0.8, 0.27)
    "Choix d'action"
    
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
                jump etables_PeurDesBufflesPart1bis
            "Sortir de l'étable":
                "Gaufrid sort de l'étable"
                jump PlaceDuVillageDefault

# -----------------------------------------#

label etables_PeurDesBufflesPart1bis:
    
    cross "..."
    show char_ernust normal right:
        xpos -0.5 zoom 0.8 ypos 0.12
        linear 1.0 xpos 0.1
    e "..."
    menu:
        cross "..."
        "Bonjour M.Crossfitrichmsze-machin":
            y "Bonjour M.Crossfitrichmsze-machin"
        "Bonjour M.Brossfitrirenlavd":
            y "Bonjour M.Brossfitrirenlavd"
        "Bonjour M.Crossfitricheval":
            y "Bonjour M.Crossfitricheval"
    cross "..."
    cross "............."
    cross "................................................"
    y "... ?"
    y "Vous m'entendez ?"
    cross "C'est Crossfitrichernvald. Comme ça se prononce."
    e "Comment ça se prononce ?"
    cross "..."
    cross "............."
    menu:
        cross "............."
        "Ca a pas l'air d'aller fort dites moi !":
            y "Ca a pas l'air d'aller fort dites moi !"
            cross "Ils...Ils sont toujours là !"
        "Satisfait de vos buffles ?":
            y "Alors, satisfait de vos buffles ?"
            cross "Ils...Ils sont toujours là !"
        "Vous êtiez plus bavard avec la prophétesse...":
            y "Ben dis donc, vous êtiez plus bavard avec la prophétesse..."
            cross "Ca n'a rien à voir ! C'est juste que..."
            cross "Ils...Ils sont toujours là !"
    y "Je vous demande pardon ?"
    cross "Les buffles crétin ! Ils sont toujours là !"
    menu:
        cross "{cps=0}Les buffles crétin ! Ils sont toujours là !{/cps}"
        "Les buffles ont une espérance de vie élevée vous savez ?":
            y "Les buffles ont une espérance de vie assez élevée vous savez ?"
            y "20 ans environ !"
            y "Du coup ils risquent d'être là encore un moment !"
            e "Sauf si tu veux les manger ! Haha !"
            cross "C'EST PAS CA LE PROBLEME !"
            cross "Regardez comme ils m'observent, les yeux imbibés de sang... Brrrr..."
            y "Attendez. Quoi ?"
        "Ils étaient censés partir ?":
            y "Mais ils étaient censés partir ?"
            cross "Evidemment !"
            cross "Ca fait 12 heures que la porte est ouverte, et ces imbéciles de bovins ne bougent pas d'un poil !"
            cross "Je sais plus quoi faire moi !"
            y "Attendez. Quoi ?"
    cross "Chuuuuuuuuuut ! Ils vont vous entendre !"
    e "... T'as peur des buffles ?"
    cross "Répète ça et je t'écrase !"
    "bruit meuglement meuuuuuuuh"
    cross "AAAAAAAAAAH !"
    cross "..."
    cross "Bon OK, je trouve les buffles absolument terrifiants, heureux ?!"
    "crossfit part en pleurant"
    nar "Il y a forcèment quelquechose à faire pour aider ce pauvre homme..."
    nar "Et qui sait... ça pourrait peut-être t'aider dans ta quête..."
    jump etables_PeurDesBufflesPart1
    
    
# -----------------------------------------#

label etables_PeurDesBufflesPart2:
    "Entrée etables_PeurDesBufflesPart1"
    
    $ inventory.add(lunettes)
    $ _testLunettes = 1
    
    "Lunettes récupérées"
    
    jump PlaceDuVillageDefault
    
# -----------------------------------------#
