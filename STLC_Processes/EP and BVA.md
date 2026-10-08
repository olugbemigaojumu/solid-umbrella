### **Testing a Range of Valid Input**

**Context:** 
You are tasked with testing a function that determines the classification of students based on their scores. 
The function accepts an integer score between 0 and 100 (inclusive) and returns a string classification as follows:

- "Fail" for scores 0-49
- "Pass" for scores 50-69
- "Merit" for scores 70-89
- "Distinction" for scores 90-100

**Objective:** 
Design test cases using Equivalence Partitioning and Boundary Value Analysis.

### Assignments

1. **Identify and define equivalence classes for the input domain, and label them as valid or invalid.**
2. **Identify and define boundary values for the input domain, using the 2 boundary value analysis technique.**
3. **Based on task 1 and 2, which test cases can you design? How many?**




### **Finding the appropriate solution**

### **1. Identify and define equivalence classes for the input domain and label them as valid or invalid.**

1. Valid Equivalence Classes:
   EC1	- 0 to 49 - Fail
   EC2	- 50 to 69 - Pass
   EC3	- 70 to 89 - Merit
   EC4  - 90 to 100 - Distinction

2. Invalid Equivalence Classes (Reject or give an error):
   EC5	- score < 0 - Below Range
   EC6	- score > 100 - Above Range
   EC7	- Non-integer number - e.g. 49.5
   EC8  - Non-numeric value - e.g. "abc", null


### **Identify and define boundary values for the input domain, using the 2 boundary value analysis technique.**

There will be 10 boundary values: -1, 0, 49, 50, 69, 70, 89, 90, 100, 101

1. Boundary Values for Valid Inputs:
    - Range of valid values:  0, 49, 50, 69, 70, 89, 90, 100
    - Lower boundary value: 0 
    - Upper boundary value: 100
2. Boundary Values for Invalid Inputs:
    - Invalid boundary values: -1, 101
    - Just outside lower boundary: -1
    - Just outside upper boundary: 101
  

### **Based on task 1 and 2, which test cases can you design? How many?**

EQUIVALENCE CLASS:
| Test Case ID | Description | Input     | Expected Output |
| ------------ | ----------- | --------- | --------------- |
| EP1          | EC1         |  25       |      Fail       |
| EP2          | EC2         |  60       |      Pass       |
| EP3          | EC3         |  80       |      Merit      |
| EP4          | EC4         |  95       |   Distinction   |
| EP5          | EC5         | -10       |   Invalid Input |
| EP6          | EC6         | 150       |   Invalid Input |

BOUNDARY VALUE:
| Test Case ID  | Description             | Input     | Expected Output |
| ------------- | ----------------------- | --------- | --------------- |
| BVA1          | Just below Min          | -1        |   Invalid Input |
| BVA2          | Min of Fail             |  0        |      Fail       |
| BVA3          | Max of Fail             |  49       |      Fail       |
| BVA4          | Min of Pass             |  50       |      Pass       |
| BVA5          | Max of Pass             |  69       |      Pass       |
| BVA6          | Min of Merit            |  70       |      Merit      |
| BVA7          | Max of Merit            |  89       |      Merit      |
| BVA8          | Min of Distinction      |  90       |   Distinction   |
| BVA9          | Max of Distinction      | 100       |   Distinction   |
| BVA10         | Just above Distinction  | 101       |   Invalid Input |


For robustness, we can check for the Invalid EP values of 49.5, "abc", null.

We would then have 16 test cases in total or 19 if we add the robustness checks.
