## Coverage

As long as a customer spends more than 50€, shipping should be free. If it is more than 25€ but less than 3 items need to be shipped, it should also be free. If there is only one item which costs more than 10€, there should be a discount, but it should not be free. In other cases, full price shipping should be paid.

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

Do the following test cases cover fully cover the code?
  print("----------------")
  is_shipping_free(30,2,True)
  print("----------------")
  is_shipping_free(15,1,False)
  print("----------------")
  is_shipping_free(15,1,True)
  print("----------------")
  is_shipping_free(50,1,False)

1. Draw a (directed acyclic graph) - State Transition Diagram for this code section
2. Calculate Statement Coverage and Branch Coverage
3. Calculate Statement Coverage and Branch Coverage, if the line print(”Additional Statement 5”) is deleted from Code.


## Let's determine an appropriate solution for this.

To answer the first question, the test set does not fully cover the code, as the tests written may probably satisfy the statement coverage but does not at all satisfy the branch coverage. Also, a part of the code is unreachable, and there is no test that covers this.
Let us calculate the coverages to determine the proper results.


1. Let's draw a directed acyclic graph showing the state transition diagram for this code section

   <img width="860" height="720" alt="image" src="https://github.com/user-attachments/assets/09d816be-1cac-4cfc-b45a-37651201674f" />


2. STATEMENT COVERAGE AND BRANCH COVERAGE CALCULATION
   STATEMENT COVERAGE:
   For the 4 test cases...
   


