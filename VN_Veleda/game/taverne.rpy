######################################################
# Ici figurent les scènes se déroulant à la Taverne. #
######################################################

label taverne_DatingIngrid:
    "label taverne_DatingIngrid"
    
    jump narration_ellipse01
 
# -----------------------------------------# 
 
label taverne_PresentationDot:
    scene bg_taverne:
        zoom 0.35
    show char_ingrid normal at speakingAnim(0.5, 1.15, 1.12, 0.3)
    
    i "Gaufrid ?!"
    i "Euh... écoute, je suis désolé d'être partie en courant la dernière fois"
    i "C'est juste que tu disais des trucs vraiment bizarre"
    
    show char_ingrid normal at notSpeakingAnim(0.5, 1.15, 1.12, 0.3)
    menu:
        i "{cps=0}C'est juste que tu disais des trucs vraiment bizarre{/cps}"
        
        "Je suis comme ça Baby. C'est à prendre ou à laisser":
            y "Je suis comme ça Baby. C'est à prendre ou à laisser"
            show char_ingrid normal at speakingAnim(0.5, 1.15, 1.12, 0.3)
            i "Euh..."
        "Ca t'es jamais arrivé de voir des chiffres au dessus de la tête des gens ?":
            y "Ca t'es jamais arrivé de voir des chiffres au dessus de la tête des gens ?"
            show char_ingrid normal at speakingAnim(0.5, 1.15, 1.12, 0.3)
            i "Euh..."
        "Je veux t'épouser Ingrid !":
            y "Ingrid épouse moi !"
            show char_ingrid normal at speakingAnim(0.5, 1.15, 1.12, 0.3)
            i "Euh..."
        
    i "Et si je te servais quelquechose à boire plutôt Gaufrid ?"
    show char_ingrid normal at notSpeakingAnim(0.5, 1.15, 1.12, 0.3)
    y "Avec plaisir !"
    
    pause 0.5
    scene black with Dissolve(2.0)
    "Add bruit glouglou"
    scene bg_taverne with Dissolve(2.0):
        zoom 0.35
    show char_ingrid normal at notSpeakingAnim(0.5, 1.15, 1.12, 0.3)    
    y "...Ingrid je..."
    y "Je t'aime, marions nous !"
    show char_ingrid normal at speakingAnim(0.5, 1.15, 1.12, 0.3)
    i "Gaufrid, c'est pas si simple que ça tu sais"
    i "L'amour n'est pas un jeu."
    i "Je ne tomberai amoureuse de toi que si tu me ramène une dot."
    show char_ingrid normal at notSpeakingAnim(0.5, 1.15, 1.12, 0.3)
    y "Une dot ?"
    show char_ingrid normal at speakingAnim(0.5, 1.15, 1.12, 0.3)
    i "Une dot. Un {b}glaive{/b} et un {b}bouclier{/b} pour être plus précise."
    show char_ingrid normal at notSpeakingAnim(0.5, 1.15, 1.12, 0.3)
    y "Mais... quoi ?"
    show char_ingrid normal at speakingAnim(0.5, 1.15, 1.12, 0.3)
    i "N'en dis pas plus Gaufrid ! Nul ne peut comprendre l'Amour !"
    show char_ingrid normal:
        xalign 0.5 yalign 0.8
        xpos 0.5 ypos 1.15 zoom 0.3
        parallel:
            linear 3.0 xpos -0.5
        parallel:
            linear 0.1 rotate 10
    i "N'oublie pas ! Un {b}glaive{/b} et un {b}bouclier{/b} !"
    show char_ingrid normal:
        xalign 0.5 yalign 0.8
        xpos -0.5 ypos 1.5 zoom 0.3 rotate 30
        linear 1.0 xpos 0.05 ypos 1.15
    pause 1.5
    i "Je te ressert à boire ?"
    show char_ingrid normal:
        xalign 0.5 yalign 0.8
        xpos 0.05 ypos 1.15 zoom 0.3 rotate 30
        linear 1.0 xpos -0.5 ypos 1.5
    pause 1.0
    scene black with Dissolve(2.0)
    
    "Add bruit glouglou"
    "Add mise en scène boire"
    
    outline "Quelques verres plus tard..."
     
    jump taverne_AbusAlcoolPart1
     
# -----------------------------------------#

label taverne_AbusAlcoolPart1:
    scene bg_taverne2:
        zoom 0.35
    show char_goat normal at notSpeakingAnim(0.5, 1.15, 1.12, 1.0)
    
    "WIP"
    
    jump taverne_AbusAlcoolPart2
    
# -----------------------------------------#

label taverne_AbusAlcoolPart2:
    "label taverne_AbusAlcoolPart2"
     
    $ inventory.add(blague)
    $ _testBlague = 1
     
    "blague récupérée"
     
    jump narration_ellipseCuite
     
# -----------------------------------------#

label taverne_ConcoursPart1:
    "label taverne_ConcoursPart1"
    
    jump taverne_ConcoursPart2
    
# -----------------------------------------#

    
label taverne_ConcoursPart2:
    "label taverne_ConcoursPart2"
    
    jump taverne_ConcoursPart3
    
# -----------------------------------------#
    
label taverne_ConcoursPart3:
    "label taverne_ConcoursPart3"
    
    jump taverne_MarryingIngridPart1
    
# -----------------------------------------#

label taverne_MarryingIngridPart1:
    "label taverne_MarryingIngridPart1"
    
    jump tourVeleda_MarryingIngridPart2
    
# -----------------------------------------#
