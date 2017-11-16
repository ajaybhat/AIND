# Overview of algorithms used in Planning

This document deals with various algorithms that are used in the field of AI planning.

### STRIPS
STRIPS (**S**tanford **R**esearch **I**nstitute **P**roblem **S**olver) is an automated planner, created by Fikes and Nilsson in 1971. The STRIPS algorithm is the prototype, whose representational structure has influenced what is known today as "classic planning".

A STRIPS instance is composed of:

* An initial state
* A set of goal states
* A set of actions, alongwith preconditions and postconditions for each action

A plan for such a planning instance is a sequence of operators that can be executed from the initial state and that leads to a goal state, similar to a formal automaton.
A prerequisite is that STRIPS cannot have negative literals.

### Planning Domain Definition Language (PDDL)

The PDDL is an extension of STRIPS, developed by McDermott in 1998. 
Planning tasks specified in PDDL are separated into two modules:
1. A _domain module_ for predicates and actions.
2. A _problem module_ for objects, initial state and goal specification.

Thus several problems may be connected to a single domain for planning, or a single domain can be used for various problem descriptions.

### GraphPlan

Graphplan is an algorithm planning based on STRIPS, developed by Blum and Furst in 1995.
GraphPlan uses a planning graph instead of a state-space search graph to reduce time required for searching for a path to a goal state.

* In a traditional state-space graph, the nodes are possible states and the edges of the search tree are used to indicate whether the goal state can be reached via some action.
* In a planning graph, the nodes are actions and atomic facts, arranged into alternate levels. The edges are of 2 kinds: one from an action to the atomic facts it makes true or false, and from atomic facts that represent boolean values of the conditions for actions.

### References
* Richard E. Fikes, Nils J. Nilsson (Winter 1971). "STRIPS: A New Approach to the Application of Theorem Proving to Problem Solving" (PDF). Artificial Intelligence. 2 (3–4): 189–208. 
* Fox, M.; Long, D. (2002). "PDDL+: Modeling continuous time dependent effects". Proceedings of the 3rd International NASA Workshop on Planning and Scheduling for Space.
* A. Blum and M. Furst (1997). Fast planning through planning graph analysis. Artificial intelligence. 90:281-300.