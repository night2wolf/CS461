adjacent(A, B, List) :- nextto(A, B, List); nextto(B, A, List).
notAdjacent(A,B,List) :- not(adjacent(A,B,List)).

solve(Nationality,Pet) :-
length(Houses, 5),
% The Raiders fan owns a dog.
member(house(_,_,dog,_,raiders), Houses),
% The cat owner is English.
member(house(english,_,cat,_,_), Houses),
% The milk drinker is Canadian.
member(house(canadian,_,_,milk,_), Houses),
% The horse owner is Vietnamese. 
member(house(vietnamese,_,horse,_,_), Houses),
% The Ravens fan owns a hamster. 
member(house(_,_,hamster,_,ravens), Houses),
% The South African drinks tea.
member(house(southafrican,_,_,tea,_), Houses),
% The Canadian lives in the green house. 
member(house(canadian,green,_,_,_), Houses),
% The Chargers fan lives in the blue house. 
member(house(_,blue,_,_,chargers), Houses),
% The Broncos fan lives in the yellow house. 
member(house(_,yellow,_,_,broncos), Houses),
% The juice drinker lives in the yellow house.
member(house(_,yellow,_,juice,_), Houses),
% The red house is the home of the Ravens fan.
member(house(_,red,_,_,ravens), Houses),
% The coffee drinker owns a cat. 
member(house(_,_,cat,coffee,_), Houses),
% The resident of the white house is South African. 
member(house(southafrican,white,_,_,_), Houses),
% The blue house is on the near (left) end. 
nth1(1, Houses, house(_,blue,_,_,_)),
% The red house is adjacent to the far end. 
nth1(4, Houses, house(_,red,_,_,_)),
% The milk drinker lives at the far end of the street. 
nth1(5, Houses, house(_,_,_,milk,_)),
% The resident of the red house has a Vietnamese neighbor.
adjacent(house(_,red,_,_,_),house(vietnamese,_,_,_,_), Houses),
% The juice drinker lives next to the dog owner.
adjacent(house(_,_,_,juice,_),house(_,_,dog,_,_), Houses),
% The dog owner lives next to the blue house.
adjacent(house(_,_,dog,_,_),house(_,blue,_,_,_), Houses),
% The neighbor of the Raiders fan keeps a horse. 
adjacent(house(_,_,_,_,raiders),house(_,_,horse,_,_), Houses),
% The cat owner and the juice drinker are NOT neighbors.
% notAdjacent(house(_,_,cat,_,_),house(_,_,_,juice,_), Houses),
% there exists some colombian
member(house(colombian,_,_,_,_), Houses),
% there exists some lizard
member(house(_,_,lizard,_,_), Houses),
% there exists a water drinker
member(house(_,_,_,water,_), Houses),
% What nationality is the owner of the red house
member(house(Nationality,red,_,_,_), Houses),
% what pet does the Chiefs fan have?
member(house(_,_,Pet,_,chiefs), Houses).

write_item(details(Nationality,Color,Pet,Beverage,Team)) :-
    write('Nationality : '), write(Nationality), nl,
    write('Color : '), write(Color), nl,
    write('Pet: '), write(Pet), nl,
    write('Beverage: '), write(Beverage), nl,
    write('Team: '),write(Team), nl, nl.
