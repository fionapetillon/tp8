from Salarie import *

class Directeur(Salarie):

    def __init__(self,nom,prenom,salaire,id,anneeNomination):
        Salarie.__init__(self,nom,prenom,salaire,id)
        self.__AN = anneeNomination

    def getAN(self):
        return self.__AN

    def setAN(self,anneeNomination):
        self.__AN = anneeNomination

    def print(self):
        print("* [",self._ID,"] Nom et prénom :",self._NAME,self._PR,", Salaire :",self._S," Statut : Directeur, Année de nomination :",self.__AN," Site :",self.__P)


