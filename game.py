from operator import add, neg
import numpy as np

def solveGame(payoff_matrix, iterations=1000):
    """
    Return the oddments (mixed strategy ratios) for a given payoff matrix
    payoff_matrix = list of lists

    Returns (rowcnt, colcnt, value_of_game)
    - divide rowcnt, colcnt by iterations to get probabilities
    """
    transpose = list(zip(*payoff_matrix))
    numrows = len(payoff_matrix)
    numcols = len(transpose)

    # Create two payoff arrays
    row_cum_payoff = [0] * numrows
    col_cum_payoff = [0] * numcols

    colpos = range(numcols)
    rowpos = list(map(neg, range(numrows)))
    colcnt = [0] * numcols
    rowcnt =[0.0] * numrows
    derp = [0]
    for _ in range(iterations):
        col_cum_payoff = list(map(add, payoff_matrix[derp[0]], col_cum_payoff))
        tempMin=list(zip(col_cum_payoff, colpos))


        min_v = min(tempMin)[0]
        derp = list(np.where(np.asarray(tempMin) == min_v)[0])
        discount = 1 / len(derp)
        for i in derp:
            colcnt[i] += discount


        row_cum_payoff = list(map(add, transpose[derp[0]], row_cum_payoff))
        tempMax = list(zip(row_cum_payoff, rowpos))
        max_v = max(tempMax)[0]
        derp = list(np.where(np.asarray(tempMax) == max_v)[0])
        discount=1/len(derp)
        for i in derp :
            rowcnt[i]+= discount



       # rowcnt = [rowcnt[i] + discount for i in derp]

    value_of_game = (max(row_cum_payoff) + min(col_cum_payoff)) / 2.0 / iterations

    row_weights = [float(row) / iterations for row in rowcnt]
    col_weights = [float(col) / iterations for col in colcnt]
    return row_weights, col_weights, value_of_game

#A = [[10,5],[10,5],[10,5],[10,5],[10,5]]
#A = np.random.rand(1024,1024)
#print(solveGame(A))

