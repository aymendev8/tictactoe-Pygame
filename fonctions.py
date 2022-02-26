import pygame

# variables 
ma_ep_cercle = 10
mon_rayon_cercle = 60
espace_croix = 55
ma_croix_ep = 25
les_lignes = 3
les_colones = 3
mon_ecran_hauteur = 600
mon_ecran_largeur = 600
mon_ecran = pygame.display.set_mode((mon_ecran_largeur,mon_ecran_hauteur))

def dessiner_ligne(ecran,couleur_ligne,epaisseur_ligne):
    pygame.draw.line(ecran,couleur_ligne,(200,0),(200, 600),epaisseur_ligne)
    pygame.draw.line(ecran,couleur_ligne,(400,0),(400, 600),epaisseur_ligne)
    pygame.draw.line(ecran,couleur_ligne,(0,200),(600, 200),epaisseur_ligne)
    pygame.draw.line(ecran,couleur_ligne,(0,400),(600, 400),epaisseur_ligne)

def placer_carre(plateau,ligne, colonne, joueur):
    plateau[ligne][colonne] = joueur

def est_disponible(ecran, ligne, colonne):
    return ecran[ligne][colonne] == 0 

def est_remplis(ecran,ligne,colonne):
    for l in ligne : 
        for c in colonne:
            if ecran[l][c] == 0:
                return False
    return True
            
def dessiner_figure(plateau,ecran,ligne,colone):
    for l in range(ligne):
         for c in range(colone):
            if plateau[l][c] == 1:
                pygame.draw.circle(ecran,(255,255,255), (int(c * 200 + 100),int(l * 200 + 100)),mon_rayon_cercle,ma_ep_cercle)
            if plateau[l][c] == 2:
                pygame.draw.line(ecran,(105,105,105),(c * 200 + espace_croix, l *200+ 200 - espace_croix),(c * 200 + 200 - espace_croix, l *200+espace_croix),ma_croix_ep)
                pygame.draw.line(ecran,(105,105,105),(c * 200 + espace_croix, l *200+   espace_croix),(c * 200 + 200 - espace_croix, l *200+200-espace_croix),ma_croix_ep)


def gagner(plateau,player,colonne,ligne):
    for c in range(colonne):
        if plateau[0][c] == player and plateau[1][c] == player and plateau[2][c] == player:
            dessiner_victoire_verticale(c,player)
            return True
    for l in range(ligne):
        if plateau[l][0] == player and plateau[l][1] == player and plateau[l][2] == player:
            dessiner_victoire_horizontale(l,player)
            return True
    if plateau[2][0] == player and plateau[1][1] == player and plateau[0][2] == player:
        dessiner_victoire_diag_m(mon_ecran,player)
        return True
    if plateau[0][0] == player and plateau[1][1] == player and plateau[2][2] == player:
        dessiner_victoire_diag__d(mon_ecran,player)
        return True
    return False

def dessiner_victoire_verticale(colonne,player):
    posx = colonne * 200 + 100
    if player == 1:
        color = (255,255,255)
    elif player == 2:
        color = (105,105,105)
    pygame.draw.line(mon_ecran,color,(posx,15),(posx,mon_ecran_hauteur -15), 15)

def dessiner_victoire_horizontale(ligne,player):
    posy = ligne * 200 + 100
    if player == 1:
        color = (255,255,255)
    elif player == 2:
        color = (105,105,105)
    pygame.draw.line(mon_ecran,color,(15,posy),(mon_ecran_hauteur -15,posy), 15)

def dessiner_victoire_diag_m(ecran,player):
    if player == 1:
        color = (255,255,255)
    elif player == 2:
        color = (105,105,105)
    pygame.draw.line(mon_ecran,color,(15,mon_ecran_hauteur -15),(mon_ecran_largeur-15,15), 15)

def dessiner_victoire_diag__d(ecran,player):
    if player == 1:
        color = (255,255,255)
    elif player == 2:
        color = (105,105,105)
    pygame.draw.line(mon_ecran,color,(15,15),(mon_ecran_largeur-15,mon_ecran_hauteur-15), 15)

def rejouer(plateau,ecran):
    ecran.fill((20, 189, 172))
    dessiner_ligne(ecran,(255,255,255),10)
    for l in range(les_lignes):
        for c in range(les_colones):
            plateau[l][c] = 0

