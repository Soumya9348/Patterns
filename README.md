# Patterns

Patterns can be printed in python using simple for loops. First outer loop is used to handle number of rows and Inner nested loop is used to handle the number of columns. Manipulating the print statements, different number patterns, alphabet patterns or star patterns can be printed. 


Steps for printing patterns

1. Decide the number of rows and columns
    There is a typical structure to print any pattern, i.e., the number of rows and columns. We need to use two loops to print any pattern, i.e., use nested loops.

    The outer loop tells us the number of rows, and the inner loop tells us the column needed to print the pattern.

    Accept the number of rows from a user using the input() function to decide the size of a pattern.

2. Iterate rows
    Next, write an outer loop to Iterate the number of rows using a for loop and range() function.

3. Iterate columns
    Next, write the inner loop or nested loop to handle the number of columns. The internal loop iteration depends on the values of the outer loop.

4. Print star or number
    Use the print() function in each iteration of nested for loop to display the symbol or number of a pattern (like a star (asterisk *) or number).

5. Add new line after each iteration of outer loop
    Add a new line using the print() function after each iteration of the outer loop so that the pattern display appropriately
