# SplitGame
Split card console game in Python

TO DOs:
- [ ] command --help print the game's instructions (at any point of the game)
- [x] command -- resume resumes the game
- [ ] the game asks 2 players for their names (name can consist of any characters, at least 1 character)
- [ ] 2 players can connect via internal network, python-request library, Flask
- [ ] implement Spit's logic
- [ ] show winner at the end (scores)
- [ ] Save score between rounds
- [x] print graphical cards onto screen
- [ ] Defect infinite loop when there are around 5 cards, some can be stacked onto 1 pile, then player is prompted to move card to an empty place
- [ ] User can choose to move a stack a duplicated card with 'y' , 'n'

TESTS use commands when:
- [ ] Game prompts for player's names
- [ ] Both users cannot move and they add cards to their spit piles
- [ ] User chooses a card
- [ ] User chooses a card to move to an empty spot
- [ ] User agrees to stack cards onto another 

Gameplay:
- [ ] Player can choose the card to be added to spit pile
- [ ] If card is repeated in their piles, the duplicate will be placed on the leftmost pile
- [ ] If the chosen cad can be put into 2 spit piles, the leftmost spit is chosen
- [ ] If the player cannot move a card, they lose their turn
- [ ] If both players cannot move a card, they both put any card to their spit piles
- [ ] Game automatically moves a duplicate card to the left pile to reveal another card. This is repeated until no more duplicate moving is possible
- [ ] If player has an empty pile, a card from right-most pile is moved to reveal another card. This is reperated till possible
- [ ] Player can choose a card to be moved onto an empty spot
