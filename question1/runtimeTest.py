import time
from main import plot_corrections_test,prob_corrections_test

def measure_runtime(function_to_run, *args):
    start_time = time.time()
    function_to_run(*args)
    end_time = time.time()
    return end_time - start_time

def average_runtime(function_to_run, num_runs, *args):
    total_time = 0.0
    for _ in range(num_runs):
        total_time += measure_runtime(function_to_run, *args)
    return total_time / num_runs

# Assuming plot_corrections and prob_corrections are set up to run without any issues
# for testing purposes, saving to excel and plotting the data to browser is disabled.

def main():
    ticker = 'SPY'
    start_date = '2014-01-01'
    num_runs = 10
    
    avg_time_plot = average_runtime(plot_corrections_test, num_runs, ticker, start_date)
    avg_time_prob = average_runtime(prob_corrections_test, num_runs, ticker, start_date)
    
    print(f"Average runtime for plot_corrections over {num_runs} runs: {avg_time_plot} seconds")
    print(f"Average runtime for prob_corrections over {num_runs} runs: {avg_time_prob} seconds")
    print(f"Total Average runtime for both over {num_runs} runs: {avg_time_plot + avg_time_prob} seconds")


if __name__ == "__main__":
    main()