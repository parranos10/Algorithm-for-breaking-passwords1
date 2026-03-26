from typing_extensions import final
import time 
abecedario = "abcdefghiojklmnopqrstuvwxyz"
contraseña = "agpd"
intentos = 0
crackeado = False
tiempo = time.time()

for i in abecedario:
  intento = i
  intentos += 1
  if intento == contraseña:
    crackeado = True
    break
    
if crackeado == False:
    for i in abecedario:
        for j in abecedario:
          intento = i + j
          intentos += 1
          if intento == contraseña:
            crackeado = True
            break
if crackeado == False:
  for i in abecedario:
    for j in abecedario:
      for k in abecedario:
        intento = i + j + k 
        intentos += 1
        if intento == contraseña:
          crackeado = True
          break
      if crackeado == True:
        break
    if crackeado == True:
      break
    
if crackeado == False:
  for i in abecedario:
    for j in abecedario:
      for k in abecedario:
        for l in abecedario:
          intento = i + j + k + l
          intentos += 1
          if intento == contraseña:
            crackeado = True
            break
        if crackeado == True:
          break
      if crackeado == True:
        break
    if crackeado == True:
      break
  

print("contraseña encontrada","intentos: ", intentos)
final = time.time()
print("el tiempo fue: ",final)

  

