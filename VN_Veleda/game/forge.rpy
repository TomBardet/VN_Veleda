####################################################
# Ici figurent les scènes se déroulant à la Forge. #
####################################################

label forge_BrutalmundEtBeaudrik:
    "label forge_BrutalmundEtBeaudrik"
    
    jump forge_BrutalMundBlaguePart1

# -----------------------------------------#

label forge_BrutalMundBlaguePart1:
    "label forge_BrutalMundBlaguePart1"
    
    if _testBlague == 1:
        menu:
            "Retour Place du Village":
                jump PlaceDuVillageDefault
            "Donner la blague":
                jump forge_BrutalMundBlaguePart2
    else:
        "Pas de blague..."
        jump PlaceDuVillageDefault

# -----------------------------------------#

label forge_BrutalMundBlaguePart2:
    "Entrée forge_BrutalMundBlaguePart2"
    
    $ inventory.add(bouclier)
    $ _testBouclier = 1
    
    "Bouclier récupéré"
    
    if _testGlaive == 1 & _testBouclier == 1:
        jump PlaceDuVillageAllObjects
    else:
        jump PlaceDuVillageDefault
    
    