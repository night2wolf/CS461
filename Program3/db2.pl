nextTo(A,B,(B,A,_,_,_)).
nextTo(A,B,(_,B,A,_,_)).
nextTo(A,B,(_,_,B,A,_)).
nextTo(A,B,(_,_,_,B,A)).
nextTo(A,B,(A,B,_,_,_)).
nextTo(A,B,(_,A,B,_,_)).
nextTo(A,B,(_,_,A,B,_)).
nextTo(A,B,(_,_,_,A,B)).
exists(A,(A,_,_,_,_)).
exists(A,(_,A,_,_,_)).
exists(A,(_,_,A,_,_)).
exists(A,(_,_,_,A,_)).
exists(A,(_,_,_,_,A)).
notAdjacent(A,B,(A,_,B,_,_)).
notAdjacent(A,B,(A,_,_,B,_)).
notAdjacent(A,B,(A,_,_,_,B)).
notAdjacent(A,B,(B,_,A,_,_)).
notAdjacent(A,B,(B,_,_,A,_)).
notAdjacent(A,B,(B,_,_,_,A)).
notAdjacent(A,B,(_,A,_,B,_)).
notAdjacent(A,B,(_,A,_,_,B)).
notAdjacent(A,B,(_,_,A,_,B)).
notAdjacent(A,B,(_,B,_,A,_)).
notAdjacent(A,B,(_,B,_,_,A)).
notAdjacent(A,B,(_,_,B,_,A)).
firstHouse(A,(A,_,_,_,_)).
lastHouse(A,(_,_,_,_,A)).
adjacentLast(A,(_,_,_,A,_)).
solution(n,c,p,d,t) :- Houses =
    (house(nationality1, color1, pet1, drink1, team1),
    house(nationality2, color2, pet2, drink2, team2),
    house(nationality3, color3, pet3, drink3, team3),
    house(nationality4, color4, pet4, drink4, team4),
    house(nationality5, color5, pet5, drink5, team5)),
% The Raiders fan owns a dog.
exists(house(_,_,dog,_,raiders), Houses),
% The cat owner is English.
exists(house(english,_,cat,_,_), Houses),
% The milk drinker is Canadian.
exists(house(canadian,_,_,milk,_), Houses),
% The horse owner is Vietnamese. 
exists(house(vietnamese,_,horse,_,_), Houses),
% The Ravens fan owns a hamster. 
exists(house(_,_,hamster,_,ravens), Houses),
% The South African drinks tea.
exists(house(southafrican,_,_,tea,_), Houses),
% The Canadian lives in the green house. 
exists(house(canadian,green,_,_,_), Houses),
% The Chargers fan lives in the blue house. 
exists(house(_,blue,_,_,chargers), Houses),
% The Broncos fan lives in the yellow house. 
exists(house(_,yellow,_,_,broncos), Houses),
% The juice drinker lives in the yellow house.
exists(house(_,yellow,_,juice,_), Houses),
% The red house is the home of the Ravens fan.
exists(house(_,red,_,_,ravens), Houses),
% The coffee drinker owns a cat. 
exists(house(_,_,cat,coffee,_), Houses),
% The resident of the white house is South African. 
exists(house(southafrican,white,_,_,_), Houses),
% The blue house is on the near (left) end. 
firstHouse(house(_,blue,_,_,_), Houses),
% The red house is adjacent to the far end. 
adjacentLast(house(_,red,_,_,_), Houses),
% The milk drinker lives at the far end of the street. 
lastHouse(house(_,_,_,milk,_), Houses),
% The resident of the red house has a Vietnamese neighbor.
nextTo(house(_,red,_,_,_),house(vietnamese,_,_,_,_), Houses),
% The juice drinker lives next to the dog owner.
nextTo(house(_,_,_,juice,_),house(_,_,dog,_,_), Houses),
% The dog owner lives next to the blue house.
nextTo(house(_,blue,_,_,_),house(_,_,dog,_,_), Houses),
% The neighbor of the Raiders fan keeps a horse. 
nextTo(house(_,_,_,_,raiders),house(_,_,horse,_,_), Houses),
% The cat owner and the juice drinker are NOT neighbors.
notAdjacent(house(_,_,cat,_,_),house(_,_,_,juice,_), Houses).

