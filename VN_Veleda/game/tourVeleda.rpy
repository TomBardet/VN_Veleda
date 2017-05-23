##########################################################
# Ici figurent les scènes se déroulant à la Tour Véléda. #
##########################################################

label tourVeleda_ErnustEtVeleda :
    scene bg_chambre
    
    show char_veleda normal at right
    
    $ interlocuteur = "vel_char"
    show screen datingSim(vel_char, 0.75, 0.25)
    
    play sound "sfx/SFX_Char_Veleda_Normal_01.ogg"
    
    v "Vous voilà Gaufrid ! Dépèchez vous, Nous attendons des clients très importants."
    
    $ loveGauge(vel_char, -3, 0.80, 0.25)

    play sound "sfx/SFX_Char_Player_Question_01.ogg"
    y "Mais c'est encore là ces chiffres ? J'ai perdu la boule ou quoi ?"
    
    play sound "sfx/SFX_Char_Veleda_Rage_01.ogg"
    
    v "Des chiffres ? De quoi parlez vous ?"
    
    $ loveGauge(vel_char, -3, 0.85, 0.25)
    
    v "Allez préparer la salle Monsieur Gaufrid, vos anneries ne Nous intéressent pas."
    
    $ loveGauge(vel_char, -3, 0.8, 0.25)
    
    v "Nous attendons un invité de marque aujourd'hui ! Monseigneur Crossfrit... croshfritsh... crosrustr..."
    
    v "Crousfrishtrenvra... Monseigneur Crossfichtruc, le digne chef de nos voisins les Bataves."
    
    menu :
        "1. Il vient demander conseil, Ô Véléda ? ":
            play sound "sfx/SFX_Char_Player_Ok_01.ogg"
            y "Crossfitrtrch... Crossfitrichernvald ? Il vient écouter la grande sagesse de vos légendaires prophéties, Ô divine Véléda ?"
            
            play sound "sfx/SFX_Char_Veleda_Normal_01.ogg"
    
            v "Oh vous ne Nous trompez pas avec vos minauderies Monsieur Gaufrid."
            
            $ loveGauge(vel_char, -3, 0.8, 0.25)
    
            v "La flatterie est le refuge des incompétents et des poissoniers."
            
            $ loveGauge(vel_char, -3, 0.8, 0.25)
            
        "2. Il veut quoi lui ?":
            play sound "sfx/SFX_Char_Player_Question_01.ogg"
            y "Crossfitrtrch... Crossfitrichernvald ? Qu'est ce qu'il veut lui ?"
            
            play sound "sfx/SFX_Char_Veleda_Normal_01.ogg"
            
            v "Oh ! Quelle vulgarité Monsieur Gaufrid !"
            
            $ loveGauge(vel_char, -3, 0.8, 0.25)
            
            v "Qu'est ce que c'est que ce langage de jarretière ?"
            
            $ loveGauge(vel_char, -3, 0.8, 0.25)
            
    v "Monseigneur Crossfritruc accuse le forgeron de notre village, Monsieur Brutalmund !"
    
    v "Il l'accuse de lui avoir dérobé sa propriété !"
    
    v "Monsieur Brutomachin nie l'accusation ! Nous allons donc les départager avec..."
    
    #Ajouter ici un son dramatique"
    
    play sound "sfx/SFX_Drama_01.ogg"
    
    v "Une prophétie !"
    
    play sound "sfx/SFX_Char_Player_Sarcasm_01.ogg"
    
    y "Euh.. ils devraient pas plutôt porter plainte ?"
    
    play sound "sfx/SFX_Char_Veleda_Rage_01.ogg"
    
    v "Vous doutez de la sagesse de Nos visions, Monsieur Gaufrid ?"
    
    $ loveGauge(vel_char, -3, 0.8, 0.25)
    
    v "Où se trouve votre cousin d'ailleurs ? Le simplet, Monsieur Ernust ?"
    
    v "Cela fait un heure qu'il doit Nous apporter de quoi Nous sustenter !"
    
    play sound "sfx/SFX_Entrance_01.ogg"
    
    v "Ah ! Cela doit être lui !"
    
    show char_ernust normal right :
        zoom 0.9 xpos 0.15 ypos 0.2
    
    play sound "sfx/SFX_Char_Ernust_Normal_01.ogg"
    
    $ interlocuteur = "ern_char"
    show screen datingSim(ern_char, 0.25, 0.10)
    
    e "Oh, Bonjour Gaufrid !"
    $ loveGauge(ern_char, 1, 0.3, 0.10)
    
    menu :
        "1. Bonjour Ernust !" :
            play sound "sfx/SFX_Char_Player_Ok_01.ogg"
            y "Bonjour Ernust, comment ça va ?"
            hide char_ernust normal right
            show char_ernust joyeux right :
                zoom 0.9 xpos 0.13 ypos 0.13
            play sound "sfx/SFX_Char_Ernust_Joyeux_01.ogg"
            $ loveGauge(ern_char, 3, 0.3, 0.10)            
            e "Ça va bien !"
            $ loveGauge(ern_char, 3, 0.3, 0.10)
            e "C'est gentil de demander Gaufrid !"
            hide char_ernust joyeux right
            show char_ernust normal right :
                zoom 0.9 xpos 0.12 ypos 0.2
            
        "2. Il est amoureux de moi ?" :
            play sound "sfx/SFX_Char_Player_Question_01.ogg"
            y "90 de love ? Mais il est amoureux de moi ou quoi ?"
            hide char_ernust normal right
            show char_ernust love :
                zoom 0.9 xpos 0.12 ypos 0.2
            play sound "sfx/SFX_Char_Ernust_Love_01.ogg"
            $ loveGauge(ern_char, 3, 0.3, 0.10)            
            e "T'es mon meilleur ami Gaufrid !"
            $ loveGauge(ern_char, 3, 0.3, 0.10)
            e "J'taime bien !"
            hide char_ernust love
            show char_ernust normal right :
                zoom 0.9 xpos 0.12 ypos 0.2
            
        "3. Ah, t'es là, toi ?" :
            play sound "sfx/SFX_Char_Player_Sarcasm_01.ogg"
            y "Ah, t'es là toi ? Pfff..."
            hide char_ernust normal right
            show char_ernust joyeux right :
                zoom 0.9 xpos 0.13 ypos 0.13
            play sound "sfx/SFX_Char_Ernust_Joyeux_01.ogg"
            $ loveGauge(ern_char, 3, 0.3, 0.10)            
            e "Oui je suis là !"
            $ loveGauge(ern_char, 3, 0.3, 0.10)
            e "Moi aussi ça me fait plaisir de te voir Gaufrid !"
            hide char_ernust joyeux right
            show char_ernust normal right :
                zoom 0.9 xpos 0.12 ypos 0.2
            
    play sound "sfx/SFX_Char_Veleda_Normal_01.ogg"
    v "Vous êtes adorables Messieurs mais amenez Nous Notre nourriture. Nous Nous tordons de douleur de faim."
    
    play sound "sfx/SFX_Char_Ernust_Normal_01.ogg"
    e "Oh Oui, Votre Excellessence Madame Véléda !"
    e "J'suis désolé hein j'ai pris longtemps !"
    e "J'suis allé dans la forêt chasser un sanglier."
    play sound "sfx/SFX_Char_Ernust_Joyeux_01.ogg"
    e "Vous savez j'me suis dit un bon sanglier rôti, ça tient le corps et c'est vraiment bon !"
    e "Avec un peu de thym et des p'tites pommes sautées..."
    
    menu :
        "1. Ça a l'air délicieux !" :
            play sound "sfx/SFX_Char_Player_Ok_01.ogg"
            y "Ça a l'air super bon Ernust, j'ai hâte de voir ça !"
            
            hide char_ernust normal right
            show char_ernust joyeux right :
                zoom 0.9 xpos 0.13 ypos 0.13
            
            play sound "sfx/SFX_Char_Ernust_Joyeux_01.ogg"
            $ loveGauge(ern_char, 3, 0.3, 0.10)
            e "T'es gentil Gaufrid !"
            $ loveGauge(ern_char, 2, 0.3, 0.10)
            e "Je pensais à toi en plus, je me suis dit, Gaufrid il doit être triste !"
            $ loveGauge(ern_char, 2, 0.3, 0.10)
            e "Ingrid elle est pas gentille avec toi !"
            e "Elle regarde tout le temps Beaudrik, tu sais le grand, là."
            e "C'est vrai qu'il est plus beau, plus fort et plus riche que toi."
            $ loveGauge(ern_char, 5, 0.3, 0.10)
            e "Mais moi je trouve que t'es vraiment spécial Gaufrid."
            
            hide char_ernust joyeux right
            show char_ernust normal right :
                zoom 0.9 xpos 0.12 ypos 0.2
            
        "2. Tu peux abréger ?" :
            play sound "sfx/SFX_Char_Player_Sarcasm_01.ogg"
            y "Abrège Ernust, on attend des clients."
            
            play sound "sfx/SFX_Char_Ernust_Normal_01.ogg"
            
            e "T'as raison Gaufrid, je parle trop encore."
            
            hide char_ernust normal right
            show char_ernust joyeux right :
                zoom 0.9 xpos 0.13 ypos 0.13
                
            play sound "sfx/SFX_Char_Ernust_Joyeux_01.ogg"
            
            $ loveGauge(ern_char, 3, 0.3, 0.10)
            e "Tu me dis tout le temps quand je fais des bêtises !"
            $ loveGauge(ern_char, 2, 0.3, 0.10)
            e "Ça m'aide beaucoup tu sais, j'ai l'impression d'être plus intelligent avec toi !"
            $ loveGauge(ern_char, 5, 0.3, 0.10)
            play sound "sfx/SFX_Char_Ernust_Joyeux_01.ogg"
            e "T'es carrément plus intelligent que Beaudrik."
            $ loveGauge(ern_char, 2, 0.3, 0.10)
            e "Tu sais le grand beau gosse là, que Ingrid regarde tout le temps."
            
            hide char_ernust joyeux right
            show char_ernust normal right :
                zoom 0.9 xpos 0.12 ypos 0.2
                
    play sound "sfx/SFX_Char_Veleda_Normal_01.ogg"
    v "Cela suffit ! Servez Nous Notre sanglier !"
    
    play sound "sfx/SFX_Char_Ernust_Inquiet_01.ogg"
    e "Ah bah non y'a pas de sanglier."
    e "J'en ai vu un dans la forêt mais bon j'ai eu peur en fait."
    e "En plus j'ai pas d'arme, ça se chasse pas à mains nues hein, le sanglier."
    
    hide char_ernust normal right
    show char_ernust joyeux right :
        zoom 0.9 xpos 0.13 ypos 0.13
    play sound "sfx/SFX_Char_Ernust_Joyeux_01.ogg"
    e "Mais j'ai trouvé des champignons alors j'ai fait une soupe ! Une bonne soupe de champignons !"
    
    play sound "sfx/SFX_Char_Veleda_Rage_01.ogg"
    v "Cela suffira ! Et vous, Gaufrid, allez accueillir Nos invités, je prophétise qu'ils vont frapper à la porte !"
    
    play sound "sfx/SFX_Knock_01.ogg"
    
    y "Ok, ok j'y vais..."
    
    hide screen datingSim
    
    jump tourVeleda_HistoireBrevetPart1
        
# -----------------------------------------#

label tourVeleda_HistoireBrevetPart1:
    "Entrée tourVeleda_HistoireBrevetPart1"
    
    jump tourVeleda_MortVeleda
    
# -----------------------------------------#
    
label tourVeleda_MortVeleda:
    "Entrée tourVeleda_MortVeleda"
    
    jump tourVeleda_HistoireBrevetPart2
    
# -----------------------------------------#
    
label tourVeleda_HistoireBrevetPart2:
    "Entrée tourVeleda_HistoireBrevetPart2"
    
    jump narration_ellipse02
    
label tourVeleda_MarryingIngridPart2:
    "label tourVeleda_MarryingIngridPart2"
    
    menu:
        "Accuser la chêvre":
            jump ending_ChevreTrahie
        "Accuser Ernust":
            jump ending_ErnustTrahi
        "S'accuser":
            jump ending_ExilPart1