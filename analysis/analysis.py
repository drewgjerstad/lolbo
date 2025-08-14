import numpy as np
import matplotlib.pyplot as plt

def process_output(fpath:str, task_id:str)->dict:
    """
    Process LOLBO terminal output stored in a text file.

    Args:
        fpath (str):
            Filepath for terminal output.
        task_id (str):
            Task ID for output (used to extract scores).

    Returns:
        output (dict):
            Dictionary with {key=num_oracle_calls, val=best_score_found}.
    """
    # Output Substrings
    score_substring = f"Best {task_id} Score: "
    oracle_substring = "Total Number of Oracle Calls (Function Evaluations): "

    # Initialize Dictionary
    output = {}

    try:
        with open(fpath, mode="r", buffering=1, encoding="utf-8") as f:
            lines = f.readlines()
            for idx, line in enumerate(lines):
                if score_substring in line:
                    # Extract Score and Number of Oracle Calls
                    best_score_found = line.strip(score_substring)
                    num_oracle_calls = lines[idx + 1].strip(oracle_substring)

                    # Store in Dictionary
                    output[int(num_oracle_calls)] = float(best_score_found)

    except FileNotFoundError as exc:
        print("File Not Found!")
        raise FileNotFoundError from exc

    return output


def generate_plot(output:dict, best_in_set:float, title:str, xlab:str, ylab:str,
                  xlim:tuple, ylim:tuple, error_bars:bool=True,
                  fpath:str="plot.png", verbose:bool=True)->None:
    """
    Generate plot from output showing progress made across calls to oracle.

    Args:
        output (dict):
            Dictionary containing output with {key=num_oracle_calls, value=best_score_found}.
        best_in_set (float):
            Best score from dataset (optional).
        title (str):
            Plot title.
        xlab (str):
            Label for x-axis.
        ylab (str):
            Label for y-axis.
        xlim (tuple):
            Tuple containing x-axis limits (i.e., [min, max])
        ylim (tuple):
            Tuple containing y-axis limits (i.e., [min, max])
        error_bars (bool):
            Indicator to add error bars to plot (default=True).
        fpath (str):
            Filepath for where to save generated plot (default="plot.png").
        verbose (bool):
            Indicator to show plot (default=True).

    Returns:
        None
    """
    # Extract Output
    num_oracle_calls = np.array(list(output.keys()))
    best_score_found = np.array(list(output.values()))

    # Initialize Figure
    fig, ax = plt.subplots(1, 1, figsize=(12, 10))

    # Plot Progress
    ax.plot(num_oracle_calls, best_score_found, linestyle="--", marker="D",
                markersize=8, color="b", label="LOLBO Progress")

    if error_bars:
        stderror = (np.std(best_score_found, ddof=1) /
                    np.sqrt(best_score_found.shape[0]))
        ax.fill_between(num_oracle_calls, best_score_found - stderror,
                        best_score_found + stderror, color="b", alpha=0.2)

    # Plot Best in Set Line
    if best_in_set:
        ax.hlines(best_in_set, xmin=xlim[0], xmax=xlim[1], colors=["k"],
                  linestyles=["dotted"], label="Best in Dataset")

    # Plot Features
    ax.set_xlim(xlim[0], xlim[1])
    ax.set_ylim(ylim[0], ylim[1])
    ax.set_xlabel(xlab)
    ax.set_ylabel(ylab)
    ax.set_title(title)
    ax.legend()
    ax.grid(True)

    # Save/Show Figure
    if fpath:
        fig.savefig(fpath)
    if verbose:
        plt.show()


def main():
    """
    Run analysis, reproduce LOLBO paper results.
    """

if __name__ == "__main__":
    main()
