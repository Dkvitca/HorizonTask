### Installation

A step-by-step series of examples that tell you how to get a development environment running.

#### Setting Up Your Environment

1. Clone the repository or download the source code to your local machine.
2. Navigate to the project directory and install the required Python packages:
   pip install -r requirements.txt

## Running the Programs

### Question 1

#### Folder Structure

- main.py: Main script to run the analysis and generate plots.
- tradeAnalyzerClass.py: Contains an abstract class used by main.py.
- runtimeTest.py: Tests the runtime of the program and prints results.

#### Execution Instructions

1. **Running the Main Analysis**:
   - Navigate to the question1 folder.
   - Run main.py to perform the analysis and generate the output:
     python main.py
   - This will answer Question 1, generate Plotly plots that will appear in your browser, and create an output.xlsx file within the question1 folder.

2. **Running Runtime Tests**:
   - Within the question1 folder, run runtimeTest.py to execute runtime tests:
     python runtimeTest.py
   - The test results will be printed to the terminal.
   - Review the runtimeSummary.txt file for a detailed analysis of the runtime, prepared based on the tests.

#### General Explanation about this question:
   - inside of main.py you can i have defined two classes, each one has the names of the functions requested 
     in the home_assigment. bot of them derive the calculations from the abstract class found inside of the
     tradeAnalyzerClass called "DataAnalyzer". both classes have same basic neccesstys for calculations,
     all of them found in the parent class. the key difference between the classes is the plotting and some 
     calculations made in prob_corrections.

   - interms of testing i have mad an evaluation of the runtime and saved it inside of runtimeSummary.txt for you to check

#### References:
   - yfinance: https://pypi.org/project/yfinance/
   - line charts in plotly: https://plotly.com/python/line-charts/#line-plots-with-plotlyexpress
   - market Cycles: https://fastercapital.com/content/Market-cycles--The-High-Low-Index-and-Market-Cycles--A-Predictive-Approach.html#Understanding-the-High-Low-Index
   - peak finding: https://plotly.com/python/peak-finding/
   - Golay_filter: https://en.wikipedia.org/wiki/Savitzky%E2%80%93Golay_filter
   - Comparison of public peak detection algorithms: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2631518/


## Question 2

### Folder Structure

- `answer.ipynb`: Jupyter Notebook containing the complete analysis for Question 2.

### Execution Instructions

1. **Running the Analysis Notebook**:
   - Open the `answer.ipynb` file in Google Colab, Jupyter Notebook, or another compatible notebook environment.
   - Run all cells in the order they appear to perform the analysis.
   - Note: The notebook reads data from a file named `data.csv` located in the root folder. If `data.csv` is not located in the root folder when you are running the notebook, you must update the file path in the notebook where `data.csv` is read.

Make sure to adjust the file paths accordingly if the structure of the directories where your files are stored differs from this setup.

#### References:
   - All Signals were learned from: https://www.investopedia.com/
   - decision trees: https://www.kaggle.com/code/sndorburian/decision-tree-for-trading-using-python
   - randomForrest: https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html
   - randomForrestVideo: https://www.youtube.com/watch?v=J4Wdy0Wc_xQ
   
   useful:
   - generalStrategy: https://medium.com/@pulsepointfx/simple-moving-average-crossover-strategy-using-python-45691c9b12c1
   - general: https://www.linkedin.com/pulse/cannot-decide-between-buy-sell-let-decision-tree-you-quantra/
