## State Transition Testing

**The scenario involves an ATM machine. To use this machine, the user needs to enter their pin code.**

The user first sees the start screen, then the ‘wait for pin’ screen. Then there are 3 tries possible, if the pin code is correct, the user has access to the account. If the user exceeds the amount of max tries, the card will be eaten.

**Assignment:**

1. Determine the states, transitions and events
2. Create the state transition table and state transition diagram




### **Let's determine an appropriate solution for this.

Given the ATM Machine Scenario above, we can determing the following states, events and transitions:
  
  STATES
  - Start screen (Idle, waiting for card)
  - Wait for PIN (1st try - Card inserted, first PIN attempt)
  - Wait for PIN (2nd try - First wrong PIN entered)
  - Wait for PIN (3rd try - Second wrong PIN entered)
  - Access granted (Correct PIN enetered)
  - Card eaten (3 Wrong PINS entered)

  EVENTS
  - Card inserted
  - Correct PIN entered
  - Wrong PIN entered

  TRANSIITONS
  - Start screen    ->     Show "Enter PIN" screen
  - Wait for PIN    ->     Correct PIN entered           ->        Grant access
  - Wait for PIN    ->     Incorrect PIN entered         ->        Show "Wrong PIN, 2 tries left"
  - Wait for PIN    ->     Correct PIN entered           ->        Grant access
  - Wait for PIN    ->     Incorrect PIN entered         ->        Show "Wrong PIN, 1 try left"
  - Wait for PIN    ->     Correct PIN entered           ->        Grant access
  - Wait for PIN    ->     Incorrect PIN entered         ->        Eat the card. Display message to user.


Let's attempt to draw the state transition diagram:

  STATE TRANSITION DIAGRAM

<img width="710" height="738" alt="image" src="https://github.com/user-attachments/assets/245c4d0b-3ce3-4634-b163-b0ebf321fc14" />
