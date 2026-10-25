# Test Cases: Grocery Mate Web Shop, New features

The test cases are designed for the three new features being developed. They use the estimates and preparations of the test plan prepared previously:

- Rating: 1 to 5 whole stars, optional review text of 10 to 500 characters, 10 reviews per page
- Age verification: minimum age 18, date of birth entered as DD/MM/YYYY
- Shipping: free from 50.00 € (50.00 € and above), flat fee of 4.95 € (including VAT) below 50.00 €

---

### **1. Product Rating System**

**Test Design Techniques being considered**: Equivalence Partitioning (EP), Boundary Value Analysis (BVA), Error Guessing

### Test Cases:

1. **Testing Different Use Cases**
   - Verify that a logged-in user can rate a product with stars and a written review.
        - **Input**: Log in as a registered user. Open a product page the user has not rated. Select 4 stars, enter a review of 50 characters and submit.
        - **Expected Outcome**: The rating and review are saved and published immediately. They appear on the product page, and the average rating and the number of ratings are updated.

   - Verify that a guest cannot rate a product.
        - **Input**: Without logging in, open a product page and try to select a star.
        - **Expected Outcome**: The guest is asked to log in. No rating is saved.

   - Verify that a user can edit their own rating.
        - **Input**: Log in as a user who rated a product with 3 stars. Change the rating to 5 stars and the review text, then save.
        - **Expected Outcome**: The rating and review are updated. The average is recalculated and the number of ratings stays the same.

    - Verify that a user can delete their own rating.
        - **Input**: Log in as a user who rated a product and delete the rating.
        - **Expected Outcome**: The rating and review are removed. The average and the number of ratings are updated. The user can rate the product again.

    - Verify that the average rating is displayed consistently on all pages.
        - **Input**: Open a product with an average of 4.3 on the product page, in the search results and in the category list.
        - **Expected Outcome**: The same average (4.3) and the same number of ratings are shown in all three places.

    - Verify the order of the reviews.
        - **Input**: Two different users submit a review on the same product one after the other. Open the product page.
        - **Expected Outcome**: The newest review is listed first.
     
    - Verify that a user can report a review.
        - **Input**: Log in as a user and click "Report" on a review written by another user.
        - **Expected Outcome**: A confirmation is shown and the report is available for moderation.
          
    - Verify the behavior of ratings when a product is removed.
        - **Input**: A moderator or admin deactivates a product that has ratings and reviews. Open the product URL and the search results.
        - **Expected Outcome**: The product, its ratings and its reviews are no longer displayed.
     
2. **Boundary Value Analysis**:
    - Verify the lowest valid star rating.
        - **Input**: Log in and select 1 star on a product, then submit.
        - **Expected Outcome**: The rating of 1 star is saved and displayed.

    - Verify the highest valid star rating.
        - **Input**: Log in and select 5 stars on a product, then submit.
        - **Expected Outcome**: The rating of 5 stars is saved and displayed.
  
    - Verify that submitting without selecting a star (0 stars) is not possible.
        - **Input**: Log in, open a product page, select no star and click submit.
        - **Expected Outcome**: Error message "Please select a star rating." No rating is saved.
     
    - Verify a review with exactly the minimum length.
        - **Input**: Select 3 stars and enter a review of 10 characters.
        - **Expected Outcome**: Rating and review are saved and displayed.
     
    - Verify a review just below the minimum length.
        - **Input**: Select 3 stars and enter a review of 9 characters.
        - **Expected Outcome**: Error message "Review must be between 10 and 500 characters." Nothing is saved.

    - Verify a review with exactly the maximum length.
        - **Input**: Select 3 stars and enter a review of 500 characters.
        - **Expected Outcome**: Rating and review are saved and displayed completely.
          
    - Verify a review just above the maximum length.
        - **Input**: Select 3 stars and enter a review of 501 characters.
        - **Expected Outcome**: Error message "Review must be between 10 and 500 characters." Nothing is saved.

    - Verify pagination with exactly 10 reviews.
        - **Input**: Open a product that has 10 reviews.
        - **Expected Outcome**: All 10 reviews are shown on one page. There is no second page.
     
    - Verify pagination with 11 reviews.
        - **Input**: Open a product that has 11 reviews and go to the second page.
        - **Expected Outcome**: The first page shows 10 reviews and the second page shows the 11th (oldest) review.
          
3. **Error Guessing**:
    - Verify that a star value above the maximum is rejected by the API.
        - **Input**: Send a rating request with value 6 (Postman) as a logged-in user.
        - **Expected Outcome**: The request is rejected with an error response (400). No rating is saved.

    - Verify that a review without a star rating cannot be submitted.
        - **Input**: Enter a review of 50 characters, select no star and submit.
        - **Expected Outcome**: Error message "Please select a star rating." The review is not saved

    - Verify that HTML or script content in the review is rejected.
        - **Input**: Select 3 stars and enter the review `<script>alert(1)</script>` and submit.
        - **Expected Outcome**: Error message that the review contains invalid content. The script is not executed and nothing is saved.

    - Verify that links in the review are rejected.
        - **Input**: Select 3 stars and enter the review "Great product, see https://example.com" and submit.
        - **Expected Outcome**: Error message that links are not allowed. Nothing is saved.
     
    - Verify that a user cannot rate the same product twice.
        - **Input**: Log in as a user who already rated a product, and try to add a second rating (also by sending a second rating request through the API).
        - **Expected Outcome**: No second rating is created. The existing rating is shown for editing and the number of ratings does not change. 

4. **Equivalence class Partitioning**:
    - Verify that the written review is optional.
        - **Input**: Select 4 stars, leave the review field empty and submit.
        - **Expected Outcome**: The star rating is saved without a review. The review section shows no text for this rating.
    
    - Verify the calculation and rounding of the average rating.
        - **Input**: Use a product with three ratings: 4, 4 and 5 stars.
        - **Expected Outcome**: The average is shown as 4.3 (4.33 rounded to one decimal) together with "3 ratings".

    - Verify the display of a product without ratings.
        - **Input**: Open the product page of a product that has no ratings.
        - **Expected Outcome**: The message "no ratings yet" is displayed. No average and no stars are shown.

---

### **2. Age Verification for Alcoholic Products**

**Test Design Techniques**: State Transition Testing, Boundary Value Analysis (BVA), Equivalence Partitioning (EP), Use Case Testing, Error Guessing

### Test Cases:
1. **Testing Different Use Cases**
   - Verify that the age verification modal appears when opening the alcoholic products category.
        - **Input**: As a user who is not yet verified, navigate to the alcoholic products category.
        - **Expected Outcome**: A modal asks for the date of birth (DD/MM/YYYY). No alcoholic product is visible or accessible while the modal is open.

   - Verify that alcoholic products are hidden in search results for an unverified user.
        - **Input**: As an unverified user, search for "beer".
        - **Expected Outcome**: Alcoholic products are not shown in the results. Non-alcoholic products that match are shown.

   - Verify that a direct product URL cannot be used to bypass the check.
        - **Input**: As an unverified user, open the URL of an alcoholic product directly.
        - **Expected Outcome**: The product details are not shown. The age verification modal appears.

   - Verify the favorites page for an unverified user.
        - **Input**: A user added an alcoholic product to favorites in an earlier verified session. In a new session, open the favorites without verifying.
        - **Expected Outcome**: The alcoholic product is not shown until the age verification is passed.

   - Verify the basket when an alcoholic product was added in an earlier session.
        - **Input**: A basket contains an alcoholic product from an earlier verified session. In a new session, open the basket and try to check out without verifying.
        - **Expected Outcome**: The user is asked to verify the age first. The alcoholic product is not shown and checkout is blocked until the verification is passed.

   - Verify that the entered date of birth is not stored.
        - **Input**: Pass the age verification with a valid date of birth. Check the user account data and the account API response.
        - **Expected Outcome**: The date of birth is not stored or returned anywhere.

   - Verify the modal on a smartphone.
        - **Input**: Open the alcoholic products category on an iPhone (Safari) and an Android phone (Chrome). Enter the date of birth with the on-screen keyboard.
        - **Expected Outcome**: The modal is fully visible, readable and usable, and the input and confirm buttons are reachable on both devices.

2. **Boundary Value Analysis**:
    - Verify access for a user who is exactly 18 years old today.
        - **Input**: Date of Birth = (Today - 18 years)
        - **Expected Outcome**: Verification successful. The modal closes and the alcoholic products are shown.

    - Verify access for a user who turns 18 tomorrow.
        - **Input**: Date of Birth = (Today - 18 years + 1 day)
        - **Expected Outcome**: Error message "You must be at least 18 years old to view alcoholic products." Access is denied and the user is redirected to the home page.

3. **Error Guessing**:
    - Verify the behavior when no date of birth is entered.
        - **Input**: Leave the date of birth field empty and confirm.
        - **Expected Outcome**: Error message "Date of birth is required." The modal stays open and access is denied.

    - Verify the behavior when an invalid date is entered.
        - **Input**: Date of Birth = "25/13/1990"
        - **Expected Outcome**: Error message "Invalid date of birth. Please use DD/MM/YYYY." Access is denied.

    - Verify the behavior when non-date input is entered.
        - **Input**: Date of Birth = "abc"
        - **Expected Outcome**: Error message "Invalid date of birth. Please use DD/MM/YYYY." Access is denied.

    - Verify the behavior when a date in the future is entered.
        - **Input**: Date of Birth = (Today + 1 day)
        - **Expected Outcome**: Error message "Invalid date of birth. Please use DD/MM/YYYY." Access is denied.

    - Verify that a non-alcoholic product does not trigger the check.
        - **Input**: As an unverified user, open the product page of a product flagged as non-alcoholic (for example non-alcoholic beer).
        - **Expected Outcome**: The modal does not appear and the product page is displayed normally.

    - Verify that the API does not return alcoholic products to an unverified user (Postman).
        - **Input**: Request the alcoholic products category through the API without a verified session.
        - **Expected Outcome**: The request is denied (403) or returns no alcoholic products.

    - Verify that an alcoholic product cannot be added to the basket by an unverified user through the API (Postman).
        - **Input**: Send an add-to-basket request for an alcoholic product without a verified session.
        - **Expected Outcome**: The request is rejected and the basket does not change.

4. **Equivalence class Partitioning**:
    - Verify access for an adult user.
        - **Input**: Date of Birth = (Today - 35 years)
        - **Expected Outcome**: Verification successful. The alcoholic products are shown.

    - Verify that a minor is denied.
        - **Input**: Date of Birth = (Today - 12 years)
        - **Expected Outcome**: Error message "You must be at least 18 years old to view alcoholic products." Access is denied and the user is redirected to the home page.

5. **State Transition Testing**:
    - Verify that closing the modal does not give access.
        - **Input**: Open the alcoholic products category as an unverified user. Close the modal with the close button, then repeat with the ESC key and with the browser back button.
        - **Expected Outcome**: In all three cases the alcoholic products stay inaccessible and the user is returned to the home page.

    - Verify that a verified user is not asked again in the same session.
        - **Input**: Pass the age verification with a valid date of birth. Navigate to the home page and open the alcoholic products category again.
        - **Expected Outcome**: The modal does not appear and the alcoholic products are shown.

    - Verify that the verification does not last beyond the session.
        - **Input**: Pass the age verification, then close the browser (or log out) and open the alcoholic products category in a new session.
        - **Expected Outcome**: The modal appears again and the alcoholic products are not shown until the user is verified.
     
---

### **3. Shipping Cost Changes**

**Test Design Techniques**: Boundary Value Analysis (BVA), Equivalence Partitioning (EP), Decision Table Testing, Use Case Testing, Error Guessing

### Test Cases:

1. **Testing Different Use Cases**
   - Verify that the shipping cost disappears when an item is added.
        - **Input**: Basket total = 45.00 € (shipping cost 4.95 €). Add a product of 5.00 € without reloading the page.
        - **Expected Outcome**: The total is updated immediately to 50.00 € and the shipping cost changes from 4.95 € to 0.00 €.

   - Verify that the shipping cost appears when an item is removed.
        - **Input**: Basket total = 50.00 € including a product of 5.00 € (shipping cost 0.00 €). Remove that product.
        - **Expected Outcome**: The total is updated immediately. The shipping cost of 4.95 € is added to the remaining 45.00 € and the total price is 49.95 €.

   - Verify the shipping cost when the quantity of a product is changed.
        - **Input**: Basket with one product of 12.50 € and quantity 3 (37.50 €). Change the quantity to 4 (50.00 €).
        - **Expected Outcome**: With quantity 3 the shipping cost is 4.95 € (total 42.45 €). With quantity 4 the shipping cost is 0.00 € (total 50.00 €).

   - Verify the message about the amount missing for free shipping.
        - **Input**: Basket total = 40.00 €. Then add products until the total is 50.00 €.
        - **Expected Outcome**: At 40.00 € a message shows that 10.00 € more is needed for free shipping. At 50.00 € the message is replaced by the information that shipping is free.

   - Verify the shipping cost display in the basket.
        - **Input**: Open the basket with a total of 30.00 €.
        - **Expected Outcome**: A separate line shows the shipping cost 4.95 € including VAT, and the total price of 34.95 €.

   - Verify that checkout and order summary show the same shipping cost.
        - **Input**: Go from the basket (total 30.00 €) through the checkout to the order summary.
        - **Expected Outcome**: The checkout and the order summary show shipping cost 4.95 € and total price 34.95 €, identical to the basket.

   - Verify the shipping cost in the confirmation email.
        - **Input**: Place an order with a total of 30.00 € and open the confirmation email.
        - **Expected Outcome**: The email shows shipping cost 4.95 € and total price 34.95 €.

   - Verify the shipping cost on the invoice.
        - **Input**: Place an order with a total of 30.00 € and open the invoice.
        - **Expected Outcome**: The invoice lists the shipping cost of 4.95 € as a separate line including VAT, and the total of 34.95 €.

   - Verify that a basket created before the release uses the new shipping rules.
        - **Input**: A basket of 45.00 € was created before the release. After the release, open the basket and go to the checkout.
        - **Expected Outcome**: The new rules are applied at checkout. Shipping cost 4.95 € and total price 49.95 €.

   - Verify that the amount charged for each payment method includes the shipping cost.
        - **Input**: Place an order with a total of 30.00 € once with each available payment method.
        - **Expected Outcome**: The amount charged is 34.95 € for each payment method.

   - Verify that the existing check-out process still works.
        - **Input**: Fill in the billing and sending information form, choose a payment method and place the order for a basket of 60.00 €.
        - **Expected Outcome**: The order is placed successfully with shipping cost 0.00 € and total price 60.00 €.

2. **Boundary Value Analysis**:
    - Verify the shipping cost just below the threshold.
        - **Input**: Basket total = 49.99 €
        - **Expected Outcome**: Shipping cost 4.95 €. Total price 54.94 €.

    - Verify the shipping cost exactly at the threshold.
        - **Input**: Basket total = 50.00 €
        - **Expected Outcome**: Shipping cost 0.00 € (free shipping applies from 50.00 € upwards). Total price 50.00 €.

    - Verify the shipping cost just above the threshold.
        - **Input**: Basket total = 50.01 €
        - **Expected Outcome**: Shipping cost 0.00 € (free shipping). Total price 50.01 €.

3. **Error Guessing**:
    - Verify the behavior with an empty basket.
        - **Input**: Open the basket without any products.
        - **Expected Outcome**: No shipping cost is shown, the total is 0.00 € and checkout is not possible.

    - Verify the threshold check with several items that add up exactly to the threshold.
        - **Input**: Basket with three products of 16.67 €, 16.67 € and 16.66 € (50.00 € in total).
        - **Expected Outcome**: Shipping cost 0.00 €. Total price 50.00 €.

    - Verify that the shipping cost cannot be manipulated through the API (Postman).
        - **Input**: Send a checkout request for a basket of 30.00 € with the shipping cost value changed to 0.00 €.
        - **Expected Outcome**: The server ignores the value or rejects the request. The order is calculated with shipping cost 4.95 €.

4. **Equivalence class Partitioning**:
    - Verify the shipping cost for an order well below the threshold.
        - **Input**: Basket total = 20.00 €
        - **Expected Outcome**: Shipping cost 4.95 €. Total price 24.95 €.

    - Verify the shipping cost for an order well above the threshold.
        - **Input**: Basket total = 80.00 €
        - **Expected Outcome**: Shipping cost 0.00 € (free shipping). Total price 80.00 €.

5. **Decision Table Testing**:
    - Verify that a percentage discount is applied before the threshold check and the order falls below the threshold.
        - **Input**: Basket total = 55.00 € with a 10% discount (49.50 € after the discount).
        - **Expected Outcome**: Shipping cost 4.95 €. Total price 54.45 €.

    - Verify that an order stays above the threshold after a voucher.
        - **Input**: Basket total = 60.00 € with a voucher of 5.00 € (55.00 € after the voucher).
        - **Expected Outcome**: Shipping cost 0.00 €. Total price 55.00 €.

    - Verify that an order falls below the threshold after a voucher.
        - **Input**: Basket total = 52.00 € with a voucher of 5.00 € (47.00 € after the voucher).
        - **Expected Outcome**: Shipping cost 4.95 €. Total price 51.95 €.

    - Verify the threshold boundary after a discount.
        - **Input**: Basket total = 62.50 € with a 20% discount (exactly 50.00 € after the discount).
        - **Expected Outcome**: Shipping cost 0.00 €. Total price 50.00 €.
