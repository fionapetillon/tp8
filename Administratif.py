from Employe import *

class Administratif(Employe):

    def __init__(self,nom,prenom,salaire,id,anneeEmbauche,nbrjourtravail,service):
        Employe.__init__(self,nom,prenom,salaire,id,anneeEmbauche,nbrjourtravail)
        self.__SERV = service


    def getSERV(self):
        return self.__SERV

    def setSERV(self,service):
        self.__SERV = service

    def print(self):
         print("* [",self._ID,"] Nom et prénom :",self._NAME,self._PR,", Salaire :",self._S," Statut : Administratif, Année d'embauche :",self.__AE," Site :",self.__P,", Nombre de jours de travail :",self.__NBRJT, "Service :",self.__SERV,".")




