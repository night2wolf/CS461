% reference material:
% https://baptiste-wicht.com/posts/2010/09/solve-einsteins-riddle-using-prolog.html
house(0, []) :- !.
house(N, [(_house_number,_color,_nationality,_pet,_beverage,_team)|T]) :- N1 is N-1, house(N1,T).
house_number([1,2,3,4,5]).
color(blue).
color(green).
color(red).
color(white).
color(yellow).
nationality(canadian).
nationality(colombian).
nationality(english).
nationality(southafrican).
nationality(vietnamese).
pet(dog).
pet(cat).
pet(hamster).
pet(horse).
pet(lizard).
beverage(coffee).
beverage(juice).
beverage(milk).
beverage(tea).
beverage(water).
team(broncos).
team(chargers).
team(chiefs).
team(raiders).
team(ravens).
% (_house_number,_color,_nationality,_pet,_beverage,_team)
% The Raiders fan owns a dog.
clue1([(_,_,_,dog,_,raiders)|_]).
clue1([_|T]) :- clue1(T).

nationality(english) :- pet(cat).
nationality(vietnamese) :- pet(horse).
team(ravens) :- pet(hamster).
nationality(canadian) :- beverage(milk).
nationality(southafrican) :- beverage(tea).
team(chargers) :- color(blue).
nationality(canadian) :- color(green).
team(broncos) :- color(yellow).
beverage(juice) :- color(yellow).
color(red) :- team(ravens).
beverage(coffee) :- pet(cat).
color(white) :- nationality(southafrican).
house_number([1]) :- color(blue).
house_number([4]) :- color(red).
house_number([5]) :- beverage(milk).