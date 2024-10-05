from ortools.linear_solver import pywraplp
import time


def create_data(Arquivo):
    caminho = f"/workspaces/Heuristicas/Heuristicas/BPP/BPPInstances/E_120_N_40_60/{
        Arquivo}"

    def read_instance(arquivo):
        with open(arquivo, "r") as file:
            lines = file.read()

        return lines

    itens = list(map(int, filter(None, read_instance(caminho).split("\n"))))
    print(itens)
    tam, bin_size = itens[0], itens[1]
    itens.pop(0), itens.pop(0)
    data = {
        "weights": itens,
        "items": list(range(len(itens))),
        "bins": list(range(len(itens))),
        "bin_capacity": bin_size,
    }
    return data


def main():
    data = create_data("E_120_N_40_60_BF0000.bpp")

    # Create the mip solver with the SCIP backend.
    solver = pywraplp.Solver.CreateSolver("SCIP")

    if not solver:
        return

    # Variables
    # x[i, j] = 1 if item i is packed in bin j.
    x = {}
    for i in data["items"]:
        for j in data["bins"]:
            x[(i, j)] = solver.IntVar(0, 1, "x_%i_%i" % (i, j))

    # y[j] = 1 if bin j is used.
    y = {}
    for j in data["bins"]:
        y[j] = solver.IntVar(0, 1, "y[%i]" % j)

    # Constraints
    # Each item must be in exactly one bin.
    for i in data["items"]:
        solver.Add(sum(x[i, j] for j in data["bins"]) == 1)

    # The amount packed in each bin cannot exceed its capacity.
    for j in data["bins"]:
        solver.Add(
            sum(x[(i, j)] * data["weights"][i] for i in data["items"])
            <= y[j] * data["bin_capacity"]
        )

    # Objective: minimize the number of bins used.
    solver.Minimize(solver.Sum([y[j] for j in data["bins"]]))

    print(f"Solving with {solver.SolverVersion()}")
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        num_bins = 0
        for j in data["bins"]:
            if y[j].solution_value() == 1:
                bin_items = []
                bin_weight = 0
                for i in data["items"]:
                    if x[i, j].solution_value() > 0:
                        bin_items.append(i)
                        bin_weight += data["weights"][i]
                if bin_items:
                    num_bins += 1
                    print("Bin number", j)
                    print("  Items packed:", bin_items)
                    print("  Total weight:", bin_weight)
                    print()
        print()
        print("Number of bins used:", num_bins)
        print("Time = ", solver.WallTime(), " milliseconds")
    else:
        print("The problem does not have an optimal solution.")


if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()

    print(f"Tempo de execução: {end_time - start_time} segundos")
"""Bin number 10
  Items packed: [37, 87, 90]
  Total weight: 150

Bin number 11
  Items packed: [20, 102, 109]
  Total weight: 150

Bin number 15
  Items packed: [16, 44, 111]
  Total weight: 150

Bin number 16
  Items packed: [49, 76, 103]
  Total weight: 150

Bin number 18
  Items packed: [15, 32, 116]
  Total weight: 150

Bin number 19
  Items packed: [21, 63, 105]
  Total weight: 150

Bin number 20
  Items packed: [38, 79, 91]
  Total weight: 150

Bin number 23
  Items packed: [73, 75, 97]
  Total weight: 148

Bin number 24
  Items packed: [47, 82, 119]
  Total weight: 150

Bin number 27
  Items packed: [2, 54, 106]
  Total weight: 150

Bin number 34
  Items packed: [29, 66, 114]
  Total weight: 150

Bin number 35
  Items packed: [10, 107]
  Total weight: 113

Bin number 40
  Items packed: [24, 41, 117]
  Total weight: 143

Bin number 41
  Items packed: [48, 86, 96]
  Total weight: 150

Bin number 44
  Items packed: [56, 72, 74]
  Total weight: 150

Bin number 45
  Items packed: [5, 46, 88]
  Total weight: 150

Bin number 49
  Items packed: [67, 68, 112]
  Total weight: 150

Bin number 50
  Items packed: [23, 81, 110]
  Total weight: 150

Bin number 56
  Items packed: [64, 92, 100]
  Total weight: 147

Bin number 57
  Items packed: [4, 28, 77]
  Total weight: 150

Bin number 58
  Items packed: [9, 13, 35]
  Total weight: 150

Bin number 59
  Items packed: [71, 78, 85]
  Total weight: 150

Bin number 61
  Items packed: [33, 60, 101]
  Total weight: 150

Bin number 62
  Items packed: [12, 27, 57]
  Total weight: 149

Bin number 66
  Items packed: [14, 45, 84]
  Total weight: 150

Bin number 67
  Items packed: [6, 19, 94]
  Total weight: 150

Bin number 69
  Items packed: [1, 61, 99]
  Total weight: 150

Bin number 71
  Items packed: [26, 53, 62]
  Total weight: 150

Bin number 73
  Items packed: [36, 65, 108]
  Total weight: 150

Bin number 74
  Items packed: [11, 70, 80]
  Total weight: 147

Bin number 75
  Items packed: [0, 89, 115]
  Total weight: 150

Bin number 80
  Items packed: [17, 43, 83]
  Total weight: 150

Bin number 81
  Items packed: [22, 95, 104]
  Total weight: 150

Bin number 84
  Items packed: [50, 113]
  Total weight: 117

Bin number 92
  Items packed: [8, 25, 58]
  Total weight: 148

Bin number 98
  Items packed: [30, 31, 59]
  Total weight: 150

Bin number 102
  Items packed: [18, 118]
  Total weight: 114

Bin number 103
  Items packed: [39, 42, 93]
  Total weight: 150

Bin number 111
  Items packed: [34, 51, 55]
  Total weight: 150

Bin number 113
  Items packed: [40, 52, 69]
  Total weight: 150

Bin number 115
  Items packed: [3, 7, 98]
  Total weight: 150


Number of bins used: 41
Time =  397748  milliseconds"""
