import multiprocessing as mp
from analisis_s import *
from analisis import *
import time


def process_file(args):
  input_path, output_path = args
  substitution_analysisS(input_path, output_path)


files = [('tests/cipher1.txt', 'decyphered1.txt'),
         ('tests/cipher2.txt', 'decyphered2.txt'),
         ('tests/cipher3.txt', 'decyphered3.txt'),
         ('tests/cipher4.txt', 'decyphered4.txt'),
         ('tests/cipher5.txt', 'decyphered5.txt'),
         ('tests/cipher6.txt', 'decyphered6.txt')]

print("NCores available:", mp.cpu_count(), '\n')
ncores = mp.cpu_count()
print("Starting decyphering:")

start_time = time.time()
substitution_analysis('tests/cipher1.txt', 'decyphered1.txt', ncores)
end_time = time.time()
Ptime = end_time - start_time
print("Parallel time text 1:", Ptime, '\n')

start_time = time.time()
substitution_analysis('tests/cipher1.txt', 'decyphered1.txt', 1)
end_time = time.time()
FullTime = end_time - start_time
print("Sequential time text 1:", FullTime, '\n')

start_time = time.time()
substitution_analysis('tests/cipher2.txt', 'decyphered2.txt', ncores)
end_time = time.time()
Ptime = end_time - start_time
print("Parallel time text 2:", Ptime, '\n')

start_time = time.time()
substitution_analysis('tests/cipher2.txt', 'decyphered2.txt', 1)
end_time = time.time()
FullTime = end_time - start_time
print("Sequential time text 2:", FullTime, '\n')

start_time = time.time()
substitution_analysis('tests/cipher3.txt', 'decyphered3.txt', ncores)
end_time = time.time()
Ptime = end_time - start_time
print("Parallel time text 3:", Ptime, '\n')

start_time = time.time()
substitution_analysis('tests/cipher3.txt', 'decyphered3.txt', 1)
end_time = time.time()
FullTime = end_time - start_time
print("Sequential time text 3:", FullTime, '\n')

start_time = time.time()
substitution_analysis('tests/cipher4.txt', 'decyphered4.txt', ncores)
end_time = time.time()
Ptime = end_time - start_time
print("Parallel time text 4:", Ptime, '\n')

start_time = time.time()
substitution_analysis('tests/cipher4.txt', 'decyphered4.txt', 1)
end_time = time.time()
FullTime = end_time - start_time
print("Sequential time text 4:", FullTime, '\n')

start_time = time.time()
substitution_analysis('tests/cipher5.txt', 'decyphered5.txt', ncores)
end_time = time.time()
Ptime = end_time - start_time
print("Parallel time text 5:", Ptime, '\n')

start_time = time.time()
substitution_analysis('tests/cipher5.txt', 'decyphered5.txt', 1)
end_time = time.time()
FullTime = end_time - start_time
print("Sequential time text 5:", FullTime, '\n')

start_time = time.time()
substitution_analysis('tests/cipher6.txt', 'decyphered6.txt', ncores)
end_time = time.time()
Ptime = end_time - start_time
print("Parallel time text 6:", Ptime, '\n')

start_time = time.time()
substitution_analysis('tests/cipher6.txt', 'decyphered6.txt', 1)
end_time = time.time()
FullTime = end_time - start_time
print("Sequential time text 6:", FullTime, '\n')

start_time = time.time()
substitution_analysis('tests/cipher7.txt', 'decyphered7.txt', ncores)
end_time = time.time()
Ptime = end_time - start_time
print("Parallel time text 7:", Ptime, '\n')

start_time = time.time()
substitution_analysis('tests/cipher7.txt', 'decyphered7.txt', 1)
end_time = time.time()
FullTime = end_time - start_time
print("Sequential time text 7:", FullTime, '\n')

start_time = time.time()
substitution_analysis('tests/cipher7.txt', 'decyphered7.txt', (ncores // 2))
end_time = time.time()
Ptime = end_time - start_time
print("Parallel time text 7 (half ncores):", Ptime, '\n')

start_time = time.time()
substitution_analysis('tests/cipher7.txt', 'decyphered7.txt', (ncores // 4))
end_time = time.time()
Ptime = end_time - start_time
print("Parallel time text 7 (1/4 ncores):", Ptime, '\n')

print("All texts test: \n Sequential:")
start_time = time.time()
manT = substitution_analysis('tests/cipher1.txt', 'decyphered1.txt', 1)
substitution_analysis('tests/cipher2.txt', 'decyphered2.txt', 1)
substitution_analysis('tests/cipher3.txt', 'decyphered3.txt', 1)
substitution_analysis('tests/cipher4.txt', 'decyphered4.txt', 1)
substitution_analysis('tests/cipher5.txt', 'decyphered5.txt', 1)
substitution_analysis('tests/cipher6.txt', 'decyphered6.txt', 1)
substitution_analysis('tests/cipher7.txt', 'decyphered7.txt', 1)
end_time = time.time()
FullTime = end_time - start_time
print("Sequential time:", FullTime, '\n')

print("Parallel:")
start_time = time.time()
pool = mp.Pool(ncores)
pool.map(process_file,
         [(input_path, output_path) for input_path, output_path in files])
# pool.map(process_file, files)

pool.close()
pool.join()
end_time = time.time()
FullTime = end_time - start_time
print("Parallel time:", FullTime, '\n')

print("done")

""" 
manual substitution:

with open('decyphered1.txt', 'r') as file:
  lines = file.read().upper()
while True:

  print("First 15 lines of decrypted text:")
  print('\n'.join(lines.splitlines()[:15]))

  swap = input("Do you want to swap two letters? (yes/no): ").strip().lower()
  if swap in ['no', 'n']:
    break

  letter1 = input("Enter the first letter to swap: ").strip()
  letter2 = input("Enter the second letter to swap: ").strip()

  if len(letter1) == 1 and len(letter2) == 1:
    lines = swap_lettersManual(lines, letter1, letter2)
  else:
    print("Please enter valid single letters.")

with open('decyphered1.txt', 'w') as file:
  file.write(lines)
"""