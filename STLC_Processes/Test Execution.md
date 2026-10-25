# Test Execution: Grocery Mate Web Shop, Upcoming Release

## 1. Execution Details

| Field | Value |
|-------|-------|
| Project | Grocery Mate Web Shop, <https://grocerymate.masterschool.com/> |
| Release / build under test | |
| Test cycle | |
| Test environment | TEST |
| Primary browser and operating system | |
| Tester | |
| Execution start date (DD/MM/YYYY) | |
| Execution end date (DD/MM/YYYY) | |
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
- 10 reviews are shown per page, newest first.

**Age Verification for Alcoholic Products**
- A modal asks for the date of birth (DD/MM/YYYY) before alcoholic products are shown.
- The minimum age is 18. Under 18, an error message is shown, access is denied and the user is redirected to the home page.

**Shipping Cost Changes**
- Free shipping from 20.00 € and above. A flat shipping fee of 5.00 € applies below 20.00 €.

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

## 4. Test Environment and Test Data

### 4.1 Platforms

| Platform | Browser | Version | Used for execution |
|----------|---------|---------|--------------------|
| Windows (PC, laptop) | Chrome | | |
| Windows (PC, laptop) | Firefox | | |
| Windows (PC, laptop) | Edge | | |
| macOS (laptop) | Safari | | |
| macOS (laptop) | Chrome | | |
| Android (smartphone, tablet) | Chrome | | |
| iOS (smartphone, tablet) | Safari | | |

### 4.2 Test Data

| Test data | Needed for | Value / ID |
|-----------|------------|------------|
| Guest (not logged in) | Rating | |
| Registered user without any purchase | Rating | |
| Registered user who bought product A only | Rating | |
| Registered user who bought the same product in two orders | Rating | |
| Moderator or admin account | Rating (report, product removal) | |
| Product A (bought by the test user) and product B (not bought) | Rating | |
| Product without ratings | Rating | |
| Product with three ratings of 4, 4 and 5 stars (average 4.3) | Rating | |
| Product with exactly 10 reviews and a product with 11 reviews (each from a different buyer) | Rating | |
| Alcoholic product and non-alcoholic product (for example non-alcoholic beer) | Age verification | |
| Dates of birth: today minus 18 years, today minus 18 years plus 1 day, today minus 35 years, today minus 12 years, tomorrow | Age verification | |
| Invalid inputs: empty, "25/13/1990", "abc" | Age verification | |
| Basket totals: 10.00 €, 12.00 €, 18.00 €, 19.99 €, 20.00 €, 20.01 €, 30.00 €, 80.00 € | Shipping cost | |
| Products of 2.00 € and 4.00 € and three products of 6.67 €, 6.67 € and 6.66 € | Shipping cost | |
| Basket created before the release (12.00 €) | Shipping cost | |
| Available payment methods and test payment details | Shipping cost | |

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

### 6.1 Product Rating System (31 test cases)

| ID | Test case | Input | Expected outcome | Actual result | Status | Defect ID |
|----|-----------|-------|------------------|---------------|--------|-----------|
| TC-01 | Verify that a user can rate a product after registering, logging in and buying it. | Register a new account and log in. Buy a product (complete the check-out) and open the product page. Select 4 stars, enter a review of 50 characters and submit. | The rating and review are saved and published immediately. They appear on the product page, and the average rating and the number of ratings are updated. | | | |
| TC-02 | Verify that a guest cannot rate a product. | Without logging in, open a product page and try to select a star. | The guest is asked to log in. No rating is saved. | | | |
| TC-03 | Verify that a registered user who has bought the product but is logged out cannot rate it. | Log in as a user who bought the product, log out, open the product page and try to select a star. | The user is asked to log in. No rating is saved. | | | |
| TC-04 | Verify that a logged-in user who has not bought the product cannot rate it. | Register a new account and log in without buying anything. Open a product page and try to select a star and submit. | The message "You need to buy this product to tell us your opinion!" is shown and the user cannot rate the product. No rating is saved. | | | |
| TC-05 | Verify that buying one product does not allow rating another product. | Log in as a user who bought product A. Open the page of product B, which the user has not bought, and try to rate it. | The message "You need to buy this product to tell us your opinion!" is shown for product B and the user cannot rate it. No rating is saved. | | | |
| TC-06 | Verify that a product in the basket cannot be rated before the purchase is completed. | Log in as a user with no orders. Add a product to the basket without completing the check-out and open the product page. Then complete the check-out and open the product page again. | Before the check-out is completed the message "You need to buy this product to tell us your opinion!" is shown and the user cannot rate the product. After the purchase is completed the user can rate it. | | | |
| TC-07 | Verify that a user can edit their own rating. | Log in as a user who bought a product and rated it with 3 stars. Change the rating to 5 stars and the review text, then save. | The rating and review are updated. The average is recalculated and the number of ratings stays the same. | | | |
| TC-08 | Verify that a user can delete their own rating. | Log in as a user who bought a product and rated it, and delete the rating. | The rating and review are removed. The average and the number of ratings are updated. The user can rate the product again. | | | |
| TC-09 | Verify that the average rating is displayed consistently on all pages. | Open a product with an average of 4.3 on the product page, in the search results and in the category list. | The same average (4.3) and the same number of ratings are shown in all three places. | | | |
| TC-10 | Verify the order of the reviews. | Two different users who both bought the product submit a review on it one after the other. Open the product page. | The newest review is listed first. | | | |
| TC-11 | Verify that a user can report a review. | Log in as a user and click "Report" on a review written by another user. | A confirmation is shown and the report is available for moderation. | | | |
| TC-12 | Verify the behavior of ratings when a product is removed. | A moderator or admin deactivates a product that has ratings and reviews. Open the product URL and the search results. | The product, its ratings and its reviews are no longer displayed. | | | |
| TC-13 | Verify the lowest valid star rating. | Log in as a user who bought the product, select 1 star and submit. | The rating of 1 star is saved and displayed. | | | |
| TC-14 | Verify the highest valid star rating. | Log in as a user who bought the product, select 5 stars and submit. | The rating of 5 stars is saved and displayed. | | | |
| TC-15 | Verify that submitting without selecting a star (0 stars) is not possible. | Log in as a user who bought the product, open the product page, select no star and click submit. | Error message "Please select a star rating." No rating is saved. | | | |
| TC-16 | Verify a review with exactly the minimum length. | Log in as a user who bought the product, select 3 stars and enter a review of 10 characters. | Rating and review are saved and displayed. | | | |
| TC-17 | Verify a review just below the minimum length. | Log in as a user who bought the product, select 3 stars and enter a review of 9 characters. | Error message "Review must be between 10 and 500 characters." Nothing is saved. | | | |
| TC-18 | Verify a review with exactly the maximum length. | Log in as a user who bought the product, select 3 stars and enter a review of 500 characters. | Rating and review are saved and displayed completely. | | | |
| TC-19 | Verify a review just above the maximum length. | Log in as a user who bought the product, select 3 stars and enter a review of 501 characters. | Error message "Review must be between 10 and 500 characters." Nothing is saved. | | | |
| TC-20 | Verify pagination with exactly 10 reviews. | Open a product that has 10 reviews (written by 10 different users who bought it). | All 10 reviews are shown on one page. There is no second page. | | | |
| TC-21 | Verify pagination with 11 reviews. | Open a product that has 11 reviews (written by 11 different users who bought it) and go to the second page. | The first page shows 10 reviews and the second page shows the 11th (oldest) review. | | | |
| TC-22 | Verify that a star value above the maximum is rejected by the API. | Send a rating request with value 6 (Postman) as a logged-in user who bought the product. | The request is rejected with an error response (400). No rating is saved. | | | |
| TC-23 | Verify that a review without a star rating cannot be submitted. | Log in as a user who bought the product, enter a review of 50 characters, select no star and submit. | Error message "Please select a star rating." The review is not saved. | | | |
| TC-24 | Verify that HTML or script content in the review is rejected. | Log in as a user who bought the product, select 3 stars and enter the review `<script>alert(1)</script>` and submit. | Error message that the review contains invalid content. The script is not executed and nothing is saved. | | | |
| TC-25 | Verify that links in the review are rejected. | Log in as a user who bought the product, select 3 stars and enter the review "Great product, see https://example.com" and submit. | Error message that links are not allowed. Nothing is saved. | | | |
| TC-26 | Verify that a user cannot rate the same product twice. | Log in as a user who already rated a product they bought, and try to add a second rating (also by sending a second rating request through the API). | No second rating is created. The existing rating is shown for editing and the number of ratings does not change. | | | |
| TC-27 | Verify that a user who bought the same product in two orders can only rate it once. | Log in as a user who bought the same product in two separate orders and rated it once. Try to add a second rating. | No second rating is created. The existing rating is shown for editing and the number of ratings does not change. | | | |
| TC-28 | Verify that the API rejects a rating for a product the user has not bought. | Send a rating request (Postman) as a logged-in user who has not bought the product. | The request is rejected with an error response (403). No rating is saved. | | | |
| TC-29 | Verify that the written review is optional. | Log in as a user who bought the product, select 4 stars, leave the review field empty and submit. | The star rating is saved without a review. The review section shows no text for this rating. | | | |
| TC-30 | Verify the calculation and rounding of the average rating. | Use a product with three ratings from three users who bought it: 4, 4 and 5 stars. | The average is shown as 4.3 (4.33 rounded to one decimal) together with "3 ratings". | | | |
| TC-31 | Verify the display of a product without ratings. | Open the product page of a product that has no ratings. | The message "no ratings yet" is displayed. No average and no stars are shown. | | | |

### 6.2 Age Verification for Alcoholic Products (21 test cases)

| ID | Test case | Input | Expected outcome | Actual result | Status | Defect ID |
|----|-----------|-------|------------------|---------------|--------|-----------|
| TC-32 | Verify that the age verification modal appears when opening the alcoholic products category. | As a user who is not yet verified, navigate to the alcoholic products category. | A modal asks for the date of birth (DD/MM/YYYY). No alcoholic product is visible or accessible while the modal is open. | | | |
| TC-33 | Verify that alcoholic products are hidden in search results for an unverified user. | As an unverified user, search for "beer". | Alcoholic products are not shown in the results. Non-alcoholic products that match are shown. | | | |
| TC-34 | Verify that a direct product URL cannot be used to bypass the check. | As an unverified user, open the URL of an alcoholic product directly. | The product details are not shown. The age verification modal appears. | | | |
| TC-35 | Verify the favorites page for an unverified user. | A user added an alcoholic product to favorites in an earlier verified session. In a new session, open the favorites without verifying. | The alcoholic product is not shown until the age verification is passed. | | | |
| TC-36 | Verify the basket when an alcoholic product was added in an earlier session. | A basket contains an alcoholic product from an earlier verified session. In a new session, open the basket and try to check out without verifying. | The user is asked to verify the age first. The alcoholic product is not shown and checkout is blocked until the verification is passed. | | | |
| TC-37 | Verify that the entered date of birth is not stored. | Pass the age verification with a valid date of birth. Check the user account data and the account API response. | The date of birth is not stored or returned anywhere. | | | |
| TC-38 | Verify the modal on a smartphone. | Open the alcoholic products category on an iPhone (Safari) and an Android phone (Chrome). Enter the date of birth with the on-screen keyboard. | The modal is fully visible, readable and usable, and the input and confirm buttons are reachable on both devices. | | | |
| TC-39 | Verify access for a user who is exactly 18 years old today. | Date of Birth = (Today - 18 years) | Verification successful. The modal closes and the alcoholic products are shown. | | | |
| TC-40 | Verify access for a user who turns 18 tomorrow. | Date of Birth = (Today - 18 years + 1 day) | Error message "You must be at least 18 years old to view alcoholic products." Access is denied and the user is redirected to the home page. | | | |
| TC-41 | Verify the behavior when no date of birth is entered. | Leave the date of birth field empty and confirm. | Error message "Date of birth is required." The modal stays open and access is denied. | | | |
| TC-42 | Verify the behavior when an invalid date is entered. | Date of Birth = "25/13/1990" | Error message "Invalid date of birth. Please use DD/MM/YYYY." Access is denied. | | | |
| TC-43 | Verify the behavior when non-date input is entered. | Date of Birth = "abc" | Error message "Invalid date of birth. Please use DD/MM/YYYY." Access is denied. | | | |
| TC-44 | Verify the behavior when a date in the future is entered. | Date of Birth = (Today + 1 day) | Error message "Invalid date of birth. Please use DD/MM/YYYY." Access is denied. | | | |
| TC-45 | Verify that a non-alcoholic product does not trigger the check. | As an unverified user, open the product page of a product flagged as non-alcoholic (for example non-alcoholic beer). | The modal does not appear and the product page is displayed normally. | | | |
| TC-46 | Verify that the API does not return alcoholic products to an unverified user (Postman). | Request the alcoholic products category through the API without a verified session. | The request is denied (403) or returns no alcoholic products. | | | |
| TC-47 | Verify that an alcoholic product cannot be added to the basket by an unverified user through the API (Postman). | Send an add-to-basket request for an alcoholic product without a verified session. | The request is rejected and the basket does not change. | | | |
| TC-48 | Verify access for an adult user. | Date of Birth = (Today - 35 years) | Verification successful. The alcoholic products are shown. | | | |
| TC-49 | Verify that a minor is denied. | Date of Birth = (Today - 12 years) | Error message "You must be at least 18 years old to view alcoholic products." Access is denied and the user is redirected to the home page. | | | |
| TC-50 | Verify that closing the modal does not give access. | Open the alcoholic products category as an unverified user. Close the modal with the close button, then repeat with the ESC key and with the browser back button. | In all three cases the alcoholic products stay inaccessible and the user is returned to the home page. | | | |
| TC-51 | Verify that a verified user is not asked again in the same session. | Pass the age verification with a valid date of birth. Navigate to the home page and open the alcoholic products category again. | The modal does not appear and the alcoholic products are shown. | | | |
| TC-52 | Verify that the verification does not last beyond the session. | Pass the age verification, then close the browser (or log out) and open the alcoholic products category in a new session. | The modal appears again and the alcoholic products are not shown until the user is verified. | | | |

### 6.3 Shipping Cost Changes (19 test cases)

| ID | Test case | Input | Expected outcome | Actual result | Status | Defect ID |
|----|-----------|-------|------------------|---------------|--------|-----------|
| TC-53 | Verify that the shipping cost disappears when an item is added. | Basket total = 18.00 € (shipping cost 5.00 €). Add a product of 2.00 € without reloading the page. | The total is updated immediately to 20.00 € and the shipping cost changes from 5.00 € to 0.00 €. | | | |
| TC-54 | Verify that the shipping cost appears when an item is removed. | Basket total = 20.00 € including a product of 2.00 € (shipping cost 0.00 €). Remove that product. | The total is updated immediately. The shipping cost of 5.00 € is added to the remaining 18.00 € and the total price is 23.00 €. | | | |
| TC-55 | Verify the shipping cost when the quantity of a product is changed. | Basket with one product of 4.00 € and quantity 4 (16.00 €). Change the quantity to 5 (20.00 €). | With quantity 4 the shipping cost is 5.00 € (total 21.00 €). With quantity 5 the shipping cost is 0.00 € (total 20.00 €). | | | |
| TC-56 | Verify the message about the amount missing for free shipping. | Basket total = 10.00 €. Then add products until the total is 20.00 €. | At 10.00 € a message shows that 10.00 € more is needed for free shipping. At 20.00 € the message is replaced by the information that shipping is free. | | | |
| TC-57 | Verify the shipping cost display in the basket. | Open the basket with a total of 10.00 €. | A separate line shows the shipping cost 5.00 € and the total price of 15.00 €. | | | |
| TC-58 | Verify that checkout and order summary show the same shipping cost. | Go from the basket (total 10.00 €) through the checkout to the order summary. | The checkout and the order summary show shipping cost 5.00 € and total price 15.00 €, identical to the basket. | | | |
| TC-59 | Verify the shipping cost in the confirmation email. | Place an order with a total of 10.00 € and open the confirmation email. | The email shows shipping cost 5.00 € and total price 15.00 €. | | | |
| TC-60 | Verify the shipping cost on the invoice. | Place an order with a total of 10.00 € and open the invoice. | The invoice lists the shipping cost of 5.00 € as a separate line and the total of 15.00 €. | | | |
| TC-61 | Verify that a basket created before the release uses the new shipping rules. | A basket of 12.00 € was created before the release. After the release, open the basket and go to the checkout. | The new rules are applied at checkout. Shipping cost 5.00 € and total price 17.00 €. | | | |
| TC-62 | Verify that the amount charged for each payment method includes the shipping cost. | Place an order with a total of 10.00 € once with each available payment method. | The amount charged is 15.00 € for each payment method. | | | |
| TC-63 | Verify that the existing check-out process still works. | Fill in the billing and sending information form, choose a payment method and place the order for a basket of 30.00 €. | The order is placed successfully with shipping cost 0.00 € and total price 30.00 €. | | | |
| TC-64 | Verify the shipping cost just below the threshold. | Basket total = 19.99 € | Shipping cost 5.00 €. Total price 24.99 €. | | | |
| TC-65 | Verify the shipping cost exactly at the threshold. | Basket total = 20.00 € | Shipping cost 0.00 € (free shipping applies from 20.00 € upwards). Total price 20.00 €. | | | |
| TC-66 | Verify the shipping cost just above the threshold. | Basket total = 20.01 € | Shipping cost 0.00 € (free shipping). Total price 20.01 €. | | | |
| TC-67 | Verify the behavior with an empty basket. | Open the basket without any products. | No shipping cost is shown, the total is 0.00 € and checkout is not possible. | | | |
| TC-68 | Verify the threshold check with several items that add up exactly to the threshold. | Basket with three products of 6.67 €, 6.67 € and 6.66 € (20.00 € in total). | Shipping cost 0.00 €. Total price 20.00 €. | | | |
| TC-69 | Verify that the shipping cost cannot be manipulated through the API (Postman). | Send a checkout request for a basket of 12.00 € with the shipping cost value changed to 0.00 €. | The server ignores the value or rejects the request. The order is calculated with shipping cost 5.00 € and total price 17.00 €. | | | |
| TC-70 | Verify the shipping cost for an order well below the threshold. | Basket total = 10.00 € | Shipping cost 5.00 €. Total price 15.00 €. | | | |
| TC-71 | Verify the shipping cost for an order well above the threshold. | Basket total = 80.00 € | Shipping cost 0.00 € (free shipping). Total price 80.00 €. | | | |

---

## 7. Execution Summary

| Feature | Total | Passed | Failed | Blocked | Skipped | Not Run |
|---------|------:|-------:|-------:|--------:|--------:|--------:|
| 1. Product Rating System | 31 | | | | | |
| 2. Age Verification | 21 | | | | | |
| 3. Shipping Cost Changes | 19 | | | | | |
| **Total** | **71** | | | | | |

---

## 8. Exit Criteria Check

| Exit criterion | Target | Actual | Met (yes/no) |
|----------------|--------|--------|--------------|
| Run rate | At least 95% | | |
| Pass rate | At least 90% | | |
| Critical and high-priority defects resolved and closed | All | | |
| Open severity 1 or severity 2 defects | None | | |
| Age verification (6.2) and shipping cost (6.3) test cases passed | 100% | | |
