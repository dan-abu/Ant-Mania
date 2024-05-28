WELCOME TO ANT MANIA!

I have written Python code to solve the Ant Mania challenge.
You will find the brief and the code in this folder.
Below, I have listed the assumptions I have made in my design and some considerations on style.

Enjoy the ant invasion!

Assumptions
- If there are multiple ants on one colony when ants are first assigned to that colony, it should not trigger a fight and the destruction of the colony. This will happen with any subsequent clashes.
- The destruction of a colony leads to other ants on that colony getting trapped and removed from the list of ants available for the invasion. As a result, they no longer contribute to the move count.
- The only command line argument used to generate instances of the colony class will be the txt files in the folder.
- The command line argument of N number of ants will be a positive integer with no comma separation (e.g. 2024 not 2,024)

Style considerations
- I have used Python's classes to model the world of Hiveum. Given this was a complex quasi-real-world problem, I did this to create an easier-to-follow solution, to reuse code and avoid repetition.

- At times, I have printed large string blocks stylised in a similar way to the "Welcome to Ant Mafia!" title at the top of this document. My key reason for doing this was to improve the user experience and I believe this is done in two ways: firstly, by adding some aesthetically pleasing elements to the output; and lastly, by clearly signalling to the user when the programme begins and finishes.

- My final style consideration neatly ties in with why there are two version of the programme in this folder. This is the case because one version uses the sleep() function from Python's built-in time module to briefly delay the programme's execution. This builds suspense for the user as they wait to find out what's happened next in the invasion. I have created a script with the sleep() function and one without it because this feature works well with a small number of ants (e.g. around 20), but severely slows down the programme if the user opts for a larger number of ants (e.g. 8000) and the medium-sized map.
