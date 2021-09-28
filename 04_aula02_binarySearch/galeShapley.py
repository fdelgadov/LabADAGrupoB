from typing import final


def galeShapley(a1, a2):
  # Este algoritmo garantiza un emparejamiento estable entre los elementos de 2 listas
  # Retona las parejas en un arreglo

  size = len(a1)
  couples = [-1 for i in range(size)]
  h = 0
  available = [0 for i in range(size)]
  goBack = -1
  while h < size:
    #print(couples)#debug
    #print(available)#debug   
    #print(f"h: {h}")#debug

    m = -1
    herCouple = -1

    # Buscar el índice de la pareja más preferida disponible
    for i in range(size):
      if(a1[h][available[h] + 1] == a2[i][0]):
        m = i

    # Buscar el índice de la pareja de 'm'
    for i in range(size):
      if couples[i] == m:
        herCouple = i
        break
    
    #print(f"m: {m}\nherCouple: {herCouple}")#debug

    if herCouple == -1:
      # 'm' no tiene pareja
      couples[h] = m
      if goBack == -1:
        h += 1
      else:
        h = goBack
        goBack = -1
    else:
      # Buscar al preferido
      for i in a2[m][1:]:
        if i == a1[h][0]:
          # El que se declara es preferido
          couples[h] = m
          couples[herCouple] = -1
          if goBack == -1:
            goBack = h + 1
          h = herCouple
          available[h] = available[h] + 1
          break
        elif i == a1[herCouple][0]:
          available[h] = available[h] + 1
          break
  
  res = []
  j = 0
  for i in couples:
    res.append([a1[j][0], a2[i][0]])
    j += 1
  return res

# Test
a1 = [
     ["Andy", "Xena", "Wendy", "Yvonne", "Zoe"],
     ["Beto", "Yvonne", "Zoe", "Xena", "Wendy"],
     ["Carlo", "Yvonne", "Xena", "Zoe", "Wendy"],
     ["Denis", "Wendy", "Zoe", "Yvonne", "Xena"]
     ]

a2 = [
     ["Wendy", "Carlo", "Denis", "Beto", "Andy"],
     ["Xena", "Carlo", "Beto", "Andy", "Denis"],
     ["Yvonne", "Andy", "Beto", "Carlo", "Denis"],
     ["Zoe", "Denis", "Carlo", "Beto", "Andy"]
     ]

print(galeShapley(a1, a2))