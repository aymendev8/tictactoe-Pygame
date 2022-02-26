import pygame 

class bouton():
    def __init__(self,couleur,x,y,hauteur,largeur,texte=""):
        self.couleur = couleur
        self.x = x
        self.y = y 
        self.hauteur = hauteur 
        self.largeur = largeur
        self.texte = texte

    def dessiner_bouton(self,ecran,taille_police, bordure = None):
        if bordure : 
            pygame.draw.rect(ecran,bordure,(self.x-2,self.y-2,self.largeur+4,self.hauteur+4),0)
        
        pygame.draw.rect(ecran,self.couleur,(self.x,self.y,self.largeur,self.hauteur),0)
        if self.texte != "":
            police = pygame.font.SysFont("comicsans",taille_police)
            texte = police.render(self.texte,1,(0,0,0))
            ecran.blit(texte,(self.x + (self.largeur/2 - texte.get_width()/2), self.y + (self.hauteur/2 - texte.get_height()/2)))
    
    def est_cliquer(self,pos,activer):
        if pos[0] > self.x and pos[0] < self.x + self.largeur:
            if pos[1] > self.y and pos[1] < self.x + self.hauteur:
                if activer == 0:
                    return True
        return False

