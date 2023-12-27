'''
LC 134. Gas Station
Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, 
otherwise return -1. If there exists a solution, it is guaranteed to be unique.
'''
def canCompleteCircuit(gas, cost):
    deficit = 0
    balance = 0
    start = 0

    # check every index if it is the answer
    for i in range(len(gas)):
        balance += gas[i] - cost[i]
        if balance < 0:
            deficit += abs(balance)
            start = i+1
            balance = 0

    if balance - deficit >= 0:
        return start
    else:
        return -1




# Main
if __name__=='__main__': 
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    print('Result:',canCompleteCircuit(gas, cost))
    # [-5, -5, -1, -1, -2]