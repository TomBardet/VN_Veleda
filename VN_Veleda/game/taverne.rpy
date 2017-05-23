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
    show char_ingrid normal at speakingAnim(0.5, 0.6, 0.56, 0.3)
    
    i "Gaufrid ?!"
    i "Euh... écoute, je suis désolé d'être partie en courant la dernière fois"
    i "C'est juste que tu disais des trucs vraiment bizarre"
    
    show char_ingrid normal at notSpeakingAnim(0.5, 0.6, 0.56, 0.3)
    menu:
        i "{cps=0}C'est juste que tu disais des trucs vraiment bizarre{/cps}"
        
        "Je suis comme ça Baby. C'est à prendre ou à laisser":
            y "Je suis comme ça Baby. C'est à prendre ou à laisser"
            show char_ingrid normal at speakingAnim(0.5, 0.6, 0.56, 0.3)
            i "Euh..."
        "Ca t'es jamais arrivé de voir des chiffres au dessus de la tête des gens ?":
            y "Ca t'es jamais arrivé de voir des chiffres au dessus de la tête des gens ?"
            show char_ingrid normal at speakingAnim(0.5, 0.6, 0.56, 0.3)
            i "Euh..."
        "Je veux t'épouser Ingrid !":
            y "Ingrid épouse moi !"
            show char_ingrid normal at speakingAnim(0.5, 0.6, 0.56, 0.3)
            i "Euh..."
        
    i "Et si je te servais quelquechose à boire plutôt Gaufrid ?"
    show char_ingrid normal at notSpeakingAnim(0.5, 0.6, 0.56, 0.3)
    y "Avec plaisir !"
    
    "Add bruit glouglou"
    "Add mise en scène boire"
    
    y "...Ingrid je..."
    y "Je t'aime, marions nous !"
    show char_ingrid normal at speakingAnim(0.5, 0.6, 0.56, 0.3)
    i "Gaufrid, c'est pas si simple que ça tu sais"
    i "L'amour n'est pas un jeu."
    i "Je ne tomberai amoureuse de toi que si tu me ramène une dot."
    show char_ingrid normal at notSpeakingAnim(0.5, 0.6, 0.56, 0.3)
    y "Une dot ?"
    show char_ingrid normal at speakingAnim(0.5, 0.6, 0.56, 0.3)
    i "Une dot. Un {b}glaive{/b} et un {b}bouclier{/b} pour être plus précise."
    show char_ingrid normal at notSpeakingAnim(0.5, 0.6, 0.56, 0.3)
    y "Mais... quoi ?"
    show char_ingrid normal at speakingAnim(0.5, 0.6, 0.56, 0.3)
    i "N'en dis pas plus Gaufrid ! Nul ne peut comprendre l'Amour !"
    i "N'oublie pas ! Un {b}glaive{/b} et un {b}bouclier{/b} !"
    i "Je te ressert à boire ?"
    show char_ingrid normal at notSpeakingAnim(0.5, 0.6, 0.56, 0.3)
    
    "Add bruit glouglou"
    "Add mise en scène boire"
    "Add fade to black"
    
    outline "Quelques verres plus tard..."
     
    jump taverne_AbusAlcoolPart1
     
# -----------------------------------------#

label taverne_AbusAlcoolPart1:
    scene bg_taverne2
    show char_goat normal
    
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
