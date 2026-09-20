#search
import state
import frontier

def search(s):
    # s = state.create(n)
    # print(s)
    f = frontier.create(s)
    count = 0
    while not frontier.is_empty(f):
        s = frontier.remove(f)
        count += 1 
        if state.is_target(s):
            return [f[1], count, state.path_len(s)]
        ns = state.get_next(s)
        for i in ns:
            frontier.insert(f,i)
            if f[1] > 1500:
                return [1500, count, 100]
    return 0

# totalPushed = 0
# totalPoped = 0
# totalLength=0
# maxPushed = 0
# maxPoped = 0
# maxLength = 0
# failures = 0
# for i in range(100):
#     pushed, poped, length = search(3)
#     totalPushed+=pushed
#     totalPoped+=poped
#     totalLength+=length
#     maxPushed = max(maxPushed, pushed)
#     maxPoped = max(maxPoped, poped)
#     maxLength = max(maxLength, length)
#     if length == 100:
#         failures += 1
# print("Total number of independent runs:", 100)
# print("Average pushed:", totalPushed / 100)
# print("Average popped:", totalPoped / 100)
# print("Average path cost:", totalLength / 100)
# print("Max total items pushed:", maxPushed)
# print("Max total items checked:", maxPoped)
# print("Max path cost of solution:", maxLength)
# print("Failure percentage:", failures / 100 * 100)

# search(3) with hdistance set to 0

# Total number of independent runs: 100
# Average pushed: 362.06
# Average popped: 208.69
# Average path cost: 12.44
# Max total items pushed: 1500
# Max total items checked: 883
# Max path cost of solution: 100

# search(3) with hdistance1

# Total number of independent runs: 100
# Average pushed: 62.98
# Average popped: 37.24
# Average path cost: 6.87
# Max total items pushed: 1500
# Max total items checked: 892
# Max path cost of solution: 100
# Failure percentage: 1.0

# search(3) with hdistance2

# Total number of independent runs: 100
# Average pushed: 24.3
# Average popped: 14.05
# Average path cost: 6.52
# Max total items pushed: 131
# Max total items checked: 77
# Max path cost of solution: 14
# Failure percentage: 0.0

# search(3) with 4hdistance2 and hdistance1

# Total number of independent runs: 100
# Average pushed: 24.48
# Average popped: 14.28
# Average path cost: 5.95
# Max total items pushed: 349
# Max total items checked: 209
# Max path cost of solution: 22
# Failure percentage: 0.0

# search(3) with hdistance3
# Total number of independent runs: 100
# Average pushed: 21.58
# Average popped: 12.55
# Average path cost: 6.09
# Max total items pushed: 151
# Max total items checked: 91
# Max path cost of solution: 14
# Failure percentage: 0.0

boards = []
for i in range(100):
    boards.append(state.create(5))

def doHeuristic(boards):
    totalPushed = 0
    totalPoped = 0
    totalLength=0
    maxPushed = 0
    maxPoped = 0
    maxLength = 0
    failures = 0
    for i in boards:
        pushed, poped, length = search(i)
        totalPushed+=pushed
        totalPoped+=poped
        totalLength+=length
        maxPushed = max(maxPushed, pushed)
        maxPoped = max(maxPoped, poped)
        maxLength = max(maxLength, length)
        if length == 100:
            failures += 1
    print("Total number of independent runs:", 100)
    print("Average pushed:", totalPushed / 100)
    print("Average popped:", totalPoped / 100)
    print("Average path cost:", totalLength / 100)
    print("Max total items pushed:", maxPushed)
    print("Max total items checked:", maxPoped)
    print("Max path cost of solution:", maxLength)
    print("Failure percentage:", failures / 100 * 100)
    print()
# print("Uniform\n")
# frontier.heuristic = "Uniform"
# doHeuristic(boards)
# print("Greedy\n")
# frontier.heuristic = "Greedy"
# doHeuristic(boards)
# print("Tiles\n")
# frontier.heuristic = "Tiles"
# doHeuristic(boards)
# print("Manhattan\n")
# frontier.heuristic = "Manhattan"
# doHeuristic(boards)
# print("Weighted\n")
# frontier.heuristic = "Weighted"
# doHeuristic(boards)
# print("Linear\n")
# frontier.heuristic = "Linear"
# doHeuristic(boards)

# print("Linear\n")

# Table for 3x3

# Heuristic    Pushed_(Ave)   Popped_(Ave)   Pushed_(Max)   Popped_(Max)   Path_Cost   Failure%
# Uniform      338.18         196.40         1500           883            11.28       6.0
# Greedy       114.49         66.86          1500           903            14.07       5.0
# Tiles        34.94          20.25          701            413            6.00        0.0
# Manhattan    21.04          12.14          229            133            6.00        0.0
# Weighted     23.16          13.31          345            198            6.12        0.0
# Linear_Con   19.14          11.00          85             50             6.00        0.0

# table for 4x4

# Heuristic    Pushed_(Ave)   Popped_(Ave)   Pushed_(Max)   Popped_(Max)   Path_Cost   Failure%
# Uniform      1440.89        674.82         1500           707            93.44       93.0
# Greedy       854.97         427.24         1500           784            63.87       48.0
# Tiles        868.05         412.79         1500           737            52.71       46.0
# Manhattan    524.69         260.60         1500           764            30.17       18.0
# Weighted     657.71         328.60         1500           773            42.79       30.0
# Linear_Con   412.52         203.77         1500           758            25.62       12.0

# table for 5x5
#
# Heuristic    Pushed_(Ave)   Popped_(Ave)   Pushed_(Max)   Popped_(Max)   Path_Cost   Failure%
# Manhattan    1343.23        632.41         1500           746            87.92       85.0
# Linear_Con   1287.83        603.95         1500           743            82.80       78.0

# Anwsers to question A and B
# A - it is not admissible because when we multiply the Manhattan distance by 4 it can overestimate the actual cost it takes to reach the desired output.

# frontier.heuristic = "Manhattan"
# doHeuristic(boards)

# B - 
# Manhattan distance + linear conflicts is admissible.
# Manhattan distance + 2 * linear conflicts is admissible.
# Manhattan distance + 4 * linear conflicts is not admissible.
# the 1 * linear conflicts version worked best. It had a 90% failure rate, compared with 100% for both the 2x and 4x