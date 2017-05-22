######################################################
# Ici figurent les scènes se déroulant à la Taverne. #
######################################################

label taverne_DatingIngrid:
    "label taverne_DatingIngrid"
    
    jump narration_ellipse01
 
# -----------------------------------------# 
 
label taverne_PresentationDot:
    "label taverne_PresentationDot"
     
    jump PlaceDuVillageDefault
     
# -----------------------------------------#

label taverne_AbusAlcoolPart1:
    "label taverne_AbusAlcoolPart1"
    
    jump taverne_AbusAlcoolPart2
    
# -----------------------------------------#

label taverne_AbusAlcoolPart2:
    "label taverne_AbusAlcoolPart2"
     
    $ inventory.add(blague)
    $ _testBlague = 1
     
    "blague récupérée"
     
    jump narration_ellipseCuite
     
# -----------------------------------------#

label taverne_ConcoursPart1:
    "label taverne_ConcoursPart1"
    
    jump taverne_ConcoursPart2
    
# -----------------------------------------#

    
label taverne_ConcoursPart2:
    "label taverne_ConcoursPart2"
    
    jump taverne_ConcoursPart3
    
# -----------------------------------------#
    
label taverne_ConcoursPart3:
    "label taverne_ConcoursPart3"
    
    jump taverne_MarryingIngridPart1
    
# -----------------------------------------#

label taverne_MarryingIngridPart1:
    "label taverne_MarryingIngridPart1"
    
    jump tourVeleda_MarryingIngridPart2
    
# -----------------------------------------#
