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
    outline "She was a goat and good at her job but, accused of a crime he didn't commit , elle he was exiled. "
    play sound "sfx/Voices/Narrateur/Narrateur_FIN_BADASS_Chevre_02.ogg"
    outline "Now she prowls the badlands."
    play sound "sfx/Voices/Narrateur/Narrateur_FIN_BADASS_Chevre_03.ogg"
    outline "An outlaw hunting outlaws, a bounty hunter, a renegade."
    
    $ renpy.music.play("music/MUSIC_FIN_BADASS_Chevre.ogg", loop = False, channel = "endings", fadein = 1.5)

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
    
    scene black with Dissolve (1.5)
    
    $ renpy.music.play("ambiances/AMB_Lieu_CarteVillage_01.ogg", channel = "ambiance", loop = True, fadein = 1)
    
    $ renpy.music.set_volume(0.4, delay=0.4, channel='music1')
    $ renpy.music.set_volume(0.4, delay=0.4, channel='music2')
    $ renpy.music.set_volume(1, delay=0.4, channel='ambiance')
    
    $renpy.pause(2.0, hard = True)
    
    play sound "sfx/Voices/Narrateur/Narrateur_FIN_Melancolique_01.ogg"
    outline "Wafflid reached his goal and married the beautiful Ingrid."
    play sound "sfx/Voices/Narrateur/Narrateur_FIN_Melancolique_02.ogg"
    outline "But on the way, he betrayed his most meaningful friendship…"
    play sound "sfx/Voices/Narrateur/Narrateur_FIN_Melancolique_03.ogg"
    outline "What will happen to the poor Ernust?"
    
    $ _window_during_transitions = False
    
    window hide
    
    $ renpy.music.play("music/MUSIC_FIN_MELANCOLIQUE_Ernust.ogg", loop = False, channel = "endings", fadein = 1.5)

    scene endSadKey with Dissolve (4.0)
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

label ending_ExilAvecErnust:
    
    scene black with Dissolve (2)
    window hide
    
    play sound "sfx/Voices/Narrateur/Narrateur_FIN_BROTRIP_Ernust_01.ogg"
    
    pause 0.7
    
    outline "Treated like pariahs, Wafflid and Ernust are exiled together."
    play sound "sfx/Voices/Narrateur/Narrateur_FIN_BROTRIP_Ernust_02.ogg"
    
    pause 0.7 
    
    outline "They expected to discover the world but they ended up discovering... themselves."

    $ renpy.music.play("music/MUSIC_FIN_BROTRIP.ogg", loop = False, channel = "endings", fadein = 1.5)
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
    
    scene black with Dissolve (2)
    window hide
    
    play sound "sfx/Voices/Narrateur/Narrateur_FIN_BROTRIP_Chevre_01.ogg"
    
    pause 0.7
    
    outline "United by an irresistible force, Wafflid and Josiane the goat are exiled together."
    
    play sound "sfx/Voices/Narrateur/Narrateur_FIN_BROTRIP_Chevre_02.ogg"
    
    pause 0.7 
    outline "Every day that goes by brings them closer together…"
    $ renpy.music.play("music/MUSIC_FIN_BROTRIP.ogg", loop = False, channel = "endings", fadein = 1.5)
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