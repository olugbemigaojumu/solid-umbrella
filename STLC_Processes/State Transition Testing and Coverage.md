## State Transition Testing

**The scenario involves an ATM machine. To use this machine, the user needs to enter their pin code.**

The user first sees the start screen, then the ‘wait for pin’ screen. Then there are 3 tries possible, if the pin code is correct, the user has access to the account. If the user exceeds the amount of max tries, the card will be eaten.

**Assignment:**

1. Determine the states, transitions and events
2. Create the state transition table and state transition diagram




### **Let's determine an appropriate solution for this.

Given the ATM Machine Scenario above, we can determing the following states, events and transitions:
  
  STATES
  - Start screen (Idle, waiting for card)    ->  S1
  - Wait for PIN (1st try - Card inserted, first PIN attempt)    ->  S2
  - Wait for PIN (2nd try - First wrong PIN entered)    ->  S3
  - Wait for PIN (3rd try - Second wrong PIN entered)    ->  S4
  - Access granted (Correct PIN enetered)    ->  S5
  - Card eaten (3 Wrong PINS entered)    ->  S6

  EVENTS
  - Card inserted     ->  E1
  - Correct PIN entered    ->  E2
  - Wrong PIN entered    ->  E3

  TRANSIITONS
  - Start screen    ->     Show "Enter PIN" screen
  - Wait for PIN    ->     Correct PIN entered           ->        Grant access
  - Wait for PIN    ->     Incorrect PIN entered         ->        Show "Wrong PIN, 2 tries left"
  - Wait for PIN    ->     Correct PIN entered           ->        Grant access
  - Wait for PIN    ->     Incorrect PIN entered         ->        Show "Wrong PIN, 1 try left"
  - Wait for PIN    ->     Correct PIN entered           ->        Grant access
  - Wait for PIN    ->     Incorrect PIN entered         ->        Eat the card. Display message to user.


Let's make the state transitions into a table:

|   FROM   |   EVENT   |    TO    |        ACTION/OUTPUT                |
|   S1     |   E1      |    S2    |    Show "Enter PIN" screen          |
|   S2     |   E2      |    S5    |    Grant access                     |
|   S1     |   E1      |    S2    |    Show "Wrong PIN, 2 tries left"   |
|   S1     |   E1      |    S2    |    Grant access                     |
|   S1     |   E1      |    S2    |    Show "Wrong PIN, 1 try left"     |
|   S1     |   E1      |    S2    |    Grant access                     |
|   S1     |   E1      |    S2    |    Eat the card                     |


Let's attempt to draw the state transition diagram:

  STATE TRANSITION DIAGRAM

<img width="710" height="738" alt="image" src="https://github.com/user-attachments/assets/245c4d0b-3ce3-4634-b163-b0ebf321fc14" />
