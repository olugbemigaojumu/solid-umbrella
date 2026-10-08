**Scenario Details:**

**The scenario involves a train ticket system with various discounts.**

- The conditions for applying a discount are:
    1. The passenger is a senior citizen (age 65 or older): 20% discount
    2. The passenger is a student: 15% discount
    3. The passenger is traveling during off-peak hours: 10% discount
    4. The passenger has a frequent traveler card: 5% discount
- Discounts can be combined, and the total discount is the sum of all applicable discounts.

**Assignment:** Create a decision table to test the discount application logic for a train ticket system. Your task is to:

1. Identify all the conditions that affect the discount application.
2. Identify the discount percentage for each condition.
3. Construct a decision table with all possible combinations of conditions.
4. Calculate the total discount for each combination based on the conditions met.



### **Finding an appropriate solution**

1. Identify all the conditions that affect the discount application.

   ### **We are considering the scenario which involves a train ticket system with various discounts. The conditions are:**
    a. The passenger is a senior citizen (age 65 or older)? Yes/No
    b. The passenger is a student? Yes/No
    c. The passenger is traveling during off-peak hours? Yes/No
    d. The passenger has a frequent traveler card? Yes/No

   With 4 binary conditions, there are 2⁴ = 16 combinations.
   

2. Identify the discount percentage for each condition.
    a. The passenger is a senior citizen (age 65 or older)?            - 20% DISCOUNT APPLIED
    b. The passenger is a student?                                     - 15% DISCOUNT APPLIED
    c. The passenger is traveling during off-peak hours?               - 10% DISCOUNT APPLIED
    d. The passenger has a frequent traveler card?                     -  5% DISCOUNT APPLIED
   
  Total discount = sum of the discounts If all conditions are true. The maximum possible is 20 + 15 + 10 + 5 = 50%.


3. Construct a decision table with all possible combinations of conditions. Total discounts are calculated below the table
   
   | Condition      | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | R15 | R16 |
   | -------------- |----|----|----|----|----|----|----|----|----|-----|-----|-----|-----|-----|-----|-----|
   | Senior         | NO | NO | NO | NO | NO | NO | NO | NO |YES | YES | YES | YES | YES | YES | YES | YES |
   | Student        | NO | NO | NO | NO |YES |YES |YES |YES | NO | NO  | NO  | NO  | YES | YES | YES | YES |
   | Off-Peak       | NO | NO |YES |YES | NO | NO |YES |YES | NO | NO  | YES | YES | NO  | NO  | YES | YES |
   | Bahn Card      | NO |YES | NO |YES | NO |YES | NO |YES | NO | YES | NO  | YES | NO  | YES | NO  | YES |
   | Total Discount | 0% | 5% |10% |15% |15% |20% |25% |30% |20% | 25% | 30% | 35% | 35% | 40% | 45% | 50% |

   Each rule becomes one test case, so we get 16 test cases if we were to write test cases for this.
  
