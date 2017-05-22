##########################################################
# Ici figurent les scènes se déroulant à la Tour Véléda. #
##########################################################

label tourVeleda_ErnustEtVeleda :
    "Entrée tourVeleda_ErnustEtVeleda"
    
    jump tourVeleda_HistoireBrevetPart1

# -----------------------------------------#

label tourVeleda_HistoireBrevetPart1:
    "Entrée tourVeleda_HistoireBrevetPart1"
    
    jump tourVeleda_MortVeleda
    
# -----------------------------------------#
    
label tourVeleda_MortVeleda:
    "Entrée tourVeleda_MortVeleda"
    
    jump tourVeleda_HistoireBrevetPart2
    
# -----------------------------------------#
    
label tourVeleda_HistoireBrevetPart2:
    "Entrée tourVeleda_HistoireBrevetPart2"
    
    jump narration_ellipse02
    
label tourVeleda_MarryingIngridPart2:
    "label tourVeleda_MarryingIngridPart2"
    
    menu:
        "Accuser la chêvre":
            jump ending_ChevreTrahie
        "Accuser Ernust":
            jump ending_ErnustTrahi
        "S'accuser":
            jump ending_ExilPart1