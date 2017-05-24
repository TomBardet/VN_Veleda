#######################################################
# Ici figurent les scènes des différentes fin du jeu. #
#######################################################

label ending_ChevreTrahie:
    scene black with Dissolve (1)
    $ renpy.music.play("music/NARRATOR_Badass.ogg", loop = False)
    outline "Elle était chèvre et elle faisait du bon travail mais, accusée d’un crime qu’elle n’a pas commis, elle est exilée. "
    outline "Elle rode maintenant du côté du Dakota."
    outline "Hors la loi qui chasse les hors la loi, elle est une fugitive, une renégate."
    play music "music/MUSIC_FIN_BADASS_Chevre.ogg"
    show endingTemp at scrollEnding(1.0,-0.5, 10) #Juste le temps de scroll à régler (la dernière valeur)
    pause 10 #pause le temps du scroll
    "d,fs"
    return
    
label ending_ErnustTrahi:
    scene black with Dissolve (1)
    outline "Gaufrid a atteint son objectif et se marie avec la belle Ingrid."
    outline "Mais sur le chemin, il a abandonné sa plus belle amitié…"
    outline "Que va devenir le pauvre Ernust ?"
    play music "music/MUSIC_FIN_MELANCOLIQUE_Ernust.ogg"
    show endingTemp at scrollEnding(1.0,-0.5, 10)#Juste le temps de scroll à régler (la dernière valeur)
    pause 10 #pause le temps du scroll
    return

label ending_ExilAvecErnust:
    scene black with Dissolve (1)
    outline "Traités en paria, Ernust et Gaufrid s’exilent ensemble."
    outline "Ils s'attendaient à découvrir le monde..."
    outline "mais ils ne s'attendaient pas à se découvrir... eux-mêmes."
    play music "music/MUSIC_FIN_BROTRIP.ogg"  
    scene endBro01 with Dissolve (2.0)
    pause 2.5 #pause le temps du scroll
    scene black with Dissolve (1.0)
    scene endBro02 with Dissolve (2.0)
    pause 2.5 #pause le temps du scroll
    scene black with Dissolve (1.0)
    scene endBro03 with Dissolve (2.0)
    pause 2.5 #pause le temps du scroll
    scene black with Dissolve (1.0)
    scene endBro04 with Dissolve (2.0)
    pause 2.5 #pause le temps du scroll
    scene black with Dissolve (1.0)
    scene endBroKey with Dissolve (2.5)
    
    outline " "
    
    return
    
label ending_ExilAvecChevre:
    scene black with Dissolve (1)  
    outline "Unis par une force irresistible Gaufrid et Josiane s’exilent ensemble et partent en voyage."
    outline "Chaque jour qui passe ne fait que les rapprocher un peu plus…"
    play music "music/MUSIC_FIN_BROTRIP.ogg"
    show endingTemp at scrollEnding(1.0,-0.5, 10)#Juste le temps de scroll à régler (la dernière valeur)
    pause 10 #pause le temps du scroll
    return