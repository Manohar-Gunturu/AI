# AI
Python AI Game
Done:
Two possible winners detection
we are cheking either dots or colors - it seems like we have to check both. 
because while playing player 1 player 2 can win.

TODO:different tests

big check:
0 8 c 1
0 2 c 3
0 3 a 1
0 1 g 1
0 3 g 2
0 8 f 2
0 1 f 1
0 8 f 1
0 7 d 1
0 6 e 5
0 6 e 1
0 6 e 2
0 1 d 4
0 2 e 3
0 2 e 4
 
0 8 f 3 --> not detecting diagnol
 
0 2 c 5
0 2 c 6
0 2 c 7
0 2 c 9
0 2 b 2
0 5 b 4
0 4 b 4
0 4 b 6
0 6 b 8
0 1 c 11
0 2 a 2
0 4 a 4
0 8 a 6
0 5 a 8
0 8 a 8
0 5 a 10
0 7 b 11
0 4 a 11
0 3 b 12
  
  
a 1 b 1 2 a 1
 
c 3 c 4 8 c 3 
c 1 c 2 4 c 1
c 3 c 4 4 c 3
 
a 1 a 1 2 g 2



check
0 6 a 1
0 5 e 1
0 6 d 1
0 2 c 1
0 6 e 2
0 3 b 1 <- bug here
0 2 f 2
 


check imp:
0 5 c 1
0 4 e 1
0 4 f 1
0 4 g 1
 
check:
0 1 a 1
0 3 c 1
0 3 e 1
0 3 c 2
0 8 d 3
0 6 e 2
0 8 e 4

check2:
0 1 a 1
0 3 c 1
0 3 c 2
0 1 a 2
0 1 b 3
0 7 b 4

check3:
0 3 A 1
0 7 C 1
0 4 E 1
0 5 C 2
0 1 C 2
0 4 F 1
0 8 G 2
0 7 G 1
0 8 G 2
0 8 H 2

check4:
0 3 A 1
0 7 C 1
0 4 E 1
0 5 C 2
C3 C4 1 C3

wrong:
0 3 D 2
0 3 C 1
0 3 C 2
