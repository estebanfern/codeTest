# 1. Balanced group symbols: 
Write a balancedGroupSymbols function that takes a string as input and returns a
boolean. The string argument containts group symbols that are well known for
mathematical operations, and consists of: Parentheses “()”, Brackets “[]” and Braces
“{}”.
If the group symbols in the input string are ‘well balanced’, then return true, else return
false.
For example, the program should produce:
> true for expression = “[()]{}{()()}”
>
> false for expression = “[(])”

# 2. Snail rearrangement:
Given an n x n array, return the array elements rearranged from outermost elements to
the middle element, traveling clockwise. Here’s an illustration for demonstration
purposes:
Given the previous array:
> [ [1,2,3], [4,5,6], [7,8,9] ] snail(array) should produce the output: [1,2,3,6,9,8,7,4,5]
