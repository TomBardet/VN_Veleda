####################################################
# Ici figurent les scènes se déroulant à la Forge. #
####################################################

label forge_BrutalmundEtBeaudrik:
    
    stop music1 fadeout 1.5
    stop ambiance fadeout 0.5
    $ renpy.music.play("ambiances/AMB_Lieu_Forge_01.ogg", channel = "ambiance", loop = True, fadein = 1)

    $ interlocuteur = "brut_char"
    $ interlocuteur = "beau_char"

    if Acte2_Forge_FirstVisit == 0:
        $ forge_cannotpay_check = 0 # Check si on a déjà dit à Brutalmund qu'on ne peut pas payer
        jump forge_Intro
    if Acte2_Forge_FirstVisit == 1:
        jump forge_Brutalmund_Tampon_HUB
        
# ----------------------------------------- #

label forge_Brutalmund_Tampon_HUB:

    scene bg_forge
    pause 0.5
    $ renpy.music.play("music/MUSIC_Forge.ogg", channel = "music1", loop = True, fadein = 1)
    show char_brutal normal :
        zoom 0.35 xpos -0.5 ypos 0.05
        linear 0.7 xpos 0.2
    brut "Gaufrid !"
    show char_brutal heureux at speakingAnim(0.52, 0.93, 0.91, 0.35)
    lay sound "sfx/Voices/Beaudrik/Char_Beaudrik_Normal_02.ogg"
    brut "Alors, ça te tente un {b}Bouclier Original de Capitaine Germanie™{/b} tout neuf ?"
    jump forge_Brutalmund_06_Hub

# -----------------------------------------#

label forge_Intro:
    
    scene bg_forge
    pause 1.0
    y "Euh... il y a quelqu'un ?"
    
    jump forge_Beaudrik_01

# -----------------------------------------#

label forge_Beaudrik_01:
    
    $ Acte2_Forge_FirstVisit = 1
    show char_beaudrik normal left :
        xalign 0.5 yalign 0.8
        zoom 0.2 xpos 1.5 ypos 0.78
        linear 0.4 xpos 0.8

jump forge_Beaudrik_02
    
# -----------------------------------------#

label forge_Beaudrik_02:
    
    pause 0.5
    show char_beaudrik normal left at speakingAnim(0.8, 0.9, 0.88, 0.2)
    play sound "sfx/Voices/Beaudrik/Char_Beaudrik_Normal_02.ogg"
    bg "Tiens ! C’est le p’tit Gaufrid !"
    show screen datingSim(beau_char, 0.75, 0.10)
    pause 0.5
    $ renpy.music.play("music/MUSIC_Forge.ogg", channel = "music1", loop = True, fadein = 1)
    bg "T’sais, justement je pensais à toi bonhomme."
    show char_beaudrik normal left at notSpeakingAnim(0.8, 0.9, 0.88, 0.2)
    y "Ah, merci Beaudrik ! Je suis flatté."
    show char_beaudrik mepris left at speakingAnim(0.8, 0.9, 0.88, 0.2)
    $ loveGauge(beau_char, -5, 0.85, 0.10)
    play sound "sfx/Voices/Beaudrik/Char_Beaudrik_Mepris_02.ogg"
    bg "J’ai entendu des rumeurs comme quoi tu veux épouser Ingrid !"
    show char_beaudrik drague right at speakingAnim(0.7, 0.9, 0.88, 0.22)
        #zoom 0.22 xpos 0.4 ypos 0.09
    play sound "sfx/Voices/Beaudrik/Char_Beaudrik_Drague_04.ogg"
    bg "C’est tellement n’importe quoi ! Ahahah."
    show char_beaudrik normal left at speakingAnim(0.8, 0.9, 0.88, 0.2)
        #zoom 0.2 xpos 0.6 ypos 0.09
    bg "On entend vraiment des trucs drôles à la taverne, quand les gens se bourrent la gueule."

jump forge_Beaudrik_03_EpouserIngrid
    
#------------------------------------------#

label forge_Beaudrik_03_EpouserIngrid:
    
    #show char_beaudrik normal left at notSpeakingAnim(0.8, 0.9, 0.88, 0.2)
    #menu:
    #    bg "On entend vraiment des trucs drôles à la taverne, quand les gens se bourrent la gueule."
    #    "Ouais… très drôles" :
    #        y "Euh… heureusement que c’est juste des rumeurs."
    #        show char_beaudrik normal left at speakingAnim(0.8, 0.9, 0.88, 0.2)
    #        bg "Ouais, grave ! Ça aurait été dommage que je te casse la gueule."
    #        jump forge_Beaudrik_04
    #    "Ça ne te regarde pas" :
    #        y "Euh… oh ! Ce qu’il se passe entre Ingrid et moi, ça ne te regarde pas !"
    #        show char_beaudrik normal left at speakingAnim(0.8, 0.9, 0.88, 0.2)
    #        bg "Ahahahah !"
    #        bg "Vraiment, tu me tues mon pote. T’as raison, faut jouer le jeu."
    #        bg "En tout cas, c’est bien que ce ne soit qu’une rumeur."
    #        bg "Ça aurait été dommage que je te casse la gueule."
    #        jump forge_Beaudrik_04
    #    "On va se marier pour de vrai !" :
    #        y "Euh… oui, mais tu sais, Ingrid et moi on va se marier vraiment !"
    #        show char_beaudrik normal left at speakingAnim(0.8, 0.9, 0.88, 0.2)
    #        bg "Ahahahah !"
    #        bg "Vraiment, tu me tues mon pote. T’as raison, faut jouer le jeu."
    #        bg "En tout cas, c’est bien que ce ne soit qu’une rumeur."
    #        bg "Ça aurait été dommage que je te casse la gueule."
    #        jump forge_Beaudrik_04
            
    jump forge_Beaudrik_04
        
#------------------------------------------#

label forge_Beaudrik_04:

    show char_beaudrik mepris left at speakingAnim(0.8, 0.9, 0.88, 0.2)
    bg "Tu sais, c’est moi qui vais marier la gonzesse. J’ai une dot et tout."
    show char_beaudrik normal left at speakingAnim(0.8, 0.9, 0.88, 0.2)
    bg "J’aime beaucoup les femmes mais là j’ai envie de me poser."
    show char_beaudrik mepris left at speakingAnim(0.8, 0.9, 0.88, 0.2)
    bg "T’sais, d’avoir quelqu’un qui me fasse des câlins et la vaisselle."
    show char_beaudrik mepris left at speakingAnim(0.8, 0.9, 0.88, 0.2)
    show char_brutal colere:
        xalign 0.5 yalign 0.8
        xpos -0.55 ypos 1.5 zoom 0.2 rotate 45
        linear 0.7 xpos 0.045 ypos 0.7
    pause 0.5
    show char_beaudrik choque left at speakingAnim(0.8, 0.9, 0.88, 0.2)
    play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere1_01.ogg"
    brut "{i}Hey feignasse ! Beaudrik ! Viens ici !{/i}"
    show char_brutal colere:
        xalign 0.5 yalign 0.8
        xpos 0.1 ypos 0.6 zoom 0.2 rotate 45
        linear 2.5 xpos -1.0 ypos 1.5
    pause 1.0
    hide char_brutal
    show char_beaudrik choque left at speakingAnim(0.8, 0.9, 0.88, 0.2)
    play sound "sfx/Voices/Beaudrik/Char_Beaudrik_Insult_02.ogg"
    bg "Oh non, papa m’appelle encore."
    show char_beaudrik normal left at speakingAnim(0.8, 0.9, 0.88, 0.2)
    bg "Bon, vaut mieux que je me casse."
    show char_beaudrik mepris left at speakingAnim(0.8, 0.9, 0.88, 0.2)
    bg "De tout façon je dois aller régler un truc avec Josiane, l’autre fiancée."

jump forge_Beaudrik_05_Josiane

#------------------------------------------#

label forge_Beaudrik_05_Josiane:
    
    show char_beaudrik normal left at notSpeakingAnim(0.8, 0.9, 0.88, 0.2)
    menu:
        bg "{cps=0}De tout façon je dois aller régler un truc avec Josiane, l’autre fiancée.{/cps}"
        "Deux fiancées ? C’est abusé" :
            y "Non mais attends, moi je me trimballe Ernust et toi tu pécho des meufs à droite et à gauche ?"
            y "C'est abusé."
            show char_beaudrik mepris left at speakingAnim(0.8, 0.9, 0.88, 0.2)
            $ loveGauge(beau_char, -5, 0.85, 0.10)
            play sound "sfx/Voices/Beaudrik/Char_Beaudrik_Mepris_02.ogg"
            bg "Euh, je sais, c’est compliqué."
        "Tu ferais ça à Ingrid ?" :
            y "Deux copines, c’est un peu abusé et pas très gentil quand même."
            y "Tu penses pas que ça briserait le cœur à Ingrid ?"
            play sound "sfx/Voices/Beaudrik/Char_Beaudrik_Mepris_02.ogg"
            show char_beaudrik mepris left at speakingAnim(0.8, 0.9, 0.88, 0.2)
            $ loveGauge(beau_char, -5, 0.85, 0.10)
            bg "Euh, je sais, c’est compliqué."
        "Brutalmund a l’air vénère" :
            y "Et ton père ? Il a pas l’air d’être content."
            show char_beaudrik normal left at speakingAnim(0.8, 0.9, 0.88, 0.2)
            play sound "sfx/Voices/Beaudrik/Char_Beaudrik_Mepris_06.ogg"
            bg "Oui, il s’est mis en tête que je dois travailler pour gagner ma vie."
            show char_beaudrik mepris left at speakingAnim(0.8, 0.9, 0.88, 0.2)
            bg "Mais là j’ai des questions de meufs à régler."

jump forge_Beaudrik_06_leaving

#------------------------------------------#

label forge_Beaudrik_06_leaving:
    
    show char_beaudrik mepris left at speakingAnim(0.8, 0.9, 0.88, 0.2)
    bg "Heureusement que toi tu n’as pas ce genre de problèmes, Gaufrid ! Je t’envie mon pote."
    show char_beaudrik normal left at speakingAnim(0.8, 0.9, 0.88, 0.2)
    bg "Bon, je me casse, avant que Papa arrive. Josiane m’attend à la taverne."
    show char_beaudrik drague right at speakingAnim(0.7, 0.9, 0.88, 0.22)
        #zoom 0.23 xpos 0.4 ypos 0.09
    hide screen datingSim
    play sound "sfx/Voices/Beaudrik/Char_Beaudrik_Normal_04.ogg"
    bg "À plus !"
    show char_beaudrik drague right :
        zoom 0.23 xpos 0.7 ypos 0.9
        linear 1.0 xpos 1.5
    pause 1
    hide char_beaudrik drague right
    pause 1.0
    play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere1_03.ogg"
    brut "Beaudrik !"
    
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
    brut "Tiens ! Je cherche un couillon, j’en trouve un autre !"
    show char_brutal heureux at speakingAnim(0.52, 0.93, 0.91, 0.35)
    show screen datingSim(brut_char, 0.57, 0.15)
    play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Heureux_02.ogg"
    brut "Ahahahah !"
    show char_brutal normal
    brut "Tu n’aurais pas vu mon fils ?"

    jump forge_Brutalmund_02
    
#------------------------------------------#

label forge_Brutalmund_02:
    
    show char_brutal normal at notSpeakingAnim(0.52, 0.93, 0.91, 0.35)
    menu:
        brut "{cps=0}Tu n’aurais pas vu mon fils ?{/cps}"
        "Pas vraiment, non" :
            y "Je l’ai pas vu, non. Pourquoi ?"
            show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.35)
            if Acte1_Tour_CoupableJugement == "Crossfit":
                show char_brutal colere at speakingAnim(0.52, 0.93, 0.91, 0.35)
                play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere1_03.ogg"
                brut "Il était censé surveiller les {b}boucliers{/b} pendant que j'allais checher les buffles !"
                show char_brutal colere at speakingAnim(0.52, 0.93, 0.91, 0.35)
                brut "Je vais le tuer !"
            if Acte1_Tour_CoupableJugement == "Brutalmund":
                show char_brutal colere at speakingAnim(0.52, 0.93, 0.91, 0.35)
                $ loveGauge(brut_char, -5, 0.57, 0.15)
                play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere1_01.ogg"
                brut "Car grâce à toi, mon p’tit interprète, on n’a plus de quoi bouffer !"
                show char_brutal colere at speakingAnim(0.52, 0.93, 0.91, 0.35)
                brut "Et tous ces {b}boucliers{/b} ne vont pas se vendre tous seuls !"
            show char_brutal colere at notSpeakingAnim(0.52, 0.93, 0.91, 0.35)
            y "Bon, il faudra que vous alliez chercher votre fils alors, non ?"
            show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.35)
            play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere1_04.ogg"
            brut "Et te laisser là tout seul avec mes précieux boucliers ?"
            show char_brutal colere at speakingAnim(0.52, 0.93, 0.91, 0.35)
            brut "Hors question !"
        "Il est à la taverne" :
            y "Il allait à la taverne, vous faites encore à temps pour l’attraper."
            show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.35)
            play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere1_04.ogg"
            brut "Et te laisser là tout seul avec mes précieux {b}boucliers{/b} ?"
            show char_brutal colere at speakingAnim(0.52, 0.93, 0.91, 0.35)
            brut "Hors question !"
            if Acte1_Tour_CoupableJugement == "Crossfit":
                jump forge_Brutalmund_03
            if Acte1_Tour_CoupableJugement == "Brutalmund":
                $ loveGauge(brut_char, -5, 0.57, 0.15)
                play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere1_02.ogg"
                brut "Tu m’as déjà dévalisé une fois avec cette histoire de buffles, tu ne m’auras pas une deuxième fois ! Ha !"

jump forge_Brutalmund_03

#------------------------------------------#

label forge_Brutalmund_03:
    
    show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.35)
    play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere2_02.ogg"
    brut "Et de toute façon ça sert à rien, Beaudrik c’est vraiment une cause perdue."
    show char_brutal colere at speakingAnim(0.52, 0.93, 0.91, 0.35)
    brut "Je le savais que j’aurais dû le jeter d’une falaise quand il est né !"
    show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.35)
    brut "Le troisième téton, c’était pas bon signe."
    show char_brutal normal at notSpeakingAnim(0.52, 0.93, 0.91, 0.35)
    menu:
        brut "{cps=0}Le troisième téton, c’était pas bon signe.{/cps}"
        "Trois tétons, c'est pas si grave" :
            y "Bon, c’est pas sa faute non plus s’il est né comme ça."
            y "Je pense que les enfants comme lui, ils ont besoin d’encore plus d’amour que les gens normaux."
            show char_brutal colere at speakingAnim(0.52, 0.93, 0.91, 0.35)
            play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere1_02.ogg"
            brut "C’est ce que sa mère disait aussi ! Et ça l’a ruiné ! Ruiné je te dis !"
        "En quoi c’est mauvais signe ?" :
            y "Ah bon ? Trois tétons c’est mauvais signe ?"
            show char_brutal colere at speakingAnim(0.52, 0.93, 0.91, 0.35)
            $ loveGauge(brut_char, -5, 0.57, 0.152)
            play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere1_02.ogg"
            brut "Mais enfin, Veléda ne t’a rien appris ?"
            show char_brutal colere at notSpeakingAnim(0.52, 0.93, 0.91, 0.35)
            y "Euh, nous on fait plutôt des prophéties. Les tétons en rab c’est pas trop notre truc."
            show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.35)
            play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Normal_05.ogg"
            brut "Et alors je t’explique..."
            show char_brutal colere at speakingAnim(0.52, 0.93, 0.91, 0.35)
            brut "Le troisième téton, c’est signe de faiblesse !"
        "Les gens comme lui, c’est des monstres" :
            y "C’est des punitions divines, les êtres comme lui."
            y "C’est peut-être pas trop tard, je vous accompagne à la falaise la plus proche ?"
            show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.35)
            $ loveGauge(brut_char, +5, 0.57, 0.15)
            play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere2_04.ogg"
            brut "Non mais là c’est mort, il fallait le faire avant."
            brut "J’ai essayé de le lâcher de l’autre côté de la Lippe, mais il revient toujours."
        "D'autres secrets bizarres sur lui ?":
            y "Ah ! Ça, ça m’intéresse."
            y "Vous savez si votre fils a d’autres secrets gênants comme celui-là ?"
            show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.35)
            play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Normal_05.ogg"
            brut "Ha ! Tu veux connaitre son secret ?"
            
    jump forge_Brutalmund_04

#------------------------------------------#

label forge_Brutalmund_04:
    
    show char_brutal colere at speakingAnim(0.52, 0.93, 0.91, 0.35)
    brut "On l’a gâté, ce petit enfoiré !"
    brut "Tu sais qu’il dort avec un nounours car il a peur du noir ?"
    brut "Genre tu l’as vu ? Il fait deux mètres cet abrouti !"
    show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.35)
    brut "Enfin bref."
    show char_brutal heureux at speakingAnim(0.52, 0.93, 0.91, 0.35)
    play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Heureux_03.ogg"
    brut "J’imagine que tu n’as pas besoin d’un {b}Bouclier Original de Capitaine Germanie™{/b}, hein ?"
    show char_brutal heureux at notSpeakingAnim(0.52, 0.93, 0.91, 0.35)
    jump forge_Brutalmund_04_choice
    
#-------------------------------------------#

label forge_Brutalmund_04_choice:
    
    menu:
        brut "{cps=0}J’imagine que tu n’as pas besoin d’un {b}Bouclier Original de Capitaine Germanie™{/b}, hein ?{/cps}"
        "{color=#FFFFFF}C'est possible un bouclier normal ?{/color}":
            y "Vous avez des sous-marques ? Je fais des economies."
            show char_brutal colere at speakingAnim(0.52, 0.93, 0.91, 0.35)
            $ loveGauge(brut_char, -5, 0.57, 0.15)
            play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere1_01.ogg"
            brut "Gaufrid, tu crois être où, chez Leader Price ?"
            show char_brutal heureux at speakingAnim(0.52, 0.93, 0.91, 0.35)
            brut "Ici, c'est que des {b}Bouclier Originaux de Capitaine Germanie™{/b}"
            show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.35)
            brut "Prendre ou laisser."
            show char_brutal normal at notSpeakingAnim(0.52, 0.93, 0.91, 0.35)
            jump forge_Brutalmund_04_choice
        "On peut le voir avant d'acheter ?":
            y "Ça m’intéresse, mais comment on sait s’ils sont bien ? On ne peut pas les voir ?"
            show char_brutal surpris at speakingAnim(0.52, 0.93, 0.91, 0.35)
            $ loveGauge(brut_char, -5, 0.57, 0.15)
            play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Choc_01.ogg"
            brut "Ah bah là tu me brise le cœur, mon p’tit Gaufrid !"
            show char_brutal heureux at speakingAnim(0.52, 0.93, 0.91, 0.35)
            brut "Mes {b}Boucliers Originaux de Capitaine Germanie™{/b}, c’est de la balle !"
            show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.35)
            brut "Je te promets."
            jump forge_Brutalmund_04_01_Branche_EssaiRoutier
        "Je ne peux pas payer...":
            jump forge_Brutalmund_05_CannotPay
            
    jump forge_Brutalmund_05_CannotPay

#-----------------------------------------#

label forge_Brutalmund_04_01_Branche_EssaiRoutier:
    
    show char_brutal normal at notSpeakingAnim(0.52, 0.93, 0.91, 0.35)
    menu:
        brut "{cps=0}Je te promets.{/cps}"
        "Ça sent l'arnaque...":
            y "Non mais c’est bon, là vous abusez. Vous seriez pas en train de m'arnaquer ?"
            show char_brutal surpris at speakingAnim(0.52, 0.93, 0.91, 0.35)
            $ loveGauge(brut_char, -5, 0.57, 0.15)
            play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Choc_01.ogg"
            brut "Qui ?! Moi ?!"
            show char_brutal surpris at speakingAnim(0.52, 0.93, 0.91, 0.35)
            brut "Moi je veux juste te faire gagner du temps, hein !"
            show char_brutal heureux at speakingAnim(0.52, 0.93, 0.91, 0.35)
            brut "Pourquoi perdre ton temps à les regarder, mon p’tit Gaufrid, quand tu peux directement les acheter ?"
            jump forge_Brutalmund_05_CannotPay
        "J'irai voir votre concurrent alors":
            y "Oui mais, le fait est que je suis indécis entre les vôtres et ceux de Crossfitrichentruc."
            show char_brutal surpris at speakingAnim(0.52, 0.93, 0.91, 0.35)
            play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Choc_01.ogg"
            brut "Ah bon !? Déjà il m'accuse de vol, et là il me fait concurrence aussi ?!"
            show char_brutal colere at speakingAnim(0.52, 0.93, 0.91, 0.35)
            play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere1_02.ogg"
            brut "Ha ! Là j’en peux plus mon p’tit Gaufrid, j’en peux plus je te dis !"
            brut "Je vais lui dire ses quatre verités."
            show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.35)
            hide screen datingSim
            brut "Attends-moi ici, je reviens dans une minute."
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
            brut "Et ne touche à rien !"
            show char_brutal colere:
                xalign 0.5 yalign 0.8
                xpos 0.1 ypos 1.1 zoom 0.35 rotate 30
                linear 1.0 xpos -1.0 ypos 2.0
            pause 1.5
            hide char_brutal
            jump forge_Brutalmund_07_Bouclier
            
        "En tout cas je ne peux pas payer…":
            jump forge_Brutalmund_05_CannotPay
        

#------------------------------------------#

label forge_Brutalmund_05_CannotPay:

    show char_brutal normal at notSpeakingAnim(0.52, 0.93, 0.91, 0.35)
    y "Euh, je veux bien, mais en tout cas je n’ai pas de quoi le troquer avec."
    show char_brutal surpris at speakingAnim(0.52, 0.93, 0.91, 0.35)
    play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Normal_05.ogg"
    brut "Rien du tout ? Allez mon p’tit Gaufrid, ça fait deux mois que je ne vends rien, fais un effort !"
    show char_brutal heureux at speakingAnim(0.52, 0.93, 0.91, 0.35)
    play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Char_Brutalmund_Heureux_02.ogg"
    brut "Là on parle de mes {b}Boucliers Originaux de Capitaine Germanie™{/b}, hein !"
    show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.35)
    brut "Il me faut quelque chose de valeur si t'en veux un."
    $ Acte2_Forge_FirstVisit = 1

jump forge_Brutalmund_06_Hub

#------------------------------------------#

label forge_Brutalmund_06_Hub:
    show char_brutal normal at notSpeakingAnim(0.52, 0.93, 0.91, 0.35)
    menu:
        brut "..."
        "Vos buffles sont en liberté..." if _testLunettes == 1:
            y "Si ça vous intéresse, j’ai récupéré vos buffles."
            show char_brutal heureux at speakingAnim(0.52, 0.93, 0.91, 0.35)
            $ loveGauge(brut_char, +10, 0.57, 0.15)
            play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Char_Brutalmund_Heureux_01.ogg"
            brut "Oh ! Ha ha ! Je le savais mon p’tit Gaufrid !"
            brut "Tu sers enfin à quelque chose !"
            #show char_brutal normal at notSpeakingAnim(0.52, 0.93, 0.91, 0.4)
            #y "Enfin, presque…"
            #show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.4)
            #brut "Euh ? Comment ça ?"
            #show char_brutal normal at notSpeakingAnim(0.52, 0.93, 0.91, 0.4)
            y "Enfin, je les ai libérés des étables, maintenant il faut aller les chercher."
            show char_brutal heureux at notSpeakingAnim(0.52, 0.93, 0.91, 0.35)
            pause 1.0
            show char_brutal surpris at notSpeakingAnim(0.52, 0.93, 0.91, 0.35)
            pause 1.0
            show char_brutal colere at speakingAnim(0.52, 0.93, 0.91, 0.35)
            $ loveGauge(brut_char, -15, 0.57, 0.15)
            play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere1_04.ogg"
            brut "Mais tu le fais exprès alors ! Ahh !"
            hide screen datingSim
            brut "Attends ici, je vais les chercher !"
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
            brut "Et ne touche à rien ! Tu n'auras pas de bouclier tant que je ne les aurai pas trouvés !"
            show char_brutal colere:
                xalign 0.5 yalign 0.8
                xpos 0.1 ypos 1.1 zoom 0.35 rotate 30
                linear 1.0 xpos -1.0 ypos 2.0
            pause 1.5
            hide char_brutal
            jump forge_Brutalmund_07_Bouclier
            
        "{color=#FFFFFF}Vous voulez quoi en échange ?{/color}":
            y "Bon, d’accord, admettons que je puisse vous payer. Vous voulez quoi en échange ?"
            show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.35)
            if Acte1_Tour_CoupableJugement == "Brutalmund":
                play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Normal_06.ogg"
                brut "Si tu trouves un moyen de me fournir un ou deux buffles… Tu sais, j’ai perdu les miens…"
                show char_brutal normal at notSpeakingAnim(0.52, 0.93, 0.91, 0.35)
                y "Vous pensez que je vous aurais imploré de me donner un bouclier si j’avais des buffles en rab ?"
                show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.35)
                brut "J’ai pas dit qu’il faut que ça soit tes buffles à toi, hein !"
                brut "Allez, mon p’tit Gaufrid ! T’es peut-être un peu un boulet, mais on sait tous les deux que t’es un débrouilleur."
                brut "Un petit litige, une prophétie… j’suis sûr que tu vas trouver une solution."
            if Acte1_Tour_CoupableJugement == "Crossfit":
                show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.35)
                play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Normal_06.ogg"
                brut "Crossfit a un peu de mal avec les buffles."
                brut "Si tu pouvais accélerer les choses... ce serait parfait."
                show char_brutal heureux at speakingAnim(0.52, 0.93, 0.91, 0.35)
            play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Heureux_03.ogg"
            brut "Amène-moi mes buffles et t’auras ton {b}Bouclier Original de Capitaine Germanie™{/b} !"
            jump forge_Brutalmund_06_Hub
            
        "Je n’ai rien à vous donner":
            y "Au moins que vous vouliez vous acheter un Ernust, je n’ai rien à vous donner pour le moment."
            show char_brutal colere at speakingAnim(0.52, 0.93, 0.91, 0.35)
            if forge_cannotpay_check == 0:
                $ loveGauge(brut_char, -5, 0.57, 0.15)
                $ forge_cannotpay_check = 1
            play sound "sfx/Voices/Brutalmund/Char_Brutalmund_Colere1_01.ogg"
            brut "Et alors dégage bonhomme ! J’ai du travail."
            show char_brutal heureux at speakingAnim(0.52, 0.93, 0.91, 0.35)
            brut "Reviens quand t’auras de quoi payer mon {b}Bouclier Original de Capitaine Germanie™{/b} !"
            hide screen datingSim

            stop music1 fadeout 1.5
            stop ambiance fadeout 0.5

            jump PlaceDuVillageDefault

#---------------------------------------------------#

label forge_Brutalmund_07_Bouclier:

    stop music1 fadeout 1.5
    
    hide  char_brutal
    y "Bon, c’était pas très dur."
    y "Vaut mieux choper un bouclier et se casser, vite !"
    $ inventory.add(bouclier)
    $ _testBouclier = 1
    show img_bouclier at center:
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
    
    stop ambiance fadeout 0.5

    if _testGlaive == 1 & _testBouclier == 1:
        jump PlaceDuVillageAllObjects
    else:
        jump PlaceDuVillageDefault
    
#--------Backup Conditions et Variables-------------#

#    if _testBlague == 1:
#        menu:
#            "Retour Place du Village":
#                jump PlaceDuVillageDefault
#            "Donner la blague":
#                jump forge_BrutalMundBlaguePart2
#    else:
#        "Pas de blague..."
#        jump PlaceDuVillageDefault

# -----------------------------------------#

#label forge_BrutalMundBlaguePart2:
#    "Entrée forge_BrutalMundBlaguePart2"
#    
#    $ inventory.add(bouclier)
#    $ _testBouclier = 1
#    
#    "Bouclier récupéré"
#    
#    if _testGlaive == 1 & _testBouclier == 1:
#        jump PlaceDuVillageAllObjects
#    else:
#        jump PlaceDuVillageDefault
    
jump PlaceDuVillageDefault   