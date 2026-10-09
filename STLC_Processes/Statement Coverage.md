## **Coverage**

As long as a customer spends more than 50€, shipping should be free. If it is more than 25€ but less than 3 items need to be shipped, it should also be free. If there is only one item which costs more than 10€, there should be a discount, but it should not be free. In other cases, full price shipping should be paid.

```python
def is_shipping_free(price, numberOfItems, isPrimeShoppingMember):
    print("Additional Statement 1")
    if price > 50 or isPrimeShoppingMember:
        print("Additional Statement 2")
    if price > 25 and numberOfItems <3:
        print("Additional Statement 3")
    elif price > 10 and numberOfItems == 1 :
        print("Additional Statement 4(discount)")
        return False
    return True
    print("Additional Statement 5")
```

Do the following test cases cover fully cover the code?

  ```python
  print("----------------")
  is_shipping_free(30,2,True)
  print("----------------")
  is_shipping_free(15,1,False)
  print("----------------")
  is_shipping_free(15,1,True)
  print("----------------")
  is_shipping_free(50,1,False)
```

1. Draw a (directed acyclic graph) - State Transition Diagram for this code section
2. Calculate Statement Coverage and Branch Coverage
3. Calculate Statement Coverage and Branch Coverage, if the line print(”Additional Statement 5”) is deleted from Code.


## **Let's determine an appropriate solution for this.**

To answer the first question, the test set does not fully cover the code, as the tests written may probably satisfy the statement coverage but does not at all satisfy the branch coverage. Also, a part of the code is unreachable, and there is no test that covers this.
Let us calculate the coverages to determine the proper results.


## 1. Let's draw a directed acyclic graph showing the state transition diagram for this code section:

<img width="896" height="743" alt="image" src="https://github.com/user-attachments/assets/01beffbc-9b93-40e0-b45a-63131e5237f8" />

## 2. STATEMENT COVERAGE AND BRANCH COVERAGE CALCULATION

### STATEMENT COVERAGE:

For the 4 test cases:

**Case 1:** `is_shipping_free(30,2,True)`
- The path is State A -> State B -> State C -> State D -> State E -> State I (State F not reached)
- The Result will be True

---

**Case 2:** `is_shipping_free(15,1,False)`
- The path is State A -> State B -> State D -> State F -> State G -> State H
- The Result will be False

---

**Case 3:** `is_shipping_free(15,1,True)`
- The path is State A -> State B -> State C -> State D -> State F -> State G -> State H
- The Result will be False

---

**Case 4:** `is_shipping_free(50,1,False)`
- The path is State A -> State B -> State D -> State E -> State I
- The Result will be True

Coverage of the code will be as follows:

| Statement                         | Covered By        |
|-----------------------------------|-------------------|
| `print("Additional Statement 1")` | All Tests         |
| `print("Additional Statement 2")` | Tests 1 and 3     |
| `print("Additional Statement 3")` | Tests 1 and 4     |
| `print("Additional Statement 4")` | Tests 2 and 3     |
| `return False`                    | Tests 2 and 3     |
| `return True`                     | Tests 1 and 4     |
| `print("Additional Statement 5")` | No Test           |

Statement coverage = 6 / 7 * 100 = **85.71%**

If we decide to also count the 3 if/elif lines as statements, our statement coverage will then be 9 / 10 * 100 = **90%.**

How about the Branch coverage? Let's have a look:

### BRANCH COVERAGE:

In the code, there are 3 decision points with 2 outcomes each, so the number of branches would be 3 * 2 = **6 Branches**

Let's look at the coverage:

| Branch            | Covered By        |
|-------------------|-------------------|
| State B if True   | Tests 1 and 3     |
| State B if False  | Tests 2 and 4     |
| State D if True   | Tests 1 and 4     |
| State D if False  | Tests 2 and 3     |
| State F if True   | Tests 2 and 3     |
| State F if False  | No Test           |

Branch coverage = 5 / 6 * 100% = **83.33%**

## 3. STATEMENT COVERAGE AND BRANCH COVERAGE CALCULATION, IF LAST LINE IS DELETED FROM CODE

### STATEMENT COVERAGE:

Coverage = 6 / 6 * 100 = **100%**.

The unreachable print statement was the only previously uncovered statement.

### BRANCH COVERAGE:

Coverage = 5 / 6 = **83.3%** **(Remains unchanged)**

The reason is that dead code has no decisions. The tests do not fully cover the code. The missing branch would need one test to reach 100% branch coverage, e.g. `is_shipping_free(15, 2, False)`
