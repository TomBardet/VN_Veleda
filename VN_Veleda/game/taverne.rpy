######################################################
# Ici figurent les scènes se déroulant à la Taverne. #
######################################################

label taverne_DatingIngrid:
    

    scene bg_taverne with Dissolve (2.5) :
        xpos 20 ypos 70 zoom 0.9
        linear 1 xpos -100 ypos -50 zoom 1.1
    
    $ renpy.music.play("ambiances/AMB_Lieu_Taverne_02.ogg", channel = "ambiance", loop = True, fadein = 0.5)
    $ renpy.music.play("music/MUSIC_Taverne.ogg", channel = "music1", loop = True, fadein = 4)
    show char_ingrid normal at notSpeakingAnim(0.5, 1.15, 1.12, 0.3) with Dissolve (1.5)

    $ _window_during_transitions = True
    
    $ lieu = "Taverne"
    $ interlocuteur = "ingrid_char"
    
    play sound "sfx/Voices/Narrateur/Narrateur_Intro_07.ogg"
    
    nar "{cps=2} {/cps}{cps=40}Tiens ?{cps=2} {/cps}{cps=20}On dirait qu'il essaie de draguer Ingrid !{/cps}"
    
    play sound "sfx/Voices/Narrateur/Narrateur_Intro_08.ogg"
    
    nar "{cps=2} {/cps}Eh,{cps=4} {/cps}{cps=28}réveille toi maintenant !{/cps}{cps=2} {/cps}{cps=25}Ça va être à ton tour.{/cps}"
    
    show char_ingrid normal at speakingAnim(0.5, 1.15, 1.12, 0.3)
    
    play sound "sfx/Voices/Ingrid/Char_Ingrid_Normal_01.ogg"
    
    i "Hihi Gaufrid t'es mignon !"

    show char_ingrid normal at notSpeakingAnim(0.5, 1.15, 1.12, 0.3)
    
    menu:
        i "{cps=0}Hihi Gaufrid t'es mignon !{/cps}"
        
        "Viens regarder les étoiles avec moi Ingrid !":
            play sound "sfx/Voices/Player/Char_Player_Normal_03.ogg"
            y "Ingrid, suis moi !"
            y "Allons observer les étoiles illuminer le clair de lune de ta beauté !"
        "C'est vrai que je suis beau.":
            play sound "sfx/Voices/Player/Char_Player_Normal_03.ogg"
            y "On me dit souvent que je suis assez beau garçon oui..."
            y "Je prends soin de moi, c'est pour ça."
        "Ingrid épouse moi !":
            play sound "sfx/Voices/Player/Char_Player_Normal_03.ogg"
            y "Épouse moi Ingrid !"
            y "Je t'aime à la folie depuis 8 jours."
            y "Je pense à toi tout le temps !"
    
    show char_ingrid degout at speakingAnim(0.5, 1.15, 1.12, 0.3)
    
    play sound "sfx/Voices/Ingrid/Char_Ingrid_Degout_04.ogg"
    
    i "Euh... je veux dire... t'es plus comme un ptit frère pour moi."
    
    show char_ingrid degout at notSpeakingAnim(0.5, 1.15, 1.12, 0.3)
    
    play sound "sfx/Voices/Player/Char_Player_Normal_04.ogg"
    y "Un petit frère... Héhé je savais que j'avais une chance !"
    nar "Quoi ?"
    nar "Comment ça une chance ?!"
    nar "Tu vas vraiment avoir besoin d'un coup de main..."
    
    show screen datingSim(ingrid_char, 0.56, 0.30)
    pause 1.5
    $ loveGauge(ingrid_char, -10, 0.65, 0.3)
    pause 1.0
    menu:
        " "
        
        "Hein ? Mais c'est quoi ces chiffres ?!":
            play sound "sfx/Voices/Player/Char_Player_Normal_01.ogg"
            y "Hein ? Mais c'est quoi ces chiffres ?!"
            
        "Hé ! Mais pourquoi j'ai perdu 10 points ?!":
            play sound "sfx/Voices/Player/Char_Player_Normal_01.ogg"
            y "Hé ! Mais pourquoi j'ai perdu 10 points ?!"

    nar "Ces chiffres représentent l'affection de ton interlocuteur."
    nar "Plus le chiffre à gauche est élevé, plus ton interlocuteur t'apprécies."
    nar "C'est le genre de mécanique qu'on trouve assez couramment dans les dating sim..."
    
    play sound "sfx/Voices/Player/Char_Player_Normal_02.ogg"        
    y "Les dating quoi ?"
    $ loveGauge(ingrid_char, -5, 0.65, 0.3)
    show char_ingrid degout at speakingAnim(0.5, 1.15, 1.12, 0.3)
    
    play sound "sfx/Voices/Ingrid/Char_Ingrid_Normal_04.ogg"
    
    i "... Gaufrid ? A qui tu parles ? Tu m'inquiètes..."
    
    show char_ingrid degout at notSpeakingAnim(0.5, 1.15, 1.12, 0.3)
    
    play sound "sfx/Voices/Player/Char_Player_Normal_04.ogg"
    y "Bah je parle au narrateur. Il a fait apparaitre des chiffres au dessus de ta tête."
    show char_ingrid degout at speakingAnim(0.5, 1.15, 1.12, 0.3)
    
    play sound "sfx/Voices/Ingrid/Char_Ingrid_Degout_02.ogg"
    
    i "..."
    i "Ecoute... je vais y aller je pense. Bisous hein !"
    
    hide screen datingSim
    show char_ingrid degout:
        xalign 0.5 yalign 0.8
        xpos 0.5 ypos 1.15 zoom 0.3
        parallel:
            linear 2.0 xpos 1.5
        parallel:
            linear 0.1 rotate 10
            
    play sound "sfx/Voices/Player/Char_Player_Normal_02.ogg"    
    y "..."
    y "Héhé, ce rencard s'est passé à merveille !"
    y "Bon je vais me coucher."
    y "Si je suis en retard demain, Véléda va encore m'engueuler."
    
    stop music1 fadeout 1.5
    stop ambiance fadeout 0.5
            
    jump narration_ellipse01
 
# -----------------------------------------# 
 
label taverne_PresentationDot:
    scene bg_taverne
    show char_ingrid normal at speakingAnim(0.5, 1.15, 1.12, 0.3)
    
    $ _window_during_transitions = True
    
    $ renpy.music.play("music/MUSIC_Taverne.ogg", channel = "music1", loop = True, fadein = 2)
    
    $ lieu = "Taverne"
    $ interlocuteur = "ingrid_char"
    show screen datingSim(ingrid_char, 0.56, 0.30)
    
    i "Gaufrid ?!"
    i "Euh... écoute, je suis désolée d'être partie en courant la dernière fois."
    i "C'est juste que tu disais des trucs vraiment bizarre  !"
    
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
            $ loveGauge(goat_char, 21, 0.55, 0.45)
            y "Je suis sérieux. Quand tu me regarde comme ça j'ai..."
            y "... j'ai l'impression que tu scrutes jusqu'au plus profond de mon âme"
            $ loveGauge(goat_char, 19, 0.55, 0.45)
            y "Tu crois aux âmes soeurs toi ?"
        "Waaaah t'as le pelage super doux !":
            y "Waaaaah ! T'as vraiment le pelage super doux !"
            $ loveGauge(goat_char, 15, 0.55, 0.45)
            y "Un poil si soyeux... Faut que tu me donnes ta marque de shampooing !"
            $ loveGauge(goat_char, 10, 0.55, 0.45)
            y "J'ai toujours accordé une immense importance à l'hygiène corporelle"
            y "Toi aussi apparemment..."
            $ loveGauge(goat_char, 13, 0.55, 0.45)
            y "Tu crois aux âmes soeurs ?"
        "Bêêêêêêêêêêêêêêêêêêêêêêêêêêêh": 
            y "Bêêêêêêêêêêêêêêêêêêêêêêêh"  
            $ loveGauge(goat_char, 20, 0.55, 0.45)
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
    $ inventory.add(blague)
    $ _testBlague = 1
    show img_blague at center:
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

#######################################################
#               CONCOURS BACHELORS, intro            ##
#######################################################
# ----------------------------------------- #

label Act2_transition_alldone:

    scene black with Dissolve(0.5)
    outline "Le meme soir, plus tard..."
    y "Ça y est ! J'ai la dot !"
    y "Ingrid, ma Choquette, j'arrive !"
    jump taverne_ConcoursPart1
    
#------------------------------------------#

label placeDuVillage_Concours_Placeholder:

    outline "Le joueur clique sur la taverne"
       
# -----------------------------------------#

label taverne_ConcoursPart1:
    "label taverne_ConcoursPart1"
    scene bg_taverne2
    show char_ingrid normal at notSpeakingAnim(0.5, 1.15, 1.12, 0.3)
    i "Gaufrid ! Enfin tu es là ! On t’attendait !"
    
    jump taverne_ConcoursPart1_choice

# -----------------------------------------#

label taverne_ConcoursPart1_choice:

    menu:
        "J'étais attendu ?":
            y "Ah bon ? Vous m’attendiez ?"
            i "Tout le village est là pour toi Gaufrid !"
            y "Ah bah tiens ! Ça fait plaisir !"
            y "On va pouvoir se marier !" 
        "Toi et...?":
            y "Vous m’attendiez ? Toi et qui d’autre ?"
            i "Moi, Brutalmund, Beaudrik… "
            i "Tout le village est là pour toi Gaufrid !"
            y "Ah bah tiens ! Ça fait plaisir !"
            y "On va pouvoir se marier !"
        "J'ai la dot !":
            y "Ingrid ! J’ai le bouclier et le glaive !"
            y "On va pouvoir se marier !"
        "Je suis là ma belle":
            y "Je suis là pour toi, ma pupuce."
            y "On peut enfin se marier !"
            
    i "Oh t’es mignon, Gaufrid ! Mais ce n’est pas si simple que ça."
    i "Maintenant que tu es là, nous pouvons enfin commencer le concours !"
    y "Oui bien sûr ! …attends, quoi ?"
    i "Shh ! ça commence !"

    jump taverne_Concours_Part2_0_Transition
    
# -----------------------------------------#

    
label taverne_Concours_Part2_0_Transition:
    scene black with Dissolve(0.5)
    outline "Il était une fois en Germanie… Beaudrik et Gaufrid, germains presque charmants."
    jump taverne_Concours_Part2_1_Intro
    
# -----------------------------------------#
    
label taverne_Concours_Part2_1_Intro:
    
    #NARRATEUR--------------> nar "{i}{color=#f2de5c}{/color}{/i}"
    scene bg_taverne with Dissolve (0.5)
    pause 1.0
    outline "Bienvenues à l’édition 1er Siècle de « Ces Chers Germains Charmants », à l’antenne tous les vendredis à la taverne du village !"
    #nar "{i}{color=#f2de5c}Bienvenues à l’édition 1er Siècle de « Ces Chers Germains Charmants », à l’antenne tous les vendredis !{/color}{/i}"
    show char_ingrid normal at notSpeakingAnim(0.5, 1.15, 1.12, 0.3):
        xpos 0.17 ypos 1.1
    outline "Ingrid est une jeune femme célibataire à la recherche de l’amour."
    outline "Tiraillée entre la beauté du corps et la beauté du cœur, Ingrid devra choisir entre deux Germains presque charmants."
    show char_beaudrik normal left :
        zoom 0.2 xpos 1.0 ypos 0.2
        linear 0.4 xpos 0.6
    outline "D'un coté, Beaudrik, \n parangon de virilité."
    outline "De l'autre, Gaufrid, \n maigre et moche."
    #nar "{i}{color=#f2de5c}Ingrid est une jeune femme célibataire à la recherche de l’amour.{/color}{/i}"
    #nar "{i}{color=#f2de5c}Tiraillée entre la beauté du corps et la beauté du cœur, Ingrid devra choisir entre deux Germains presque charmants."
    #nar "{i}{color=#f2de5c}D'un coté, Beaudrik, parangon de virilité.{/color}{/i}"
    #nar "{i}{color=#f2de5c}De l'autre, Gaufrid, maigre et moche.{/color}{/i}"

    jump taverne_Concours_Part2_1_Intro_choice
    
# -----------------------------------------#   

label taverne_Concours_Part2_1_Intro_choice:
    
    menu:
        "T’es moche toi-même":
            y "Euh ! Comment oses-tu ?"
            outline "Tais-toi quand je parle."
            outline "Et n’oublie pas que je \n peux lire tes \n choix de dialogue."
            outline "Je disais…"
        "Qu’est-ce qu’il se passe ?":
            y "Quelqu’un peut m’expliquer ce qu’il se passe ?"
            i "Laisse le présentateur parler, Gaufrid !"
            outline "Je disais…"
        "Laissez-moi tranquil !":
            y "Mais... Pourquoi toujours sur moi les trucs comme ça ?!"
            i "Laisse le présentateur parler, Gaufrid !"
            outline "Je disais…"

    hide char_ingrid normal
    hide char_beaudrik normal left

    jump taverne_Concours_Part2_2_Manual

# -----------------------------------------#

label taverne_Concours_Part2_2_Manual:

    outline "Il est maintenant l’heure de l’ultime épreuve qui départagera Beaudrik et Gaufrid !"
    outline "« Le Procès de l’Amour ! »"
    outline "Gaufrid, avez-vous lu le manuel, \n ou faut-il que je vous explique les règles ?"

    menu:
        "Quel manuel ?":
            y "Euh ?"
            outline "Celui à votre gauche, Gaufrid. \n Juste à côté de l’ordi."
            pause 1.5
            outline "..."
            outline "C'est bon ou pas ?"
            jump taverne_Concours_Part2_2_Manual_Extra
        "Bien sûr que oui":
            y "Je l’ai appris par cœur."
            outline "Maigre, moche et menteur."
            outline "Ça va surement bien se passer pour vous."
            jump taverne_Concours_Part2_3_Rules
        "J’ai oublié règles":
            y "Euh… j’ai un trou de mémoire."
            outline "Maigre, moche et amnésique."
            outline "Ça va surement bien se passer pour vous."
            jump taverne_Concours_Part2_3_Rules

# -----------------------------------------#

label taverne_Concours_Part2_2_Manual_Extra:
    
    menu:
        "Toujours pas":
            y "Je ne vois pas de manuels."
            outline "Maigre, moche et aveugle."
            outline "Ça va surement bien se passer pour vous."
        "J’ai trouvé":
            y "Euh… c’est bon !"
            outline "Maigre, moche et menteur."
            outline "Ça va surement bien se passer pour vous."
        "Un manuel de jeu en 2017 ?":
            y "Ça fait 10 ans que les jeux-vidéo n’ont plus de manuels."
            outline "Ne faites pas le type moderne, Gaufrid."
            outline "Vous êtes un germain du 1er siècle \n et vous jouez à une Visual Novel."
            outline "Vous n’êtes pas vraiment avant-gardiste."
    
    jump taverne_Concours_Part2_3_Rules

# -----------------------------------------#

label taverne_Concours_Part2_3_Rules:
    
    outline "Bref, je vous explique les règles."
    outline "Pour ce dernier test, {i}{b}{color=#f2de5c}Beaudrik{/color}{/b}{/i}, Champion en Titre, sera acclamé par les habitants du village pour ses nombreuses qualités."
    outline "{i}{b}{color=#f2de5c}Gaufrid{/color}{/b}{/i}, Challengeur de cet épisode, devra faire preuve d’humilité et se taire, car de toute façon il ne vaut rien."
    outline "Ceci dit, il pourra {i}{b}{color=#f2de5c}faire objection{/color}{/b}{/i} aux nombreux compliments faits à Beaudrik, s’il le souhaitera."
    outline "Nous pouvons passer aux {i}{b}{color=#f2de5c}interviews{/color}{/b}{/i}, ou {i}{b}{color=#f2de5c}commencer le jeu{/color}{/b}{/i}."
    outline "Que souhaitez-vous faire, Gaufrid ?"
    
    jump taverne_Concours_Part2_4_Hub

# -----------------------------------------#

label taverne_Concours_Part2_4_Hub:
    
    menu:
        "{color=#FFFFFF}Interview de Ingrid{/color}":
            y "Je voudrais voir l’interview de Ingrid."
            outline "Excellent choix !"
            show char_ingrid normal at notSpeakingAnim(0.5, 1.15, 1.12, 0.3):
                xpos 0.17 ypos 1.1
            outline "Monsieur dames : Ingrid, 22 ans, belle du village et prix à gagner !"
            i "Bonjour ! Merci, merci !"
            outline "Ingrid, décrivez-nous votre homme idéal."
            i "J’ai besoin d’un homme fort qui sait monter les meubles."
            i "Je trouve que c’est vachement important un mec qui sait monter des meubles car… moi c’est pas du tout mon truc et…"
            i "...voilà, s’il ne sait pas monter des meubles je ne sais pas comment on va faire."
            i "Sinon j’aime bien les hommes courageux, honnêtes et sans anormalités physiques."
            outline "Merci Ingrid ! A bientôt !"
            hide char_ingrid normal
            jump taverne_Concours_Part2_4_Hub
            
        "{color=#FFFFFF}Interview de Beaudrik{/color}":
            y "Je voudrais voir l’interview de Beaudrik."
            outline "Excellent choix !"
            outline "Monsieur dames : Beaudrik, Champion en titre !"
            show char_beaudrik normal left :
                zoom 0.2 xpos 1.0 ypos 0.2
                linear 0.4 xpos 0.6
            bg "Merci les gars !"
            outline "Beaudrik, vous sentez-vous prêt ?"
            bg "Je suis à fond dans le truc. Moi, les compètes j’aime bien."
            bg "Sinon je suis un peu nerveux car Josiane, mon ex, est parmi le public."
            bg "J’espère que Ingrid ne découvre pas que ce n’est pas fini-fini entre Josiane et moi."
            outline "Beaudrik, je vous rappelle que Gaufrid, votre adversaire, est juste devant vous."
            bg "Ah ! Tiens, salut Gaufrid !"
            outline "Au revoir Beaudrik !"
            hide char_beaudrik normal left
            jump taverne_Concours_Part2_4_Hub
            
        "{color=#FFFFFF}Mon interview{/color}":
            y "Je voudrais m’interviewer moi-même."
            outline "Gaufrid, déjà on ne vous donne pas favori."
            outline "Ne vous tirez pas une balle dans le pied non plus."
            jump taverne_Concours_Part2_4_Hub
            
        "On peut commencer !":
            y "C’est bon, je suis prêt !"
            jump taverne_Concours_Part3_Brutalmund

# -----------------------------------------#
label taverne_Concours_Part3_Brutalmund:
    
    outline "Très bien, nous appelons le premier témoin : le père de Beaudrik !"
    show char_brutal normal :
        zoom 0.4 xpos -0.5 ypos 0.05
        linear 0.7 xpos 0.001
    brut "Alors déjà, tu ne m’appelles pas comme ça. C’est un peu gratuit quand même."
    outline "Excusez-moi, Monsieur Brutalmund."
    brut "Deuxième chose, je ne voulais pas venir. On m’a obligé ! Obligé je vous dis !"
    brut "Mais vous savez comment c’est. Je n’en peux plus de mon fils là, Beaudrik."
    brut "Alors j’ai envie qu’il gagne, histoire qu’il se marie et qu’il se casse."
    outline "Que pensez-vous de votre fils, Monsieur Brutalmund ?"
    brut "C’est une vraie mauviett…"
    brut "Euh, attendez, il faut que je dise des trucs bien pour qu’il gagne ?"
    outline "C’est l’idée."
    brut "Ah… euh… il est fort et courageux."
    jump taverne_Concours_Part3_Brutalmund_Choice

# -----------------------------------------#

label taverne_Concours_Part3_Brutalmund_Choice:

    menu:
        "Objection !":
            y "Objection !"
            y "Beaudrik est un lâche !"
            brut "Gaufrid, mon pote ! Ne me fais pas ça !"
            show char_beaudrik normal left :
                zoom 0.2 xpos 1.0 ypos 0.2
                linear 0.4 xpos 0.6
            bg "Ne t’inquiète pas pour moi, Papounet, en tout cas il ne peut pas le prouver !"
            jump taverne_Concours_Part3_Brutalmund_Choice_Subchoice
            
        "C'est pas faux":
            y "J’aimerais bien être comme lui."
            hide char_brutal normal
            outline "Mais c’est le cas, Gaufrid."
            outline "Vous ne saviez pas que Beaudrik dort avec un nounours car il peur du noir ?"
            jump taverne_Concours_Part3_Ingrid

# -----------------------------------------#

label taverne_Concours_Part3_Brutalmund_Choice_Subchoice:
    
    hide char_brutal normal
    menu:
        "Il a peur du noir":
            y "Brutalmund est un menteur. Il sait très bien que son fils dort avec un nounours !"
            bg "Papounet, pourquoi tu lui as dit ?!"
            i "Tu dors avec un nounours ?!"

        "Il a peur des buffles":
            y "Les buffles, ils le terrifient !"
            outline "Non, ça c'est l'autre"
            bg "Mais comment tu peux dire ça ?!"
            bg "Les buffles, c’est délicieux."
            outline "Mauvaise réponse, Gaufrid ! La bonne réponse était qu’il a peur du noir."

        "Il a peur de Ernust":
            y "J’ai vu comment tu regardes Ernust."
            y "Il te fait peur !"
            bg "Écoute, on sait bien que ton pote ça craint. Mais en vrai je l’aime bien."
            outline "Mauvaise réponse, Gaufrid ! La bonne réponse était qu’il a peur du noir."

    jump taverne_Concours_Part3_Ingrid

            
# -----------------------------------------#

label taverne_Concours_Part3_Ingrid:

    show char_ingrid normal at notSpeakingAnim(0.5, 1.15, 1.12, 0.3):
        xpos 0.17 ypos 1.1
    hide char_beaudrik normal left

    i "Tiens, moi aussi !"
    i "Mais les hommes sensibles c’est pas trop mon truc."
    outline "Silence ! J’appelle le \n dernier témoin, Ingrid elle-même !"
    i "Faisons-ça vite, je ferme dans dix minutes !"
    outline "Ingrid, que pensez-vous de Beaudrik ?"
    i "Bon, ce n’est pas le plus intelligent, mais Gaufrid n’est pas un génie non plus !"
    i "Au moins Beaudrik est beau gosse, c’est un bon parti."

    jump taverne_Concours_Part3_Ingrid_Choice
    
# -----------------------------------------#   
  
label taverne_Concours_Part3_Ingrid_Choice:

    menu:
        "Objection ! Il est moche !":
            y "Objection !"
            y "Beaudrik est moche !"
            i "Tu n’aurais pas bu un coup de trop, Gaufrid ?"
            show char_beaudrik normal left :
                zoom 0.2 xpos 1.0 ypos 0.2
                linear 0.4 xpos 0.6
            i "Comment ça il est moche ?"
            jump taverne_Concours_Part3_Ingrid_Choice_Subchoice
            
        "En effet":
            y "C’est un joli garçon, en effet."
            show char_beaudrik normal left :
                zoom 0.2 xpos 1.0 ypos 0.2
                linear 0.4 xpos 0.6
            bg "Oh c’est gentil !"
            bg "J’ai beau être un homme mais j’aime bien prendre soin de moi."
            outline "Même de votre troisième téton ?"
            jump taverne_Concours_Part4_Final

# -----------------------------------------#  

label taverne_Concours_Part3_Ingrid_Choice_Subchoice:
    
    menu:
        "Il a un gros nez !":
            y "Vous avez vu son nez ? C’est une caverne !"
            i "Je sais pas, moi je trouve ça sécurisant."
            outline "Ça va vous rassurer quand vous verrez son troisième téton."

        "Il a 3 tétons !":
            y "Toutes les jeunes femmes du village le savent ! Il a un troisième téton !"

        "{color=#FFFFFF}Il est maigre et moche !{/color}":
            y "Euh… il est maigre et moche !"
            outline "Non Gaufrid, ça c’est vous."
            y "Ah oui, c’est vrai. Désolé."
            outline "Non, non, c’est moi. Excusez-moi."
            outline "Je n’ai peut-être pas assez insisté là-dessus."
            y "C’était pas super clair en effet."
            outline "Alors écoutez-moi bien :"
            outline "{b}VOUS ETES MAIGRE ET MOCHE.{/b}"
            outline "C’est mieux comme ça ?"
            y "Beaucoup mieux, merci."
            outline "De rien. Hésitez pas s’il y a autre chose qui vous échappe."
            y "Merci bien."
            outline "Je vous remets dans la boucle."
            y "C’est gentil."
            jump taverne_Concours_Part3_Ingrid_Choice_Subchoice

    jump taverne_Concours_Part4_Final

# -----------------------------------------# 

label taverne_Concours_Part4_Final:
    
    i "Un troisième téton ?! Mais c’est une imperfection physique complètement discrète et négligeable !"
    i "C’est dégueulasse !"
    i "Beaudrik, je suis très déçue."
    bg "Ingrid ! Ne dis pas ça !"
    i "Ce n’est pas le téton, hein. C’est le principe."
    i "T’aurais dû me le dire. Je ne sais pas si je peux te faire confiance."
    i "Tu m’avais promis que tu n’avais que deux tétons !"
    outline "Bon. En parlant de confiance, Ingrid, pensez-vous que Beaudrik est un gars honnête ?"
    i "Hors-mis le téton N°3 ?"
    outline "Oui."
    i "Il ne m’a jamais menti. Je pense qu’il serait un époux fidèle et loyal."

    jump taverne_Concours_Part4_Final_Choice

# -----------------------------------------#

label taverne_Concours_Part4_Final_Choice:
    
    menu:
        "Objection !":
            y "Objection !"
            y "Beaudrik a déjà une copine !"
            i "Comment ça il a une copine ?!"
            i "Comment elle s’appelle cette vache ?!"
            jump taverne_Concours_Part4_Final_Choice_Subchoice
            
        "Elle a raison":
            y "C’est vraiment un mec bien."
            i "N’est-ce pas ?"
            outline "Dommage qu’il soit déjà pris. Votre ami a déjà une fiancée."
            outline "Elle s’appelle Josiane."
            jump taverne_Concours_Part5_Ending
            
# -----------------------------------------#

label taverne_Concours_Part4_Final_Choice_Subchoice:

    menu:
        "Johanne":
            y "Euh… Johanne ?"
            outline "Vous y étiez presque, Gaufrid."
            outline "Elle s’appelle Josiane."
            jump taverne_Concours_Part5_Ending

        "Josiane":
            y "Josiane ! Elle s’appelle Josiane !"
            jump taverne_Concours_Part5_Ending

        "Jovanne":
            y "Euh… Jovanne ?"
            outline "Vous y étiez presque, Gaufrid."
            outline "Elle s’appelle Josiane."
            jump taverne_Concours_Part5_Ending

        "{color=#FFFFFF}Ernust{/color}":
            y "Ernust !"
            show char_ernust normal right :
                zoom 0.9 xpos 0.4 ypos 0.2
            e "Gaufrid ! Tu m’as appelé ?"
            y "Oui, comment elle s’appelle la copine de Beaudrik déjà ?"
            e "Ça commence avec un J, je crois."
            y "Ça m’aide beaucoup."
            e "On est vraiment un duo dynamique !"
            y "Dégage ! Hop !"
            hide char_ernust normal right
            i "Alors ?! Comment elle s’appelle ?"
            jump taverne_Concours_Part4_Final_Choice_Subchoice

# -----------------------------------------#

label taverne_Concours_Part5_Ending:

    i "JOSIANE ?!"
    i "LA CHEVRE !?!"
    goat "Beeeh !"
    i "MAIS QU’EST-CE QU’ELLE A DE PLUS QUE MOI ?!"
    bg "C’est platonique, Ingrid, crois-moi !"
    outline "Beaudrik, vous êtes disqualifié."
    bg "Tu vas me la payer, Gaufrid !"
    bg "Je le dirai à mon Papa."
    hide char_beaudrik normal left
    
    jump taverne_Concours_Part5_Ending_BadEnding
    
# ------------BAD ENDING----------------#

label taverne_Concours_Part5_Ending_BadEnding:
    
    pause 2.0
    i "Euh…"
    i "Bon Gaufrid, il ne reste plus que toi."
    y "Ah ! Bien, bien !"
    y "C’est bon ? Je te fais la demande ?"

    jump taverne_Concours_Part6_Conclusion

# ------------GOOD ENDING----------------#

label taverne_Concours_Part5_Ending_GoodEnding:

    i "Gaufrid ! Oh Gaufrid !"
    y "Ingrid ! Oh Ingrid!"
    i "Gaufrid !"
    y "C’est bon ? je te fais la demande ?" 
    
    jump taverne_Concours_Part6_Conclusion
    
# -----------------------------------------#

label taverne_Concours_Part6_Conclusion:

    i "Oh, non merci, ça ira !"
    i "On peut se marier directement, ça ira plus vite !"
    i "Il nous reste plus qu’à demander la bénédiction de Véléda !"
    y "Ah oui… c’est vrai qu’il y a cette tradition."
    show char_ernust normal right :
                zoom 0.9 xpos 0.4 ypos 0.2
    e "Mince, dommage que Véléda soit morte !"
    i "Euh ?"
    y "MORTE… de rire pour les bêtises que tu racontes, mon cher Ernust !"
    i "Bon ! C'est décidé ! Demain matin tu viendras me chercher et on ira se marier à la tour !"
    i "Sois ponctuel !"
    
    jump taverne_Concours_Part6_FadeToBlack

# -----------------------------------------#

label taverne_Concours_Part6_FadeToBlack:

    scene black with Dissolve(0.5)
    y "On est mal. On est très mal."
    y "Comment on va faire ?"
    outline "Bon, moi j’ai fait ma part."
    outline "Là tu vas devoir te débrouiller tout seul."
    outline "Allez, salut ma caille !"
    pause 2.0
    outline "{i}Le lendemain matin...{/i}"

label taverne_MarryingIngridPart1:

# -----------------------------------------#

    "label taverne_MarryingIngridPart1"
    jump tourVeleda_MarryingIngridPart2
    
# -----------------------------------------#
