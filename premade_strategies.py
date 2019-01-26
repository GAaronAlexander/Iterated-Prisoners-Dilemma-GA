def pavlov():
  """Returns a string representing the Pavlov strategy."""
  pavlov_strategy = ['0'] * 85
  pavlov_strategy[84] = '1'
  for i in range(0, 84):
    if i < 64:
      moves_str = list(format(i, '06b'))    
    elif i < 80:    
      moves_str = list(format(i-64, '04b')) 
    else:
      moves_str = list(format(i-80, '02b'))
    my_last_move = moves_str[-2]
    their_last_move = moves_str[-1]
    if their_last_move == '1':
      pavlov_strategy[i] = my_last_move
    else:
      pavlov_strategy[i] = str(1 - int(my_last_move))
  return ''.join(pavlov_strategy)


def tit_for_tat():
  """Returns a string representing the tit-for-tat (copycat) strategy."""
  return '01' * 42 + '1'


def always_defect():
  """Returns a string representing the always defect strategy."""
  return '0' * 85


def always_cooperate():
  """Returns a string representing the always cooperate strategy."""
  return '1' * 85
