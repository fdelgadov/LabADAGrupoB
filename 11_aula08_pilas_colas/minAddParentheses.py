def minAddParentheses(exp: str):
  # Este programa retorna el número necesario de paréntesis que se deben
  # agregar a la cadena para que sea válida

  stack = []
  for i in exp:
    if i == ')':
      if len(stack) > 0 and stack[-1] == '(':
        stack.pop()
      else:
        stack.append(i)
    else:
      stack.append(i)
  
  return len(stack)

# Test
exp = ''
print(minAddParentheses(exp))

exp = '(())()'
print(minAddParentheses(exp))

exp = '())'
print(minAddParentheses(exp))

exp = '((('
print(minAddParentheses(exp))

exp = '(()))('
print(minAddParentheses(exp))

exp = '()))(('
print(minAddParentheses(exp))