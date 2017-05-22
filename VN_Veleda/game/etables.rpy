#####################################################
# Ici figurent les scènes se déroulant aux étables. #
#####################################################

label etables_PeurDesBufflesPart1:
    "Entrée etables_PeurDesBufflesPart1"
    
    if _testTrompette == 1:
        menu:
            "Retour Place du Village":
                jump PlaceDuVillageDefault
            "Faire peur aux buffles":
                jump etables_PeurDesBufflesPart2
    else:
        "Pas de trompette..."
        jump PlaceDuVillageDefault

# -----------------------------------------#

label etables_PeurDesBufflesPart2:
    "Entrée etables_PeurDesBufflesPart1"
    
    $ inventory.add(lunettes)
    $ _testLunettes = 1
    
    "Lunettes récupérées"
    
    jump PlaceDuVillageDefault
    
# -----------------------------------------#
