Tutorial
=

Script [example_script.py]() in this folder contains a solution for the problem ["Find a Position in Genome Minimizing the Skew"](http://rosalind.info/problems/ba1f/) (with a caveat that until January 31st instead of an algorithm, that solves the problem, there is going to be a placeholder, that always outputs the answer for the sample dataset).

Running the script in the terminal:

```bash
    python example_script.py input.txt
```

In this tutorial input dataset is provided to the script as an argument in the `input.txt` file (file you would download from Rosalind).



PyCharm setup for Algorithms in Bioinformatics
--

The simplest setup for the Pycharm, that can suite you well in this class is as follows:
 
 * create a new project (name it just the way you want)
 ![screen shot 2017-01-27 at 7 28 27 pm](https://cloud.githubusercontent.com/assets/1204593/22392505/066773a2-e4c8-11e6-9fe3-0e52ada251e7.png)
 
 * each problem corresponds to an independent script (i.e., *problem1.py*)
 ![screen shot 2017-01-27 at 7 28 28 pm](https://cloud.githubusercontent.com/assets/1204593/22392535/5b8249ca-e4c8-11e6-8f50-3c286bb33fcc.png)
 

 * create a run configuration
 ![screen shot 2017-01-27 at 7 28 28 pm](https://cloud.githubusercontent.com/assets/1204593/22392516/1b032888-e4c8-11e6-8c5a-4d4f726e8dfe.png)
 
 * for every problem adjuct the run configuration to point to the script, that corresponds to the current problem (alter the Script: field in the Run/Debug Configuration)
 
At all times, the input for the current problem is named *intput.txt*. Once the problem is solved, the input can be *archive*
 as *problemX.txt*. In this approach you will not need to change cli arguments in the run configuration, but you will still have all of the datasets in place.
 
 

