from Salarie import *


class Filiale:

    def __init__(self, nom,pays,dateCreation,tab2=[]):
        self.__NOM = nom
        self.__P = pays
        self.__DateCrea = dateCreation
        self.__tab2=tab2

    def getNOM(self):
        return self.__NOM

    def getPays(self):
        return self.__P

    def getDC(self):
        return self.__DateCrea

    def getTAB2(self):
        return self.__tab2


    def setNOM(self,nom):
        self.__NOM = nom

    def setPays(self,pays):
        self.__P = pays

    def setDC(self,dateCreation):
        self.__DateCrea=dateCreation

    def ajouter(self,salarie):
        self.__tab2.append(salarie)
        return self.__tab2

    def supprimer(self,salarie):
        self.__tab2.remove(salarie)
        return self.__tab2

    def print(self):
        pass

