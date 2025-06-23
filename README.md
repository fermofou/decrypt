# decrypt
Python code that decripts text using parallel programming

On this project, my team (Monica Sóberon, Bernardo Willis) and I were tasked with decrypting different texts that used a monoalphabetic substitution cipher. My role on this project was the implementation developer, and I developed this solution. We created a function to count letters in a given message; then create a substitution "key" by pairing the frequencies based on the average of english alphabet; and finally replace the letter using said key.

We applied parallel programming in 2 different ways: one was processig text by chunks, and create key with joint results; and the other was running different files using multiprocessing, each proccess in a sequential manner.

When comparing results, individually there was some underperformance against a sequential approach on our .txt files, however there was a massive improvement on performance when running all files at the same time, compared to one by one.

This was a cool project to get to know a useful technique and to understand when it's better to use this tool (heavier or larger tasks,preferably that can be solved independently) against a sequential approach (tasks with dependencies on same resources or variables.)

This code was created using the libaries multiprocessing (for parallel application), collections (to count the repetition of letters on text) and time (to compare test runs).

<div class="row justify-content-sm-center">
    <div class="col-sm-8 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/p5.jpg" title="Parallel execution vs sequential execution" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm-4 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/p6.jpg" title="Multiprocessing vs sequential processes on only 1 file" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Here are some test results I got on my code. To see for yourself, you can visit my  <a href="https://replit.com/@FernandoMoran4/E2-Applied-parallel-programming#main.py">replit</a>
</div>

<!-- The code is simple.
Just wrap your images with `<div class="col-sm">` and place them inside `<div class="row">` (read more about the <a href="https://getbootstrap.com/docs/4.4/layout/grid/">Bootstrap Grid</a> system).
To make images responsive, add `img-fluid` class to each; for rounded corners and shadows use `rounded` and `z-depth-1` classes. -->

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

