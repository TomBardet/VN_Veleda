#######################################################################################################
# On gère ici les interventions du narrateur sans décor, ainsi que la place du village et les endings #
#######################################################################################################

label start:
    
    python :
        
        #########################################################################################
        ######################## - Defining Misc - ##############################################
        interlocuteur = "None" ## Ne pas oublier d'actualiser le nom de l'interlocuteur à chaque changement
        lieu = "None" ## Ne pas oublier d'actualiser le nom du lieu à chaque changement
        CAactif = False ## Set à False après chaque actionChoice
        inventory = Inventory()
        
        ######### - LES PERSONNAGES DATING SIM - ############
        
        goat_char = Chara("Goat", 20,100)
        ingrid_char = Chara("Ingrid", 50, 100)
        vel_char = Chara("Véléda", 25,100)
        ern_char = Chara("Ernust", 90, 9999)
        brut_char = Chara("Brutalmund", 35, 100)
        cross_char = Chara("Crossfitrichernvald", 20, 100)

        
        ########## - LES ITEMS DE L'INVENTAIRE - ############
        
        glaive = Item("glaive",player="ex", imageIdle="images/inv_swordIdle.png",imageHover="images/inv_swordHover.png")
        bouclier = Item("bouclier",player="ex", imageIdle="images/inv_shieldIdle.png",imageHover="images/inv_shieldHover.png")   
        blague = Item("blague",player="goat_char", imageIdle="images/inv_jokeIdle.png",imageHover="images/inv_jokeHover.png") 
        lunettes = Item("lunettes",player="ex", imageIdle="images/inv_glassesIdle.png",imageHover="images/inv_glassesHover.png")
        trompette = Item("trompette",player="ex", imageIdle="images/inv_glassesIdle.png",imageHover="images/inv_glassesHover.png")
            
        ########## - LES ITEMS DE L'INVENTAIRE - ############
        
        _testBlague = 0
        _testBouclier = 0
        _testGlaive = 0
        _testLunettes = 0
        _testTrompette = 0

    jump intro
    
# -----------------------------------------#
    
label intro:
    window hide
    show bg_map:
        zoom 1.1,xanchor 0.0 yanchor 0.0
        xpos 0.0 ypos -0.10
        linear 6.0 xpos -0.3 ypos 0.0 zoom 1.4
        
    outline "En l'an 70 après Jissé, toute la Germanie est occupée par les Romains"
    show bg_champ with Dissolve(2.0):
        zoom 1.1,xanchor 0.0 yanchor 0.0
        xpos 0.0 xpos -0.10
        linear 10.0 ypos -0.3 xpos 0.0 zoom 1.4
    outline "Bon, pas vraiment toute en faite..."
    show bg_blacksmith with Dissolve(2.0):
        zoom 1.1,xanchor 0.0 yanchor 0.0
        xpos 0.0 ypos -0.10
        linear 11.0 xpos -0.3 ypos 0.0 zoom 1.4
    outline "En tout cas pas le village des Bructères, où habite la légendaire prophétesse Véléda."
    outline "Mais toi, tu vas plutôt incarner Gaufrid, son assistant. Il doit sûrement être à la taverne"
    outline "C'est un peu sa deuxième maison..."
    
    jump taverne_DatingIngrid
    
# -----------------------------------------#

label narration_ellipse01: #La première ellipse après le Dating Sim avec Ingrid
    "Entrée dans narration_ellipse01"
    
    dig "Wesh weh"
    jump tourVeleda_ErnustEtVeleda
    
# -----------------------------------------#    
    
label narration_ellipse02:
    "Entrée narration_ellipse02"
    
    jump taverne_PresentationDot
    
# -----------------------------------------#

label PlaceDuVillageDefault:
    menu:
        "Aller à la Taverne":
            jump taverne_AbusAlcoolPart1
        "Aller aux Etables":
            jump etables_PeurDesBufflesPart1
        "Aller à la Forge":
            jump forge_BrutalmundEtBeaudrik
        "Aller à la Tente Romaine":
            jump romains_PremiereRencontre

# -----------------------------------------#

label narration_ellipseCuite:
    "narration_ellipseCuite"
    
    jump PlaceDuVillageDefault

# -----------------------------------------#

label PlaceDuVillageAllObjects:
    "Tous les objets réunis !"
    menu:
        "Aller à la Taverne":
            jump taverne_ConcoursPart1

# -----------------------------------------#





###########################################################################################
# OLD - Le proto technique avec les dialogues correspondant et les enchainements utilisés #
###########################################################################################

label OLD_start:
    python :
        ###Les personnages
        goat_char = Chara("Goat", 20,100)
        vel_char = Chara("Véléda", 25,100)
        #### On crée nos items
        glaive = Item("glaive",player="ex", imageIdle="images/inv_swordIdle.png",imageHover="images/inv_swordHover.png")
        bouclier = Item("bouclier",player="ex", imageIdle="images/inv_shieldIdle.png",imageHover="images/inv_shieldHover.png")   
        blague = Item("blague",player="goat_char", imageIdle="images/inv_jokeIdle.png",imageHover="images/inv_jokeHover.png") 
        lunettes = Item("lunettes",player="ex", imageIdle="images/inv_glassesIdle.png",imageHover="images/inv_glassesHover.png") 
            
        inventory = Inventory()
        inventory.add(glaive)
        inventory.add(bouclier)
        inventory.add(blague)
        inventory.add(lunettes)  
        
        interlocuteur = "None" ## Ne pas oublier d'actualiser le nom de l'interlocuteur à chaque changement
        lieu = "None"
        CAactif = False ## Set à False après chaqu actionChoice

label startBar:
    
    scene bg_bar with Dissolve (2.0)
    window show
    show goat with Dissolve(1.5)
    hide screen inventory_button

    $ lieu = "bar"
    
    $ CAactif = True
    $ actionChoice = "action_choice_"+ str(lieu) ##Copier ces lignes à chaque fois qu'on change de lieu, en actualisant le nom
    $ CAactif = False
    $ _return = renpy.call_screen(actionChoice)
    
    if _return == "boire":
        narration "Tu bois un verre."
        narration "C'est de l'eau."
        narration "L'effet escompté n'est pas au rendez-vous..."
        jump startBar
        
    elif _return == "sortir":
        narration "Tu essaies de sortir"
        narration "Malheureusement, les développeurs n'ont pas encore développé cette feature"
        
        menu:
            narration "t'es vraiment sur de vouloir sortir ?"
            
            "OUIIIII !":
                menu:
                    
                    narration "genre vraiment ?"
                   
                    "OUI.":
                        narration "bon, ok. ciao"
                        return
                   
                    "Non pas vraiment en fait, je voulais juste voir ce que ça faisait, mais maintenant j'hésite":
                        narration "sage décision"
                        jump startBar
           
            "Je suis pas sur du tout ! Je déteste faire des choix ça me stresse ! aaaaaah!":
                narration "Oui, tout-à-fait..."
                narration "On va faire comme si rien ne s'était passé ok ?"
                jump startBar
        
    elif _return == "goat2":
        $ interlocuteur = "goat_char"
        show screen datingSim(goat_char, 0.54, 0.45) 
        jump goat

label goat:
    c "Bêêêêêêêêê"
    
    menu :
        c "{cps=0}Bêêêêêêêêê{/cps}"
        "{color=#c4ae33}1. Absolument, tu as raison{/color}":
            y "Mais... OUI !"
            $ loveGauge(goat_char, 5)
            y "C'est TOUT A FAIT CA !"
            $ loveGauge(goat_char, 10)
            y "Mon dieu, toi et moi c'est comme si notre conscience ne faisait qu'un !"
            $ loveGauge(goat_char, 2)
            y "Tu sais... moi j'appelle ça le destin"
            y "On pense pareil, on fait les même réflexion, on fréquente la même taverne..."
            $ loveGauge(goat_char, 1)
            y "Tu crois aux âmes soeurs toi ?"
            jump goat_a2
        "{color=#c4ae33}2. Je ne suis pas daccord{/color}":
            y "Je peux pas te laisser dire ça désolé !"
            $ loveGauge(goat_char, -2)
            y "C'est complètement irrespectueux pour les buffles, ils ont pas une vie facile les buffles tu sais ?"
            $ loveGauge(goat_char, -3)
            y "Et puis c'est fondamentalement faux en plus"
            $ loveGauge(goat_char, -3)
            y "Non vraiment, ce que tu dis là, ça me déçoit de toi !"
            $ loveGauge(goat_char, -5)
            jump goat_b2
        "3. Je n'ai pas compris":
            y "Excusez-moi, je n'ai pas bien saisi le sens de ce que vous venez de dire"
            y "Vous pouvez détailler ?"
            y "..."
            y "non ?"
            jump goat_a2

label goat_a2:        
    c "Bêêêêêêêêê"
    menu :
        c "{cps=0}Bêêêêêêêêê{/cps}"
        
        "{color=#c4ae33}1. Ouais, moi non plus... {/color}":
            y "Ouais, moi non plus j'y crois pas..."
            $ loveGauge(goat_char, 5)
            y "Comme disait mon oncle pêcheur, les âmes soeurs ça vaut rien, mieux vaut un bon âme-çon"
            $ loveGauge(goat_char, -3)
            y "Je sais pas pourquoi ça le faisait toujours rire de dire ça..."
            $ loveGauge(goat_char, 10)
            jump goat_a3
            
        "{color=#c4ae33}2. Tu devrais y croire tu sais !{/color}":
            y "Tu devrais y croire aux âmes soeurs, tu sais !"
            y "Certaines choses ne peuvent pas être simplement le fruit du hasard !"
            y "Les étoiles dans le ciel, le chant des oiseaux, notre rencontre..."
            $ loveGauge(goat_char, 3)
            y "C'était forcément écrit !"
            $ loveGauge(goat_char, 15)
            jump goat_a3
        
        "{color=#c4ae33}3. Tu t'en fiches en fait ?{/color}":
            y "Tu t'en fiches en fait ?"
            y "Tu peux le dire clairement hein, pas besoin d'être méprisante !"
            $ loveGauge(goat_char, -5)
            y "C'est blessant tu sais ?"
            y "Parfois... J'ai l'impression que t'écoutes pas vraiment ce que je dis..."
            $ loveGauge(goat_char, -2)
            jump goat_a3
            
label goat_a3:
    c "Bêêêêêêêêê"
    menu :
        c "{cps=0}Bêêêêêêêêê{/cps}"
        
        "{color=#c4ae33}1. Sinon, tu sais que tu as de beaux yeux ? {/color}":
            y "Sinon, on t'as déjà dit que t'avais de beaux yeux ?"
            $ loveGauge(goat_char, 5)
            y "Je suis sérieux, l'éclat de tes yeux illumine les tréfonds de mon âme"
            $ loveGauge(goat_char, 15)
            jump goat_a4
        "1. T'as raison, ça n'a pas d'importance, désolé":
            y "T'as raison, ça n'a aucune importance, désolé..."
            $ loveGauge(goat_char, 2)
            y "C'est ma faute j'ai  tendance à divaguer et à changer de sujet"
            y "J'ai toujours eu du mal à suivre le fil d'une discussion"
            y "C'est assez handicapant au quotidien tu sais ?"
            y "T'as jamais eu cette impression que tout n'était qu'illusion ?"
            $ loveGauge(goat_char, 6)
            y "Que tes choix, tes interactions avec les autres, tout ça n'avait aucune importance ?"
            $ loveGauge(goat_char, 1)
            y "Que quoi que tu fasses, la fin sera la même ?"
            y "Enfin... Voilà que je recommence... Revenons à nos moutons"
            c "Bêêêêêêê !"
            $ loveGauge(goat_char, -5)
            y "Oups pardon je voulais pas te vexer !"
            y "Je suis absolument confus..."
            $ loveGauge(goat_char, 3)
            jump goat_a3
            
label goat_a4:
    c "Bêêêêêêêêê"
    menu :
        c "{cps=0}Bêêêêêêêêê{/cps}"
        
        "{color=#c4ae33}1. Marions-nous ! {/color}":
            y "Tu es la perfection incarnée"
            $ loveGauge(goat_char, 20)
            y "Et je suis pas mal non plus"
            y "On est fait l'un pour l'autre, marions-nous !"
            c "Bêêêêêêêêêêê !"
            jump mariage
        "{color=#c4ae33}2. Viens chez moi {/color}":
            y "Tu sais... chez moi, j'ai un hydromel que mon cousin fait lui-même"
            $ loveGauge(goat_char,3)
            y "Il a un goût fabuleux !"
            $ loveGauge(goat_char,6)
            y "Légèrement fruité, avec un arôme de crustacé qui relêve le tout"
            y "On peut peut-être en boire ensemble... ?"
            $ loveGauge(goat_char,11)
            c "Bêêêêêêêêêêê !"
            jump mariage

label goat_b2:
    y "Tu devrais faire attention à ce que tu dis tu sais"
    $ loveGauge(goat_char, -4)
    y "Moi, c'est bon, je t'aime bien donc ça va"
    $ loveGauge(goat_char, 2)
    y "Mais si tu dis ça à la mauvais personne, tu risque de la vexer"
    $ loveGauge(goat_char, -1)
    y "Imagine, si le père de la personne en question est un buffle !"
    y "C'est l'accident diplomatique assuré !"
    c "Bêêêêêêêêêêêêêêê"
    y "Voilà, je préfère ça !"
    c "Bêêêêêêêêêêêêêêê"
    y "Mais... OUI !"
    $ loveGauge(goat_char, 5)
    y "C'est TOUT A FAIT CA !"
    $ loveGauge(goat_char, 10)
    y "Mon dieu, toi et moi on est pareil en fait!"
    $ loveGauge(goat_char, 2)
    y "Désolé de m'être énervé tout à l'heure"
    y "Je pensais juste pas rencontrer quelqu'un comme toi ici"
    y "Tu sais... moi j'appelle ça le destin"
    y "On pense pareil, on fait les même réflexion, on fréquente la même taverne..."
    $ loveGauge(goat_char, 1)
    y "Tu crois aux âmes soeurs toi ?"
    jump goat_a2
label mariage:
    y "Comment ? Tu me trouves ennuyant ?"
    "{i}*Si seulement j'avais une histoire drôle à lui raconter...*{/i}"
    hide screen datingSim
    show screen inventory_screen(obj = "blague")
    narration "{w=1.5}Gaufrid sort une blague de son sac"
    jump useBlagueSuccess