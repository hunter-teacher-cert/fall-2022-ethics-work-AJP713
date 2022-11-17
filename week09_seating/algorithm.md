## Adam Prado
## Seating Algorithm

## Java Script Code
- Here is a link to the code in a replit that runs easier (with the index, scipt files set up, not sure how to do with in the file tree).
https://replit.com/@ajprado/planeSeatingTest#script.js
- The code is also in plane_seating.py in this folder
- The code does the first part of the algorithm but I ran into problem with filling different size groups of passengers. 

Algorithm
 1) Create a plane with a given number of rows and columns accross.
 2) Determine a % of economy plus passengers that will purchase seats.
 3) Assign Econ Plus seats on either the first or last seat (0, length-1) of each row, which would be the window.  Starting at the front of the plane and going back.
 4) Create a list of regular (non Econ Plus) passenger groups, it is a list of list the first value is the name regular plus an index number, the 2nd value is a number representing the group size.  The size of the group is assigned a random integer from 1 to the maximum party size. This continues until the maximum number of seats on the plane are accounted for ex)  [[reg1,2],[reg2,3]...]
 5) There is a function that determines how many seats are available in each row.
 6) The list of regular passengers is then assigned seats starting with the largest group value.  It loops through assigning the largest groups first and then working down to smaller and smaller groups until it is individual passengers
- If there is a row with exactly the number of avialable seats as the largest unassigned group, then that group will be assigned that row.  The plane will be updated to show their names taking the consecutive seats.  This will look from the front of the plane to the back.
- If there is not a row with the exact number, then the code will look for a row with more available seats than needed.  If it find them it will take the first set of seats in a row with more seats available, updating the plane.
- Only if it can't find either a row with exact or more seats, will it spit the group into two smaller parts.  It will then look for two consective rows to put them in.
- This continues for all groups of passengers until the plane is full.
- At some point groups might be split into individuals to take the empty seats on the plane.  

    