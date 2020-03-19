from Ingenieur import *

class IngSenior(Ingenieur):

    def __init__(self,nom,prenom,salaire,id,anneeEmbauche,nbrjourtravail,nbrheureprojet,nbrheuregestion,responsabilite):
        Ingenieur.__init__(self,nom,prenom,salaire,id,anneeEmbauche,nbrjourtravail,nbrheureprojet,nbrheuregestion)
        self.__RESP = responsabilite

    def getRESP(self):
       return self.__RESP

    def setRESP(self,responsabilite):
        self.__RESP = responsabilite

    def print(self):
        print("* [",self._ID,"] Nom et prénom :",self._NAME,self._PR,", Salaire :",self._S," Statut : Ingénieur-Sénior, Année d'embauche' :",self.__AE," Site :",self.__P," Nombre de jours de travail :",self.__NBRJT,"Nombre d'heures de projet",self.__NBRHP,"Nombre d'heures de gestion:",self.__NBRHG,"Responsabilité :",self.__RESP,".")
        print(f"")
