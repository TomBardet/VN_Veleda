################################################################################
# Ici figurent les scènes se déroulant à l'aurée du village, chez les romains. #
################################################################################

label romains_PremiereRencontre:
    "label romains_PremiereRencontre"
    
    jump romains_Part1

# -----------------------------------------#

label romains_Part1:
    "label romains_Part1"
    
    menu:
        "Rentrer au village":
            jump PlaceDuVillageDefault
        "Faire visiter le village":
            jump romains_VisitePart1
        "Faire une blague":
            jump romains_Blague
            
# -----------------------------------------#

label romains_VisitePart1:
    "label romains_VisitePart1"
    
    if _testLunettes == 1:
        "lunettes ok"
        jump romains_VisitePart2
    else:
        "pas de lunettes"
        jump romains_Part1
        
# -----------------------------------------#

label romains_VisitePart2:
    "label romains_VisitePart2"
    
    jump romains_VisiteVeleda
    
# -----------------------------------------#

label romains_VisiteVeleda:
    "label romains_VisiteVeleda"
    
    $ inventory.add(glaive)
    $ _testGlaive = 1
    
    "glaive récupéré"
    
    if _testGlaive == 1 & _testBouclier == 1:
        jump PlaceDuVillageAllObjects
    else:
        jump PlaceDuVillageDefault
    
# -----------------------------------------#

label romains_Blague:
    "label romains_Blague"
    
    if _testBlague == 1:
        "blague ok"
        $ inventory.add(trompette)
        $ _testTrompette = 1
    
        "trompette récupérée"
        jump PlaceDuVillageDefault
    else:
        "pas de blague"
        jump romains_Part1
         