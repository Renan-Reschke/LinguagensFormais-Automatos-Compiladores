% Definicao dos operadores
:-op(501, fy, ~).
:-op(502, yfx, &).
:-op(502, yfx, \/).
:-op(503, yfx, ==>).
:-op(504, yfx, <==>).

% Definicao de fbf's validas
fbf(true).
fbf(false).
fbf(a).
fbf(b).
fbf(c).
fbf(d).
fbf(e).
fbf(f).
fbf(g).
fbf(h).
fbf(i).
fbf(j).
fbf(k).
fbf(l).
fbf(m).
fbf(n).
fbf(o).
fbf(p).
fbf(q).
fbf(r).
fbf(s).
fbf(t).
fbf(u).
fbf(v).
fbf(w).
fbf(x).
fbf(y).
fbf(z).

% regras para especificar fbf's
fbf(~X):-
    fbf(X).

fbf(A&B):-
    fbf(A),
    fbf(B).

fbf(A\/B):-
    fbf(A),
    fbf(B).

fbf(A==>B):-
    fbf(A),
    fbf(B).

fbf(A<==>B):-
    fbf(A),
    fbf(B).

% Exemplos de fbf corretas:
% 1. a \/ b ==> c.
% 2. a & b & c.
% 3. (a ==> b) & a ==> b.
% 4. ~a \/ b <==> c.
% 5. (a ==> b) & (~a \/ c).

% Exemplos de fbf corretas:
% 1. a ~\/ b ==> c.
% 2. a & b & ==> c.
% 3. (a ==> b) & \/ a ==> b.
% 4. ~a & \/ b <==> c.
% 5. (a ==> b) & (~a ~ \/ c).