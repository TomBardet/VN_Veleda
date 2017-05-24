####################################################
# Ici figurent les scènes se déroulant à la Forge. #
####################################################

label forge_BrutalmundEtBeaudrik:
    
    jump forge_Intro

# -----------------------------------------#

label forge_Intro:
    
    scene bg_forge
    "label forge_Intro"
    y "Euh... il y a quelqu'un ?"
    
    jump forge_Beaudrik_01

# -----------------------------------------#

label forge_Beaudrik_01:

    "label forge_Beaudrik_01"
    show char_beaudrik normal left :
        zoom 0.2 xpos 1.0 ypos 0.09
        linear 0.4 xpos 0.6

jump forge_Beaudrik_02
    
# -----------------------------------------#

label forge_Beaudrik_02:

    bg "Tiens ! C’est le p’tit Gaufrid !"
    bg "T’sais, justement je pensais à toi bonhomme."
    y "Ah, merci Beaudrik ! Je suis flatté."
    show char_beaudrik mepris left
    bg "J’ai entendu des rumeurs comme quoi tu veux épouser Ingrid !"
    show char_beaudrik drague right :
        zoom 0.22 xpos 0.4 ypos 0.09
    bg "C’est tellement n’importe quoi ! Ahahah."
    show char_beaudrik normal left :
        zoom 0.2 xpos 0.6 ypos 0.09
    bg "On entend vraiment des trucs drôles à la taverne, quand les gens se bourrent la gueule."

jump forge_Beaudrik_03_EpouserIngrid
    
#------------------------------------------#

label forge_Beaudrik_03_EpouserIngrid:
    
    menu:
        "Ouais… très drôles" :
            y "Euh… heureusement que c’est juste des rumeurs."
            bg "Ouais, grave ! Ça aurait été dommage que je te casse la gueule."
            jump forge_Beaudrik_04
        "Ça ne te regarde pas" :
            y "Euh… oh ! Ce qu’il se passe entre Ingrid et moi, ça ne te regarde pas !"
            bg "Ahahahah !"
            bg "Vraiment, tu me tues mon pote. T’as raison, faut jouer le jeu."
            bg "En tout cas, c’est bien que ce ne soit qu’une rumeur."
            bg "Ça aurait été dommage que je te casse la gueule."
            jump forge_Beaudrik_04
        "On va se marier pour de vrai !" :
            y "Euh… oui, mais tu sais, Ingrid et moi on va se marier vraiment !"
            bg "Ahahahah !"
            bg "Vraiment, tu me tues mon pote. T’as raison, faut jouer le jeu."
            bg "En tout cas, c’est bien que ce ne soit qu’une rumeur."
            bg "Ça aurait été dommage que je te casse la gueule."
            jump forge_Beaudrik_04
        
#------------------------------------------#

label forge_Beaudrik_04:

    bg "Tu sais, c’est moi qui vais marier la gonzesse. J’ai une dote et tout."
    bg "J’aime beaucoup les femmes mais là j’ai envie de me poser."
    bg "T’sais, d’avoir quelqu’un qui me fasse des câlins et la vaisselle."
    brut "Euh feignasse ! Beaudrik ! Viens ici !"
    bg "Tsk, papa m’appelle encore."
    bg "Bon, moi je dois aller régler un truc avec Josiane, l’autre copine."

jump forge_Beaudrik_05_Josiane

#------------------------------------------#

label forge_Beaudrik_05_Josiane:

    menu:
        "Deux copines ? C’est abusé" :
            y "Non mais attends, moi je me trimballe Ernust et toi tu pécho des meufs à droite et à gauche ?"
            y "C'est abusé."
            bg "Euh, je sais, c’est compliqué."
        "Tu ferais ça à Ingrid ?" :
            y "Deux copines, c’est un peu abusé et pas très gentil quand même."
            y "Tu penses pas que ça briserait le cœur à Ingrid ?"
            bg "Euh, je sais, c’est compliqué."
        "Brutalmund a l’air vénère" :
            y "Et ton père ? Il a pas l’air d’être content."
            bg "Oui, il s’est mis en tête que je dois travailler pour gagner ma vie."
            bg "Mais là j’ai des questions de meufs à régler."

jump forge_Beaudrik_06_leaving

#------------------------------------------#

label forge_Beaudrik_06_leaving:
    
    bg "Heureusement que toi tu n’as pas ce genre de problèmes, Gaufrid ! Je t’envie mon pote."
    bg "Bon, je me casse, avant que Papa arrive. Josiane m’attends à la taverne."
    show char_beaudrik drague right :
        zoom 0.23 xpos 0.4 ypos 0.09
    bg "À plus !"
    show char_beaudrik drague right :
        zoom 0.23 xpos 0.4 ypos 0.09
        linear 1.0 xpos 1.0
    pause 1
    hide char_beaudrik drague right
    pause 1.0
    brut "Beaudrik !"
    
    jump forge_Brutalmund_01
    
#------------------------------------------#

label forge_Brutalmund_01:
    
    show char_brutal colere :
        zoom 0.4 xpos -0.5 ypos 0.05
        linear 0.7 xpos 0.2
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
    
    menu:
        "Pas vraiment, non" :
            y "Je l’ai pas vu, non. Pourquoi ?"
            brut "$$$ Brutalmund explique que Beaudrik devait aller chercher les buffles aux étables"
            brut "$$$ et qu'il ne peut pas laisser son magasin car il y a des voleurs de boucliers"
            brut "Car grâce à toi, mon p’tit interprète, on n’a plus de quoi bouffer !"
            brut "Et tous ces boucliers ne vont pas se vendre tous seuls !"
        "Il est à la taverne" :
            y "$$$"
    
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