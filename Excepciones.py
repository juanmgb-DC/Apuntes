#Inicio
"""

COMPROBAR DNI:

def setDni(self,dni)
if len(dni) == 9: (LONXITUDE)
   if dni[-1:].isalpha(): (¿TEN LETRA AO FINAL?)
      if dni[:-1].isdigital(): (¿SON NUMEROS DENDE O INICIO ATA A PENULTIMA?)
         letras = 'T,R,W,A,G,M,Y,F,P,D,X,B,N,J,Z,S,Q,V,H,L,C,K,E'
         resto = int(dni[:-1])%23
         if letras[resto] == dni[-1:].upper():
            self.__dni = dni
         else:
            raise ValueError ("Letra do DNI incorrecta")
      else:
         raise ValueError ("Non son numeros dende o inicio ata a penultima")
   else:
      raise ValueError ("Non ten letra ao final")
else:
   raise ValueError ("Lonxitude Incorrecta)



















"""