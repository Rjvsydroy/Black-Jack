#ce programme simule une partie de Jeu BlackJack
from random import shuffle

class Blackjack:
 valeurs={'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10,'A':11}
  
 def joue(self):
  '''jouer un jeu'''   
  d = JeuDeCartes()
  d.battre()
  
  banque = Main('Banque')
  joueur = Main('Joueur')

  # donne deux cartes au joueur et deux cartes a la banque
  for i in range(2):  
    joueur.ajouteCarte(d.tireCarte())
    banque.ajouteCarte(d.tireCarte())

  # montre les mains
  banque.montreMain()
  joueur.montreMain()

  # tant que le joueur demande Carte!, la banque tire des cartes
  reponse = input('Carte? Oui ou non? (Par défaut oui) ')
  while reponse in ['','o','O','oui','Oui']:
    c = d.tireCarte()
    print("Vous avez:")
    print(c)
    joueur.ajouteCarte(c)
    if self.total(joueur) > 21:
       print("Vous avez dépassé 21. Vous avez perdu.")
       return   
    reponse = input('Carte? Oui ou non? (Par défaut oui) ')

  # la banque joue avec ses regles  
  while self.total(banque) < 17:
    c = d.tireCarte()
    print("La banque a:")
    print(c)
    banque.ajouteCarte(c)
    if self.total(banque) > 21:
       print("La banque a dépassé 21. Vous avez gagné.")
       return

  # si 21 n'est pas depassée, compare les mains pour trouver le gagnant  
  self.compare(banque, joueur)

      
 def total(self, main):
    ''' (Main) -> int
    calcule la somme des valeur de toutes les cartes dans la main
    '''
    valeurs={'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10,'A':11}

    # a completer
     # calculez la somme de toutes les valeurs de la main
    total = 0                                #pour stocker la somme de toutes les valeurs dans la main 
    countAs = 0                              #pour stocker le nombre de As, "A"
    for i in range(len(main.main)):          #parcourir la liste
        a=str(main.main[i][0])               #mettre l'élément de la liste en string
        total = total + valeurs[a]           #b[0] clé du dictionnaire et valeurs de la carte
        if a == "A":                       #condition pour vérifier si le joueur ou la banque possède un ou des As dans la main 
            countAs = countAs + 1
    
    # while la somme > 21 et il y a des As, deduisez 10 points pour chaque As
    if total > 21 and countAs > 0:        #Condition si les valeurs des cartes dépasse 21 et le joueur désire changer la valeur des As en 1
        total = total - countAs*10

    return total# a changer

 def compare(self, banque, joueur):
    ''' (Main, Main) -> None
    Compare la main du joueur avec la main de la banque
    et affiche de messages
    '''
    bank = self.total(banque) #bank sera le total des valeurs de la carte de la banque
    player = self.total(joueur)#player sera le total des valeurs de la carte du joueur

    # si le total de la banque > le total du joueur affichez 'Vous avez perdu.'
    if bank > player:
        print('Vous avez perdu.')

    # si le total de la banque < le total du joueur affichez 'Vous avez gagné.'   
    if bank < player:
        print('Vous avez gagné.')

    # en cas d'egalite, si le total est 21m si la banque a un blackjack
    if bank == player:
        if bank == 21 and player == 21:
        #pour trouver le nombre de As et de buche dans la main de la banque
            AsBank = 0                       #stocker le nombre de AS 
            BucheBank = 0                    #stocker le nombre de bûche
            for i in range(len(banque.main)):#parcourir la liste de carte de la banque 
                a=str(banque.main[i][0])     #transformer l'élément de la liste de la  banque en string
                if b[0] == "A":              #b[0] est la "valeurs" de la carte
                    AsBank = AsBank + 1
                elif  valeurs[a] == 10:   #pour trouver si il y la carte est une bûche
                    BucheBank = BucheBank + 1

        #pour trouver le nombre de As et de buche dans la main du joueur
            AsPlayer = 0                     #stocker le nombre de AS 
            BuchePlayer = 0                  #stocker le nombre de bûche
            for i in range(len(joueur.main)):#parcourir la liste
                a=str(joueur.main[i][0])     #transformer l'élément de la liste du joueur en string       
                if b[0] == "A":              #b[0] est la "valeurs" de la carte car la liste est représentée comme suit:['C', 'a', 'r', 't', 'e', '(', '2', ',', ' ', '♠', ')']
                    AsPlayer = AsPlayer + 1
                elif  valeurs[a] == 10:      #pour trouver si il y la carte est une bûche
                    BuchePlayer = BuchePlayer + 1

    # affichez 'Vous avez perdu.'; si le joueur a un blackjack 'Vous avez gagné.'
            if (AsBank == 1 and BucheBank == 1) and (AsPlayer != 1 or BuchePlayer != 1):#condition si la banque possède un blackjack
                print("Vous avez perdu.")
            elif (AsPlayer == 1 and BuchePlayer == 1) and (AsBank != 1 or BucheBank != 1):#condition si le joueur possède un blackjack
                print("Vous avez gagné.")
    # sinon, affichez 'Egalité.'
        else:
            print("Egalité")

class Main(object):
    '''represente une main des cartes a jouer'''

    def __init__(self, joueur = "Joueur"):
        '''(Main, str)-> none
        initialise le nom du joueur et la liste de cartes avec liste vide'''
        # a completer
        self.joueur = joueur
        self.main = []

    
    def ajouteCarte(self, carte):
        '''(Main, Carte) -> None
        ajoute une carte a la main'''
        # a completer
        self.main.append(carte)

    def montreMain(self):
        '''(Main)-> None
        affiche le nom du joueur et la main'''
        # a completer
        print(self.joueur,':', self.main[0][0],self.main[0][1],' ',self.main[1][0],self.main[1][1])
                
    def __eq__(self, autre):
        '''retourne True si les main ont les meme cartes
           dans la meme ordre'''
        # a completer
        return self.main == autre.main

    def __repr__(self):
        '''retourne une representation de l'objet'''
        # a completer
        return str(self.joueur)+':'+ str(self.main[0][0])+str(self.main[0][1])+' '+str(self.main[1][0])+str(self.main[1][1])

class Carte:
    '''represente une carte a jouer'''

    def __init__(self, valeur, couleur):
        '''(Carte,str,str)->None        
        initialise la valeur et la couleur de la carte'''
        self.valeur = valeur
        self.couleur = couleur  # pique, coeur, trefle ou carreau

    def __repr__(self):
        '''(Carte)->str
        retourne une representation de l'objet'''
        return 'Carte('+self.valeur+', '+self.couleur+')'

    def __eq__(self, autre):
        '''(Carte,Carte)->bool
        self == autre si la valeur et la couleur sont les memes'''
        return self.valeur == autre.valeur and self.couleur == autre.couleur

class JeuDeCartes:
    '''represente une jeu de 52 cartes'''
    # valeurs et couleurs sont des variables de classe
    valeurs = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    couleurs = ['\u2660', '\u2661', '\u2662', '\u2663']
    # couleurs est un set de 4 symboles Unicode qui representent les 4 couleurs
    # pique, coeur, trefle ou carreau
    
    def __init__(self):
        'initialise le paquet de 52 cartes'
        self.paquet = []          # paquet vide au debut
        for couleur in JeuDeCartes.couleurs: 
            for valeur in JeuDeCartes.valeurs: # variables de classe
                # ajoute une Carte de valeur et couleur
                self.paquet.append((valeur,couleur))

    def tireCarte(self):
        '''(JeuDeCartes)->Carte
        distribue une carte, la premiere du paquet'''
        return self.paquet.pop()

    def battre(self):
        '''(JeuDeCartes)->None
        pour battre le jeu des cartes'''
        shuffle(self.paquet)

    def __repr__(self):
        '''retourne une representation de l'objet'''
        return 'Paquet('+str(self.paquet)+')'

    def __eq__(self, autre):
        '''retourne True si les paquets ont les meme cartes
           dans la meme ordre'''
        return self.paquet == autre.paquet
    
    
b = Blackjack()
b.joue()

