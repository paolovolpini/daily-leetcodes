## Problem
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.

Example 1:

Input: tokens = ["2","1","+","3","*"]\
Output: 9\
Explanation: ((2 + 1) * 3) = 9

Example 2:

Input: tokens = ["4","13","5","/","+"]\
Output: 6\
Explanation: (4 + (13 / 5)) = 6\

## Approach
The problem is very simple. Operations are applied when reading the operator. Thus we can use a stack to push the numbers. Then when we read an operator, we just pop two numbers, apply the operations and push the result in the stack. After every operation we will be left with one item in the stack, which is the result. 
