def polishNotation(exp: list):
  # Este algoritmo resuelve expresiones matemáticas en notación polaca inversa
  # La expresión matemática se ingresa en un arreglo
  # Se utiliza una pila para la solución de las operaciones hasta completarlas todas
  # Retorna la solución de la operación enviada

  stack = []
  for i in exp:
    if isOperator(i):
      op = i
      n2 = stack.pop()
      n1 = stack.pop()

      if op == "+":
        res = int(n1) + int(n2)
        stack.append(f'{res}')

      if op == "-":
        res = int(n1) - int(n2)
        stack.append(f'{res}')

      if op == "x":
        res = int(n1) * int(n2)
        stack.append(f'{res}')

      if op == "/":
        res = int(n1) / int(n2)
        stack.append(f'{int(res)}')
    else:
      stack.append(i)

  return stack[0]

def isOperator(ch):
  # Este programa retorna True si el caracter ingresado es un operador matemático
  # De lo contrario retorna False
  
  if ch == '+' or ch == '-' or ch == 'x' or ch == '/':
    return True
  return False

# Test
expression = ['1', '5', 'x']
print(expression)
print(polishNotation(expression))

expression = ['2', '1', '+', '3', 'x']
print(expression)
print(polishNotation(expression))

expression = ['4', '13', '5', '/', '+']
print(expression)
print(polishNotation(expression))

expression = ['10', '6', '9', '3', '+', '-11', 'x', '/', 'x', '17', '+', '5', '+']
print(expression)
print(polishNotation(expression))