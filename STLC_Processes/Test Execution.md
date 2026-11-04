# Test Execution: Grocery Mate Web Shop, Upcoming Release

## 1. Execution Details

| Field | Value |
|-------|-------|
| Project | Grocery Mate Web Shop, <https://grocerymate.masterschool.com/> |
| Release / build under test | grocerymate V1.0 |
| Test cycle | 1 |
| Test environment | TEST |
| Primary browser and operating system | Chrome/ Windows |
| Tester | Olu |
| Execution start date (DD/MM/YYYY) | 04/11/2026 |
| Execution end date (DD/MM/YYYY) | 04/11/2026 |
| Test plan | Test_Plan.md |
| Test case source | Test_Cases_Feature_1_Rating.md, Test_Cases_Feature_2_Age_Verification.md, Test_Cases_Feature_3_Shipping.md |
| Document version | 1.0 |

---

## 2. Rules Under Test

The expected outcomes in this document are based on these rules.

**Product Rating System**
- A user must register (create an account), log in and buy a product before the user can rate it.
- A user who has not bought the product sees the message "You need to buy this product to tell us your opinion!"
- A rating is 1 to 5 whole stars. A written review is optional, but if entered it must have 10 to 500 characters.
- One rating per user and product. The user can edit and delete their own rating.

**Age Verification for Alcoholic Products**
- A modal asks for the date of birth (DD-MM-YYYY) before alcoholic products are shown.
- The minimum age is 18. Under 18, an error message is shown, access is denied and the user is redirected to the home page.

**Shipping Cost Changes**
- Free shipping from 20.00€ and above. A flat shipping fee of 5.00€ applies below 20.00€ purchase.

---

## 3. Entry Criteria Check

Tick the box when the criterion is met before the execution starts.

- [ ] The requirements are approved and the open questions are answered and documented
- [ ] The test plan is approved by the Test Manager
- [ ] Test cases are designed and reviewed, and the test data is prepared
- [ ] The new features are developed and unit testing is completed with no open critical defects
- [ ] The build is deployed to the test environment and passes the smoke test
- [ ] The test environment, devices, browsers, tools and user accounts are available

---

## 4. Test Data

| Test data | Needed for | Value |
|-----------|------------|-------|
| Guest (not logged in) | Rating | No account. Open the shop in a new private browser window and do not log in. |
| Registered user without any purchase | Rating | tester2@testingacademy.com / Test123@ (registered, no orders) |
| Registered user who bought product A only | Rating | tester3@testingacademy.com / Test123@ (one completed order containing product A only) |
| Product A (bought by the test user) and product B (not bought) | Rating | Product A: the product in the completed order of tester3@testingacademy.com. Product B: any other product that tester3@testingacademy.com has not bought. |
| Product without ratings | Rating | Any product without ratings and reviews |
| Product with three ratings of 4, 4 and 5 stars (average 4.3) | Rating | A product rated with 4 stars by tester4@testingacademy.com, 4 stars by tester5@testingacademy.com and 5 stars by tester6@testingacademy.com (all three bought it, password Test123@). Shown as 4.3 with "3 ratings". |
| Alcoholic product and non-alcoholic product (for example non-alcoholic beer) | Age verification | Alcoholic: any product from the alcoholic products category. Non-alcoholic: any product that is not flagged as alcoholic. |
| Dates of birth: today minus 18 years, today minus 18 years plus 1 day, today minus 35 years, today minus 12 years, tomorrow | Age verification | Today is 04/11/2026: 04/11/2008; 05/11/2008; 04/11/1991; 04/11/2014; 05/11/2026 |
| Invalid inputs: empty, "25/13/1990", "abc" | Age verification | Empty field; 25/13/1990; abc (typed into the date of birth field of the modal) |
| Basket totals: 10.00 €, 12.00 €, 18.00 €, 19.99 €, 20.00 €, 20.01 €, 30.00 €, 80.00 € | Shipping cost | 10.00 € = 5 x 2.00 €; 12.00 € = 4 x 3.00 €; 18.00 € = 6 x 3.00 €; 19.99 € = 6 x 3.00 € + 1.99 €; 20.00 € = 10 x 2.00 €; 20.01 € = 6 x 3.00 € + 2.01 €; 30.00 € = 10 x 3.00 €; 80.00 € = 40 x 2.00 € (products of the given prices, quantity set in the basket) |
| Products of 0.50 €, 1.50 €, 1.99 €, 2.00 €, 2.01 €, 2.50 €, 3.00 €, 3.50 € | Shipping cost | One product of each price. |
| Available payment methods and test payment details | Shipping cost | Credit card (the only payment method): test card 4242 4242 4242 4242, expiry 12/30, CVC 123 |

---

## 5. Status Values

| Status | Meaning |
|--------|---------|
| Passed | Actual result matches the expected outcome |
| Failed | Actual result differs from the expected outcome |
| Blocked | The test case cannot be executed (for example, a defect or missing test data blocks it) |
| Skipped | The test case is deliberately not executed, with a reason in Actual result |
| Not Run | The test case has not been executed yet |

---

## 6. Test Execution

### 6.1 Product Rating System

| ID | Test case | Steps | Expected outcome | Actual result | Status |
|----|-----------|-------|------------------|---------------|--------|
| TC-01 | Verify that a user can rate a product after registering, logging in and buying it. | 1. Register a new account and log in.<br>2. Buy a product (complete the check-out) and open the product page.<br>3. Select 4 stars, enter a review of 50 characters and submit. | The rating and review are saved and published immediately. They appear on the product page, and the average rating and the number of ratings are updated. | Works as described | Passed |
| TC-02 | Verify that a guest cannot rate a product. | 1. Open the shop without logging in.<br>2. Open a product page.<br>3. Try to check for a star rating. | The guest is asked to log in. | Works as expected | Passed |
| TC-03 | Verify that a registered user who has bought the product but is logged out cannot rate it. | 1. Log in as a user who bought the product.<br>2. Log out.<br>3. Open the product page.<br>4. Try to select a star. | The user is asked to log in. Login page opens. | Works as expected | Passed |
| TC-04 | Verify that a logged-in user who has not bought the product cannot rate it. | 1. Register a new account and log in without buying anything.<br>2. Open a product page and try to select a star and submit. | The message "You need to buy this product to tell us your opinion!" is shown and the user cannot rate the product. No rating is saved. | Works as expected | Passed |
| TC-05 | Verify that buying one product does not allow rating another product. | 1. Log in as a user who bought product A.<br>2. Open the page of product B, which the user has not bought, and try to rate it. | The message "You need to buy this product to tell us your opinion!" is shown for product B and the user cannot rate it. No rating is saved. | Works as expected | Passed |
| TC-06 | Verify that a product in the basket cannot be rated before the purchase is completed. | 1. Log in as a user with no orders.<br>2. Add a product to the basket without completing the check-out and open the product page.<br>3. Then complete the check-out and open the product page again. | Before the check-out is completed the message "You need to buy this product to tell us your opinion!" is shown and the user cannot rate the product. After the purchase is completed the user can rate it. | Works as expected | Passed |
| TC-07 | Verify that a user can edit their own rating. | 1. Log in as a user who bought a product and rated it with 3 stars.<br>2. Change the rating to 5 stars and the review text, then save. | The rating and review are updated. The average is recalculated and the number of ratings stays the same. | Works as expected | Passed |
| TC-08 | Verify that a user can delete their own rating. | 1. Log in as a user who bought a product and rated it.<br>2. Open the product page.<br>3. Delete the rating. | The rating and review are removed. The average and the number of ratings are updated. The user can rate the product again. | Works as expected | Passed |
| TC-09 | Verify that the average rating is displayed consistently on all pages. | 1. Open a product with an average of 4.3 on the product page.<br>2. Open the same product in the search results.<br>3. Open the same product in the category list. | The same average (4.3) and the same number of ratings are shown in all three places. | Works as expected | Passed |
| TC-10 | Verify the order of the reviews. | 1. Two different users who both bought the product submit a review on it one after the other.<br>2. Open the product page. | The newest review is listed first. | Works as expected | Passed |
| TC-11 | Verify the lowest valid star rating. | 1. Log in as a user who bought the product.<br>2. Open the product page.<br>3. Select 1 star.<br>4. Submit. | The rating of 1 star is saved and displayed. | Works as expected | Passed |
| TC-12 | Verify the highest valid star rating. | 1. Log in as a user who bought the product.<br>2. Open the product page.<br>3. Select 5 stars.<br>4. Submit. | The rating of 5 stars is saved and displayed. | Works as expected | Passed |
| TC-13 | Verify that submitting without selecting a star (0 stars) is not possible. | 1. Log in as a user who bought the product.<br>2. Open the product page.<br>3. Select no star.<br>4. Click submit. | Error message "Please check your input." No rating is saved. | Works as expected | Passed |
| TC-14 | Verify that a user cannot rate the same product twice. | 1. Log in as a user who already rated a product they bought.<br>2. Open the product page and try to add a second rating.<br>3. Send a second rating request for the same product through the API (Postman). | No second rating is created. The existing rating is shown for editing and the number of ratings does not change. | Works as expected | Passed |
| TC-15 | Verify that the written review is optional. | 1. Log in as a user who bought the product.<br>2. Open the product page.<br>3. Select 4 stars.<br>4. Leave the review field empty.<br>5. Submit. | The star rating is saved without a review. The review section shows no text for this rating. | Works as expected | Passed |
| TC-16 | Verify that the written review is saved. | 1. Log in as a user who bought the product.<br>2. Open the product page.<br>3. Select 4 stars.<br>4. Leave a review comment.<br>5. Submit. | The star rating is saved with the review comment. The review section shows the text for this rating. | Only stars are captured. No rating comment is shown after submitting rating | Failed |
| TC-17 | Verify a review just above the maximum length. | 1. Log in as a user who bought the product.<br>2. Open the product page.<br>3. Select 3 stars.<br>4. Enter a review of 501 characters.<br>5. Submit. | Error message "Review must be between 10 and 500 characters." Nothing is saved. | Works as expected | Passed |
| TC-18 | Verify a review's maximum length during editing. | 1. Log in as a user who bought the product.<br>2. Open the product page.<br>3. Select 3 stars.<br>4. Enter a review of 500 characters.<br>5. Submit.<br>6. Edit the review.<br>7. Enter a text of more 501 characters.<br>8 Submit. | Error message "Review must not be more than 500 characters." Nothing is saved. | Text longer than 500 characters was accepted and saved after editing | Failed |


### 6.2 Age Verification for Alcoholic Products

| ID | Test case | Steps | Expected outcome | Actual result | Status |
|----|-----------|-------|------------------|---------------|--------|
| TC-19 | Verify that the age verification modal appears when opening the alcoholic products category. | 1. Open the shop as a user who is not yet verified.<br>2. Navigate to the alcoholic products category. | A modal asks for the date of birth (DD/MM/YYYY). No alcoholic product is visible or accessible while the modal is open. | Alcoholic products are shown | Failed |
| TC-20 | Verify that alcoholic products are hidden in search results for an unverified user. | 1. Open the shop as an unverified user.<br>2. Search for "alcohol". | Alcoholic products are not shown in the results. Non-alcoholic products that match are shown. | All alcoholic products are shown | Failed |
| TC-21 | Verify the favorites page for an unverified user. | 1. A user added an alcoholic product to favorites in an earlier verified session.<br>2. In a new session, open the favorites without verifying. | The alcoholic product is not shown until the age verification is passed. | Works as expected | Passed |
| TC-22 | Verify access for a user who is exactly 18 years old today. | 1. Open the shop as an unverified user.<br>2. Navigate to the alcoholic products category.<br>3. Enter Date of Birth = (Today - 18 years).<br>4. Confirm. | Verification successful. The modal closes and the alcoholic products are shown. | Works as expected | Passed |
| TC-23 | Verify access for a user who turns 18 tomorrow. | 1. Open the shop as an unverified user.<br>2. Navigate to the alcoholic products category.<br>3. Enter Date of Birth = (Today - 18 years + 1 day).<br>4. Confirm. | Error message "You must be at least 18 years old to view alcoholic products." Access is denied and the user is redirected to the home page. | Works as expected | Passed |
| TC-24 | Verify the behavior when no date of birth is entered. | 1. Open the shop as an unverified user.<br>2. Navigate to the alcoholic products category.<br>3. Leave the date of birth field empty.<br>4. Confirm. | Error message "Date of birth is required." The modal stays open and access is denied. |  Modal disappears and message says "You are underage"| Failed |
| TC-25 | Verify the behavior when an invalid date is entered. | 1. Open the shop as an unverified user.<br>2. Navigate to the alcoholic products category.<br>3. Enter Date of Birth = "25/13/1990".<br>4. Confirm. | Error message "Invalid date of birth. Please use DD-MM-YYYY." Access is denied. | Modal disappears and message says "You are underage"| Failed |
| TC-26 | Verify the behavior when non-date input is entered. | 1. Open the shop as an unverified user.<br>2. Navigate to the alcoholic products category.<br>3. Enter Date of Birth = "abc".<br>4. Confirm. | Error message "Invalid date of birth. Please use DD-MM-YYYY." Access is denied. | Modal disappears and message says "You are underage"| Failed |
| TC-27 | Verify the behavior when a date in the future is entered. | 1. Open the shop as an unverified user.<br>2. Navigate to the alcoholic products category.<br>3. Enter Date of Birth = (Today + 1 day).<br>4. Confirm. | Error message "Invalid date of birth. Please use DD-MM-YYYY." Access is denied. | Modal disappears and message says "You are underage"| Failed |
| TC-28 | Verify that a non-alcoholic product does not trigger the check. | 1. Open the shop as an unverified user.<br>2. Open the product page of a product flagged as non-alcoholic (for example non-alcoholic beer). | The modal does not appear and the product page is displayed normally. | Works as expected | Passed |
| TC-29 | Verify access for an adult user. | 1. Open the shop as an unverified user.<br>2. Navigate to the alcoholic products category.<br>3. Enter Date of Birth = (Today - 35 years).<br>4. Confirm. | Verification successful. The alcoholic products are shown. | Works as expected | Passed |
| TC-30 | Verify that a minor is denied. | 1. Open the shop as an unverified user.<br>2. Navigate to the alcoholic products category.<br>3. Enter Date of Birth = (Today - 12 years).<br>4. Confirm. | Error message "You must be at least 18 years old to view alcoholic products." Access is denied and the user is redirected to the home page. | Works as expected | Passed |
| TC-31 | Verify that a verified user is not asked again in the same session. | 1. Pass the age verification with a valid date of birth.<br>2. Navigate to the home page and open the alcoholic products category again. | The modal does not appear and the alcoholic products are shown. | Works as expected | Passed |
| TC-32 | Verify that the verification does not last beyond the session. | 1. Pass the age verification.<br>2. Close the browser (or log out).<br>3. Open the alcoholic products category in a new session. | The modal appears again and the alcoholic products are not shown until the user is verified. | Works as expected | Passed |

### 6.3 Shipping Cost Changes

| ID | Test case | Steps | Expected outcome | Actual result | Status |
|----|-----------|-------|------------------|---------------|--------|
| TC-33 | Verify that the shipping cost disappears when an item is added. | 1. Basket total = 18.00 € (shipping cost 5.00 €).<br>2. Add a product of 2.00 € without reloading the page. | The total is updated immediately to 20.00 € and the shipping cost changes from 5.00 € to 0.00 €. | Works as expected | Passed |
| TC-34 | Verify that the shipping cost appears when an item is removed. | 1. Basket total = 20.00 € including a product of 2.00 € (shipping cost 0.00 €).<br>2. Remove that product. | The total is updated immediately. The shipping cost of 5.00 € is added to the remaining 18.00 € and the total price is 23.00 €. | Shipping cost remains 0.00 after update | Failed |
| TC-35 | Verify the shipping cost when the quantity of a product is changed. | 1. Basket with one product of 2.50 € and quantity 7 (17.50 €).<br>2. Change the quantity to 8 (20.00 €). | With quantity 7 the shipping cost is 5.00 € (total 22.50 €). With quantity 8 the shipping cost is 0.00 € (total 20.00 €). | Shipping cost not updated | Failed |
| TC-36 | Verify the shipping cost display in the basket. | 1. Add products to the basket so that the total is 10.00 €.<br>2. Open the basket. | A separate line shows the shipping cost 5.00 € and the total price of 15.00 €. | Works as expected | Passed |
| TC-37 | Verify that checkout and order summary show the same shipping cost. | 1. Add products to the basket so that the total is 10.00 €.<br>2. Open the basket.<br>3. Go to the checkout.<br>4. Continue to the order summary. | The checkout and the order summary show shipping cost 5.00 € and total price 15.00 €, identical to the basket. | No order summary and order confirmation page displayed | Failed |
| TC-38 | Verify the shipping cost just below the threshold. | 1. Add products to the basket so that the total is 19.99 €.<br>2. Open the basket. | Shipping cost 5.00 €. Total price 24.99 €. | Works as expected | Passed |
| TC-39 | Verify the shipping cost exactly at the threshold. | 1. Add products to the basket so that the total is 20.00 €.<br>2. Open the basket. | Shipping cost 0.00 € (free shipping applies from 20.00 € upwards). Total price 20.00 €. | Works as expected | Passed |
| TC-40 | Verify the shipping cost just above the threshold. | 1. Add products to the basket so that the total is 20.01 €.<br>2. Open the basket. | Shipping cost 0.00 € (free shipping). Total price 20.01 €. |nWorks as expected | Passed |
| TC-41 | Verify the behavior with an empty basket. | 1. Make sure the basket is empty.<br>2. Open the basket. | No shipping cost is shown, the total is 0.00 € and checkout is not possible. | Works as expected | Passed |

---

## 7. Execution Summary

| Feature | Total | Passed | Failed | Blocked | Skipped | Not Run |
|---------|------:|-------:|-------:|--------:|--------:|--------:|
| 1. Product Rating System | 18 | 16 | 2 | 0 | 0 | 0 |
| 2. Age Verification | 14 | 8 | 6 | 0 | 0 | 0 |
| 3. Shipping Cost Changes | 9 | 6 | 3 | 0 | 0 | 0 |
| **Total** | **41** | 30 | 11 | 0 | 0 | 0 |

---

## 8. Exit Criteria Check

| Exit criterion | Target | Actual | Met (yes/no) |
|----------------|--------|--------|--------------|
| Run rate (executed test cases / total test cases x 100, where executed = Passed + Failed) | At least 95% | 100% | Yes |
| Pass rate (Passed / executed test cases x 100) | At least 90% | 73% | No |
| Critical and high-priority defects resolved and closed | All | None | No |
| Open severity 1 or severity 2 defects | None | None | Yes |
| Age verification (6.2) and shipping cost (6.3) test cases passed | 100% | 67% | No |
