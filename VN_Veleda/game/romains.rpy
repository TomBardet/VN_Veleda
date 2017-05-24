################################################################################
# Ici figurent les scènes se déroulant à l'aurée du village, chez les romains. #
################################################################################

label romains_PremiereRencontre:
    "label romains_PremiereRencontre"
    
    jump romains_Part1

# -----------------------------------------#

label romains_Part1:
    "label romains_Part1"
    
    scene bg_romains
    menu:
        "Rentrer au village":
            jump PlaceDuVillageDefault
        "S'approcher de la tente":
            jump romains_ApparitionRomain
            
                     
# -----------------------------------------#

label romains_ApparitionRomain:
    "label romains_ApparitionRomain"
    
    show char_numerimus normal
    show char_digitimus normal at right 
    jump romains_Part2
    
# -----------------------------------------#

label romains_Part2:
    "label romains_Part2"
    
    menu :
        num "Avé sauvage !"
        
        "1. Heu...Avé ? ":
            y "Avé à vous... j'imagine ?"
            y "Et sinon vous êtes qui ?"
            jump romains_Part3
            
        "2. Jolies chaussettes":
            y "Jolies chaussettes centurion."
            y "A part ça qui êtes vous, et qu'est ce que vous venez faire dans le coin ?"
            jump romains_Part3
        
# -----------------------------------------#

label romains_Part3:
    "label romains_Part3"
    
    num "T’as l’air d’un marrant, germain. Moi c’est Numerimus et lui là c’est Digitimus, c’est mon cousin, germain."
    dig "avé…"
    num "On est là en touriste, histoire de s’amuser de vos coutumes étranges"
    jump romains_Part4

# -----------------------------------------#

label romains_Part4:
    "label romains_Part4"
    
    hide char_numerimus choque
    hide char_digitimus choque
    show char_numerimus normal
    show char_digitimus normal at right
    
    menu :
        "1. Je vais y aller moi. ":
            y "M'en voulez pas hein..."
            y "Mais je vais me rentrer moi."
            jump romains_Part4
            
        "2. Ca se passe les vacances ?":
            y "Alors les romains, ces vacances ?"
            jump romains_Part5bis

# -----------------------------------------#
#label romains_Part5:
    #"label romains_Part5"
    
    #num "On s’ennuie..."
    #dig "On s’ennuie vraiment..."
    #num "Ouais… Je donnerais jusqu'a mon glaive pour un peu d’amusement."
    #jump romains_Part5bis

# -----------------------------------------#

label romains_Part5bis:
    "label romains_Part5bis"
    
    num "On s’ennuie."
    dig "On s’ennuie vraiment le Germain..."
    menu :
        "1. Faites un tour du quartier. ":
            y "Il y a des belles choses dans le coin."
            y "Visitez les alentours ça devrait vous occuper."
            jump romains_VisitePart1
            
        "2. Je connais une blague.":
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
        
                
        "3. C'est pas mon problème.":
             y "Je peux pas vous aider les gars."
             jump romains_Part4
 
# -----------------------------------------#
                #VISITE
# -----------------------------------------#
label romains_VisitePart1:
    "label romains_VisitePart1"
     
    num "Je vois pas à 2 mètres. Pour le folklore local on repassera...  "
    num "Mon génie porte-enseigne a oublié mes lunettes à Rome."
    
    if _testLunettes == 0:
        num "Vous avez de la chance j’en ai justement une paire sur moi."
        num "On aura vu mieux comme scénar’"
        num "Allez tenez. J’imagine que c’est à votre vue en plus du reste."
        jump romains_VisitePart2
        
    else:
        menu :
            "1. Vous en avez pas une autre paire ?":
                y "Alors les romains, ces vacances ?"
                num "non, aucune. Ca nous aiderait pas mal si vous en trouveriez une, Germain."
                jump romains_Part5bis
                
            "2. Retournez-y. ":
                y "Ca tombe bien, toutes les routes y mènent."
                num "..."
                jump romains_Part5bis
                
        
# -----------------------------------------#

label romains_VisitePart2:
    "label romains_VisitePart2"
    
    hide char_numerimus normal
    show char_numerimus heureux
    num "Mais c'est super germain ! Passe moi ça !"
    
    jump romains_VisitePart3
    
# -----------------------------------------#

label romains_VisitePart3:
    "label romains_VisitePart3"
    
    hide char_numerimus heureux
    show char_numerimus normal
    num "Bon du coup..."
    jump romains_VisitePart3bis
    
# -----------------------------------------#
label romains_VisitePart3bis:
    "label romains_VisitePart3bis"
    
    menu :
        num "Qu’est ce qu’il y a à voir dans le coin ?"
        "1. L’air vivifiant du paysage Bructère !":
            y "La Lippe, l'herbe fraiche, l'air vivifiant du paysage Bructère !"
            dig "Mais encore... ?"
            jump romains_VisitePart3bis
        "2. Deux gros abrutis.":
            y "Deux bons gros abrutis."
            num "Ah vous en avez vous aussi."
            y "Ici, les abrutis c'est presque culturel."
            y "Parfois il viennent de loin."
            jump romains_VisitePart3bis
        "3. Véléda ?":
            y "Il y a bien la prophetesse Véléda mais..."
            num "Super idée l'Germain, on l'a toujours pas vu celle là."
            y "non mais elle est pas forcément..."
            num "Vendu ! On y va {b}tout de suite{/b} !"
            scene black with Dissolve (1.0)
            nar "Dans quoi tu t'es encore fourré...?"
            jump romains_VisitePart4
    
    
# -----------------------------------------#

label romains_VisitePart4:
    "label romains_VisitePart4"
    
    scene bg_antichambre with Dissolve (1.0)
    show char_ernust normal
    jump romains_VisitePart5
    
# -----------------------------------------#

label romains_VisitePart5:
    "label romains_VisitePart5"
    
    y "Ernust. J'ai fait une connerie."
    e "Mais non voyons ça ne t'arrive jamais à toi !"
    y "Si, là clairement ça m'est arrivé."
    y "Ya deux romains qui arrivent d'une minute à l'autre pour voir Véléda..."
    e "Hoo, dommage qu'elle soit morte."
    num "Héo ! Le Germain, t'es là ? On rentre nous !"
    y "Ahhhhh !! Les voilà !"
    e "T'en fais pas Gaufrid j'ai une idée géniale, fais moi confiance !"
    menu :
        "1. Je ne te fais absolument pas confiance.":
            y "Non Ernust c'est mort !"
            y "Je te fais absolument pas confiance..."
            y "Mais j'ai pas vraiment le choix là tout de suite..."
            jump romains_VisitePart6
            
        "2. Je valide, je te fais clairement pas confiance! ":
            y "Tu vas encore faire une connerie !"
            y "Tu serais capable de la re-tuer"
            y "Mais le temps presse, j'ai pas vraiment le choix... je compte sur toi."
            jump romains_VisitePart6
            
# -----------------------------------------#

label romains_VisitePart6:
    "label romains_VisitePart6"
    
    hide char_ernust normal with Dissolve (1.0)
    jump romains_VisitePart7
    
# -----------------------------------------#
label romains_VisitePart7:
    "label romains_VisitePart7"
    
    show char_numerimus normal with Dissolve (1.0)
    num "Ah bah t'es là le Germain."
    num "Bon on va la voir la tarée ?"
    menu :
        "1. Un peu de respect !":
            y "Un peu de respect je vous prie !"
            num "Boooh l'autre hé, fais pas le mijoré le Germain on le sait tous qu'elle a un pet au casque."
            y "Vous croyez pas si bien dire..."
            jump romains_VisitePart8
            
        "2. euuh attendez...":
            y "Je ne suis pas sûr qu'elle soit...prète."
            num "Qu'elle se prépare alors !"
            num "Je vais pas faire attendre mon imbécile de porte enseigne trop longtemps."
            jump romains_VisitePart8
           
            
        "3. Il est ou l'autre ?":
            num "Je l'ai laissé derrière, il s'en fiche lui de tout ça."
            num "Et puis entre nous... c'est pas que je l'aime pas mais bon..."
            y "Je vois... on a tous un 'Ernust' j'imagine..."
            jump romains_VisitePart8

            
# -----------------------------------------#

label romains_VisitePart8:
    "label romains_VisitePart8"
    
    y "Ca devrait être bon... j'imagine..."
    y "Suivez-moi."
    jump romains_VisitePart9

# -----------------------------------------#

label romains_VisitePart9:
    "label romains_VisitePart9"
    
    scene black with Dissolve (1.0)
    y "Ernust, on... on arrive nous."
    y "On monte hein..."
    y "Là on... monte les marches."
    scene bg_chambre with Dissolve (1.0)
    jump romains_VisitePart10

# -----------------------------------------#
label romains_VisitePart10:
    "label romains_VisitePart9"
    
    show char_numerimus normal at left
    show char_veledaernust normal
    
    num " Bonjour m'dam."
    ve "Bonnnnnnnjouuuuur etranger !"
    ve "Je vaiiiis vous faire une prophétie !!!"
    nar "Mais qu'est ce qu'il nous fait celui là..."
    
    jump romains_VisitePart11

# -----------------------------------------#
label romains_VisitePart10:
    "label romains_VisitePart9"
    
    show char_numerimus normal at left
    show char_veledaernust normal
    
    jump romains_VisitePart11

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
        y "J'ai une amie qui m'a fillé la meilleur des boutades."
        y "Tenez lisez ça..."
        nar "C'est là où j'explique que tu tend le bras pour leur donner la blague ? Non ?"
        num "Ahahaha"
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
         