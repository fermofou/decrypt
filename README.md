# decrypt
Python code that decripts text using parallel programming

On this project, my team (Monica Sóberon, Bernardo Willis) and I were tasked with decrypting different texts that used a monoalphabetic substitution cipher. My role on this project was the implementation developer, and I developed this solution. We created a function to count letters in a given message; then create a substitution "key" by pairing the frequencies based on the average of english alphabet; and finally replace the letter using said key.

We applied parallel programming in 2 different ways: one was processig text by chunks, and create key with joint results; and the other was running different files using multiprocessing, each proccess in a sequential manner.

When comparing results, individually there was some underperformance against a sequential approach on our .txt files, however there was a massive improvement on performance when running all files at the same time, compared to one by one.

This was a cool project to get to know a useful technique and to understand when it's better to use this tool (heavier or larger tasks,preferably that can be solved independently) against a sequential approach (tasks with dependencies on same resources or variables.)

This code was created using the libaries multiprocessing (for parallel application), collections (to count the repetition of letters on text) and time (to compare test runs).

To see for yourself, you can visit my  <a href="https://replit.com/@FernandoMoran4/E2-Applied-parallel-programming#main.py">replit</a>


Here's a code extract, with a simple implementation of multiprocessing to run our program to all .txt files on our test list:


```python
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
```

