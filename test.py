from Multinationale import *
from Filiale import *
from Salarie import *
from Directeur import *
from Employe import *
from Administratif import *
from Ingenieur import *
from IngJunior import *
from IngSenior import *

M=Multinationale("RCAT","la France",[])
F1=Filiale("RCAT","Tunisie","1998",[])
F2=Filiale("RCAT","Belgique","1999",[])
F3=Filiale("RCAT","Maroc","2002",[])
F4=Filiale("RCAT","Angleterre","2005",[])
M.ajouter(F1)
M.ajouter(F2)
M.ajouter(F3)
M.ajouter(F4)
S1=Salarie("VAZ","YANICE","2","153")
S2=Salarie("BIARD","ERIN","3","121")
S3=Salarie("LACOUR","JULIETTE","1","154")
S4=Salarie("GABORIAU","ANGELE","2","122")
S5=Salarie("RUER","NATHAN","6","133")
S6=Salarie("MOCK","MAEL","2","160")
F1.ajouter(S1)
F2.ajouter(S2)
F3.ajouter(S3)
F4.ajouter(S4)
F1.ajouter(S5)
F2.ajouter(S6)
M.print()
