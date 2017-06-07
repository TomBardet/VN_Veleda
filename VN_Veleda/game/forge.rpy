####################################################
# Ici figurent les scènes se déroulant à la Forge. #
####################################################

label forge_BrutalmundEtBeaudrik:

    if Acte2_Forge_FirstVisit == 0:
        jump forge_Intro
    if Acte2_Forge_FirstVisit == 1:
        jump forge_Brutalmund_Tampon_HUB
        
# ----------------------------------------- #

label forge_Brutalmund_Tampon_HUB:

    scene bg_forge
    pause 0.5
    show char_brutal normal :
        zoom 0.4 xpos -0.5 ypos 0.05
        linear 0.7 xpos 0.2
    brut "Gaufrid !"
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
    bg "Tiens ! C’est le p’tit Gaufrid !"
    bg "T’sais, justement je pensais à toi bonhomme."
    show char_beaudrik normal left at notSpeakingAnim(0.8, 0.9, 0.88, 0.2)
    y "Ah, merci Beaudrik ! Je suis flatté."
    show char_beaudrik mepris left at speakingAnim(0.8, 0.9, 0.88, 0.2)
    bg "J’ai entendu des rumeurs comme quoi tu veux épouser Ingrid !"
    show char_beaudrik drague right at speakingAnim(0.7, 0.9, 0.88, 0.22)
        #zoom 0.22 xpos 0.4 ypos 0.09
    bg "C’est tellement n’importe quoi ! Ahahah."
    show char_beaudrik normal left at speakingAnim(0.8, 0.9, 0.88, 0.2)
        #zoom 0.2 xpos 0.6 ypos 0.09
    bg "On entend vraiment des trucs drôles à la taverne, quand les gens se bourrent la gueule."

jump forge_Beaudrik_03_EpouserIngrid
    
#------------------------------------------#

label forge_Beaudrik_03_EpouserIngrid:
    
    show char_beaudrik normal left at notSpeakingAnim(0.8, 0.9, 0.88, 0.2)
    menu:
        bg "On entend vraiment des trucs drôles à la taverne, quand les gens se bourrent la gueule."
        "Ouais… très drôles" :
            y "Euh… heureusement que c’est juste des rumeurs."
            show char_beaudrik normal left at speakingAnim(0.8, 0.9, 0.88, 0.2)
            bg "Ouais, grave ! Ça aurait été dommage que je te casse la gueule."
            jump forge_Beaudrik_04
        "Ça ne te regarde pas" :
            y "Euh… oh ! Ce qu’il se passe entre Ingrid et moi, ça ne te regarde pas !"
            show char_beaudrik normal left at speakingAnim(0.8, 0.9, 0.88, 0.2)
            bg "Ahahahah !"
            bg "Vraiment, tu me tues mon pote. T’as raison, faut jouer le jeu."
            bg "En tout cas, c’est bien que ce ne soit qu’une rumeur."
            bg "Ça aurait été dommage que je te casse la gueule."
            jump forge_Beaudrik_04
        "On va se marier pour de vrai !" :
            y "Euh… oui, mais tu sais, Ingrid et moi on va se marier vraiment !"
            show char_beaudrik normal left at speakingAnim(0.8, 0.9, 0.88, 0.2)
            bg "Ahahahah !"
            bg "Vraiment, tu me tues mon pote. T’as raison, faut jouer le jeu."
            bg "En tout cas, c’est bien que ce ne soit qu’une rumeur."
            bg "Ça aurait été dommage que je te casse la gueule."
            jump forge_Beaudrik_04
        
#------------------------------------------#

label forge_Beaudrik_04:

    bg "Tu sais, c’est moi qui vais marier la gonzesse. J’ai une dot et tout."
    bg "J’aime beaucoup les femmes mais là j’ai envie de me poser."
    bg "T’sais, d’avoir quelqu’un qui me fasse des câlins et la vaisselle."
    show char_beaudrik normal left at notSpeakingAnim(0.8, 0.9, 0.88, 0.2)
    brut "Euh feignasse ! Beaudrik ! Viens ici !"
    show char_beaudrik normal left at speakingAnim(0.8, 0.9, 0.88, 0.2)
    bg "Tsk, papa m’appelle encore."
    bg "Bon, moi je dois aller régler un truc avec Josiane, l’autre fiancée."

jump forge_Beaudrik_05_Josiane

#------------------------------------------#

label forge_Beaudrik_05_Josiane:
    
    show char_beaudrik normal left at notSpeakingAnim(0.8, 0.9, 0.88, 0.2)
    menu:
        bg "Bon, moi je dois aller régler un truc avec Josiane, l’autre copine."
        "Deux fiancées ? C’est abusé" :
            y "Non mais attends, moi je me trimballe Ernust et toi tu pécho des meufs à droite et à gauche ?"
            y "C'est abusé."
            show char_beaudrik normal left at speakingAnim(0.8, 0.9, 0.88, 0.2)
            bg "Euh, je sais, c’est compliqué."
        "Tu ferais ça à Ingrid ?" :
            y "Deux copines, c’est un peu abusé et pas très gentil quand même."
            y "Tu penses pas que ça briserait le cœur à Ingrid ?"
            show char_beaudrik normal left at speakingAnim(0.8, 0.9, 0.88, 0.2)
            bg "Euh, je sais, c’est compliqué."
        "Brutalmund a l’air vénère" :
            y "Et ton père ? Il a pas l’air d’être content."
            show char_beaudrik normal left at speakingAnim(0.8, 0.9, 0.88, 0.2)
            bg "Oui, il s’est mis en tête que je dois travailler pour gagner ma vie."
            bg "Mais là j’ai des questions de meufs à régler."

jump forge_Beaudrik_06_leaving

#------------------------------------------#

label forge_Beaudrik_06_leaving:
    
    bg "Heureusement que toi tu n’as pas ce genre de problèmes, Gaufrid ! Je t’envie mon pote."
    bg "Bon, je me casse, avant que Papa arrive. Josiane m’attend à la taverne."
    show char_beaudrik drague right at speakingAnim(0.7, 0.9, 0.88, 0.22)
        #zoom 0.23 xpos 0.4 ypos 0.09
    bg "À plus !"
    show char_beaudrik drague right :
        zoom 0.23 xpos 0.7 ypos 0.9
        linear 1.0 xpos 1.5
    pause 1
    hide char_beaudrik drague right
    pause 1.0
    brut "Beaudrik !"
    
    jump forge_Brutalmund_01
    
#------------------------------------------#

label forge_Brutalmund_01:
    
    show char_brutal normal :
        xalign 0.5 yalign 0.8
        zoom 0.4 xpos -0.5 ypos 0.77
        linear 0.7 xpos 0.52
    pause 0.9
    show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.4)
    brut "..."
    show char_brutal normal
    brut "Ah ! Je cherche un couillon, j’en trouve un autre !"
    show char_brutal heureux
    brut "Ahahahah !"
    show char_brutal normal
    brut "Tu n’aurais pas vu mon fils ?"

    jump forge_Brutalmund_02
    
#------------------------------------------#

label forge_Brutalmund_02:
    
    show char_brutal normal at notSpeakingAnim(0.52, 0.93, 0.91, 0.4)
    menu:
        brut "Tu n’aurais pas vu mon fils ?"
        "Pas vraiment, non" :
            y "Je l’ai pas vu, non. Pourquoi ?"
            show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.4)
            if Acte1_Tour_CoupableJugement == "Crossfit":
                brut "Il était censé surveiller les {b}boucliers{/b} pendant que j'allais checher les buffles !"
                brut "Je vais le tuer !"
            if Acte1_Tour_CoupableJugement == "Brutalmund":
                brut "Car grâce à toi, mon p’tit interprète, on n’a plus de quoi bouffer !"
                brut "Et tous ces {b}boucliers{/b} ne vont pas se vendre tous seuls !"
            show char_brutal normal at notSpeakingAnim(0.52, 0.93, 0.91, 0.4)
            y "Bon, il faudra que vous alliez chercher votre fils alors, non ?"
            show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.4)
            brut "Et te laisser là tout seul avec mes précieux boucliers ? Hors question !"
        "Il est à la taverne" :
            y "Il allait à la taverne, vous faites encore à temps pour l’attraper."
            show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.4)
            brut "Et te laisser là tout seul avec mes précieux {b}boucliers{/b} ? Hors question !"
            if Acte1_Tour_CoupableJugement == "Crossfit":
                jump forge_Brutalmund_03
            if Acte1_Tour_CoupableJugement == "Brutalmund":
                brut "Tu m’as déjà dévalisé une fois avec cette histoire de buffles, tu ne m’auras pas une deuxième fois ! Ha !"

jump forge_Brutalmund_03

#------------------------------------------#

label forge_Brutalmund_03:
    
    brut "Et de toute façon ça sert à rien, Beaudrik c’est vraiment une cause perdue."
    brut "Je le savais que j’aurais dû le jeter d’une falaise quand il est né !"
    brut "Le troisième téton, c’était pas bon signe."
    show char_brutal normal at notSpeakingAnim(0.52, 0.93, 0.91, 0.4)
    menu:
        brut "Le troisième téton, c’était pas bon signe."
        "Trois tétons, c'est pas si grave" :
            y "Bon, c’est pas sa faute non plus s’il est né comme ça."
            y "Je pense que les enfants comme lui, ils ont besoin d’encore plus d’amour que les gens normaux."
            show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.4)
            brut "C’est ce que sa mère disait aussi ! Et ça l’a ruiné ! Ruiné je te dis !"
        "En quoi c’est mauvais signe ?" :
            y "Ah bon ? Trois tétons c’est mauvais signe ?"
            show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.4)
            brut "Mais enfin, Veléda ne t’a rien appris ?"
            show char_brutal normal at notSpeakingAnim(0.52, 0.93, 0.91, 0.4)
            y "Euh, nous on fait plutôt des prophéties. Les tétons en rame c’est pas trop notre truc."
            show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.4)
            brut "Et alors je t’explique..."
            brut "Le troisième téton, c’est signe de faiblesse !"
        "Les gens comme lui, c’est des monstres" :
            y "C’est des punitions divines, les êtres comme lui."
            y "C’est peut-être pas trop tard, je vous accompagne à la falaise la plus proche ?"
            show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.4)
            brut "Non mais là c’est mort, il fallait le faire avant."
            brut "J’ai essayé de le lâcher de l’autre côté de la Lippe, mais il revient toujours."
        "D'autres secrets bizarres sur lui ?":
            y "Ah ! Ça, ça m’intéresse."
            y "Vous savez si votre fils a d’autres secrets gênants comme celui-là ?"
            show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.4)
            brut "Ha ! Tu veux connaitre son secret ?"
            
    jump forge_Brutalmund_04

#------------------------------------------#

label forge_Brutalmund_04:
    
    brut "On l’a gâté, ce petit enfoiré !"
    brut "Tu sais qu’il dort avec un nounours car il a peur du noir ?"
    brut "Genre tu l’as vu ? Il fait deux mètres cet abrouti !"
    brut "Enfin bref."
    brut "J’imagine que tu n’as pas besoin d’un {b}Bouclier-Traineau à trois vitesses™{/b}, hein ?"
    jump forge_Brutalmund_04_choice
    
#-------------------------------------------#

label forge_Brutalmund_04_choice:
    
    show char_brutal normal at notSpeakingAnim(0.52, 0.93, 0.91, 0.4)
    menu:
        "{color=#FFFFFF}Juste le bouclier, sans traineau{/color}":
            y "C’est possible sans traineau ? Je fais des économies."
            show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.4)
            brut "Gaufrid, tu m’as pris pour qui, le Burger King ?"
            brut "Mes {b}Boucliers-Traineaux à trois vitesses™{/b}, je les vends comme ça, prendre ou laisser."
            jump forge_Brutalmund_04_choice
        "On peut faire un essai routier ?":
            y "Ça m’intéresse, mais comment on sait s’il roule bien ? Il me faudrait au moins un essai routier."
            show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.4)
            brut "Ah bah là tu me brise le cœur, mon p’tit Gaufrid !"
            brut "Mes {b}Boucliers Originaux de Capitaine Germanie™{/b}, c’est de la balle !"
            brut "Je te promets ! Pas besoin d’essayer !"
            jump forge_Brutalmund_04_01_Branche_EssaiRoutier
        "Je ne peux pas payer...":
            jump forge_Brutalmund_05_CannotPay
            
    jump forge_Brutalmund_05_CannotPay

#-----------------------------------------#

label forge_Brutalmund_04_01_Branche_EssaiRoutier:
    
    show char_brutal normal at notSpeakingAnim(0.52, 0.93, 0.91, 0.4)
    menu:
        brut "Je te promets ! Pas besoin d’essayer !"
        "Ça sent l'arnaque...":
            y "Non mais c’est bon, là vous abusez. On peut au moins les voir, ces boucliers ?"
            show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.4)
            brut "Mais pourquoi perdre ton temps à les regarder, mon p’tit Gaufrid, quand tu peux directement les acheter !"
            brut "Acheter je te dis !"
            jump forge_Brutalmund_05_CannotPay
        "J'irai voir votre concurrent":
            y "Oui mais, le fait est que je suis indécis entre les vôtres et ceux de Crossfitrichentruc."
            show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.4)
            brut "Ah bon !? Déjà il m'insulte, et là il me fait concurrence aussi ?!"
            brut "Ha ! Là j’en peux plus mon p’tit Gaufrid, j’en peux plus je te dis !"
            brut "Je vais lui dire ses quatre verités."
            brut "Attends-moi ici, je reviens dans une minute."
            brut "Et ne touche à rien !"
            hide char_brutal
            pause 1.5
            jump forge_Brutalmund_07_Bouclier
            
        "En tout cas je ne peux pas payer…":
            jump forge_Brutalmund_04
        

#------------------------------------------#

label forge_Brutalmund_05_CannotPay:

    y "Euh, je veux bien, mais en tout cas je n’ai pas de quoi le troquer avec."
    show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.4)
    brut "Rien du tout ? Allez mon p’tit Gaufrid, ça fait deux mois que je ne vends rien, fais un effort !"
    brut "Là on parle de mes {b}Boucliers-Traineaux à trois vitesses™{/b}, hein !"
    show char_brutal normal at notSpeakingAnim(0.52, 0.93, 0.91, 0.4)
    y "Un ongle mâchouillé, ça vous tente ?"
    show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.4)
    brut "Ne plaisante pas, tu sais que j’ai arrêté !"
    brut "$$$ Il me faut quelque chose de valeur si tu veux un bouclier"
    $ Acte2_Forge_FirstVisit = 1

jump forge_Brutalmund_06_Hub

#------------------------------------------#

label forge_Brutalmund_06_Hub:
    show char_brutal normal at notSpeakingAnim(0.52, 0.93, 0.91, 0.4)
    menu:
        "Vos buffles sont en liberté..." if _testLunettes == 1:
            y "Si ça vous intéresse, j’ai récupéré vos buffles."
            show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.4)
            brut "Oh ! Ha ha ! Je le savais mon p’tit Gaufrid !"
            brut "Tu sers enfin à quelque chose !"
            show char_brutal normal at notSpeakingAnim(0.52, 0.93, 0.91, 0.4)
            y "Enfin, presque…"
            show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.4)
            brut "Euh ? Comment ça ?"
            show char_brutal normal at notSpeakingAnim(0.52, 0.93, 0.91, 0.4)
            y "Bon, je les ai libérés des étables, maintenant il faut aller les chercher."
            show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.4)
            brut "Mais tu le fais exprès alors ! Ahh !"
            brut "Attends ici, je vais les chercher !"
            brut "Et touche à rien ! T’auras pas de bouclier tant que je ne les aurai pas trouvés !"
            hide char_brutal
            pause 1.5
            jump forge_Brutalmund_07_Bouclier
            
        "{color=#FFFFFF}Vous voulez quoi en échange ?{/color}":
            y "Bon, d’accord, admettons que je puisse vous payer. Vous voulez quoi en échange ?"
            show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.4)
            brut "Si tu trouves un moyen de me fournir un ou deux buffles… Tu sais,  j’ai perdu les miens…"
            show char_brutal normal at notSpeakingAnim(0.52, 0.93, 0.91, 0.4)
            y "Vous pensez que je vous aurais imploré de me donner un bouclier si j’avais des buffles en rame ?"
            show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.4)
            brut "J’ai pas dit qu’il faut que ça soit tes buffles à toi, hein !"
            brut "Allez, mon p’tit Gaufrid ! T’es peut-être un peu un boulet, mais on sait tous les deux que t’es un débrouilleur."
            brut "Un petit litige, une prophétie… j’suis sûr que tu vas trouver une solution."
            brut "Trouve-moi des buffles et t’auras ton {b}Bouclier-Traineau à trois vitesses™{/b} !"
            jump forge_Brutalmund_06_Hub
            
        "Je n’ai rien à vous donner":
            y "Au moins que vous vouliez vous acheter un Ernust, je n’ai rien à vous donner pour le moment."
            show char_brutal normal at speakingAnim(0.52, 0.93, 0.91, 0.4)
            brut "Bon, alors dégage bonhomme ! J’ai du travail." 
            brut "Reviens quand t’auras de quoi payer mon {b}Bouclier-Traineau à trois vitesses™{/b} !"
            jump PlaceDuVillageDefault

#---------------------------------------------------#

label forge_Brutalmund_07_Bouclier:

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
    y "Bon... Ben c'était pas si dur"

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