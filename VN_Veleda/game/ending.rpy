#######################################################
# Ici figurent les scènes des différentes fin du jeu. #
#######################################################

label ending_ChevreTrahie:
    "fin ending_ChevreTrahie"
    
    return
    
label ending_ErnustTrahi:
    "fin ending_ErnustTrahi"
    
    return
    
label ending_ExilPart1:
    "label ending_ExilPart1"
    
    menu:
        "Partir avec Ernust":
            jump ending_ExilAvecErnust
        "Partir avec la Chêvre":
            jump ending_ExilAvecChevre

label ending_ExilAvecErnust:
    "fin ending_ExilAvecErnust"
    
    return
    
label ending_ExilAvecChevre:
    "fin ending_ExilAvecChevre"
    
    return