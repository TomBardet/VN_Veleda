#########################################################################################
######################## - Defining Characters - ########################################

init:
    
    define goat = Character("Chêvre : ",
        what_suffix=" ",
        ctc=anim.Blink("gui/ctc.png"))
    
    define y = Character("Gaufrid : ",
        what_suffix=" ",
        ctc=anim.Blink("gui/ctc.png"))
    
    define e = Character("Ernust : ",
        what_suffix=" ",
        ctc=anim.Blink("gui/ctc.png"))
    
    define i = Character("Ingrid : ",
        what_suffix=" ",
        ctc=anim.Blink("gui/ctc.png"))
    
    define v = Character("Véléda : ",
        what_suffix=" ",
        ctc=anim.Blink("gui/ctc.png"))
    
    define brut = Character("Brutalmund : ",
        what_suffix=" ",
        ctc=anim.Blink("gui/ctc.png"))
    
    define cross = Character("Crossfitrichernvald : ",
        what_suffix=" ",
        ctc=anim.Blink("gui/ctc.png"))
    
    define bg = Character("Beaudrik : ",
        what_suffix=" ",
        ctc=anim.Blink("gui/ctc.png"))
    
    define num = Character("Numerimus : ",
        what_suffix=" ",
        ctc=anim.Blink("gui/ctc.png"))
    
    define dig = Character("Digitimus : ",
        what_suffix=" ",
        ctc=anim.Blink("gui/ctc.png"))

    define nar = Character("Narrateur : ",
        what_xalign = 0.5,
        what_xpos=0.5,
        what_italic=True,
        what_suffix=" ",
        ctc=anim.Blink("gui/ctc.png"))
    
    $ outline = Character(None,
        what_size=32,
        what_color = "#ffffff",
        what_outlines=[(2, "#000000", 0, 0)],
        what_layout="subtitle",
        what_xalign=0.5,
        what_text_align=0.5,
        window_background=None,
        window_yminimum=0,
        window_xfill=True,
        window_xalign=0.5,
        window_yalign=0.5)

#########################################################################################
######################## - Defining Images - ############################################

init:
    
    image bg_bar = "images/bg_bar.png"
    image bg_blackscreen = "images/bg_blackscreen.png"
    image goat = "images/goat_idle.png"
    image bg_champ = "images/bg_champs.png"
    image bg_blacksmith = "images/bg_blacksmith.jpg"
    image bg_house = "gui/menu_bg.jpg"
    image bg_map = "images/bg_map.png"
    
#########################################################################################
######################## - Defining Sounds & Musics - ###################################

# Il n'y a pas encore de Sons et Musiques dans le jeu

