from Salarie import *

class Employe(Salarie):

    def __init__(self,nom,prenom,salaire,id,anneeEmbauche,nbrjourtravail):
        Salarie.__init__(self,nom,prenom,salaire,id)
        self._AE = anneeEmbauche
        self._NBRJT=nbrjourtravail

    def getAE(self):
        return self._AE

    def setAE(self,anneeEmbauche):
        self._AE = anneeEmbauche

    def getNBRJOURT(self):
        return self._NBRJT

    def setNBRJOURT(self,nbrjourtravail):
        self._NBRJT = nbrjourtravail

    def print(self):
        pass

