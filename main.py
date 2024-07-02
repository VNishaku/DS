# seq1 = ['foo', 'bar', 'baz']
# seq2 = ['one', 'two', 'three']
# zipped=zip(seq1,seq2)
# print(list(zipped))
# for i, (a, b) in enumerate(zip(seq1, seq2)):
#     print('{0}: {1}, {2}'.format(i, a, b))

# pitchers = [('Nolan', 'Ryan'), ('Roger', 'Clemens'),('Schilling', 'Curt')]
# first_names, last_names = zip(*pitchers)
# print(first_names)
# states = [' Alabama ', 'Georgia!', 'Georgia', 'georgia', 'FlOrIda', 'south carolina##', 'West virginia?']
# import re
# def clean_strings(strings):
#  result = []
#  for value in strings:
#  value = value.strip()
#  value = re.sub('[!#?]', '', value)
#  value = value.title()
#  result.append(value)
#  return result
import tensorflow as tf
print(tf.__version__)