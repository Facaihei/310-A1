# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    
    support_stack = util.Stack()
    start_state = problem.getStartState()
    visited = []
    support_stack.push([start_state, []])
    while True:
        if (support_stack.isEmpty() == True):
            break
        current = support_stack.pop()
        state, curr_actions = current[0], current[1]
        #print (state, state in visited)

        if (problem.isGoalState(state)):
            return curr_actions
        
        if (state in visited):
            continue
        else:
            visited.append(state)
            successor = problem.getSuccessors(state)
            #print ("successor", successor)
            for i in successor:
                successor_state = i[0]
                successor_action = i[1]
                #print ("successor state:", successor_state, successor_action)
                if (successor_state not in visited):
                    #visited.append(successor_state)
                    support_stack.push([successor_state, curr_actions + [successor_action]]) 
                      
    #util.raiseNotDefined()
def breadthFirstSearch(problem):
    support_stack = util.Queue()
    start_state = problem.getStartState()
    visited = []
    support_stack.push([start_state, []])
    while True:
        if (support_stack.isEmpty() == True):
            break
        current = support_stack.pop()
        state, curr_actions = current[0], current[1]
        #print (state, state in visited)

        if (problem.isGoalState(state)):
            return curr_actions
        
        if (state in visited):
            continue
        else:
            visited.append(state)
            successor = problem.getSuccessors(state)
            #print ("successor", successor)
            for i in successor:
                successor_state = i[0]
                successor_action = i[1]
                #print ("successor state:", successor_state, successor_action)
                if (successor_state not in visited):
                    #visited.append(successor_state)
                    support_stack.push([successor_state, curr_actions + [successor_action]]) 
    return curr_actions                
    '''
    fringe = util.Queue()
    visited = []
    fringe.push((problem.getStartState(), [], 1))
    while not fringe.isEmpty():
        node = fringe.pop()
        state = node[0]
        actions = node[1]
        if (problem.isGoalState(state)):
            return actions 
        if state not in visited:
            visited.append(state)
            successors = problem.getSuccessors(state)
            for child in successors:
                child_state = child[0]
                child_action = child[1]
                if child_state not in visited:
                    child_action = actions + [child_action]
                    fringe.push((child_state, child_action, 1))               
                    '''
def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    support_stack = util.PriorityQueue()
    start_state = problem.getStartState()
    visited = []
    support_stack.push([start_state, [], 0], 0)
    while True:
        if (support_stack.isEmpty() == True):
            break
        current = support_stack.pop()
        state, curr_actions, curr_cost = current[0], current[1], current[2]
        #print (state, state in visited)

        if (problem.isGoalState(state)):
            return curr_actions
        
        if (state in visited):
            continue
        else:
            visited.append(state)
            successor = problem.getSuccessors(state)
            #print ("successor", successor)
            for i in successor:
                successor_state = i[0]
                successor_action = i[1]
                successor_cost = i[2]
                #print ("successor state:", successor_state, successor_action)
                if (successor_state not in visited):
                    #visited.append(successor_state)
                    cost = successor_cost + curr_cost
                    support_stack.push([successor_state, curr_actions + [successor_action], cost], cost) 
    #util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    support_stack = util.PriorityQueue()
    start_state = problem.getStartState()
    visited = []
    support_stack.push([start_state, []], nullHeuristic(start_state, problem))

    while True:
        if (support_stack.isEmpty() == True):
            break
        current = support_stack.pop()
        state, curr_actions = current[0], current[1]
        #print (state, state in visited)

        if (problem.isGoalState(state)):
            return curr_actions
        
        if (state in visited):
            continue
        else:
            visited.append(state)
            successor = problem.getSuccessors(state)
            #print ("successor", successor)
            for i in successor:
                successor_state = i[0]
                successor_action = i[1]
                #print ("successor state:", successor_state, successor_action)
                if (successor_state not in visited):
                    #visited.append(successor_state)
                    curr_cost = problem.getCostOfActions(curr_actions + [successor_action])

                    support_stack.push([successor_state, curr_actions + [successor_action]], curr_cost) 
    #util.raiseNotDefined()

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
