######################################################
# Ici figurent les scènes se déroulant à la Taverne. #
######################################################

label taverne_DatingIngrid:
    "label taverne_DatingIngrid"
    
    jump narration_ellipse01
 
# -----------------------------------------# 
 
label taverne_PresentationDot:
    scene bg_taverne
    show char_ingrid normal at speakingAnim(0.5, 1.15, 1.12, 0.3)
    
    $ _window_during_transitions = True
    
    $ lieu = "Taverne"
    $ interlocuteur = "ingrid_char"
    
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

    scene black with Dissolve(2.0)
    "Add bruit glouglou"
    scene bg_taverne
    show char_ingrid normal at notSpeakingAnim(0.5, 1.12, 1.12, 0.3)    
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
    y "... Oui."
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
    scene bg_taverne2
    show char_goat normal at notSpeakingAnim(0.45, 0.7, 0.68, 1.0)
    
    $ lieu = "Taverne2"
    $ interlocuteur = "goat_char"
    
    y "Et là elle m'dit : "
    y "Ramène moi un {b}bouclier{/b} et un {b}glaive{/b}"
    show char_goat normal at speakingAnim(0.45, 0.7, 0.68, 1.0)
    goat "Bêêêêêêêêêêêêêêêh"
    show char_goat normal at notSpeakingAnim(0.45, 0.7, 0.68, 1.0)
    y "Non mais t'y crois toi ?"
    show char_goat normal at speakingAnim(0.45, 0.7, 0.68, 1.0)
    goat "Bêêêêêêêêêêêêêêêh"
    show char_goat normal at notSpeakingAnim(0.45, 0.7, 0.68, 1.0)
    menu:
        goat "{cps=0}Bêêêêêêêêêêêêêêêh{/cps}"
        "T'as complètement raison":
            y "Nan mais t'as complètement raison"
            y "Faut pas prendre bibi pour un canard sauvage hein !"
            y "Enfin... Je m'emportes. Retournons à nos moutons."
            show char_goat normal at speakingAnim(0.45, 0.7, 0.68, 1.0)
            goat "BÊÊÊÊÊÊÊÊÊÊÊÊÊÊH !"
            show char_goat normal at notSpeakingAnim(0.45, 0.7, 0.68, 1.0)
            y "Oups, pardon je voulais pas te vexer"
        "T'y vas ptêtre un peu fort":
            y "T'y vas ptêtre un peu fort là par contre"
            y "Elle a pas dit ça méchamment non plus hein"
            show char_goat normal at speakingAnim(0.45, 0.7, 0.68, 1.0)
            goat "BÊÊÊÊÊÊÊÊÊÊÊÊÊÊH !"
            show char_goat normal at notSpeakingAnim(0.45, 0.7, 0.68, 1.0)
            y "Oups, pardon je voulais pas te vexer"
        "Bêêêêêêêêêêêêêêêh":
            y "Bêêêêêêêêêêêêêêêh"
    show char_goat normal at speakingAnim(0.45, 0.7, 0.68, 1.0)
    goat "Bêêêêêêêêêêêêêêêh"
    show char_goat normal at notSpeakingAnim(0.45, 0.7, 0.68, 1.0)
    menu:
        goat "{cps=0}Bêêêêêêêêêêêêêêêh{/cps}"
        "Ouf, je suis content que tu me pardonnes":
            y "Ouf, je suis vraiment content que tu me pardonnes"
            y "Pendant un court instant, j'ai... j'ai cru que j'avais tout ruiné entre nous !"
            y "Dieu merci, tu es clémente"
        "Vraiment ? Tu m'en veux pas ?":
            y "Vraiment ? Tu m'en veux pas?"
            y "Tu me rassures énormèment !"
            y "Pendant un court instant, j'ai... j'ai cru que j'avais tout ruiné entre nous !"
            y "Dieu merci, tu es clémente"
        "Bêêêêêêêêêêêêêêêh":
            y "Bêêêêêêêêêêêêêêêh" 
    show char_goat normal at speakingAnim(0.45, 0.7, 0.68, 1.0)
    goat "Bêêêêêêêêêêêêêêêh"
    show char_goat normal at notSpeakingAnim(0.45, 0.7, 0.68, 1.0)
    menu:
        goat "{cps=0}Bêêêêêêêêêêêêêêêh{/cps}"
        "Je pensais être le seul à penser ça !":
            y "Comment ?! Mais c'est fou !"
            y "J'ai toujours cru être le seul à penser ça !"
            y "Ahah toi et moi on est vraiment trop pareil !"
        "Noooooooon ?! Raconte !":
            y "Noooooooooon ?! Il a dit ça ?! Raconte !"
            show char_goat normal at speakingAnim(0.45, 0.7, 0.68, 1.0)
            goat "Bêêêêêêêêêêêêêêêh" 
            show char_goat normal at notSpeakingAnim(0.45, 0.7, 0.68, 1.0)
            y "Ahah, il a pas osé !"
            y "J'avoue que c'est cocasse !"
        "Bêêêêêêêêêêêêêêêh": 
            y "Bêêêêêêêêêêêêêêêh"
    show char_goat normal at speakingAnim(0.45, 0.7, 0.68, 1.0)
    goat "Bêêêêêêêêêêêêêêêh" 
    show char_goat normal at notSpeakingAnim(0.45, 0.7, 0.68, 1.0)
    menu:
        goat "{cps=0}Bêêêêêêêêêêêêêêêh{/cps}"
        "Tu sais que t'as de beaux yeux ?":
            y "... Dis... Tu sais que t'as de beaux yeux ?"
            y "Je suis sérieux. Quand tu me regarde comme ça j'ai..."
            y "... j'ai l'impression que tu scrutes jusqu'au plus profond de mon âme"
            y "Tu crois aux âmes soeurs toi ?"
        "Waaaah t'as le pelage super doux !":
            y "Waaaaah ! T'as vraiment le pelage super doux !"
            y "Un poil si soyeux... Faut que tu me donnes ta marque de shampooing !"
            y "J'ai toujours accordé une immense importance à l'hygiène corporelle"
            y "Toi aussi apparemment..."
            y "Tu crois aux âmes soeurs ?"
        "Bêêêêêêêêêêêêêêêh": 
            y "Bêêêêêêêêêêêêêêêh"  
    show char_goat normal at speakingAnim(0.45, 0.7, 0.68, 1.0)
    goat "Bêêêêêêêêêêêêêêêh" 
    goat "Bêêêêhêêêhêê- *tousse*"
    goat "F-F-Faaaaudriiid !"
    show char_goat normal at notSpeakingAnim(0.45, 0.7, 0.68, 1.0)
    y "Gaufrid."
    show char_goat normal at speakingAnim(0.45, 0.7, 0.68, 1.0)
    goat "Pardon. G-G-Gaaaaaaaufriiiid"
    goat "Tu as rompu le malèfice en me parlant avec amour"
    goat "Tu es une personne extraordinaire Gaufrid. Vraiment."
    goat "En gage de ma gratitude, je te donne cette {b}blague{/b}."
    "Mise en scène de la blague qui arrive dans l'inventaire"
    $ inventory.add(blague)
    $ _testBlague = 1    
    goat "Elle fera rire tous tes interlocuteurs, et marquera ton ascension dans la société"
    goat "Je dois y aller maintenant"
    goat "Au revoir Gaufrid"
    show char_goat normal:
        xalign 0.5 yalign 0.8
        zoom 1.0 xpos 0.45 ypos 0.7
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
    y "NOOOON ! Reviens !"
    y "..."
    y "Elle est partie..."
    y "... J'ai trop bu..."
    scene black with Dissolve (2.0)
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
