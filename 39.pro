cal_area(A,B,C) :- P is A + B + C , write('primeter is'),write(P).
triangle(A,A,A) :- write('Equilaterial triangle').
triangle(A,_,A) :- write('Equilaterial triangle').
triangle(_,A,A) :- write('Equilaterial triangle').
triangle(_,_,_) :-  write('Unequal triangle').
max_val(A,B,C) :- A >= B, A >= C , write('Max value '), write(A).
max_val(A,B,C) :- B >= A, B >= C , write('Max value '), write(B).
max_val(A,B,C) :- C >= B, C >= A , write('Max value '), write(C).
right_tra(_,B,C,P) :- V1 is A*A, V2 is B*B, V3 is C*C, V1 is V2+V3, A is P-B-C.
right_tra(A,B,C,P) :- V1 is A*A, V2 is B*B, V3 is C*C, V1 is V2+V3, P is A+B+C.
right_tra(A,B,C,P) :- V1 is A*A, V2 is B*B, V3 is C*C, V2 is V1+V3, P is A+B+C.
right_tra(A,B,C,P) :- V1 is A*A, V2 is B*B, V3 is C*C, V3 is V1+V2, P is A+B+C.
