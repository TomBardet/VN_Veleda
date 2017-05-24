#######################################################
# Ici figurent les scènes des différentes fin du jeu. #
#######################################################

label ending_ChevreTrahie:
    scene black with Dissolve (1)
    $ renpy.music.play("music/NARRATOR_Badass.ogg", loop = False)

    outline "Elle était chèvre et elle faisait du bon travail mais, accusée d’un crime qu’elle n’a pas commis, elle est exilée. "
    outline "Elle rode maintenant du côté du Dakota."
    outline "Hors la loi qui chasse les hors la loi, elle est une fugitive, une renégate."    
    show endingTemp at scrollEnding(1.0,-0.5, 10)#Juste le temps de scroll à régler (la dernière valeur)
    pause 10 #pause le temps du scroll
    "d,fs"
    return
    
label ending_ErnustTrahi:
    scene black with Dissolve (1)
    play music "music/MUSIC_FIN_MELANCOLIQUE_Ernust.ogg"
    outline "Gaufrid a atteint son objectif et se marie avec la belle Ingrid."
    outline "Mais sur le chemin, il a abandonné sa plus belle amitié…"
    outline "Que va devenir le pauvre Ernust ?"
    show endingTemp at scrollEnding(1.0,-0.5, 10)#Juste le temps de scroll à régler (la dernière valeur)
    pause 10 #pause le temps du scroll
    return

label ending_ExilAvecErnust:
    scene black with Dissolve (1)
    play music "music/MUSIC_FIN_BROTRIP.ogg"  
    outline "Traités en paria, Ernust et Gaufrid s’exilent ensemble."
    outline "Ils s'attendaient à découvrir le monde..."
    outline "mais ils ne s'attendaient pas à se découvrir... eux-mêmes."
    show endingTemp at scrollEnding(1.0,-0.5, 10)#Juste le temps de scroll à régler (la dernière valeur)
    pause 10 #pause le temps du scroll
    return
    
label ending_ExilAvecChevre:
    scene black with Dissolve (1)
    play music "music/MUSIC_FIN_BADASS_Chevre.ogg"
    outline "Unis par une force irresistible Gaufrid et Josiane s’exilent ensemble et partent en voyage."
    outline "Chaque jour qui passe ne fait que les rapprocher un peu plus…"
    show endingTemp at scrollEnding(1.0,-0.5, 10)#Juste le temps de scroll à régler (la dernière valeur)
    pause 10 #pause le temps du scroll
    return