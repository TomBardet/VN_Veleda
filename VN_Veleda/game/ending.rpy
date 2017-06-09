#######################################################
# Ici figurent les scènes des différentes fin du jeu. #
#######################################################

label ending_ChevreTrahie:
    
    scene black with Dissolve (1.5)
    $ renpy.music.play("ambiances/AMB_Lieu_CarteVillage_01.ogg", channel = "ambiance", loop = True, fadein = 1)
    
    $ renpy.music.set_volume(0.4, delay=0.4, channel='music1')
    $ renpy.music.set_volume(0.4, delay=0.4, channel='music2')
    $ renpy.music.set_volume(1, delay=0.4, channel='ambiance')
    
    $renpy.pause(2.0, hard = True)
    
    play sound "sfx/Voices/Narrateur/Narrateur_FIN_BADASS_Chevre_01.ogg"
    outline "Elle était chèvre et elle faisait du bon travail mais, accusée d’un crime qu’elle n’a pas commis, elle est exilée. "
    play sound "sfx/Voices/Narrateur/Narrateur_FIN_BADASS_Chevre_02.ogg"
    outline "Elle rode maintenant du côté du Dakota."
    play sound "sfx/Voices/Narrateur/Narrateur_FIN_BADASS_Chevre_03.ogg"
    outline "Hors la loi qui chasse les hors la loi, elle est une fugitive, une renégate."
    
    $ renpy.music.play("music/MUSIC_FIN_BADASS_Chevre.ogg", channel = "music1", fadein = 1.5, loop = False)
    
    play music "music/MUSIC_FIN_BADASS_Chevre.ogg"
    scene endBadKey with Dissolve (2.0)
    $renpy.pause(4.50, hard = True)
    show endBad01 :
        alpha 0.0
        linear 3.90 alpha 0.8
    pause 5.2
    show endBad01 :
        alpha 0.8
        linear 2.6 alpha 0.0
    show endBad02 :
        alpha 0.0
        linear 3.90 alpha 0.8
    pause 5.2
    show endBad02 :
        alpha 0.9
        linear 2.6 alpha 0.0
    show endBad03 :
        alpha 0.0
        linear 3.90 alpha 0.8
    pause 5.2
    show endBad03 :
        alpha 0.8
        linear 2.6 alpha 0.0
    show endBad04 :
        alpha 0.0
        linear 3.90 alpha 0.8
    pause 5.2
    show endBad04 :
        alpha 0.9
        linear 2.6 alpha 0.0
    scene black with Dissolve (2.6)
    window hide
    " "
    return
    
label ending_ErnustTrahi:
    scene black with Dissolve (1)
    outline "Gaufrid a atteint son objectif et se marie avec la belle Ingrid."
    outline "Mais sur le chemin, il a abandonné sa plus belle amitié…"
    outline "Que va devenir le pauvre Ernust ?"
    $ _window_during_transitions = False
    window hide
    play music "music/MUSIC_FIN_MELANCOLIQUE_Ernust.ogg"
    show endSadKey with Dissolve (4.6)
    window hide
    pause 2.0
    scene endSad01 with Dissolve (3.5)
    pause 3.90 #pause le temps du scroll
    scene black with Dissolve (2.6)
    scene endSad02 with Dissolve (2.6)
    pause 3.90 #pause le temps du scroll
    scene black with Dissolve (1.6)
    scene endSad03 with Dissolve (2.6)
    pause 3.90#pause le temps du scroll
    scene black with Dissolve (1.6)
    scene endSad04 with Dissolve (2.6)
    pause 3.90 #pause le temps du scroll
    scene black with Dissolve (2.6)
    " "
    return

label ending_ExilAvecErnust:
    scene black with Dissolve (2)
    window hide
    outline "Traités en paria, Ernust et Gaufrid s’exilent ensemble."
    outline "Ils s'attendaient à découvrir le monde..."
    outline "mais ils ne s'attendaient pas à se découvrir... eux-mêmes."
    $ renpy.music.play("music/MUSIC_FIN_BROTRIP.ogg", loop = False)  
    scene endBro01 with Dissolve (3.5)
    pause 3.90 #pause le temps du scroll
    scene black with Dissolve (2.6)
    scene endBro02 with Dissolve (2.6)
    pause 3.90 #pause le temps du scroll
    scene black with Dissolve (1.6)
    scene endBro03 with Dissolve (2.6)
    pause 3.90#pause le temps du scroll
    scene black with Dissolve (1.6)
    scene endBro04 with Dissolve (2.6)
    pause 3.90 #pause le temps du scroll
    scene black with Dissolve (2.6)
    window hide
    show endBroKey with Dissolve (4.6)
    outline " "
    
    return
    
label ending_ExilAvecChevre:
    scene black with Dissolve (1)  
    outline "Unis par une force irresistible Gaufrid et Josiane s’exilent ensemble et partent en voyage."
    outline "Chaque jour qui passe ne fait que les rapprocher un peu plus…"
    play music "music/MUSIC_FIN_BROTRIP.ogg"
    scene endGoat01 with Dissolve (2.6)
    $renpy.pause(3.90, hard=True) #pause le temps du scroll
    scene black with Dissolve (2.6)
    scene endGoat02 with Dissolve (2.6)
    $renpy.pause(3.90, hard=True) #pause le temps du scroll
    scene black with Dissolve (1.6)
    scene endGoat03 with Dissolve (2.6)
    $renpy.pause(3.90, hard=True)#pause le temps du scroll
    scene black with Dissolve (1.6)
    scene endGoat04 with Dissolve (2.6)
    $renpy.pause(3.90, hard=True) #pause le temps du scroll
    scene black with Dissolve (2.6)
    window hide
    show endGoatKey with Dissolve (4.6)   
    outline " "
    return