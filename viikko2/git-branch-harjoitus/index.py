# tehdään alussa importit

from logger import logger
from summa import summa
from erotus import erotus
from tulo import tulo 

logger("aloitetaan ohjelma") # muutos mainissa

x = int(input("luku 1: "))
y = int(input("luku 2: "))
print(f"Lukujen {x} ja {y} summa on {x} + {y} = {summa(x, y)}")  # yhdistelmämuutos bugikorjaus-branchissa ja mainissa
print(f"Lukujen {x} ja {y} erotus on {x} - {y} = {erotus(x, y)}")  # yhdistelmämuutos bugikorjaus-branchissa ja mainissa
print(f"{x} * {y} = {tulo(x, y)}")

logger("lopetetaan ohjelma")
print("goodbye!") # lisäys bugikorjaus-branchissa