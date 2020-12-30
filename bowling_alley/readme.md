# String Calculator Kata 

The aim is to create a scoring engine for 10-pin Bowling. In 10-pin bowling you have ten frames where you can roll one, two (or three) balls and score the pins that you knock down. Sounds simple right?

Except the scoring is weird. You’d think 10 pins and ten frames would yield a highest possible score of 100, but you’d be wrong. The lowest possible score (all misses) is zero, but the highest possible score is 300. For more information about 10-pin bowling scoring I suggest reading the Wikipedia page. But this is exactly why it is a fun system to model for our kata.

## Spec

1. Gutter game scores zero - When you roll all misses, you get a total score of zero.
2. All ones scores 20 - When you knock down one pin with each ball, your total score is 20.
3. A spare in the first frame, followed by three pins, followed by all misses scores 16.
4. A strike in the first frame, followed by three and then four pins, followed by all misses, scores 24.
5. A perfect game (12 strikes) scores 300.
