class Salarie:

    def __init__(self, nom,prenom,salaire,id):
        self._NAME = nom
        self._PR = prenom
        self._S = salaire
        self._ID= id

    def getNAME(self):
        return self._NAME

    def getPrenom(self):
        return self._PR

    def getSalaire(self):
        return self._S

    def getID(self):
        return self._ID

    def setNAME(self,nom):
        self._NAME = nom

    def setPrenom(self,prenom):
        self._PR = prenom

    def setSalaire(self,salaire):
        self._S = salaire

    def setID(self,id):
        self._ID = id

    def print(self):
        pass

