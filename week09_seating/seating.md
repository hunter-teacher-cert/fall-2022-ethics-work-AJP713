## Adam Prado
## Seating Algorithm
## Week 9 
## 11/1/22

## Seating Algorithm

### Overview/Goals
- The airline is a company and so charging money for passengers to pick their seats while not equitable still seems reasonable.  My algorihtm will attempt to not reduce revenue while maximizing as many people as possible to sit with their family/party.

### Algorithm
1) Set up the empty plane with the given number of rows, columns (seats)
2) Passengers that paid to select their seats (economy plus) are assigned seats on a first-come first-select basis.  If a seat that an EP passenger wants is taken, they will be given an opportunity to re-select for their 2nd choice.  And so on until they have selected a seat.  If they plane sells out with just EP then no economy seats will be sold.
3) Economy passengers will then be given the opportunity to buy seats, tickets will continue to be sold until the plan is full but seats will not be assigned until all tickets are sold (or soon before take-off)
5) The passengers that did not pay to select their seats (economy) will be assigned in order of party/family size.  Larger groups will be assigned seats first.
6) Starting with largest group, the algorithm will first attempt to put the entire party in the same row.  It will prioritze a row with the exact number of adjaent seats they need left.  For example if the party is size 4, it will prioritze finding a row with 4 adjacent empty seats.
7) If there is not a row with the exact number of seats left, it will then look to the row with the most available seats. Since it is grouping from largest to smallest group size there will not be a larger group that will need that row.
8) If there is not a row with enough adjacent seats available for the largest party then it will then attemp to place them in consecutive rows, first prioritzing pairs of rows with exactly the number of empty seats needed.  Ex. party of 5 would be split into 2 and 3 in consecutive rows with exactly 2 and 3 seats available.
9) If there are not consecutive rows with enough seats then it would attempt to seat them in rows that are as close as possible.
10) This would continue down through smaller and smaller groups until the plane was filled. 



Instructions


Design an algorithm that would seat people more equitably.
Write up a description of your algorithm and save it as week09_seating/seating.pdf (or week09_seating/seating.md). Make sure this description states how it should improve equity and also how it might affect other concerns.
NO CODE IS NEEDED OR EXPECTED HERE -- just a description -- but make a note of implementation issues that might make your algorithm more practical or more difficult to implement
In class next week you will share your ideas and algorithms and ultimately decide on what to recommend to the airlines.