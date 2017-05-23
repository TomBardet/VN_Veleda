##########################################################
# Ici figurent les scènes se déroulant à la Tour Véléda. #
##########################################################

label tourVeleda_ErnustEtVeleda :
    scene bg_chambre
    
    show char_veleda normal at right
    
    $ interlocuteur = "vel_char"
    show screen datingSim(vel_char, 0.75, 0.25)
    
    play sound "sfx/Char_Veleda_Normal_01.ogg"
    
    v "Vous voilà Gaufrid ! Dépèchez vous, Nous attendons des clients très importants."
    
    $ loveGauge(vel_char, -3, 0.5, 0.5)

    y "Mais c'est encore là ces chiffres ? J'ai perdu la boule ou quoi ?"
    
    play sound "sfx/Char_Veleda_Rage_01.ogg"
    
    v "Des chiffres ? De quoi parlez vous ?"
    
    $ loveGauge(vel_char, -3, 0.5, 0.5)
    
    v "Allez préparer la salle Monsieur Gaufrid, vos anneries ne Nous intéressent pas."
    
    $ loveGauge(vel_char, -3, 0.5, 0.5)
    
    v "Nous attendons un invité de marque aujourd'hui ! Monseigneur Crossfrit... croshfritsh... crosrustr..."
    
    v "Crousfrishtrenvra... Monseigneur Crossfichtruc, le digne chef de nos voisins les Bataves."
    
    menu :
        "1. Il vient demander conseil, Ô Véléda ? ":
            y "Crossfitrtrch... Crossfitrichernvald ? Il vient écouter la grande sagesse de vos légendaires prophéties, Ô divine Véléda ?"
            
            play sound "sfx/Char_Veleda_Normal_01.ogg"
    
            v "Oh vous ne Nous trompez pas avec vos minauderies Monsieur Gaufrid."
            
            $ loveGauge(vel_char, -3, 0.5, 0.5)
    
            v "La flatterie est le refuge des incompétents et des poissoniers."
            
            $ loveGauge(vel_char, -3, 0.5, 0.5)
            
        "2. Il veut quoi lui ?":
            y "Crossfitrtrch... Crossfitrichernvald ? Qu'est ce qu'il veut lui ?"
            
            play sound "sfx/Char_Veleda_Normal_01.ogg"
            
            v "Oh ! Quelle vulgarité Monsieur Gaufrid !"
            
            $ loveGauge(vel_char, -3, 0.5, 0.5)
            
            v "Qu'est ce que c'est que ce langage de jarretière ?"
            
            $ loveGauge(vel_char, -3, 0.5, 0.5)
            
    v "Monseigneur Crossfritruc accuse le forgeron de notre village, Monsieur Brutalmund !"
    
    v "Il l'accuse de lui avoir dérobé sa propriété !"
    
    v "Monsieur Brutomachin nie l'accusation ! Nous allons donc les départager avec..."
    
    #Ajouter ici un son dramatique"
    
    play sound "sfx/SFX_Drama_01.ogg"
    
    v "Une prophétie !"
    
    y "Euh.. ils devraient pas plutôt porter plainte ?"
    
    play sound "sfx/Char_Veleda_Rage_01.ogg"
    
    v "Vous doutez de la sagesse de Nos visions, Monsieur Gaufrid ?"
    
    $ loveGauge(vel_char, -3, 0.5, 0.5)
    
    v "Où se trouve votre cousin d'ailleurs ? Le simplet, Monsieur Ernust ?"
    
    v "Cela fait un heure qu'il doit Nous apporter de quoi Nous sustenter !"
    
    play sound "sfx/SFX_Entrance_01.ogg"
    
    v "Ah ! Cela doit être lui !"
    
    show char_ernust normal right :
        zoom 0.9 xpos 0.15 ypos 0.1
    
    play sound "sfx/Char_Ernust_Normal_01.ogg"
    
    $ interlocuteur = "ern_char"
    show screen datingSim(ern_char, 0.25, 0.10)
    
    e "Oh, Bonjour Gaufrid !"
    
    menu :
        "1. Bonjour Ernust !" :
            y "Bonjour Ernust, comment ça va ?"
            
            hide char_ernust normal right
            show char_ernust joyeux right :
                zoom 0.9 xpos 0.12 ypos 0.07
        "2. Il est amoureux de moi ?" :
            y "90 de love ? Mais il est amoureux de moi ou quoi ?"
        "3. Ah, t'es là, toi ?" :
            y "Ah, t'es là toi ? Pfff..."
            
    v "End of sequence"
    
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