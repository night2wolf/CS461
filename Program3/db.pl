% reference material:
% https://baptiste-wicht.com/posts/2010/09/solve-einsteins-riddle-using-prolog.html
% https://stackoverflow.com/questions/9252656/einsteins-riddle-prolog 
houses(0, []) :- !.
houses(N, [(Color,Nationality,Pet,Beverage,Team)|T]) :- N1 is N-1, houses(N1,T).
house(1, [H|_], H) :- !.
house(N, [_|T], R) :- N1 is N-1, house(N1, T, R).
color([blue,green,red,white,yellow]).
nationality([canadian,colombian,english,southafrican,vietnamese]).
pet([dog,cat,hamster,horse,lizard]).
beverage([coffee,juice,milk,tea,water]).
team([broncos,chargers,chiefs,raiders,ravens]).
% (color,nationality,pet,beverage,team)
% The Raiders fan owns a dog.
clue1([(_,_,dog,_,raiders)|_]).
clue1([_|T]) :- clue1(T).
% The cat owner is English.
clue2([(_,english,cat,_,_)|_]).
clue2([_|T]) :- clue2(T).
% The milk drinker is Canadian.
clue3([(_,canadian,_,milk,_)|_]).
clue3([_|T]) :- clue3(T).
% The horse owner is Vietnamese. 
clue4([(_,vietnamese,horse,_,_)|_]).
clue4([_|T]) :- clue4(T).
% The Ravens fan owns a hamster. 
clue5([(_,_,hamster,_,ravens)|_]).
clue5([_|T]) :- clue5(T).
% The South African drinks tea.
clue6([(_,southafrican,_,tea,_)|_]).
clue6([_|T]) :- clue6(T).
% The Canadian lives in the green house. 
clue7([(green,canadian,_,_,_)|_]).
clue7([_|T]) :- clue7(T).
% The Chargers fan lives in the blue house. 
clue8([(blue,_,_,_,chargers)|_]).
clue8([_|T]) :- clue8(T).
% The Broncos fan lives in the yellow house. 
clue9([(yellow,_,_,_,broncos)|_]).
clue9([_|T]) :- clue9(T).
% The juice drinker lives in the yellow house.
clue10([(yellow,_,_,juice,_)|_]).
clue10([_|T]) :- clue10(T).
% The red house is the home of the Ravens fan.
clue11([(red,_,_,_,ravens)|_]).
clue11([_|T]) :- clue11(T).
% The coffee drinker owns a cat. 
clue12([(_,_,cat,coffee,_)|_]).
clue12([_|T]) :- clue12(T).
% The resident of the white house is South African. 
clue13([(white,southafrican,_,_,_)|_]).
clue13([_|T]) :- clue13(T).
% The blue house is on the near (left) end. 
clue14(Houses) :- house(1, Houses, (blue,_,_,_,_)).
% The red house is adjacent to the far end. 
clue15(Houses) :- house(4, Houses,(red,_,_,_,_)).
% The milk drinker lives at the far end of the street. 
clue16(Houses) :- house(5,Houses,(_,_,_,milk,_)).
% The resident of the red house has a Vietnamese neighbor.
clue17([(red,_,_,_,_),(_,vietnamese,_,_,_)|_]).
clue17([(_,vietnamese,_,_,_),(red,_,_,_,_)|_]).
clue17([_|T]) :- clue17(T).
% The juice drinker lives next to the dog owner.
clue18([(_,_,_,juice,_),(_,_,dog,_,_)|_]).
clue18([(_,_,dog,_,_),(_,_,_,juice,_)|_]).
clue18([_|T]) :- clue18(T).
% The dog owner lives next to the blue house.
clue19([(blue,_,_,_,_),(_,_,dog,_,_)|_]).
clue19([(_,_,dog,_,_),(blue,_,_,_,_)|_]).
clue19([_|T]) :- clue19(T).
% The neighbor of the Raiders fan keeps a horse. 
clue20([(_,_,_,_,raiders),(_,_,horse,_,_)|_]).
clue20([(_,_,horse,_,_),(_,_,_,_,raiders)|_]).
clue20([_|T]) :- clue20(T).
% The cat owner and the juice drinker are NOT neighbors.
%clue21([(_,_,_,juice,_), (_,_,cat,_,_)|_]).
%clue21([(_,_,cat,_,_), (_,_,_,juice,_)|_]).
%clue21([_|T]) :- \+ clue21(T).
% a lizard exists
clue22([(_,_,lizard,_,_)|_]).
clue22([_|T]) :- clue22(T).
% a colombian exists
clue23([(_,colombian,_,_,_)|_]).
clue23([_|T]) :- clue23(T).
% a water drinker exists
clue24([(_,_,_,water,_)|_]).
clue24([_|T]) :- clue24(T).
% What nationality is the owner of the red house?
problem1([(red,_,_,_,_)|_]).
problem1([_|T]) :- problem1(T).
% what pet does the Chiefs fan have?
problem2([(_,_,_,_,chiefs)|_]).
problem2([_|T]) :- problem2(T).


solution(Houses) :- 
houses(5,Houses),
clue1(Houses),
clue2(Houses),
clue3(Houses),
clue4(Houses),
clue5(Houses),
clue6(Houses),
clue7(Houses),
clue8(Houses),
clue9(Houses),
clue10(Houses),
clue11(Houses),
clue12(Houses),
clue13(Houses),
clue14(Houses),
clue15(Houses),
clue16(Houses),
clue17(Houses),
clue18(Houses),
clue19(Houses),
clue20(Houses),
% clue21(Houses),
clue22(Houses),
clue23(Houses),
clue24(Houses),
problem1(Houses),
problem2(Houses).


