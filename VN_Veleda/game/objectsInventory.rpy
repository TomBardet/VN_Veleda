#######################################################################
######### - Le Check de l'objet qu'on utilise - #######################

label Obj_use (obj = "none", objUser = "none"):
    if objUser == interlocuteur :
        if obj == "glaive":
            jump useGlaiveSuccess
        elif obj == "bouclier":
            jump useBouclierSuccess
        elif obj == "blague":
            jump useBlagueSuccess
        elif obj == "lunettes" :
            jump useLunettesSuccess
        else:
            "erreur pas d'objet sélectionné - Success"
    else :                          # Ecrire ici les conditions d'échec d'objet, on peut en faire pour chaque interlocuteur ! faut en profiter
        if obj == "glaive" :
            y "I don't think a glaive would be useful here"
        elif obj == "bouclier":
            y "I could use the shield if I get assaulted, but I don't feel like there is any danger here"
        elif obj == "blague" :
            y "This is not an appropriate moment to make a joke..."
        elif obj == "lunettes" :
            y "I don't see how glasses could be useful here"
        else:
            "erreur pas d'objet sélectionné - Failed"
    call screen inventory_screen
    
label useGlaiveSuccess:
    narration "success"
    jump start
label useBouclierSuccess:
    narration "success"
    jump start
label useBlagueSuccess:
    hide screen inventory_screen
    narration "Héhé, tout le monde sait que chêvre qui rit, à moitié dans son lit !"
    y "Dis, tu connais l'histoire du goth, de l'ostrogoth et du wisogoth qui vont au cirque ?"
    hide screen datingSim
    show bg_blackscreen with Dissolve(2.0)
    c "Bêêêêêêêêêêêêêhêhêh"
    narration "Et c'est ainsi que la chêvre, séduite par ton humour"
    narration "Succomba des suite d'une crise de fou rire aigüe"
    narration "C'est triste mais c'est comme ça."
    narration "Fin."
    narration "..."
    narration "..........."
    narration "......................................................."
    narration "Non pour de vrai c'est fini, vous pouvez partir"
    narration "Genre, là le jeu est censer retourner sur le menu en fait"
    narration "Veuillez excusez les développeurs, il semblerait qu'il y ait un incident technique"
    narration "C'est étrange ça marche super bien d'habitude"
    narration "J'ai vraiment pas de chance aujo-"
    return
label useLunettesSuccess:
    narration "success"
    jump start