from Employe import *

class Ingenieur(Employe):

    def __init__(self,nom,prenom,salaire,id,anneeEmbauche,nbrjourtravail,nbrheureprojet,nbrheuregestion):
        Employe.__init__(self,nom,prenom,salaire,id,anneeEmbauche,nbrjourtravail)
        self._NBRHP = nbrheureprojet
        self._NBRHG=nbrheuregestion

    def getNBRHP(self):
        return self._NBRHP

    def setNBRHP(self,nbrheureprojet):
        self._NBRHP = nbrheureprojet

    def getNBRHG(self):
        return self._NBRHG

    def setNBRHG(self,nbrheuregestion):
        self._NBRHG = nbrheuregestion
