% Sudoku Solver
%
% Hints:
% For subgrid of size n, subgrids can be identified by labels 1..n*n
% A cell (x,y) can be mapped to the subgrid labeled 1+(((x-1)/n)*n+(y-1)/n)

% Your implementation please...

% Dimensions as valid numbers
row(1..9).
col(1..9).
num(1..9).

% Subgrid shenanigans
subgrid(X,Y,G) :- row(X), col(Y), G = (((X - 1)/3) * 3 + ((Y - 1)/3)+1).

% Each cell has exactly one number
1 { sudoku(X,Y,N) : num(N) } 1 :- row(X), col(Y).

% If a cell has an initial number, the solution must match
:- initial(X,Y,N), not sudoku(X,Y,N).

% No two different cells in the same row share a number
:- sudoku(X,Y1,N), sudoku(X,Y2,N), Y1 != Y2.

% Same but columns this time
:- sudoku(X1,Y,N), sudoku(X2,Y,N), X1 != X2.

% No two different cells can have the same number
:- sudoku(X1,Y1,N), sudoku(X2,Y2,N), X1 != X2, Y1 != Y2, subgrid(X1,Y1,G), subgrid(X2,Y2,G).

#show sudoku/3.