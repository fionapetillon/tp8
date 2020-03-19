from Filiale import *

class Multinationale:

    def __init__(self, nom, paysOrigine,tab=[]):
        self.__N = nom
        self.__PO = paysOrigine
        self.__tab= tab

    def getNom(self):
        return self.__N

    def getpaysOrigine(self):
        return self.__PO

    def setNom(self,nom):
        self.__N = nom

    def setPaysOrigine(self,paysOrigine):
        self.__PO = paysOrigine

    def ajouter(self,filiale):
        self.__tab.append(filiale)
        return self.__tab

    def supprimer(self,filiale):
        self.__tab.remove(filiale)
        return self.__tab

    def print(self):
        print("- La multinationale",self.__N,"est composée de",len(self.__tab),"filiales. Son pays d'origine est",self.__PO,".")

        datePlusAncienne = self.__tab[0].getDC()
        filialePlusAncienne= self.__tab[0]

        for i in self.__tab :
            if i.getDC()< datePlusAncienne:
                filialePlusAncienne = i

        print("- La filiale la plus ancienne de cette multinationale est :",filialePlusAncienne.getNOM(),"-",filialePlusAncienne.getPays(),". Elle est composée de ",len(filialePlusAncienne.getTAB2()),"salariés.")

        nbsalarie=0
        for i in self.__tab:
            nbsalarie+= len(i.getTAB2())

        print("-",self.__N,"est composée de",nbsalarie,"salariés:")







