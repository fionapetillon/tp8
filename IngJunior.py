from Ingenieur import *

class IngJunior(Ingenieur):

   def __init__(self,nom,prenom,salaire,id,anneeEmbauche,nbrjourtravail,nbrheureprojet,nbrheuregestion,nbranneeexp):
        Ingenieur.__init__(self,nom,prenom,salaire,id,anneeEmbauche,nbrjourtravail)
        self.__NBRAE = nbranneeexp

   def getNBRAE(self):
       return self.__NBRAE

   def setNBRAE(self,nbranneeexp):
        self.__NBRAE = nbranneeexp

   def print(self):
        print("* [",self._ID,"] Nom et prénom :",self._NAME,self._PR,", Salaire :",self._S," Statut : Ingénieur-Junior, Année d'embauche' :",self.__AE," Site :",self.__P," Nombre de jours de travail :",self.__NBRJT,"Nombre d'heures de projet",self.__NBRHP,"Nombre d'heures de gestion:",self.__NBRHG,"Nombre d'années d'expérience:",self.__NBRAE,"ans.")

