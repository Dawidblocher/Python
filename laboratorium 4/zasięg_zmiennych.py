a = int(10)
def print_global():
  print(a)

def shadow_a():
  a = 5
  print(a)

counter = int(1)

def increase_counter(n):
  localCounter = int(counter)
  localCounter = localCounter + n
  print(localCounter)

print_global()
shadow_a()
increase_counter(1)
increase_counter(2)
increase_counter(3)
increase_counter(4)
increase_counter(5)

  