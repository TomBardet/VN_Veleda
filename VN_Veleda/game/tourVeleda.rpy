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
    v "Cela suffira ! Et vous, Gaufrid, allez accueillir Nos invités, Nous prophétisons qu'ils vont frapper à la porte !"
    
    play sound "sfx/SFX_Knock_01.ogg"
    v "Haa, vous voyez ? Allez-y Monsieur Gaufrid."
    
    play sound "sfx/SFX_Char_Player_Ok_01.ogg"
    y "Ok, ok j'y vais..."
    
    hide screen datingSim
    
    scene black with Dissolve(0.5)
    play sound "sfx/SFX_Stairs_01.ogg"
    outline "Travelling vers le bas"
    
    jump tourVeleda_HistoireBrevetPart1
        
# -----------------------------------------#

label tourVeleda_HistoireBrevetPart1:
    
    scene bg_antichambre
    
    show char_brutal normal :
        zoom 0.35 xpos 0.48 ypos 0.09
    show char_crossfit colere right :
        zoom 0.32 xpos 0 ypos 0.13
    
    play sound "sfx/SFX_Char_Crossfit_Serieux_01.ogg"
    cross "Nous voilà ! Je vais enfin trouver justice, Brutalmund !"
    
    play sound "sfx/SFX_Char_Brutalmund_Normal_01.ogg"
    brut "J't'ai déjà dit que j't'ai rien volé du tout !"
    
    play sound "sfx/SFX_Char_Crossfit_Colere_01.ogg"
    cross "Toi, l'assistant, va chercher la prophétesse !"
    
    play sound "sfx/SFX_Char_Player_No_01.ogg"
    y "Ah non, c'est pas comme ça que ça marche."
    y "La prophétesse ne voit pas directement ses visiteurs."
    
    
    play sound "sfx/SFX_Char_Crossfit_Colere_01.ogg"
    cross "Quoi ? Je ne peux pas voir la prophétesse ?"
    
    play sound "sfx/SFX_Char_Player_No_01.ogg"
    y "Non, non. Vous m'expliquez le problème, je lui transmet et elle s'adresse aux dieux..."
    y "Elle divague un peu et moi je vous interprète ses visions."
    
    play sound "sfx/SFX_Char_Crossfit_Serieux_01.ogg"
    cross "Très bien, serviteur, mais si tu ne transmet pas nos messages exactement, je t'égorge."
    
    menu :
        "1. Oui, Monseigneur" :
            play sound "sfx/SFX_Char_Player_Ok_01.ogg"  
            y "Bien sur Monsieur Crossftrichtrolvd, je ferai bien attention."
            
        "2. Je sais faire mon travail, hein" :
            play sound "sfx/SFX_Char_Player_Sarcasm_01.ogg"  
            y "Eh oh je sais ce que je fais hein ? Pas la peine de me menacer."
            
    y "Bon, dites moi tout, quel est le problème ?"
    
    play sound "sfx/SFX_Char_Brutalmund_Normal_01.ogg"
    brut "J'vais t'expliquer, Gaufrid, mon pote."
    brut "Tu vois, l'autre jour, Crossfitrichernvald, il passe devant chez moi."
    brut "T'sais j'ai une forge moi, j'suis forgeron."
    brut "Et donc il voit un bouclier qui ressemble au sien."
    
    play sound "sfx/SFX_Char_Brutalmund_Colere_01.ogg"
    brut "Et il gueule !"
    
    play sound "sfx/SFX_Char_Brutalmund_Normal_01.ogg"
    brut "Mais en fait, je l'ai pas volé c'te bouclier !"
    brut "C'est moi qui l'ai fait. De mes mains ! J'te jure mon p'tit Gaufrid !"
    
    play sound "sfx/SFX_Char_Crossfit_Colere_01.ogg"
    cross "Ah mais tu sais bien que c'est pas ça le problème, escroc !"
    
    play sound "sfx/SFX_Char_Brutalmund_Colere_01.ogg"
    brut "Moi ? Un escroc ?"
    
    play sound "sfx/SFX_Char_Crossfit_Serieux_01.ogg"
    cross "Oui, un escroc ! Ce bouclier est exactement le même que le mien." 
    cross "Un magnifique bouclier-traîneau à 3 vitesses !"
    cross "Je me souviens très bien, aux dernier jeux inter-germains, tu as fait un commentaire dessus !"
    
    menu :
        "1. Il l'a volé ?" :
        
            play sound "sfx/SFX_Char_Player_Ok_01.ogg"
            y "Il l'aimait bien alors il l'a volé, c'est ça ?"
            
            play sound "sfx/SFX_Char_Brutalmund_Colere_01.ogg"
            brut "Mon propre ami, Gaufrid, qui me traite de voleur !"
            
            play sound "sfx/SFX_Char_Crossfit_Colere_01.ogg"
            cross "Tu n'as rien compris, valet ! Ce qu'il a volé, c'est l'idée !" 
            cross "C'est du vol de propriété intellectuelle !"
            
        "2. Il en a fait un pareil ?" :
            
            play sound "sfx/SFX_Char_Player_Ok_01.ogg"
            y "Donc il a fait une copie ? Quel est le problème ?"
            
            play sound "sfx/SFX_Char_Crossfit_Colere_01.ogg"
            cross "Le problème ? Mais c'est du vol de propriété intellectuelle !"
            
    play sound "sfx/SFX_Char_Brutalmund_Colere_01.ogg"
    brut "Oh, toi, tout de suite avec les grands mots hein !"
    
    play sound "sfx/SFX_Char_Crossfit_Serieux_01.ogg"
    cross "Le concept de propriété intellectuelle est fondamental à la société Germaine !"
    cross "D'après la convention de Genava de l'an 2 avant Jésus-christ et d'après l'alinéa 51 des textes runiques de Wotan et Tyr..."
    cross "Toute invention Germaine sera respectée comme la propriété propre, indétachable et sans exception de son inventeur."
    
    menu :
        "1. C'est très grave !" :
            
            y "Si les textes le disent, c'est que c'est très grave !"
            brut "Tu t'y mets toi aussi ! Mon Gaufrid, mon poteau !"
            y "Bon, je vais voir ce qu'en dit notre divine prophétesse."
        "2. On s'en fout, non ?" :
            
            y "Y'a pas de quoi en faire toute une chouquette, non ?"
            
            cross "Comment oses-tu, domestique ?"
            cross "Nos lois sont clairs ! Va voir la prophétesse maintenant !"
            
            y "Ok ! Ok, j'y vais ! Faut pas s'énerver comme ça !"
            
    hide char_brutal normal
    hide char_crossfit colere right

    scene black with Dissolve(0.5)
    play sound "sfx/SFX_Stairs_02.ogg"
    outline "Travelling vers le haut"
    
    jump tourVeleda_MortVeleda
    
# -----------------------------------------#
    
label tourVeleda_MortVeleda:
    
    scene bg_chambre
    show char_ernust normal right :
        zoom 0.9 xpos 0.12 ypos 0.2
    
    e "Ah Gaufrid, ça c'est bien passé ?"
    e "Véléda fait une petite sieste !"
    
    y "Comment ça une sieste ?"
    y "On a besoin d'une prophétie là !"
    
    e "Bah oui, elle a mangé ma soupe aux champignons et après elle a fait des bruits bizarres."
    e "Je pense qu'elle a vomi à un moment mais après elle s'est endormie tranquillement !"
    
    y "Quoi ? Mais c'était quoi comme champignons ?"
    y "Va voir tout de suite si elle va bien !"
    
    outline "Ernust se faufile derrière le voile (on change son image"
    
    e "Elle va pas bien du tout Gaufrid !"
    e "Je sens pas du tout son pouls !"
    
    y "Quoi ? Mais.. tu as tué Véléda, Ernust !"
    y "La prophétesse la plus connue de toute l'histoire !"
    y "Qu'est ce qu'on va faire ?"
    
    e "Oh je suis désolé Gaufrid !"
    e "Tu peux peut être faire une prophétie toi ?"
    
    menu :
        "1. C'est complètement idiot." :
            y "Tu dis vraiment n'importe quoi Ernust !"
            y "J'ai l'air d'être un prophête moi ?"
            y "Mais attend... j'ai une idée !"
            y "Je vais faire semblant ! Je vais inventer une prophétie !"
            y "Ils verront jamais la différence !"
            
            e "Qu'est ce que t'es intelligent Gaufrid !"

        "2. Bonne idée !" :
            y "Bien vu Ernust ! Ça c'est vraiment une bonne idée !"
            y "Je vais inventer une prophétie ! Ils verront jamais la différence !"
            
    y "J'y vais, bouge surtout pas d'ici !"
    
    scene black with Dissolve(0.5)
    play sound "sfx/SFX_Stairs_01.ogg"
    outline "Travelling vers le bas"
    
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