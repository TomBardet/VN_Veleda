################################################################################
# Ici figurent les scènes se déroulant à l'aurée du village, chez les romains. #
################################################################################

label romains_PremiereRencontre:
    "label romains_PremiereRencontre"
    
    jump romains_Part1

# -----------------------------------------#

label romains_Part1:
    scene bg_romains
    if Acte2_Romains_FirstVisit == 1:
        jump romains_Part5
    else :
        menu:
            "S'approcher de la tente":
                jump romains_Part2
            "Rentrer au village":
                jump PlaceDuVillageDefault

            
                     
# -----------------------------------------#

label romains_Part2:
    
    show char_numerimus normal at speakingAnim(0.50, 0.82, 0.8, 1.0)
    show char_digitimus normal at notSpeakingAnim(0.8, 0.82, 0.8, 1.25)
    
    #play sound "sfx/SFX_Char_Numerimus_Normal_01.ogg"
    num "Avé sauvage !"
    show char_numerimus normal at notSpeakingAnim(0.50, 0.82, 0.8, 1.0)
    menu :
        
        "Heu...Avé ? ":
            #play sound "sfx/SFX_Char_Player_Question_01.ogg"
            y "Avé à vous... j'imagine ?"
            y "Et sinon vous êtes qui ?"
            jump romains_Part3
            
        "Jolies chaussettes":
           # play sound "sfx/SFX_Char_Player_Sarcasm_01.ogg"
            y "Jolies chaussettes centurion."
            y "A part ça qui êtes vous, et qu'est ce que vous venez faire dans le coin ?"
            jump romains_Part3
        
# -----------------------------------------#

label romains_Part3:
    
    show char_numerimus normal at speakingAnim(0.50, 0.82, 0.8, 1.0)
   # play sound "sfx/SFX_Char_Numerimus_Heureux_01.ogg"
    num "T’as l’air d’un marrant, germain. Moi c’est Numerimus et lui là c’est Digitimus, c’est mon cousin, germain."
    show char_numerimus normal at notSpeakingAnim(0.50, 0.82, 0.8, 1.0)
    
  #  play sound "sfx/SFX_Char_Digitimus_Normal_01.ogg"
    show char_digitimus normal at speakingAnim(0.8, 0.82, 0.8, 1.25)
    dig "avé…"
    show char_digitimus normal at notSpeakingAnim(0.8, 0.82, 0.8, 1.25)
     
 #  play sound "sfx/SFX_Char_Numerimus_Normal_01.ogg"
    
    show char_numerimus normal at speakingAnim(0.50, 0.82, 0.8, 1.0)
    num "On est là en touriste, histoire de s’amuser de vos coutumes étranges"
    show char_numerimus normal at notSpeakingAnim(0.50, 0.82, 0.8, 1.0)
    jump romains_Part4

# -----------------------------------------#

label romains_Part4:
    
    hide char_numerimus choque at notSpeakingAnim(0.50, 0.82, 0.8, 1.0)
    hide char_digitimus choque at notSpeakingAnim(0.8, 0.82, 0.8, 1.25)
    show char_numerimus normal at notSpeakingAnim(0.50, 0.82, 0.8, 1.0)
    show char_digitimus normal at notSpeakingAnim(0.8, 0.82, 0.8, 1.25)
    
  #  play sound "sfx/SFX_Char_Player_Question_01.ogg"
    y "Alors les romains, ces vacances ?"
    show char_numerimus normal at speakingAnim(0.50, 0.82, 0.8, 1.0)
   # play sound "sfx/SFX_Char_Numerimus_Normal_01.ogg"
    num "On s’ennuie."
    show char_numerimus normal at notSpeakingAnim(0.50, 0.82, 0.8, 1.0)
    
   # play sound "sfx/SFX_Char_Digitimus_Enerve_01.ogg"
    show char_digitimus normal at speakingAnim(0.8, 0.82, 0.8, 1.25)
    dig "On s’ennuie vraiment le Germain..."
    show char_digitimus normal at notSpeakingAnim(0.8, 0.82, 0.8, 1.25)
    
    jump romains_Part5

# -----------------------------------------#

label romains_Part5:
    $ Acte2_Romains_FirstVisit = 1
    show char_numerimus normal at notSpeakingAnim(0.50, 0.82, 0.8, 1.0)
    show char_digitimus normal at notSpeakingAnim(0.8, 0.82, 0.8, 1.25)
    
    menu :
        num "On s'ennuie..."
        "Faites un tour du quartier. ":
     #       play sound "sfx/SFX_Char_Player_Question_01.ogg"
            y "Il y a des belles choses dans le coin."
            y "Visitez les alentours ça devrait vous occuper."
            jump romains_VisitePart1
            
        "Je connais une blague.":
      #      play sound "sfx/SFX_Char_Player_Sarcasm_01.ogg"
            y "Bougez pas, je vais vous faire rire avec une bonne blague de chez nous."
            if _testTrompette == 0:
                hide char_numerimus normal at notSpeakingAnim(0.50, 0.82, 0.8, 1.0)
                hide char_digitimus normal at notSpeakingAnim(0.8, 0.82, 0.8, 1.25)
                show char_numerimus dubitatif at notSpeakingAnim(0.50, 0.82, 0.8, 1.0)
                show char_digitimus dubitatif at notSpeakingAnim(0.8, 0.82, 0.8, 1.25)
                jump romains_Blague
                
            else:
                show char_digitimus normal at speakingAnim(0.8, 0.82, 0.8, 1.25)
                dig "Ouais ouais c'est bien gentil mais on la connait."
                show char_digitimus normal at notSpeakingAnim(0.8, 0.82, 0.8, 1.25)
                jump romains_Part5
                
        
                
        "C'est pas mon problème, j'ai autre chose à faire.":
      #       play sound "sfx/SFX_Char_Player_No_01.ogg"
             y "Je peux pas vous aider les gars."
             y "J'ai d'autres affaires à regler, je vous laisse."
             jump PlaceDuVillageDefault
             
# -----------------------------------------#
                #VISITE
# -----------------------------------------#
label romains_VisitePart1:
    
 #   play sound "sfx/SFX_Char_Numerimus_Normal_01.ogg"
    show char_numerimus normal at speakingAnim(0.50, 0.82, 0.8, 1.0)
    num "Je vois pas à 2 mètres. Pour le folklore local on repassera...  "
    num "Mon génie porte-enseigne a oublié mes lunettes à Rome."
    show char_numerimus normal at notSpeakingAnim(0.50, 0.82, 0.8, 1.0)
    
    if _testLunettes == 1:
   #     play sound "sfx/SFX_Char_Player_Sarcasm_01.ogg"
        y "Vous avez de la chance j’en ai justement une paire sur moi."
        y "On aura vu mieux comme scénar’"
        y "Allez tenez. J’imagine que c’est à votre vue en plus du reste."
        jump romains_VisitePart2
        
    else:
        menu :
            "Vous en avez pas une autre paire ?":
        #        play sound "sfx/SFX_Char_Player_Question_01.ogg"
                y "Alors les romains, ces vacances ?"
                
                show char_numerimus normal at speakingAnim(0.50, 0.82, 0.8, 1.0)
                num "non, aucune. Ca nous aiderait pas mal si vous en trouveriez une, Germain."
                show char_numerimus normal at notSpeakingAnim(0.50, 0.82, 0.8, 1.0)
                jump romains_Part5
                
            "Retournez-y. ":
         #       play sound "sfx/SFX_Char_Player_Sarcasm_01.ogg"
                y "Ca tombe bien, toutes les routes y mènent."
                show char_numerimus normal at speakingAnim(0.50, 0.82, 0.8, 1.0)
                num "..."
                show char_numerimus normal at notSpeakingAnim(0.50, 0.82, 0.8, 1.0)
                jump romains_Part5
                
        
# -----------------------------------------#

label romains_VisitePart2:
    
    hide char_numerimus normal
    show char_numerimus heureux
  #  play sound "sfx/SFX_Char_Numerimus_Heureux_01.ogg"
    show char_numerimus normal at speakingAnim(0.50, 0.82, 0.8, 1.0)
    num "Mais c'est super germain ! Passe moi ça !"
    show char_numerimus normal at notSpeakingAnim(0.50, 0.82, 0.8, 1.0)
    
    jump romains_VisitePart3

# -----------------------------------------#
label romains_VisitePart3:
    
    hide char_numerimus heureux
    show char_numerimus normal
    
  #  play sound "sfx/SFX_Char_Numerimus_Normal_01.ogg"
    show char_numerimus normal at speakingAnim(0.50, 0.82, 0.8, 1.0)
    num "Bon du coup...Qu’est ce qu’il y a à voir dans le coin ?"
    show char_numerimus normal at notSpeakingAnim(0.50, 0.82, 0.8, 1.0)
            
    menu :
        num "Bon du coup...Qu’est ce qu’il y a à voir dans le coin ?"
        "L’air vivifiant du paysage Bructère !":
            
   #         play sound "sfx/SFX_Char_Player_Ok_01.ogg"
            y "La Lippe, l'herbe fraiche, l'air vivifiant du paysage Bructère !"
            
   #         play sound "sfx/SFX_Char_Digitimus_Ok_01.ogg"
            show char_digitimus normal at speakingAnim(0.8, 0.82, 0.8, 1.25)
            dig "Mais encore... ?"
            show char_digitimus normal at notSpeakingAnim(0.8, 0.82, 0.8, 1.25)
            jump romains_VisitePart3
            
        "Deux gros abrutis.":
    #        play sound "sfx/SFX_Char_Player_Sarcasm_01.ogg"
            y "Deux bons gros abrutis."
            
    #        play sound "sfx/SFX_Char_Numerimus_Rire_01.ogg"
            show char_numerimus normal at speakingAnim(0.50, 0.82, 0.8, 1.0)
            num "Ah vous en avez vous aussi."
            show char_numerimus normal at notSpeakingAnim(0.50, 0.82, 0.8, 1.0)
            
    #        play sound "sfx/SFX_Char_Player_Sarcasm_01.ogg"
            y "Ici, les abrutis c'est presque culturel."
            y "Parfois il viennent de loin."
            jump romains_VisitePart3
            
        "Véléda ?":
    #        play sound "sfx/SFX_Char_Player_Question_01.ogg"
            y "Il y a bien la prophetesse Véléda mais..."
            
     #       play sound "sfx/SFX_Char_Numerimus_Heureux_01.ogg"
            show char_numerimus normal at speakingAnim(0.50, 0.82, 0.8, 1.0)
            num "Super idée l'Germain, on l'a toujours pas vu celle là."
            show char_numerimus normal at notSpeakingAnim(0.50, 0.82, 0.8, 1.0)
            
    #        play sound "sfx/SFX_Char_Player_No_01.ogg"
            y "non mais elle est pas forcément..."
            
       #     play sound "sfx/SFX_Char_Numerimus_Normal_01.ogg"
            show char_numerimus normal at speakingAnim(0.50, 0.82, 0.8, 1.0)
            num "Vendu ! On y va {b}tout de suite{/b} !"
            show char_numerimus normal at notSpeakingAnim(0.50, 0.82, 0.8, 1.0)
            
            scene black with Dissolve (1.0)
            nar "Dans quoi tu t'es encore fourré...?"
            jump romains_VisitePart4
    
# -----------------------------------------#
                #VISITE (A LA TOUR)
# -----------------------------------------#
    
# -----------------------------------------#

label romains_VisitePart4:
    
    scene bg_antichambre with Dissolve (1.0)
    show char_ernust normal right at notSpeakingAnim(0.40, 0.92, 0.9, 0.7)
    jump romains_VisitePart5
    
# -----------------------------------------#

label romains_VisitePart5:
    
  #  play sound "sfx/SFX_Char_Player_Ok_01.ogg"
    y "Ernust. J'ai fait une connerie."
    
   # play sound "sfx/SFX_Char_Ernust_Joyeux_01.ogg"
    show char_ernust normal right at speakingAnim(0.40, 0.92, 0.9, 0.7)
    e "Mais non voyons ça ne t'arrive jamais à toi !"
    show char_ernust normal right at notSpeakingAnim(0.40, 0.92, 0.9, 0.7)
    
   # play sound "sfx/SFX_Char_Player_No_01.ogg"
    y "Si, là clairement ça m'est arrivé."
    y "Ya deux romains qui arrivent d'une minute à l'autre pour voir Véléda..."
    
    #play sound "sfx/SFX_Char_Ernust_Normal_01.ogg"
    show char_ernust normal right at speakingAnim(0.40, 0.92, 0.9, 0.7)
    e "Hoo, dommage qu'elle soit morte."
    show char_ernust normal right at notSpeakingAnim(0.40, 0.92, 0.9, 0.7)
    
   # play sound "sfx/SFX_Knock_01.ogg"
    num "Héo ! Le Germain, t'es là ? Je rentre moi !"
    
    #play sound "sfx/SFX_Char_Player_Question_01.ogg"
    y "Ahhhhh !! Les voilà !"
    
   # play sound "sfx/SFX_Char_Ernust_Love_01.ogg"
    show char_ernust normal right at speakingAnim(0.40, 0.92, 0.9, 0.7)
    e "T'en fais pas Gaufrid j'ai une idée géniale, fais moi confiance !"
    show char_ernust normal right at notSpeakingAnim(0.40, 0.92, 0.9, 0.7)
    menu :
        "Je ne te fais absolument pas confiance.":
    #        play sound "sfx/SFX_Char_Player_Sarcasm_01.ogg"
            y "Non Ernust c'est mort !"
            y "Je te fais absolument pas confiance..."
            y "Mais j'ai pas vraiment le choix là tout de suite..."
            jump romains_VisitePart7
            
        "Je valide, je te fais clairement pas confiance! ":
     #       play sound "sfx/SFX_Char_Player_Sarcasm_01.ogg"
            y "Tu vas encore faire une connerie !"
            y "Tu serais capable de la re-tuer"
            y "Mais le temps presse, j'ai pas vraiment le choix... je compte sur toi."
            jump romains_VisitePart7
            
# -----------------------------------------#
label romains_VisitePart7:
    
    hide char_ernust normal right with Dissolve (1.0)
   # play sound "sfx/SFX_Char_Player_Ok_01.ogg"
    y "Entrez !"
  #  play sound "sfx/SFX_Entrance_01.ogg"
    
    show char_numerimus normal at speakingAnim(0.5, 0.92, 0.9, 1.25)
 #   play sound "sfx/SFX_Char_Numerimus_Normal_01.ogg"
    num "Ah bah t'es là le Germain."
    num "Bon on va la voir la tarée ?"
    show char_numerimus normal at notSpeakingAnim(0.5, 0.92, 0.9, 1.25)
    menu :
        "Un peu de respect !":
      #      play sound "sfx/SFX_Char_Player_Sarcasm_01.ogg"
            y "Un peu de respect je vous prie !"
            
       #     play sound "sfx/SFX_Char_Numerimus_Normal_01.ogg"
            show char_numerimus normal at notSpeakingAnim(0.5, 0.92, 0.9, 1.25)
            num "Boooh l'autre hé, fais pas le mijoré le Germain on le sait tous qu'elle a un pet au casque."
            show char_numerimus normal at speakingAnim(0.5, 0.92, 0.9, 1.25)
            
            y "Vous croyez pas si bien dire..."
            jump romains_VisitePart8
            
        "euuh attendez...":
        #    play sound "sfx/SFX_Char_Player_No_01.ogg"
            y "Je ne suis pas sûr qu'elle soit...prète."
            
        #    play sound "sfx/SFX_Char_Numerimus_Normal_01.ogg"
            show char_numerimus normal at speakingAnim(0.5, 0.92, 0.9, 1.25)
            num "Qu'elle se prépare alors !"
            num "Je vais pas faire attendre mon imbécile de porte enseigne trop longtemps."
            show char_numerimus normal at notSpeakingAnim(0.5, 0.92, 0.9, 1.25)
            jump romains_VisitePart8
           
            
        "Il est ou l'autre ?":
       #     play sound "sfx/SFX_Char_Player_Question_01.ogg"
            y "Vous êtes venu seul, et votre porte-enseigne ?"
            
       #     play sound "sfx/SFX_Char_Numerimus_Normal_01.ogg"
            show char_numerimus normal at speakingAnim(0.5, 0.92, 0.9, 1.25)
            num "Je l'ai laissé derrière, il s'en fiche lui de tout ça."
            num "Et puis entre nous... c'est pas que je l'aime pas mais bon..."
            show char_numerimus normal at notSpeakingAnim(0.5, 0.92, 0.9, 1.25)
            
       #     play sound "sfx/SFX_Char_Player_Ok_01.ogg"
            y "Je vois...faut croire qu'on a tous un 'Ernust'..."
            jump romains_VisitePart8

            
# -----------------------------------------#

label romains_VisitePart8:
    
 #   play sound "sfx/SFX_Char_Player_Ok_01.ogg"
    y "Ca devrait être bon... j'imagine..."
    y "Suivez-moi."
    jump romains_VisitePart9

# -----------------------------------------#

label romains_VisitePart9:
    
    scene black with Dissolve (1.0)
  #  play sound "sfx/SFX_Char_Player_Question_01.ogg"
    y "Ernust, on... on arrive nous."
    y "On monte hein..."
    y "Là on... monte les marches."
    scene bg_chambre with Dissolve (1.0)
    jump romains_VisitePart10

# -----------------------------------------#
label romains_VisitePart10:
    
    show char_numerimus normal at speakingAnim(0.1, 0.92, 0.9, 1)
    show char_veledaernust normal at notSpeakingAnim(0.55, 0.65, 0.67, 1)
    
  #  play sound "sfx/SFX_Char_Numerimus_Normal_01.ogg"
    num " Bonjour m'dam."
    show char_numerimus normal at notSpeakingAnim(0.1, 0.92, 0.9, 1)
    
    show char_veledaernust normal at speakingAnim(0.55, 0.65, 0.67, 1)
    ve "Bonnnnnnnjouuuuur etranger !"
    ve "Je vaiiiis vous faire une prophétie !!!"
    ve "Souuus le soleil de la pierre couleur cailloux !!!!!!"
    show char_veledaernust normal at notSpeakingAnim(0.55, 0.65, 0.67, 1)
    
 #   play sound "sfx/SFX_Char_Numerimus_Normal_01.ogg"
    show char_numerimus normal at speakingAnim(0.1, 0.92, 0.9, 1)
    num "Mais qu’est-ce qu’elle raconte celle là ?"
    show char_numerimus normal at notSpeakingAnim(0.1, 0.92, 0.9, 1)
    
 #   play sound "sfx/SFX_Char_Player_Ok_01.ogg"
    y "Euuh là elle dit... qu’a votre retour les... gens à Rome.. Seront… très… content de vous voir."
    
 #   play sound "sfx/SFX_Char_Numerimus_Heureux_01.ogg"
    show char_numerimus normal at speakingAnim(0.1, 0.92, 0.9, 1)
    num "humm... c'est une maline."
    show char_numerimus normal at notSpeakingAnim(0.1, 0.92, 0.9, 1)
    
    jump romains_VisiteProphetie
    
# -----------------------------------------#
label romains_VisiteProphetie:
    
    #Proph 01#
    show char_veledaernust normal at speakingAnim(0.55, 0.65, 0.67, 1)
    ve  " La rosée du matinnnnnnnn, c’est ce qui nourrit les arbres !" 
    show char_veledaernust normal at notSpeakingAnim(0.55, 0.65, 0.67, 1)
    
#    play sound "sfx/SFX_Char_Player_Ok_01.ogg"
    menu :
        y "Là elle dit que..."
        "Il pleuvra" :
            y "La pluie tombera demain."
        "Elle annonce une menace !" :
            y "La fuite inexorable du temps rendra vos adversaires plus forts !"
        "Vos olives pousseront." :
            y "Sur vos oliviers pousseront bientôt les meilleurs olives de Rome"
    
#    play sound "sfx/SFX_Char_Numerimus_Normal_01.ogg"
    show char_numerimus normal at speakingAnim(0.1, 0.92, 0.9, 1)
    num "humm..."
    show char_numerimus normal at notSpeakingAnim(0.1, 0.92, 0.9, 1)
    
    #Proph 02#
    show char_veledaernust normal at speakingAnim(0.55, 0.65, 0.67, 1)
    ve  " Les oiseauuuuuuux chantent on dirait des corbeaux  !" 
    show char_veledaernust normal at notSpeakingAnim(0.55, 0.65, 0.67, 1)
    
 #   play sound "sfx/SFX_Char_Player_Ok_01.ogg"
    menu :
        y "Et là elle vous raconte que..."
        "La mort est proche." :
            y "Un présage de mort plane sur vous..."
        "Il y a... des corbeaux ?" :
            y "Les oiseaux sont surement des corbeaux."
        "On chantera votre gloire." :
            y "Les chants de victoires retentiront bientôt, votre gloire sera chantée."
    
    #Proph 03#
    show char_veledaernust normal at speakingAnim(0.55, 0.65, 0.67, 1)
    ve  " Eau chauuuuuude….. et eau froide ne font pas bon ménage  !" 
    show char_veledaernust normal at notSpeakingAnim(0.55, 0.65, 0.67, 1)
    
 #   play sound "sfx/SFX_Char_Player_Ok_01.ogg"
    menu :
        y "Ô Véléda, grande prophetesse, je transmet votre message..."
        "Un taître !" :
            y "Il y a un traître dans vos rangs !"
        "Vous allez sortir du lot." :
            y "Vous vous démarquerez en tant que grand centurion."
        "L'eau tiède c'est agréable" :
            y "Qu'un peu d'eau chaude, avec un peu d'eau froide,  ça fait de l'eau tiède ben agréable quand on y pense." 
    
    #Proph 04#
    show char_veledaernust normal at speakingAnim(0.55, 0.65, 0.67, 1)
    ve  " Ah.... Je commence à avoir mal au bras..."
    show char_veledaernust normal at notSpeakingAnim(0.55, 0.65, 0.67, 1)
    
 #   play sound "sfx/SFX_Char_Numerimus_Normal_01.ogg"
    show char_numerimus normal at speakingAnim(0.1, 0.92, 0.9, 1)
    num "hein ?"
    show char_numerimus normal at notSpeakingAnim(0.1, 0.92, 0.9, 1)
    
#    play sound "sfx/SFX_Char_Player_Ok_01.ogg"
    menu :
        y "Heuuu là... elle dit que..."
        "Vous vous faites vieu." :
            y "La vieillesse vous guette… et de près"
            jump romains_FinDeLaVisite80
        "Votre bras agile." :
            y "Votre bras droit est plus agile que le gauche. "
            jump romains_FinDeLaVisite80
        "Le poid de la réussite !" :
            y "Le poids de votre réussite se fera sentir sur tout l’empire."
            jump romains_FinDeLaVisite80
    
    #if Love < 20 :
        #jump romains_FinDeLaVisite20
    #if Love < 50 :
        #jump romains_FinDeLaVisite50
    #if Love < 80 :
        #jump romains_FinDeLaVisite80


# -----------------------------------------#
label romains_FinDeLaVisite80:
    
 #   play sound "sfx/SFX_Char_Numerimus_Rire_01.ogg"
    show char_numerimus normal at speakingAnim(0.1, 0.92, 0.9, 1)
    num "C'était vraiment sympa votre petite coutume là les germains !"
    num "Allez, tiens attrape machin, tu l'a bien mérité."
    show char_numerimus normal at notSpeakingAnim(0.1, 0.92, 0.9, 1)
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
 #       play sound "sfx/SFX_Char_Player_Sarcasm_01.ogg"
        y "J'ai une amie qui m'a fillé la meilleur des boutades."
        y "Tenez lisez ça..."
        nar "C'est là où j'explique que tu tend le bras pour leur donner la blague ? Non ?"
        
  #      play sound "sfx/SFX_Char_Numerimus_Rire_01.ogg"
        
        show char_numerimus normal at speakingAnim(0.50, 0.82, 0.8, 1.0)
        num "Ahahaha"
        show char_numerimus normal at notSpeakingAnim(0.50, 0.82, 0.8, 1.0)
        
  #      play sound "sfx/SFX_Char_Digitimus_Ok_01.ogg"
        show char_digitimus normal at speakingAnim(0.8, 0.82, 0.8, 1.25)
        dig "ahahahahaha... ahahaha!"
        dig "ahaha... ahahaha!"
        dig "aha..."
        dig "T'es vraiment un marrant toi."
        dig "Tiens on t'avait dit qu'on te donnerait un truc si tu nous divertissais. Attrape Germain !"
        show char_digitimus normal at notSpeakingAnim(0.8, 0.82, 0.8, 1.25)
        nar "Le romain te lance donc une... trompette."
        $ inventory.add(trompette)
        $ _testTrompette = 1
        "trompette récupérée"
        jump romains_Part5
        
    else:
        y "Alors, c'est l'histoire de..."
        y "Comment... est-ce qu'on... appelle "
        y "Une salade césar en Asie ?"
        y "Une Gengis khan..."
        hide char_numerimus dubitatif at notSpeakingAnim(0.50, 0.82, 0.8, 1.0)
        hide char_digitimus dubitatif at notSpeakingAnim(0.8, 0.82, 0.8, 1.25)
        show char_numerimus choque at notSpeakingAnim(0.50, 0.82, 0.8, 1.0)
        show char_digitimus choque at notSpeakingAnim(0.8, 0.82, 0.8, 1.25)
        nar "C'était de loin la pire blague que j'ai jamais entendu"
        nar "Et je parle même pas du fait que t'as 12 siècles d'avance."
        num "C'était horrible... La prochaine fois reviens avec une blague correcte."
        jump romains_Part5
         