import pandas as pd
from math import*
import numpy as np
import matplotlib.pyplot as plt
import numpy.random as npr

print("=="*10 + "points en 3D"+ "="*10)

class point3D:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def afficher(self):
        return f"Les coordonnées sont: {(self.x,self.y,self.z)}"
    
    def distance(self,p):
        return round(sqrt((self.x-p.x)**2+(self.y-p.y)**2+(self.z-p.z)**2),2)
    
print("===illustration===")
p=point3D(3,0,1)
q=point3D(-3,0,0)

print(p.afficher())
print(p.distance(q))

###############################################################


class CompteBancaire:
    
    def __init__(self,titulaire,solde=0):
        self.nom=titulaire
        self.solde=solde
    def deposer(self,montant):
        """
        Cette méthode permet d'ajouter un montant au montant existant
        """
        self.solde+=montant
        print(f"Nouveau solde après dépôt: {self.solde}")
        return self
    
    def retirer(self,montant):
        if self.solde>=montant:
               self.solde-=montant
               print(f"Nouveau solde restant après retrait: {self.solde}")
        else:
            print(f"Solde insufisant!")
            
        return self
    
    def afficher_resume(self):
        return f" {self.nom}, votre solde actuel est: {self.solde}"


########## Illustration #############

compte = CompteBancaire("M/mme Gervais Nguessan")
print(compte.deposer(100).retirer(151).deposer(50).afficher_resume())

    
####### Classe Héritage ############
 

class CompteEpargne(CompteBancaire):
    def __init__(self,titulaire,solde=0,taux_interet=0.05):
        super().__init__(titulaire,solde) ## Le mot super() veut dire "Fais appel à la classe parente".
        self.interet=taux_interet
    
    def appliquer_interet(self):
        self.solde+=self.interet*self.solde
        return self
    
    def retirer(self, montant):
         """Etant donner que retirer existe dejà dans la class
    parent, en créant une méthode retirer dans la class enfant, nous masquons la méthode retirer existant  dans la classe parent dans le 
    le programme entier. Chacune d'elle pourra être appliquée différemment en fonction des besoin"""
       
         if self.solde>= montant+5:
                self.solde-=(montant+5)
                print(f"Votre Solde après retrait est: {self.solde}")
         else:
                print("Votre Solde est insuffissant!")
         return self

# M/mme Gervais ouvre un compte épargne à 5% d'intérêt
compte_epargne = CompteEpargne("M/mme Gervais Nguessan") # taux_interet est 0.05 par défaut

resume = compte_epargne.deposer(1000).appliquer_interet().afficher_resume()
print(resume)

######### Overriding ##########




# M/mme Gervais ouvre un compte épargne à 5% d'intérêt
compte_epargne = CompteEpargne("M/mme Gervais Nguessan") # taux_interet est 0.05 par défaut

resume = compte_epargne.deposer(1000).retirer(50).appliquer_interet().afficher_resume()
print(resume)

# Un compte classique (Parent)
compte_normal = CompteBancaire("Alice")
print(f"solde Alice {compte_normal.deposer(100).retirer(50)}")
# -> Alice a 50 (pas de frais, la méthode d'origine est toujours là !)

# Un compte épargne (Enfant)
compte_epargne = CompteEpargne("Bob")
print(f"Solde Bob{compte_epargne.deposer(100).retirer(50)}")
# -> Bob a 45 (frais de 5€ appliqués, c'est ta méthode surchargée qui tourne !)


#### Client####

class Client:
     count_id=1001
     def __init__(self,nom,prénom,total_depense=0):
          self.nom=nom.capitalize()
          self.prénom=prénom.upper()
          self.total_depense=total_depense
          self.id=Client.count_id
          Client.count_id+=1
     def affiche_client(self):
          return f"Nom:{self.nom}, Prénom:{self.prénom}, identifiant:{self.id}"
     def ajouter_depense(self,montant):
          """Méthode permettant d'ajouter une dépense"""
          self.total_depense+=montant
          return self
     def affiche_depense(self):
          """Cette méthode affiche les dépenses du client"""
          return f"Le client {self.nom} {self.prénom} a dépensé un total de {self.total_depense}€"
     def compare_depense(self,client):
          if self.total_depense>client.total_depense:
               return self.id
          elif self.total_depense<client.total_depense:
            
               return client.id
          else:
               return f"Les clients {self.nom} {self.prénom} et {client.nom} {client.prénom} ont dépensé le même montant"
     

     ########### Test avec des cas pratiques ###########

alex = Client("alex", "rider")
john = Client("john", "smith")
print(alex.affiche_client())
print(john.affiche_client())
print(alex.affiche_depense())
print(alex.ajouter_depense(10))
print(alex.affiche_depense())
print(john.ajouter_depense(10))
print(alex.compare_depense(john))
print(john.ajouter_depense(15))
print(alex.compare_depense(john))



### Clsse enfant ########

class ClientVIP(Client):
    """Définir un client VIP"""
    
    # 1. On garde le même ordre (nom, prenom) que le parent
    def __init__(self, nom, prenom, total_depense=0):
        super().__init__(nom, prenom, total_depense) # super() est souvent placé en premier
        self.nombre_bon = 3

    def afficher_bons_restants(self):
        return f"Le client {self.nom} {self.prénom} a un bon restant de {self.nombre_bon}"
    
    def ajouter_depense(self, montant):
        if self.nombre_bon > 0:
            # 2. On ajoute le NOUVEAU montant avec 10% de réduction
            self.total_depense += (montant * 0.9)
            self.nombre_bon -= 1
            print(f"Bon utilisé ! Nombre restant de bons : {self.nombre_bon}")
            return self # On renvoie self pour le chaînage
        else:
            print("Vous n'avez plus de bons. Tarif normal appliqué.")
            # 3. La magie de super() : on appelle la méthode du parent pour faire le travail normal !
            return super().ajouter_depense(montant)


#### Test pour le VIP :

jack = ClientVIP("sparrow", "jack") # Sparrow en majuscule, Jack avec majuscule initiale
print(jack.affiche_client())
print(jack.afficher_bons_restants())

# On peut maintenant utiliser le chaînage (Method Chaining) que tu as appris !
print("\n--- Achats de Jack ---")
jack.ajouter_depense(10).affiche_depense() # Utilise un bon (ajoute 9)
jack.ajouter_depense(10).affiche_depense() # Utilise un bon (ajoute 9)
jack.ajouter_depense(10).affiche_depense() # Utilise un dernier bon (ajoute 9)

# Plus de bons !
jack.ajouter_depense(10).affiche_depense() # Tarif normal (ajoute 10 via le super())