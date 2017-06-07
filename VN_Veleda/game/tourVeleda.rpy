##########################################################
# Ici figurent les scènes se déroulant à la Tour Véléda. #
##########################################################

label tourVeleda_ErnustEtVeleda :
    
    scene bg_tour with Dissolve (2.5) :
        xpos 0 ypos 0
    
    $ renpy.music.play("music/MUSIC_Tour_Chambre_Jour.ogg", channel = "music1", loop = True, fadein = 1)
    $ renpy.music.play("ambiances/AMB_Lieu_Tour_Chambre_01.ogg", channel = "ambiance", loop = True, fadein = 1)
    
    show vel_normal with Dissolve (2.5) :
        xpos 0 ypos 0

    
    #show char_veleda normal at speakingAnim(0.48,0.82,0.80,0.7)
    
    $ interlocuteur = "vel_char"
    show screen datingSim(vel_char, 0.7, 0.4)
    
    play sound "sfx/Voices/Veleda/Char_Veleda_Normal_04.ogg"
    
    v "Vous voilà Gaufrid ! Dépèchez vous, nous attendons des clients très importants."
    #show char_veleda normal at notSpeakingAnim(0.48,0.82,0.80,0.7)
    
    play sound "sfx/Voices/Player/Char_Player_Normal_02.ogg"
    y "Mais... c'est encore là ces chiffres ? J'ai perdu la boule ou quoi ?"
    
    play sound "sfx/Voices/Veleda/Char_Veleda_rage_01.ogg"
    #show char_veleda normal at speakingAnim(0.48,0.82,0.80,0.7)
    $ loveGauge(vel_char, -3, 0.75, 0.4)

    v "Des chiffres ? De quoi parlez vous, enfin ?"
    
    $ loveGauge(vel_char, -3, 0.75, 0.4)
    
    v "Allez préparer la salle, Monsieur Gaufrid. Vos anneries ne nous intéressent pas."
    


    play sound "sfx/Voices/Veleda/Char_Veleda_Normal_02.ogg"
    
    v "Nous attendons un invité de marque aujourd'hui ! Monseigneur Crossfrit... croshfritsh... crosrustr..."
    
    v "Monseigneur Crossfichtruc, le digne chef de nos voisins les Bataves."
    #show char_veleda normal at notSpeakingAnim(0.48,0.82,0.80,0.7)
    menu :
        "Il vient demander conseil, Ô Véléda ? ":
            play sound "sfx/Voices/Player/Char_Player_Normal_04.ogg"
            y "Vous voulez dire Crossfitrichernvald ?" 
            y "Il vient écouter la grande sagesse de vos légendaires prophéties, Ô divine Véléda ?"
            
            play sound "sfx/Voices/Veleda/Char_Veleda_Normal_03.ogg"
            #show char_veleda normal at speakingAnim(0.48,0.82,0.80,0.7)
            
            $ loveGauge(vel_char, -3, 0.5, 0.25)
            
            v "Oh vous ne nous trompez pas avec vos minauderies Monsieur Gaufrid."
            
            $ loveGauge(vel_char, -3, 0.75, 0.4)
    
            v "La flatterie est le refuge des incompétents."
            
            
        "Il veut quoi lui ?":
            play sound "sfx/Voices/Player/Char_Player_Normal_04.ogg"
            y "Vous voulez dire Crossfitrichernvald ?" 
            play sound "sfx/Voices/Player/Char_Player_Sarcastic_04.ogg"
            y "Qu'est ce qu'il veut, celui-là ?"
            
            play sound "sfx/Voices/Veleda/Char_Veleda_Normal_03.ogg"
            #show char_veleda normal at speakingAnim(0.48,0.82,0.80,0.7)
            
            $ loveGauge(vel_char, -3, 0.5, 0.25)
            v "Oh ! Quelle vulgarité Monsieur Gaufrid !"
            
            $ loveGauge(vel_char, -3, 0.5, 0.25)
            v "Qu'est ce que c'est que ce langage de sauvage ?"

            
    play sound "sfx/Voices/Veleda/Char_Veleda_Normal_01.ogg"
    
    v "Monseigneur Crossfriture accuse le forgeron de notre village, Monsieur Brutalmund, de lui avoir dérobé sa propriété !"
    
    v "Monsieur Brutalmund nie l'accusation ! Nous allons donc les départager avec..."
    
    play sound "sfx/SFX_Drama_01.ogg"
    
    v "Une prophétie !"
    #show char_veleda normal at notSpeakingAnim(0.48,0.82,0.80,0.7)
 #   play sound "sfx/SFX_Char_Player_Sarcasm_01.ogg"
 
    play sound "sfx/Voices/Player/Char_Player_Hesitation_01.ogg"
    y "Euh.. ils devraient pas plutôt porter plainte ?"
    
    play sound "sfx/Voices/Veleda/Char_Veleda_Rage_01.ogg"
    #show char_veleda normal at speakingAnim(0.48,0.82,0.80,0.7)
    
    $ loveGauge(vel_char, -3, 0.8, 0.25)
    v "Vous doutez de la sagesse de nos visions, Monsieur Gaufrid ?"
    
    v "Où se trouve votre cousin d'ailleurs ? Le simplet, Monsieur Ernust ?"
    
    play sound "sfx/Voices/Veleda/Char_Veleda_Normal_04.ogg"
    v "Cela fait une heure qu'il doit nous apporter de quoi nous sustenter !"
    
    play sound "sfx/SFX_Entrance_01.ogg"
    
    v "Ah ! Cela doit être lui !"
    #show char_veleda normal at notSpeakingAnim(0.48,0.82,0.80,0.7)
    show char_ernust normal right at speakingAnim(0.20,0.92,0.9,0.8)
   
    
 #   play sound "sfx/SFX_Char_Ernust_Normal_01.ogg"
    
    $ interlocuteur = "ern_char"
    show screen datingSim(ern_char, 0.25, 0.10)
    
    play sound "sfx/Voices/Ernust/Char_Ernust_Joyeux_03.ogg"
    e "Oh, Bonjour Gaufrid !"
    $ loveGauge(ern_char, 1, 0.3, 0.10)
    show char_ernust normal right at notSpeakingAnim(0.20,0.92,0.9,0.8)
    menu :
        e "{cps=0}Oh, bonjour Gaufrid !{/cps}"
        "Bonjour Ernust !" :
            play sound "sfx/Voices/Player/Char_Player_Normal_01.ogg"
            y "Bonjour Ernust, comment ça va ?"
            
            show char_ernust joyeux right at speakingAnim(0.20,0.92,0.9,0.8)
            play sound "sfx/Voices/Ernust/Char_Ernust_Normal_05.ogg"
            $ loveGauge(ern_char, 3, 0.3, 0.10)            
            e "Ça va bien !"
            $ loveGauge(ern_char, 3, 0.3, 0.10)
            e "C'est gentil de demander Gaufrid !"
            show char_ernust normal right at notSpeakingAnim(0.20,0.92,0.9,0.8)
            
        "90 points d'affection ?" :
            play sound "sfx/Voices/Player/Char_Player_Hesitation_04.ogg"
            y "90 de love ? Il est amoureux de moi ?"

            show char_ernust love at speakingAnim(0.20,0.92,0.9,0.8)
            play sound "sfx/Voices/Ernust/Char_Ernust_Normal_05.ogg"
            $ loveGauge(ern_char, 3, 0.3, 0.10)            
            e "T'es mon meilleur ami Gaufrid !"
            $ loveGauge(ern_char, 3, 0.3, 0.10)
            e "J'taime bien !"

            show char_ernust normal right at notSpeakingAnim(0.20,0.92,0.9,0.8)

            
        "Ah... t'es là, toi ?" :
            play sound "sfx/Voices/Player/Char_Player_Sarcastic_01.ogg"
            y "Ah... t'es là toi ? Pfff..."

            show char_ernust joyeux right at speakingAnim(0.20,0.92,0.9,0.8)

            play sound "sfx/Voices/Ernust/Char_Ernust_Normal_05.ogg"
            $ loveGauge(ern_char, 3, 0.3, 0.10)            
            e "Oui je suis là !"
            $ loveGauge(ern_char, 3, 0.3, 0.10)
            e "Moi aussi ça me fait plaisir de te voir Gaufrid !"

            show char_ernust normal right at notSpeakingAnim(0.20,0.92,0.9,0.8)
            
    play sound "sfx/Voices/Veleda/Char_Veleda_Normal_03.ogg"
    #show char_veleda normal at speakingAnim(0.48,0.82,0.80,0.7)
    v "Vous êtes adorables Messieurs, mais amenez nous notre nourriture. Nous mourrons de faim."
    #show char_veleda normal at notSpeakingAnim(0.48,0.82,0.80,0.7)
    play sound "sfx/Voices/Ernust/Char_Ernust_Normal_06.ogg"
    show char_ernust normal right at speakingAnim(0.20,0.92,0.9,0.8)
    e "Oh oui, Votre Excellessence Madame Véléda !"
    e "Je suis allé dans la forêt chasser un sanglier."
    play sound "sfx/Voices/Ernust/Char_Ernust_Normal_03.ogg"
    e "Je me suis dit : un bon sanglier rôti, ça tient le corps et c'est vraiment bon !"
    e "Avec un peu de thym et des p'tites pommes sautées..."
    show char_ernust normal right at notSpeakingAnim(0.20,0.92,0.9,0.8)
    menu :
        "Ça a l'air délicieux !" :
            play sound "sfx/Voices/Player/Char_Player_Heureux_03.ogg"
            y "Ça a l'air super bon Ernust, j'ai hâte de voir ça !"
            
            show char_ernust joyeux right at speakingAnim(0.20,0.92,0.9,0.8)
            
            play sound "sfx/Voices/Ernust/Char_Ernust_Joyeux_01.ogg"
            $ loveGauge(ern_char, 3, 0.3, 0.10)
            e "T'es gentil Gaufrid !"
            $ loveGauge(ern_char, 2, 0.3, 0.10)
            e "Je pensais à toi en plus. Je me suis dit : Gaufrid, il doit être triste !"
            $ loveGauge(ern_char, 2, 0.3, 0.10)
            play sound "sfx/Voices/Ernust/Char_Ernust_Inquiet_02.ogg"
            e "Ingrid elle est pas gentille avec toi !"
            $ loveGauge(ern_char, 5, 0.3, 0.10)
            e "Mais moi, je trouve que t'es vraiment spécial Gaufrid."
            
            show char_ernust normal right at notSpeakingAnim(0.20,0.92,0.9,0.8)
            
        "Tu peux abréger ?" :
            play sound "sfx/Voices/Player/Char_Player_Non_04.ogg"
            y "Abrège Ernust, on attend des clients."
            
            play sound "sfx/Voices/Ernust/Char_Ernust_Inquiet_02.ogg"
            show char_ernust normal right at speakingAnim(0.20,0.92,0.9,0.8)
            e "T'as raison Gaufrid. Je parle trop encore !"
            
            show char_ernust joyeux right at speakingAnim(0.20,0.92,0.9,0.8)
            
            $ loveGauge(ern_char, 3, 0.3, 0.10)
            e "Tu me dis tout le temps quand je fais des bêtises !"
            
            play sound "sfx/Voices/Ernust/Char_Ernust_Normal_02.ogg"
            $ loveGauge(ern_char, 2, 0.3, 0.10)
            e "Ça m'aide beaucoup tu sais. J'ai l'impression d'être plus intelligent avec toi !"
            
            show char_ernust normal right at notSpeakingAnim(0.20,0.92,0.9,0.8)
                
    play sound "sfx/Voices/Veleda/Char_Veleda_Normal_01.ogg"
    #show char_veleda normal at speakingAnim(0.48,0.82,0.80,0.7)
    v "Cela suffit ! Servez nous notre sanglier !"
    #show char_veleda normal at notSpeakingAnim(0.48,0.82,0.80,0.7)
    play sound "sfx/Voices/Ernust/Char_Ernust_Normal_06.ogg"
    show char_ernust normal right at speakingAnim(0.20,0.92,0.9,0.8)
    e "Ah bah non, y'a pas de sanglier !"
    e "J'en ai vu un dans la forêt mais bon... j'ai pas d'arme !"
    e "Ça se chasse pas à mains nues, hein, le sanglier."
    
    show char_ernust joyeux right at speakingAnim(0.20,0.92,0.9,0.8)
    
    play sound "sfx/Voices/Ernust/Char_Ernust_Joyeux_03.ogg"
    e "Mais j'ai trouvé des champignons, alors j'ai fait une soupe ! Une bonne soupe de champignons !"
    show char_ernust joyeux right at notSpeakingAnim(0.20,0.92,0.9,0.8)
    #show char_veleda normal at speakingAnim(0.48,0.82,0.80,0.7)
    play sound "sfx/Voices/Veleda/Char_Veleda_Normal_03.ogg"
    v "Cela suffira ! Et vous, Gaufrid, allez accueillir nos invités. Nous prophétisons qu'ils vont frapper à la porte !"
    
    play sound "sfx/SFX_Knock_01.ogg"
    v "Haa, vous voyez ? Allez-y, Monsieur Gaufrid."
    #show char_veleda normal at notSpeakingAnim(0.48,0.82,0.80,0.7)
    play sound "sfx/Voices/Player/Char_Player_Normal_04.ogg"
    y "Ok, ok, j'y vais..."
    
    window hide 
    
    stop music1 fadeout 1.5
    stop ambiance fadeout 0.5
    
    scene bg_tour :
        xpos 0 ypos 0
        linear 2.0 xpos 0 ypos -960
    show vel_normal :
        xpos 0 ypos 0
        linear 2.0 xpos 0 ypos -960
    show char_ernust normal right :
        xalign 0.5 yalign 0.8
        xpos 0.20 ypos 0.92 zoom 0.8
        linear 2.0 xpos 0.25 ypos -0.52
    show char_crossfit colere right :
        xalign 0.5 yalign 0.8
        xpos 0.20 ypos 3.0 zoom 0.32
        linear 2.0 xpos 0.26 ypos 0.84
    show char_brutal normal:
        xalign 0.5 yalign 0.8
        xpos 0.81 ypos 3.0 zoom 0.32
        linear 2.0 xpos 0.75 ypos 0.92
        
    play sound "sfx/SFX_Stairs_01.ogg"   
    $ renpy.pause(2.5, hard = True)
             
    
    jump tourVeleda_HistoireBrevetPart1
    #jump tourVeleda_MarryingIngridPart2
        
# -----------------------------------------#

label tourVeleda_HistoireBrevetPart1:

    $ renpy.music.play("music/MUSIC_Tour_Antichambre.ogg", channel = "music1", loop = True, fadein = 1)
    $ renpy.music.play("ambiances/AMB_Lieu_Antichambre_01.ogg", channel = "ambiance", loop = True, fadein = 1)
    

    #show char_brutal normal at notSpeakingAnim(0.75, 0.92,0.92,0.32) with Dissolve(1)

    
 #   play sound "sfx/SFX_Char_Crossfit_Serieux_01.ogg"
    show char_crossfit colere right at speakingAnim(0.26,0.94,0.92,0.32)
    cross "Nous voilà ! Je vais enfin trouver justice, Brutalmund !"
    
    show char_crossfit colere right at notSpeakingAnim(0.26,0.94,0.92,0.32)
    show char_brutal colere at speakingAnim(0.75, 0.82,0.80,0.32)
    #  play sound "sfx/SFX_Char_Brutalmund_Normal_01.ogg"
    brut "J't'ai déjà dit que j't'ai rien volé du tout !"
    
    show char_brutal normal at notSpeakingAnim(0.75, 0.92,0.92,0.32)
    show char_crossfit serieux at speakingAnim(0.26,0.94,0.92,0.32)
    #   play sound "sfx/SFX_Char_Crossfit_Colere_01.ogg"
    cross "Toi, l'assistant, va chercher la prophétesse !"
    
    show char_crossfit colere right at notSpeakingAnim(0.26,0.94,0.92,0.32)
 #   play sound "sfx/SFX_Char_Player_No_01.ogg"
    y "Ah non ! La prophétesse ne voit pas directement ses visiteurs."
    y "Vous m'expliquez le problème, je lui transmet, et elle s'adresse aux dieux..."
    y "Elle divague un peu et moi, je vous interprète ses visions."
    
    show char_crossfit colere right at speakingAnim(0.26,0.94,0.92,0.32)
 #   play sound "sfx/SFX_Char_Crossfit_Serieux_01.ogg"
    cross "Très bien, serviteur, mais si tu ne transmet pas nos messages exactement, je t'égorge."
    
    show char_crossfit colere right at notSpeakingAnim(0.26,0.94,0.92,0.32)
    menu :
        cross "{cps=0}Très bien, serviteur, mais si tu ne transmet pas nos messages exactement, je t'égorge.{/cps}"
        "Oui, Monseigneur" :
  #          play sound "sfx/SFX_Char_Player_Ok_01.ogg"  
            y "Bien sur Monsieur Crossfritrchrernvold, je ferai bien attention."
            
        "Je sais faire mon travail, hein" :
  #          play sound "sfx/SFX_Char_Player_Sarcasm_01.ogg"  
            y "Eh oh je sais ce que je fais hein ? Pas la peine de me menacer."
            
    y "Dites moi tout, quel est le problème ?"
    
 #   play sound "sfx/SFX_Char_Brutalmund_Normal_01.ogg"
    show char_brutal normal at speakingAnim(0.75, 0.92,0.92,0.32)
    brut "J'vais t'expliquer, Gaufrid, mon pote !"
    brut "T'vois, l'autre jour, Crossfitrichernvald, il passe d'vant chez moi."
    brut "Et donc, il voit un bouclier qui ressemble au sien."
    
 #   play sound "sfx/SFX_Char_Brutalmund_Normal_01.ogg"
    brut "Mais en fait, j'l'ai pas volé c'te bouclier !"
    brut "C'est moi qui l'ai fait. De mes p'tites mains ! J'te jure mon p'tit Gaufrid !"
    show char_brutal normal at notSpeakingAnim(0.75, 0.92,0.92,0.32)
 #   play sound "sfx/SFX_Char_Crossfit_Colere_01.ogg"
    show char_crossfit colere right at speakingAnim(0.26,0.94,0.92,0.32)
    cross "Ah mais tu sais bien que c'est pas ça le problème, escroc !"
    show char_crossfit colere right at notSpeakingAnim(0.26,0.94,0.92,0.32)
 #   play sound "sfx/SFX_Char_Brutalmund_Colere_01.ogg"
    show char_brutal normal at speakingAnim(0.75, 0.92,0.92,0.32)
    brut "Moi ? Un escroc ?"
    show char_brutal normal at notSpeakingAnim(0.68,0.94,0.92,0.35)
#    play sound "sfx/SFX_Char_Crossfit_Serieux_01.ogg"
    show char_crossfit colere right at speakingAnim(0.26,0.94,0.92,0.32)
    cross "Oui, un escroc ! Ce bouclier est exactement le même que le mien. Tu l'as copié !"
    cross "C'est du vol de propriété intellectuelle !"
    show char_crossfit colere right at notSpeakingAnim(0.26,0.94,0.92,0.32)        
 #   play sound "sfx/SFX_Char_Brutalmund_Colere_01.ogg"
    show char_brutal normal at speakingAnim(0.75, 0.92,0.92,0.32)
    brut "Oh, toi, tout de suite avec les grands mots hein !"
    show char_brutal normal at notSpeakingAnim(0.75, 0.92,0.92,0.32)
 #   play sound "sfx/SFX_Char_Crossfit_Serieux_01.ogg"
    show char_crossfit colere right at speakingAnim(0.26,0.94,0.92,0.32)
    cross "Le concept de propriété intellectuelle est fondamental à la société Germaine du premier siècle !"
    show char_crossfit colere right at notSpeakingAnim(0.26,0.94,0.92,0.32)
    menu :
        cross "{cps=0}Le concept de propriété intellectuelle est fondamental à la société Germaine du premier siècle !{/cps}"
        "C'est très grave !" :
            
            y "C'est vrai que c'est très grave !"
            show char_brutal normal at speakingAnim(0.75, 0.92,0.92,0.32)
            brut "Tu t'y mets, toi aussi ! Mon Gaufrid, mon poteau !"
            show char_brutal normal at notSpeakingAnim(0.75, 0.92,0.92,0.32)
            y "Bon, je vais voir ce qu'en dit notre divine prophétesse."
        
        "On s'en fout, non ?" :
            y "Y'a pas de quoi en faire tout un plat, non ?"
            show char_crossfit colere right at speakingAnim(0.26,0.94,0.92,0.32)
            cross "Comment oses-tu, domestique ?"
            cross "Nos lois sont claires ! Va voir la prophétesse maintenant !"
            show char_crossfit colere right at notSpeakingAnim(0.26,0.94,0.92,0.32)
            y "Ok ! Ok ! J'y vais ! Faut pas s'énerver comme ça !"
            
    window hide 
    
    stop music1 fadeout 1.5
    stop ambiance fadeout 0.5
    
    scene bg_tour :
        xpos 0 ypos -960
        linear 2.0 xpos 0 ypos 0
    show vel_morte :
        xpos 0 ypos -960
        linear 2.0 xpos 0 ypos 0
    show char_ernust normal right :
        xalign 0.5 yalign 0.8
        xpos 0.25 ypos -0.52 zoom 0.8
        linear 2.0 xpos 0.20 ypos 0.92
    show char_crossfit colere right :
        xalign 0.5 yalign 0.8
        xpos 0.26 ypos 0.84 zoom 0.32
        linear 2.0 xpos 0.20 ypos 3.0
    show char_brutal normal:
        xalign 0.5 yalign 0.8
        xpos 0.75 ypos 0.92 zoom 0.32
        linear 2.0 xpos 0.81 ypos 3.0
        
    play sound "sfx/SFX_Stairs_01.ogg"   
    $ renpy.pause(2.5, hard = True)
    
    jump tourVeleda_MortVeleda
    
# -----------------------------------------#
    
label tourVeleda_MortVeleda:
    
    $ renpy.music.play("music/MUSIC_Tour_Chambre_Jour.ogg", channel = "music1", loop = True, fadein = 1)
    $ renpy.music.play("ambiances/AMB_Lieu_Tour_Chambre_01.ogg", channel = "ambiance", loop = True, fadein = 1)
    
    show char_ernust normal right  at speakingAnim(0.20,0.92,0.9,0.8)
    
    e "Ah Gaufrid, ça c'est bien passé ?"
    e "Véléda fait une petite sieste !"
    show char_ernust normal right  at notSpeakingAnim(0.20,0.92,0.9,0.8)
    y "Comment ça une sieste ?"
    show char_ernust normal right  at speakingAnim(0.20,0.92,0.9,0.8)
    e "Bah oui, elle a mangé ma soupe aux champignons et après elle a fait des bruits bizarres."
    e "Je pense qu'elle a vomi à un moment mais après elle s'est endormie tranquillement !"
    show char_ernust normal right  at notSpeakingAnim(0.20,0.92,0.9,0.8)
    y "Quoi ? Mais c'était quoi comme champignons ?"
    y "Va voir tout de suite si elle va bien !"
    
    outline "Ernust se faufile derrière le voile (on change son image)"
    show char_ernust normal right  at speakingAnim(0.20,0.92,0.9,0.8)
    e "Elle va pas bien du tout Gaufrid !"
    e "Je sens pas du tout son pouls !"
    show char_ernust normal right  at notSpeakingAnim(0.20,0.92,0.9,0.8)
    y "Quoi ? Mais.. tu as tué Véléda, Ernust !"
    y "La prophétesse la plus connue de toute l'histoire !"
    y "Qu'est ce qu'on va faire ?"
    show char_ernust normal right  at speakingAnim(0.20,0.92,0.9,0.8)
    e "Oh je suis désolé Gaufrid !"
    e "Tu peux peut être faire une prophétie toi ?"
    show char_ernust normal right  at notSpeakingAnim(0.20,0.92,0.9,0.8)
    menu :
        "C'est complètement idiot." :
            y "Tu dis vraiment n'importe quoi Ernust !"
            y "J'ai l'air d'être un prophête moi ?"
            y "Mais attend... j'ai une idée !"
            y "Je vais faire semblant ! Je vais inventer une prophétie !"
            y "Ils verront jamais la différence !"
            show char_ernust normal right  at speakingAnim(0.20,0.92,0.9,0.8)
            e "Qu'est ce que t'es intelligent Gaufrid !"
            show char_ernust normal right  at notSpeakingAnim(0.20,0.92,0.9,0.8)
        "Bonne idée !" :
            y "Bien vu Ernust ! Ça c'est vraiment une bonne idée !"
            y "Je vais inventer une prophétie ! Ils verront jamais la différence !"
            
    y "J'y vais, bouge surtout pas d'ici !"
    
    scene bg_tour
    
    stop music1 fadeout 1.5
    stop ambiance fadeout 0.5
    
    play sound "sfx/SFX_Stairs_02.ogg"
    
    outline "Travelling vers le bas"
    
    jump tourVeleda_HistoireBrevetPart2
    
# -----------------------------------------#
    
label tourVeleda_HistoireBrevetPart2:

    scene bg_antichambre

    $ renpy.music.play("music/MUSIC_Tour_Antichambre.ogg", channel = "music1", loop = True, fadein = 1)
    $ renpy.music.play("ambiances/AMB_Lieu_Antichambre_01.ogg", channel = "ambiance", loop = True, fadein = 1)
    
    show char_brutal normal at notSpeakingAnim(0.75, 0.92,0.92,0.32)

    
    show char_crossfit colere right at speakingAnim(0.26,0.94,0.92,0.32)
    cross "Ah, enfin ! Parle, larbin."
    
    show char_crossfit colere right at notSpeakingAnim(0.26,0.94,0.92,0.32)
    y "Messieurs ! La divine Véléda a consulté les dieux, et m'a transmis sa prophétie !"
    
    menu :
        y "{cps=0}Messieurs ! La divine Véléda a consulté les dieux, et m'a transmis sa prophétie !{/cps}"
        "Brutalmund doit être châtié !" :
            $ Acte1_Tour_CoupableJugement = "Brutalmund"
            y "Brutalmund va devoir payer réparations !"
            show char_crossfit colere right at speakingAnim(0.26,0.94,0.92,0.32)   
            cross "Aha !"
            show char_crossfit colere right at notSpeakingAnim(0.26,0.94,0.92,0.32)
            show char_brutal normal at speakingAnim(0.75, 0.92,0.92,0.32)
            brut "Eh non !"
            show char_brutal normal at notSpeakingAnim(0.75, 0.92,0.92,0.32)
            y "Brutlamund va donner 2 buffles à Crossfritrichtrvald !"
            show char_brutal normal at speakingAnim(0.75, 0.92,0.92,0.32)
            brut "Quoi ? Deux buffles ? Ça va pas la tête ?"
            show char_brutal normal at notSpeakingAnim(0.75, 0.92,0.92,0.32)
            show char_crossfit colere right at speakingAnim(0.26,0.94,0.92,0.32)
            cross "Des... des buffles ?"
            
        "Les dieux se fichent de la propriété intellectuelle !":
            $ Acte1_Tour_CoupableJugement = "Crossfit"
            y "Les dieux sont insultés par la frivolité de cette accusation !"
            show char_brutal normal at speakingAnim(0.75, 0.92,0.92,0.32)
            brut "Hehe ! J'le savais !"
            show char_brutal normal at notSpeakingAnim(0.75, 0.92,0.92,0.32)
            show char_crossfit colere right at speakingAnim(0.26,0.94,0.92,0.32) 
            cross "Quel scandale !"
            show char_brutal normal at notSpeakingAnim(0.75, 0.92,0.92,0.32)
            y "Crossfitrichenfer doit payer deux buffles à Brutalmund en tant que frais de dossier !"
            show char_brutal normal at speakingAnim(0.75, 0.92,0.92,0.32)
            brut "Des buffles ? Bah ! J'en ai plein déjà."
            show char_brutal normal at notSpeakingAnim(0.75, 0.92,0.92,0.32)
            show char_crossfit colere right at speakingAnim(0.26,0.94,0.92,0.32)
            cross "Des... des buffles ?"
    
    show char_crossfit colere right at notSpeakingAnim(0.26,0.94,0.92,0.32)
    y "La prophétesse a parlé messieurs !"
    
    y "Je vous prie de dégager de là vite fait, merci."
    
 #   play sound "sfx/SFX_Walk_02.ogg"
    
    transform char_brutal :
        linear 2.0 xpos 3000
    #hide char_brutal normal with Dissolve(0.2)
    hide char_crossfit colere right with Dissolve(0.2)
    
    y "Allez hop hop hop"
    
    show char_ernust normal right at speakingAnim(0.6,0.95,0.93,0.8) with Dissolve (0.5)
    
    e "Ils t'ont cru Gaufrid ! T'es vraiment trop fort !"
    e "Qu'est ce qu'on va faire maintenant ?"
    show char_ernust normal right at notSpeakingAnim(0.6,0.95,0.93,0.8)
    y "Ben moi je vais aller à la taverne ! Ça donne soif toutes ces émotions !"
    y "Je vais pouvoir voir Ingrid en plus !"
    
    stop music1 fadeout 1.5
    stop ambiance fadeout 0.5
    
    jump narration_ellipse02
    #jump tourVeleda_MarryingIngridPart2
    
# -----------------------------------------#

label tourVeleda_MarryingIngridPart2:
    scene bg_place
    
    $ renpy.music.play("music/MUSIC_Main_CarteVillage.ogg", channel = "music1", loop = True, fadein = 1)
    $ renpy.music.play("ambiances/AMB_Lieu_CarteVillage_01.ogg", channel = "ambiance", loop = True, fadein = 1)
    
    show char_ernust normal right with Dissolve (0.5) :
        zoom 0.9 xpos 0.4 ypos 0.2
    
    y "Passe devant et prépare la Vélédarionnette, Ernust."
    e "Oui Gaufrid !"
    
    hide char_ernust
    
    show char_ingrid normal at notSpeakingAnim(0.5, 1.15, 1.12, 0.3)
    
    i "Oh ma Gaufrette, on va pouvoir se marier !"
    i "Viens, on va vite voir Véléda pour sa bénédiction !"
    
    y "Allons-y ma pupuce !"
    
    stop music1 fadeout 1.5
    stop ambiance fadeout 0.5
    
    scene bg_chambre
    
    $ renpy.music.play("music/MUSIC_Tour_Antichambre.ogg", channel = "music1", loop = True, fadein = 1)
    $ renpy.music.play("ambiances/AMB_Lieu_Antichambre_01.ogg", channel = "ambiance", loop = True, fadein = 1)
    
    show char_ingrid normal at notSpeakingAnim(0.15, 1.15, 1.12, 0.3)
    show char_veledaernust normal
    
    ve "Ooooh mes enfants les dieux bénissent votre marriage !"
    ve "Oh bah... elle arrête pas de gigoter !"
    
    i "...gigoter ? C'est bizarre comme prophétie !"
    
#    play sound "sfx/SFX_Char_Veleda_Normal_01.ogg"
    v "Ernust ! Qu'est ce que vous faites !"
#    play sound "sfx/SFX_Char_Veleda_Rage_01.ogg"
    v "Lachez nous immédiatement !"
    
    show char_ingrid choc
    i "Ernust ! Tu as fait semblant d'être Véléda ?"
    i "Quelle horreur ! Tu as bafoué toutes nos traditions !"
    
    scene black
    
    outline "ici scène clé des personnages de la VN tous sous le choc"
    
    scene bg_chambre
    
    show char_ingrid choc at notSpeakingAnim(0.15, 1.15, 1.12, 0.3)
    show char_veleda normal :
        zoom 0.7 xpos 0.38 ypos 0.22
    show char_ernust normal left :
        zoom 0.75 xpos 0.75 ypos 0.27
    
#    play sound "sfx/SFX_Char_Ernust_Normal_01.ogg"
    e "Euh... oh bah..."
    i "Ma Gaufrette ! Qu'est ce qu'il se passe ici ?"
    i "Tu étais au courant ?"

    menu:
        " "
        "Tu m'as dit qu'elle était morte Ernust ?":
            jump ending_AskErnust
        "Ernust ! Comment as tu osé ?":
            jump ending_ErnustPart1
        "Ingrid, je dois t'avouer la vérité !":
            jump ending_Admit
        "C'est la faute de la chèvre !":
            jump ending_ChevrePart1
# -----------------------------------------#

label ending_AskErnust:
    y "Mais Ernust, tu m'as dit qu'elle était morte ?"
    
    e "Bah oui ! Je l'ai reniflée et j'ai pas senti son pouls."
    e "C'est comme ça qu'on fait, non ?"
    
    i "Tu étais dans le coup mon Gaufridou !"
    
    menu :
        " "
        "Ingrid, je dois t'avouer la vérité !" :
            jump ending_Admit
        "Non, c'était la chèvre !" :
            jump ending_ChevrePart1

# -----------------------------------------#
label ending_ChevrePart1 :

    y "Non ma choupette je te jure !"
    y "C'est Josiane la chèvre, j'en suis sur !"
    show char_goat choc at center
    goat "Bêêê !"
            
    y "Elle est dans tous les sales coups !"
    
    v "Josiane comment avez vous pu nous faire cela ?"
    
    goat "Bêê bêêêê, bêê !"
    
    i "Josiane ? J'arrive pas à y croire !"
    
    v "Après tout ce que nous avons vécu ensemble, Josiane !"
    v "Après cet été langoureux de nos 20 ans..."
    
    goat "Bêê... bêêê..."
    
    v "Josiane, je suis bouleversée !"
    v "Mais je vais devoir vous condamener à..."
#    play sound "sfx/SFX_Drama_01.ogg"
    v "L'exil !"
    
    goat "Bêêêêê !"
    
    v "Adieu Josiane..."
    v "Mon amie..."

    stop music1 fadeout 1.5
    stop ambiance fadeout 0.5

jump ending_ChevreTrahie
# -----------------------------------------#
label ending_Admit :
    
    y "Ingrid, je dois tout t'avouer..."
    y "Je suis coupable avec Ernust !"
    
    i "Oh ! Mon tout nouveau fiancé !"
    i "Comment as tu pu ? Quelle tristesse !"
    i "Je me suis tellement attachée à toi depuis que tu m'as amené un {b}glaive{/b} et un {b}bouclier{/b} !"
    
    v "Monsieur Gaufrid ! Comment avez vous pu crachoter sur nos traditions de la sorte ?"
    v "Votre punition sera..."
#    play sound "sfx/SFX_Drama_01.ogg"
    v "L'exil !"
    
    stop music1 fadeout 1.5
    stop ambiance fadeout 0.5
    
jump ending_ExilPart1
# -----------------------------------------#
label ending_ErnustPart1 :
    y "Ernust ? Comment tu as pu faire une chose pareil !"
    
    e "Oh bah mais... Gaufrid !"
    
    y "Silence ! Je peux pas écouter un tel criminel !"
    
    i "Ernust... il semblait si gentil !"
    
    v "Monsieur Ernust, votre bétise nous a toujours dégoûté !"
    v "Nous avions prévenu vos parents..."
    v "Après qu'il vous ai cogné contre le pourtour d'un chaudron !"
    
    e "Mais... mais euh..."
    
    v "C'est avec grand plaisir que nous vous condamnons à..."
 #   play sound "sfx/SFX_Drama_01.ogg"
    v "L'exil !"
    
    e "Oh non ! Mais où je vais aller ?"
    
    i "Le pauvre Ernust !"
    
    y "Laisse tomber ma belle Ingridounette, c'est un criminel !"
    y "Viens on va vivre heureux et faire beaucoup d'enfants !"
    
    i "Ohlalala quel coquin !"
    
    hide char_ingrid
    
    stop music1 fadeout 1.5
    stop ambiance fadeout 0.5
    
    e "Je suis... tout seul"


jump ending_ErnustTrahi
# -----------------------------------------#

label ending_ExilPart1 :
    y "L'exil ? Très bien !"
    y "Je suis désolé ma Gridounette..."
    y "Au moment de notre marriage, je te laisse seule !"
    
    i "Oh t'inquiète pas y'a Beaudrik !"
    
    y "Ah bon d'accord..."
    y "Au moins je peux partir avec mon meilleur ami !"
    
    e "Oh bah alors Gaufrid..."
    e "Tu parles de moi ?"
    
    menu:
        " "
        "Oui Ernust, on s'en va !":
            y "Oui Ernust, tu es mon meilleur ami !"
            y "Des fois je suis un peu méchant avec toi..."
            y "Mais tu es toujours là pour moi !"
            
#            play sound "sfx/SFX_Char_Ernust_Joyeux_01.ogg"
            e "Ohlala Gaufrid tu vas me faire rougir !"
            
            y "Viens, on part en voyage ensemble !"
            
#            play sound "sfx/SFX_Char_Ernust_Joyeux_01.ogg"
            e "Oh Bah Gaufrid... je suis tellement content !"
            
            stop music1 fadeout 1.5
            stop ambiance fadeout 0.5
            
            jump ending_ExilAvecErnust
            
        "Je pars avec la chèvre !":
            y "Viens Josiane, on va découvrir le monde ensemble !"
            
            goat "Bêêê ?"
            goat "Bê !"
            goat "..."
            goat "Bêêêêê."
            
            stop music1 fadeout 1.5
            stop ambiance fadeout 0.5
            
            e "Au... au revoir Gaufrid !"
            
            jump ending_ExilAvecChevre