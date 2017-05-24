################################################################################
# Ici figurent les scènes se déroulant à l'aurée du village, chez les romains. #
################################################################################

label romains_PremiereRencontre:
    "label romains_PremiereRencontre"
    
    jump romains_Part1

# -----------------------------------------#

label romains_Part1:
    
    scene bg_romains
    menu:
        "Rentrer au village":
            jump PlaceDuVillageDefault
        "S'approcher de la tente":
            jump romains_ApparitionRomain
            
                     
# -----------------------------------------#

label romains_ApparitionRomain:
    
    show char_numerimus normal
    show char_digitimus normal :
        xpos 0.5
    jump romains_Part2
    
# -----------------------------------------#

label romains_Part2:
    
    play sound "sfx/SFX_Char_Numerimus_Normal_01.ogg"
    menu :
        
        num "Avé sauvage !"
        
        "Heu...Avé ? ":
            play sound "sfx/SFX_Char_Player_Question_01.ogg"
            y "Avé à vous... j'imagine ?"
            y "Et sinon vous êtes qui ?"
            jump romains_Part3
            
        "Jolies chaussettes":
            play sound "sfx/SFX_Char_Player_Sarcasm_01.ogg"
            y "Jolies chaussettes centurion."
            y "A part ça qui êtes vous, et qu'est ce que vous venez faire dans le coin ?"
            jump romains_Part3
        
# -----------------------------------------#

label romains_Part3:
    
    play sound "sfx/SFX_Char_Numerimus_Heureux_01.ogg"
    num "T’as l’air d’un marrant, germain. Moi c’est Numerimus et lui là c’est Digitimus, c’est mon cousin, germain."
    
    play sound "sfx/SFX_Char_Digitimus_Normal_01.ogg"
    dig "avé…"
    
    play sound "sfx/SFX_Char_Numerimus_Normal_01.ogg"
    num "On est là en touriste, histoire de s’amuser de vos coutumes étranges"
    jump romains_Part4

# -----------------------------------------#

label romains_Part4:
    
    hide char_numerimus choque
    hide char_digitimus choque
    show char_numerimus normal
    show char_digitimus normal :
        xpos 0.5
    
    menu :
        "Je vais y aller moi. ":
            play sound "sfx/SFX_Char_Player_Ok_01.ogg"
            y "M'en voulez pas hein..."
            y "Mais je vais me rentrer moi."
            jump romains_Part4
            
        "Ca se passe les vacances ?":
            play sound "sfx/SFX_Char_Player_Question_01.ogg"
            y "Alors les romains, ces vacances ?"
            jump romains_Part5bis

# -----------------------------------------#

label romains_Part5bis:
    
    play sound "sfx/SFX_Char_Numerimus_Normal_01.ogg"
    num "On s’ennuie."
    
    play sound "sfx/SFX_Char_Digitimus_Enerve_01.ogg"
    dig "On s’ennuie vraiment le Germain..."
    menu :
        "Faites un tour du quartier. ":
            play sound "sfx/SFX_Char_Player_Question_01.ogg"
            y "Il y a des belles choses dans le coin."
            y "Visitez les alentours ça devrait vous occuper."
            jump romains_VisitePart1
            
        "Je connais une blague.":
            play sound "sfx/SFX_Char_Player_Sarcasm_01.ogg"
            y "Bougez pas, je vais vous faire rire avec une bonne blague de chez nous."
            if _testTrompette == 0:
                hide char_numerimus normal
                hide char_digitimus normal
                show char_numerimus dubitatif
                show char_digitimus dubitatif at right
                jump romains_Blague
            else:
                dig "Ouais ouais c'est bien gentil mais on la connait."
                jump romains_Part5bis
        
                
        "C'est pas mon problème.":
             play sound "sfx/SFX_Char_Player_No_01.ogg"
             y "Je peux pas vous aider les gars."
             jump romains_Part4
 
# -----------------------------------------#
                #VISITE
# -----------------------------------------#
label romains_VisitePart1:
    
    play sound "sfx/SFX_Char_Numerimus_Normal_01.ogg"
    num "Je vois pas à 2 mètres. Pour le folklore local on repassera...  "
    num "Mon génie porte-enseigne a oublié mes lunettes à Rome."
    
    if _testLunettes == 0:
        play sound "sfx/SFX_Char_Player_Sarcasm_01.ogg"
        y "Vous avez de la chance j’en ai justement une paire sur moi."
        y "On aura vu mieux comme scénar’"
        y "Allez tenez. J’imagine que c’est à votre vue en plus du reste."
        jump romains_VisitePart2
        
    else:
        menu :
            "Vous en avez pas une autre paire ?":
                play sound "sfx/SFX_Char_Player_Question_01.ogg"
                y "Alors les romains, ces vacances ?"
                num "non, aucune. Ca nous aiderait pas mal si vous en trouveriez une, Germain."
                jump romains_Part5bis
                
            "Retournez-y. ":
                play sound "sfx/SFX_Char_Player_Sarcasm_01.ogg"
                y "Ca tombe bien, toutes les routes y mènent."
                num "..."
                jump romains_Part5bis
                
        
# -----------------------------------------#

label romains_VisitePart2:
    
    hide char_numerimus normal
    show char_numerimus heureux
    play sound "sfx/SFX_Char_Numerimus_Heureux_01.ogg"
    num "Mais c'est super germain ! Passe moi ça !"
    
    jump romains_VisitePart3

# -----------------------------------------#
label romains_VisitePart3:
    
    hide char_numerimus heureux
    show char_numerimus normal
    
    play sound "sfx/SFX_Char_Numerimus_Normal_01.ogg"
    menu :
        num "Bon du coup...Qu’est ce qu’il y a à voir dans le coin ?"
        "L’air vivifiant du paysage Bructère !":
            
            play sound "sfx/SFX_Char_Player_Ok_01.ogg"
            y "La Lippe, l'herbe fraiche, l'air vivifiant du paysage Bructère !"
            
            play sound "sfx/SFX_Char_Digitimus_Ok_01.ogg"
            dig "Mais encore... ?"
            jump romains_VisitePart3
            
        "Deux gros abrutis.":
            play sound "sfx/SFX_Char_Player_Sarcasm_01.ogg"
            y "Deux bons gros abrutis."
            
            play sound "sfx/SFX_Char_Numerimus_Rire_01.ogg"
            num "Ah vous en avez vous aussi."
            
            play sound "sfx/SFX_Char_Player_Sarcasm_01.ogg"
            y "Ici, les abrutis c'est presque culturel."
            y "Parfois il viennent de loin."
            jump romains_VisitePart3
            
        "Véléda ?":
            play sound "sfx/SFX_Char_Player_Question_01.ogg"
            y "Il y a bien la prophetesse Véléda mais..."
            
            play sound "sfx/SFX_Char_Numerimus_Heureux_01.ogg"
            num "Super idée l'Germain, on l'a toujours pas vu celle là."
            
            play sound "sfx/SFX_Char_Player_No_01.ogg"
            y "non mais elle est pas forcément..."
            
            play sound "sfx/SFX_Char_Numerimus_Normal_01.ogg"
            num "Vendu ! On y va {b}tout de suite{/b} !"
            
            scene black with Dissolve (1.0)
            nar "Dans quoi tu t'es encore fourré...?"
            jump romains_VisitePart4
    
    
# -----------------------------------------#

label romains_VisitePart4:
    
    scene bg_antichambre with Dissolve (1.0)
    show char_ernust normal right :
        zoom 0.7 xpos 0.4 ypos 0.2
    jump romains_VisitePart5
    
# -----------------------------------------#

label romains_VisitePart5:
    
    play sound "sfx/SFX_Char_Player_Ok_01.ogg"
    y "Ernust. J'ai fait une connerie."
    
    play sound "sfx/SFX_Char_Ernust_Joyeux_01.ogg"
    e "Mais non voyons ça ne t'arrive jamais à toi !"
    
    play sound "sfx/SFX_Char_Player_No_01.ogg"
    y "Si, là clairement ça m'est arrivé."
    y "Ya deux romains qui arrivent d'une minute à l'autre pour voir Véléda..."
    
    play sound "sfx/SFX_Char_Ernust_Normal_01.ogg"                                                                              
    e "Hoo, dommage qu'elle soit morte."
    
    play sound "sfx/SFX_Knock_01.ogg"
    num "Héo ! Le Germain, t'es là ? Je rentre moi !"
    
    play sound "sfx/SFX_Char_Player_Question_01.ogg"
    y "Ahhhhh !! Les voilà !"
    
    play sound "sfx/SFX_Char_Ernust_Love_01.ogg"
    e "T'en fais pas Gaufrid j'ai une idée géniale, fais moi confiance !"
    menu :
        "Je ne te fais absolument pas confiance.":
            play sound "sfx/SFX_Char_Player_Sarcasm_01.ogg"
            y "Non Ernust c'est mort !"
            y "Je te fais absolument pas confiance..."
            y "Mais j'ai pas vraiment le choix là tout de suite..."
            jump romains_VisitePart7
            
        "Je valide, je te fais clairement pas confiance! ":
            play sound "sfx/SFX_Char_Player_Sarcasm_01.ogg"
            y "Tu vas encore faire une connerie !"
            y "Tu serais capable de la re-tuer"
            y "Mais le temps presse, j'ai pas vraiment le choix... je compte sur toi."
            jump romains_VisitePart7
            
# -----------------------------------------#
label romains_VisitePart7:
    
    hide char_ernust normal right with Dissolve (1.0)
    play sound "sfx/SFX_Char_Player_Ok_01.ogg"
    y "Entrez !"
    play sound "sfx/SFX_Entrance_01.ogg"
    show char_numerimus normal with Dissolve (1.0)
    
    play sound "sfx/SFX_Char_Numerimus_Normal_01.ogg"
    num "Ah bah t'es là le Germain."
    num "Bon on va la voir la tarée ?"
    menu :
        "Un peu de respect !":
            play sound "sfx/SFX_Char_Player_Sarcasm_01.ogg"
            y "Un peu de respect je vous prie !"
            
            play sound "sfx/SFX_Char_Numerimus_Normal_01.ogg"
            num "Boooh l'autre hé, fais pas le mijoré le Germain on le sait tous qu'elle a un pet au casque."
            
            y "Vous croyez pas si bien dire..."
            jump romains_VisitePart8
            
        "euuh attendez...":
            play sound "sfx/SFX_Char_Player_No_01.ogg"
            y "Je ne suis pas sûr qu'elle soit...prète."
            
            play sound "sfx/SFX_Char_Numerimus_Normal_01.ogg"
            num "Qu'elle se prépare alors !"
            num "Je vais pas faire attendre mon imbécile de porte enseigne trop longtemps."
            jump romains_VisitePart8
           
            
        "Il est ou l'autre ?":
            play sound "sfx/SFX_Char_Player_Question_01.ogg"
            y "Vous êtes venu seul, et votre porte-enseigne ?"
            
            play sound "sfx/SFX_Char_Numerimus_Normal_01.ogg"
            num "Je l'ai laissé derrière, il s'en fiche lui de tout ça."
            num "Et puis entre nous... c'est pas que je l'aime pas mais bon..."
            
            play sound "sfx/SFX_Char_Player_Ok_01.ogg"
            y "Je vois...faut croire qu'on a tous un 'Ernust'..."
            jump romains_VisitePart8

            
# -----------------------------------------#

label romains_VisitePart8:
    
    play sound "sfx/SFX_Char_Player_Ok_01.ogg"
    y "Ca devrait être bon... j'imagine..."
    y "Suivez-moi."
    jump romains_VisitePart9

# -----------------------------------------#

label romains_VisitePart9:
    
    scene black with Dissolve (1.0)
    play sound "sfx/SFX_Char_Player_Question_01.ogg"
    y "Ernust, on... on arrive nous."
    y "On monte hein..."
    y "Là on... monte les marches."
    scene bg_chambre with Dissolve (1.0)
    jump romains_VisitePart10

# -----------------------------------------#
label romains_VisitePart10:
    
    show char_numerimus normal at left
    show char_veledaernust normal
    
    play sound "sfx/SFX_Char_Numerimus_Normal_01.ogg"
    num " Bonjour m'dam."
    
    ve "Bonnnnnnnjouuuuur etranger !"
    ve "Je vaiiiis vous faire une prophétie !!!"
    ve "Souuus le soleil de la pierre couleur cailloux !!!!!!"
    
    play sound "sfx/SFX_Char_Numerimus_Normal_01.ogg"
    num "Mais qu’est-ce qu’elle raconte celle là ?"
    
    play sound "sfx/SFX_Char_Player_Ok_01.ogg"
    y "Euuh là elle dit... qu’a votre retour les... gens à Rome.. Seront… très… content de vous voir."
    
    play sound "sfx/SFX_Char_Numerimus_Heureux_01.ogg"
    num "humm... c'est une maline."
    
    jump romains_VisiteProphetie
    
# -----------------------------------------#
label romains_VisiteProphetie:
    
    #Proph 01#
    ve  " La rosée du matinnnnnnnn, c’est ce qui nourrit les arbres !" 
    
    play sound "sfx/SFX_Char_Player_Ok_01.ogg"
    menu :
        y "Là elle dit que..."
        "Il pleuvra" :
            y "La pluie tombera demain."
        "Elle annonce une menace !" :
            y "La fuite inexorable du temps rendra vos adversaires plus forts !"
        "Vos olives pousseront." :
            y "Sur vos oliviers pousseront bientôt les meilleurs olives de Rome"
    
    play sound "sfx/SFX_Char_Numerimus_Normal_01.ogg"
    num "humm..."
    
    #Proph 02#
    ve  " Les oiseauuuuuuux chantent on dirait des corbeaux  !" 
    
    play sound "sfx/SFX_Char_Player_Ok_01.ogg"
    menu :
        y "Et là elle vous raconte que..."
        "La mort est proche." :
            y "Un présage de mort plane sur vous..."
        "Il y a... des corbeaux ?" :
            y "Les oiseaux sont surement des corbeaux."
        "On chantera votre gloire." :
            y "Les chants de victoires retentiront bientôt, votre gloire sera chantée."
    
    #Proph 03#
    ve  " Eau chauuuuuude….. et eau froide ne font pas bon ménage  !" 
    
    play sound "sfx/SFX_Char_Player_Ok_01.ogg"
    menu :
        y "Ô Véléda, grande prophetesse, je transmet votre message..."
        "Un taître !" :
            y "Il y a un traître dans vos rangs !"
        "Vous allez sortir du lot." :
            y "Vous vous démarquerez en tant que grand centurion."
        "L'eau tiède c'est agréable" :
            y "Qu'un peu d'eau chaude, avec un peu d'eau froide,  ça fait de l'eau tiède ben agréable quand on y pense." 
    
    #Proph 04#
    ve  " Ah.... Je commence à avoir mal au bras..."
    play sound "sfx/SFX_Char_Numerimus_Normal_01.ogg"
    num "hein ?"
    
    play sound "sfx/SFX_Char_Player_Ok_01.ogg"
    menu :
        y "Heuuu là... elle dit que..."
        "Vous vous faites vieu." :
            y "La vieillesse vous guette… et de près"
        "Votre bras agile." :
            y "Votre bras droit est plus agile que le gauche. "
        "Le poid de la réussite !" :
            y "Le poids de votre réussite se fera sentir sur tout l’empire."
            
    jump romains_VisitePart10


# -----------------------------------------#
label romains_FinDeLaVisite:
    "label romains_VisiteVeleda"
    
    $ inventory.add(glaive)
    $ _testGlaive = 1
    
    "glaive récupéré"
    
    if _testGlaive == 1 & _testBouclier == 1:
        jump PlaceDuVillageAllObjects
    else:
        jump PlaceDuVillageDefault
    
# -----------------------------------------#
                #BLAGUE
# -----------------------------------------#

label romains_Blague:
    "label romains_Blague"
    
    if _testBlague == 1:
        play sound "sfx/SFX_Char_Player_Sarcasm_01.ogg"
        y "J'ai une amie qui m'a fillé la meilleur des boutades."
        y "Tenez lisez ça..."
        nar "C'est là où j'explique que tu tend le bras pour leur donner la blague ? Non ?"
        
        play sound "sfx/SFX_Char_Numerimus_Rire_01.ogg"
        num "Ahahaha"
        
        play sound "sfx/SFX_Char_Digitimus_Ok_01.ogg"
        dig "ahahahahaha... ahahaha!"
        dig "ahaha... ahahaha!"
        dig "aha..."
        dig "T'es vraiment un marrant toi."
        dig "Tiens on t'avait dit qu'on te donnerait un truc si tu nous divertissais. Attrape Germain !"
        nar "Le romain te lance donc une... trompette."
        $ inventory.add(trompette)
        $ _testTrompette = 1
        "trompette récupérée"
        jump romains_Part4
        
    else:
        y "Alors, c'est l'histoire de..."
        y "Comment... est-ce qu'on... appelle "
        y "Une salade césar en Asie ?"
        y "Une Gengis khan..."
        hide char_numerimus dubitatif
        hide char_digitimus dubitatif
        show char_numerimus choque
        show char_digitimus choque at right
        nar "C'était de loin la pire blague que j'ai jamais entendu"
        nar "Et je parle même pas du fait que t'as 12 siècles d'avance."
        num "C'était horrible... La prochaine fois reviens avec une blague correcte."
        jump romains_Part4
         