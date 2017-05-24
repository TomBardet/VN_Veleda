######################################################
# Ici figurent les scènes se déroulant à la Taverne. #
######################################################

label taverne_DatingIngrid:
    scene bg_taverne
    show char_ingrid normal at notSpeakingAnim(0.5, 1.15, 1.12, 0.3)

    $ _window_during_transitions = True
    
    $ lieu = "Taverne"
    $ interlocuteur = "ingrid_char"
    
    nar "On dirait qu'il essaie de draguer Ingrid encore."
    nar "Réveille toi, ça va être ton tour."
    
    show char_ingrid normal at speakingAnim(0.5, 1.15, 1.12, 0.3)
    i "Hihi Gaufrid t'es mignon !"
    show char_ingrid normal at notSpeakingAnim(0.5, 1.15, 1.12, 0.3)
    
    menu:
        i "{cps=0}Hihi Gaufrid t'es mignon !{/cps}"
        
        "Viens avec moi, on va... regarder les étoiles...":
            y "Ingrid, suis moi"
            y "Allons observer les étoiles illuminer le clair de lune de leur beauté"
        "On me dit souvent que je suis assez beau garçon oui...":
            y "On me dit souvent que je suis assez beau garçon oui..."
            y "Je prends soin de moi, c'est pour ça"
        "Ingrid épouse moi !":
            y "Ingrid épouse moi !"
            y "Je t'aime à la folie depuis 8 jours"
            y "Je pense à toi tout le temps !"
    
    show char_ingrid normal at speakingAnim(0.5, 1.15, 1.12, 0.3)
    i "Euh... je veux dire, t'es plus comme un ptit frère pour moi"
    show char_ingrid normal at notSpeakingAnim(0.5, 1.15, 1.12, 0.3)
    y "* Un petit frère... Héhé je savais que j'avais une chance ! *"
    nar "Comment ça une chance ?!"
    nar "Tu vas vraiment avoir besoin d'un coup de main..."
    
    show screen datingSim(ingrid_char, 0.56, 0.30)
    pause 1.5
    $ loveGauge(ingrid_char, -10, 0.65, 0.3)
    pause 1.0
    menu:
        " "
        
        "Hein ? Mais c'est quoi ces chiffres ?!":
            y "Hein ? Mais c'est quoi ces chiffres ?!"
            nar "Ces chiffres représentent l'affection de ton interlocuteur"
            nar "Plus le chiffre à gauche est élevé, plus ton interlocuteur t'apprécies"
            nar "C'est le genre de mécanique qu'on trouve assez couramment dans les dating sim..."
            y "Les dating quoi ?"
        "Hé ! Mais pourquoi j'ai perdu 10 points ?!":
            y "Hé ! Mais pourquoi j'ai perdu 10 points ?!"
            nar "Ces chiffres représentent l'affection de ton interlocuteur"
            nar "Plus le chiffre à gauche est élevé, plus ton interlocuteur t'apprécies"
            nar "C'est le genre de mécanique qu'on trouve assez couramment dans les dating sim..."
            y "Les dating quoi ?"
    
    $ loveGauge(ingrid_char, -5, 0.65, 0.3)
    show char_ingrid normal at speakingAnim(0.5, 1.15, 1.12, 0.3)
    i "... Gaufrid ? A qui tu parles ? Tu m'inquiètes..."
    show char_ingrid normal at notSpeakingAnim(0.5, 1.15, 1.12, 0.3)
    y "Bah je parle au narrateur. Il a fait apparaitre des chiffres au dessus de ta tête"
    $ loveGauge(ingrid_char, -10, 0.65, 0.3)
    show char_ingrid normal at speakingAnim(0.5, 1.15, 1.12, 0.3)
    i "..."
    i "Ecoute... je vais y aller je pense. Bisous hein !"
    hide screen datingSim
    show char_ingrid normal:
        xalign 0.5 yalign 0.8
        xpos 0.5 ypos 1.15 zoom 0.3
        parallel:
            linear 2.0 xpos 1.5
        parallel:
            linear 0.1 rotate 10
    y "..."
    y "Héhé, ce rencard s'est passé à merveille !"
            
    jump narration_ellipse01
 
# -----------------------------------------# 
 
label taverne_PresentationDot:
    scene bg_taverne
    show char_ingrid normal at speakingAnim(0.5, 1.15, 1.12, 0.3)
    
    $ _window_during_transitions = True
    
    $ lieu = "Taverne"
    $ interlocuteur = "ingrid_char"
    show screen datingSim(ingrid_char, 0.56, 0.30)
    
    i "Gaufrid ?!"
    i "Euh... écoute, je suis désolé d'être partie en courant la dernière fois"
    i "C'est juste que tu disais des trucs vraiment bizarre"
    
    show char_ingrid normal at notSpeakingAnim(0.5, 1.15, 1.12, 0.3)
    menu:
        i "{cps=0}C'est juste que tu disais des trucs vraiment bizarre{/cps}"
        
        "Je suis comme ça Baby. C'est à prendre ou à laisser":
            y "Je suis comme ça Baby. C'est à prendre ou à laisser"
            $ loveGauge(ingrid_char, -2, 0.65, 0.3)
            show char_ingrid normal at speakingAnim(0.5, 1.15, 1.12, 0.3)
            i "Euh..."
        "Ca t'es jamais arrivé de voir des chiffres au dessus de la tête des gens ?":
            y "Ca t'es jamais arrivé de voir des chiffres au dessus de la tête des gens ?"
            $ loveGauge(ingrid_char, -1, 0.65, 0.3)
            show char_ingrid normal at speakingAnim(0.5, 1.15, 1.12, 0.3)
            i "Euh..."
        "Je veux t'épouser Ingrid !":
            y "Ingrid épouse moi !"
            $ loveGauge(ingrid_char, -4, 0.65, 0.3)
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
    $ loveGauge(ingrid_char, 2, 0.65, 0.3)
    show char_ingrid normal at speakingAnim(0.5, 1.15, 1.12, 0.3)
    i "Bon écoute, Gaufrid, c'est pas si simple que ça tu sais"
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
    hide screen datingSim
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
    show screen datingSim(goat_char, 0.48, 0.46)

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
            $ loveGauge(goat_char, 6, 0.55, 0.45)
            y "Faut pas prendre bibi pour un canard sauvage hein !"
            $ loveGauge(goat_char, 4, 0.55, 0.45)
            y "Enfin... Je m'emportes. Retournons à nos moutons."
            $ loveGauge(goat_char, -4, 0.55, 0.45)
            show char_goat normal at speakingAnim(0.45, 0.7, 0.68, 1.0)
            goat "BÊÊÊÊÊÊÊÊÊÊÊÊÊÊH !"
            show char_goat normal at notSpeakingAnim(0.45, 0.7, 0.68, 1.0)
            y "Oups, pardon je voulais pas te vexer"
        "T'y vas ptêtre un peu fort":
            y "T'y vas ptêtre un peu fort là par contre"
            $ loveGauge(goat_char, -1, 0.55, 0.45)
            y "Elle a pas dit ça méchamment non plus hein"
            $ loveGauge(goat_char, -1, 0.55, 0.45)
            y "Enfin... Je m'emportes. Retournons à nos moutons."
            $ loveGauge(goat_char, -2, 0.55, 0.45)
            show char_goat normal at speakingAnim(0.45, 0.7, 0.68, 1.0)
            goat "BÊÊÊÊÊÊÊÊÊÊÊÊÊÊH !"
            show char_goat normal at notSpeakingAnim(0.45, 0.7, 0.68, 1.0)
            y "Oups, pardon je voulais pas te vexer"
        "Bêêêêêêêêêêêêêêêh":
            y "Bêêêêêêêêêêêêêêêh"
            $ loveGauge(goat_char, 6, 0.55, 0.45)
    show char_goat normal at speakingAnim(0.45, 0.7, 0.68, 1.0)
    goat "Bêêêêêêêêêêêêêêêh"
    show char_goat normal at notSpeakingAnim(0.45, 0.7, 0.68, 1.0)
    menu:
        goat "{cps=0}Bêêêêêêêêêêêêêêêh{/cps}"
        "Ouf, je suis content que tu me pardonnes":
            y "Ouf, je suis vraiment content que tu me pardonnes"
            $ loveGauge(goat_char, 5, 0.55, 0.45)
            y "Pendant un court instant, j'ai... j'ai cru que j'avais tout ruiné entre nous !"
            $ loveGauge(goat_char, 7, 0.55, 0.45)
            y "Dieu merci, tu es clémente"
            $ loveGauge(goat_char, 5, 0.55, 0.45)
        "Vraiment ? Tu m'en veux pas ?":
            y "Vraiment ? Tu m'en veux pas?"
            $ loveGauge(goat_char, 1, 0.55, 0.45)
            y "Tu me rassures énormèment !"
            $ loveGauge(goat_char, 4, 0.55, 0.45)
            y "Pendant un court instant, j'ai... j'ai cru que j'avais tout ruiné entre nous !"
            $ loveGauge(goat_char, 6, 0.55, 0.45)
            y "Dieu merci, tu es clémente"
            $ loveGauge(goat_char, 5, 0.55, 0.45)
        "Bêêêêêêêêêêêêêêêêêêêêêêêh":
            y "Bêêêêêêêêêêêêêêêêêêêh" 
            $ loveGauge(goat_char, 4, 0.55, 0.45)
    show char_goat normal at speakingAnim(0.45, 0.7, 0.68, 1.0)
    goat "Bêêêêêêêêêêêêêêêh"
    show char_goat normal at notSpeakingAnim(0.45, 0.7, 0.68, 1.0)
    menu:
        goat "{cps=0}Bêêêêêêêêêêêêêêêh{/cps}"
        "Je pensais être le seul à penser ça !":
            y "Comment ?! Mais c'est fou !"
            y "J'ai toujours cru être le seul à penser ça !"
            $ loveGauge(goat_char, 6, 0.55, 0.45)
            y "Ahah toi et moi on est vraiment trop pareil !"
            $ loveGauge(goat_char, 9, 0.55, 0.45)
        "Noooooooon ?! Raconte !":
            y "Noooooooooon ?! Il a dit ça ?! Raconte !"
            $ loveGauge(goat_char, 5, 0.55, 0.45)
            show char_goat normal at speakingAnim(0.45, 0.7, 0.68, 1.0)
            goat "Bêêêêêêêêêêêêêêêh" 
            show char_goat normal at notSpeakingAnim(0.45, 0.7, 0.68, 1.0)
            y "Ahah, il a pas osé !"
            $ loveGauge(goat_char, 8, 0.55, 0.45)
            y "J'avoue que c'est cocasse !"
            $ loveGauge(goat_char, 7, 0.55, 0.45)
        "Bêêêêêêêêêêêêêêêêêêêêêêêh": 
            y "Bêêêêêêêêêêêêêêêêêêêêêêêêêêêh"
            $ loveGauge(goat_char, 5, 0.55, 0.45)
    show char_goat normal at speakingAnim(0.45, 0.7, 0.68, 1.0)
    goat "Bêêêêêêêêêêêêêêêh" 
    show char_goat normal at notSpeakingAnim(0.45, 0.7, 0.68, 1.0)
    menu:
        goat "{cps=0}Bêêêêêêêêêêêêêêêh{/cps}"
        "Tu sais que t'as de beaux yeux ?":
            y "... Dis... Tu sais que t'as de beaux yeux ?"
            $ loveGauge(goat_char, 16, 0.55, 0.45)
            y "Je suis sérieux. Quand tu me regarde comme ça j'ai..."
            y "... j'ai l'impression que tu scrutes jusqu'au plus profond de mon âme"
            $ loveGauge(goat_char, 12, 0.55, 0.45)
            y "Tu crois aux âmes soeurs toi ?"
        "Waaaah t'as le pelage super doux !":
            y "Waaaaah ! T'as vraiment le pelage super doux !"
            $ loveGauge(goat_char, 10, 0.55, 0.45)
            y "Un poil si soyeux... Faut que tu me donnes ta marque de shampooing !"
            $ loveGauge(goat_char, 9, 0.55, 0.45)
            y "J'ai toujours accordé une immense importance à l'hygiène corporelle"
            y "Toi aussi apparemment..."
            $ loveGauge(goat_char, 9, 0.55, 0.45)
            y "Tu crois aux âmes soeurs ?"
        "Bêêêêêêêêêêêêêêêêêêêêêêêêêêêh": 
            y "Bêêêêêêêêêêêêêêêêêêêêêêêh"  
            $ loveGauge(goat_char, 9, 0.55, 0.45)
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
    hide screen datingSim
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
