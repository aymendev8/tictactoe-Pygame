from platform import python_branch
import pygame
import numpy as np 
import fonctions
import Bouton

pygame.init()

#Mes Variables 
mon_icon = pygame.image.load('Images/logo.jpg')
touche = pygame.K_SPACE
game_over = False
joueur = 1
les_lignes = 3
les_colones = 3
mon_plateau = np.zeros((les_lignes,les_colones))
premier_clic = 0 
enlever_bouton = 0
jeu_activer = 0 
mon_ecran_hauteur = 600
mon_ecran_largeur = 600
mon_epaisseur_ligne = 10
ma_couleur_ligne = (255,255,255)
ma_couleur_fond = (20, 189, 172)

#fenetre de jeu 
mon_ecran = pygame.display.set_mode((mon_ecran_largeur,mon_ecran_hauteur))
pygame.display.set_caption('TicTacToe')
pygame.display.set_icon(mon_icon)
mon_ecran.fill(ma_couleur_fond)

# Menu d'accueil
le_bouton_play =Bouton.bouton(ma_couleur_ligne,210,210,70,180,"Jouer")
le_bouton_play.dessiner_bouton(mon_ecran,60,(ma_couleur_ligne))
le_bouton_rejouer =Bouton.bouton(ma_couleur_fond,210,310,70,180,"appuyer sur espace pour rejouer")
le_bouton_rejouer.dessiner_bouton(mon_ecran,30)


print(fonctions.est_disponible(mon_plateau,1,1))

#Boucle du jeu 
mon_jeu = True
while mon_jeu:
    pygame.display.update()
    if jeu_activer == 1 :
        fonctions.dessiner_ligne(mon_ecran,ma_couleur_ligne,mon_epaisseur_ligne)
    for evt in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if evt.type == pygame.QUIT:
            mon_jeu = False
            print("Jeu fermer")
        if evt.type == pygame.MOUSEBUTTONDOWN :
            if le_bouton_play.est_cliquer(pos,enlever_bouton):
                enlever_bouton = 1
                jeu_activer = 1
                print("La partie se lance")
                mon_ecran.fill(ma_couleur_fond)
            if evt.type == pygame.MOUSEBUTTONDOWN  and not game_over and jeu_activer == 1 : 
                sourisX = evt.pos[0]
                sourisY = evt.pos[1]
                ligne_selectionner = int(sourisY // 200)
                colonne_selectionner = int(sourisX // 200)
                if fonctions.est_disponible(mon_plateau,ligne_selectionner,colonne_selectionner) and premier_clic == 1:
                    if joueur == 1 :
                        fonctions.placer_carre(mon_plateau,ligne_selectionner,colonne_selectionner,1)
                        if fonctions.gagner(mon_plateau,joueur,les_colones,les_lignes):
                             game_over = True
                        joueur = 2
                    elif joueur == 2:
                        fonctions.placer_carre(mon_plateau,ligne_selectionner,colonne_selectionner,2)
                        if fonctions.gagner(mon_plateau,joueur,les_colones,les_lignes):
                            game_over = True
                        joueur = 1
                    fonctions.dessiner_figure(mon_plateau,mon_ecran,les_lignes,les_lignes)      
                else:
                    premier_clic = 1        
        if evt.type == pygame.KEYDOWN:
            if evt.key == pygame.K_SPACE:
                game_over = False
                fonctions.rejouer(mon_plateau,mon_ecran)

    pygame.display.update()       
                    