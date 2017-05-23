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
    image temp = "images/inv_sword.png"
    image temp2 = "images/goat_idle.png"
    
    #Les images des Lieux
    image bg_taverne = "images/decor/Lieu_taverne.jpg"
    image bg_taverne2 = "images/decor/Lieu_taverne2.png"
    image bg_etables = "images/decor/Lieu_etables.jpg"
    image bg_forge = "images/decor/Lieu_forge.jpg"
    image bg_antichambre = "images/decor/Lieu_antichambre.jpg"
    image bg_chambre = "images/decor/Lieu_chambre.jpg"
    image bg_romains = "images/decor/Lieu_romains.png"
    image bg_place = "images/decor/Lieu_place.png"
    
    #------ Les images des Personnages -------
    
    #Véléda
    image char_veleda normal = "images/char/Char_veleda_normal.png"
    image char_veleda morte = "images/char/Char_veleda_morte.png"
    image char_veleda marionnette = "images/char/Char_veleda_marionnette.png"
    
    #Ernust
    image char_ernust normal = "images/char/Char_ernust_normal.png"
    image char_ernust joyeux = "images/char/Char_ernust_joyeux.png"
    image char_ernust love = "images/char/Char_ernust_love.png"
    image char_ernust marionnette = "images/char/Char_ernust_marionnette.png"
    
    #Ingrid
    image char_ingrid normal = "images/char/Char_ingrid_normal.png"
    image char_ingrid degout = "images/char/Char_ingrid_degout.png"
    image char_ingrid love = "images/char/Char_ingrid_love.png"
    image char_ingrid choc = "images/char/Char_ingrid_choc.png"
    
    #Crossfit
    image char_crossfit colere = "images/char/Char_crossfit_colere.png"
    image char_crossfit colere2 = "images/char/Char_crossfit_colere2.png"
    image char_crossfit serieux = "images/char/Char_crossfit_serieux.png"
    image char_crossfit inquiet = "images/char/Char_crossfit_inquiet.png"
    
    #Brutalmund
    image char_brutal normal = "images/char/Char_brutal_normal.png"
    image char_brutal colere = "images/char/Char_brutal_colere.png"
    image char_brutal heureux = "images/char/Char_brutal_heureux.png"
    
    #Beaudrik
    image char_beaudrik mepris = "images/char/Char_beaudrik_mepris.png"
    image char_beaudrik drague = "images/char/Char_beaudrik_drague.png"
    image char_beaudrik insulte = "images/char/Char_beaudrik_insulte.png"
    
    #Numerimus
    image char_numerimus normal = "images/char/Char_numerimus_normal.png"
    image char_numerimus heureux = "images/char/Char_numerimus_heureux.png"
    image char_numerimus choque = "images/char/Char_numerimus_choque.png"
    image char_numerimus dubitatif = "images/char/Char_numerimus_dubitatif.png"
    
    #Digitimus
    image char_digitimus normal = "images/char/Char_digitimus_normal.png"
    image char_digitimus choque = "images/char/Char_digitimus_choque.png"
    image char_digitimus rire = "images/char/Char_digitimus_rire.png"
    image char_digitimus dubitatif = "images/char/Char_digitimus_dubitatif.png"
    
    #Chêvre-Josiane
    image char_goat normal = "images/char/Char_goat_normal.png"
    image char_goat love = "images/char/Char_goat_love.png"
    image char_goat choc = "images/char/Char_goat_choc.png"
    
    ##PROTO ASSETS
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

