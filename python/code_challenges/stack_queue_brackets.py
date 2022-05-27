from data_structures.queue import Queue


def multi_bracket_validation(str):
  temp_list = []
  bracket_ex = {
      '(': ')',
      '[': ']',
      '{': '}'
  }
  for i in range(len(str)):
      if(str[i] == '(' or str[i] == '[' or str[i] == '{' ):
          temp_list.append(str[i])
      else:
          closed_bracket = temp_list.pop()
          if(str[i] != bracket_ex[closed_bracket]):
              return False
  if (len(temp_list) != 0):
      return False

  return True

print(multi_bracket_validation('(({[]}))'))
