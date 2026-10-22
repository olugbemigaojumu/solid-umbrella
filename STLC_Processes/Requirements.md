> This is a Requirements document that states critical questions to be asked for the new features that are to be developed for our Grocery Mate Web Shop.

---

## The software

<https://grocerymate.masterschool.com/>

The webshop has the following basic functionalities:

1. Register and login functionality
2. Searching for products, sorting on price, categories of products
3. Add products to favorites
4. Add products to basket
5. Check-out process: billing and sending information in a form, choose payment method. Calculation of costs (calculate total price)

## New features

### 1. Product Rating System

**Requirement:** Users should be able to rate products with a 5-star system and have the option to add written feedback.

### 2. Age Verification for Alcoholic Products

**Requirement:** Alcoholic products require age verification. A modal should appear when navigating to the alcoholic products category asking if the user is 18+. Users must input their age before accessing the alcoholic products.

### 3. Shipping Cost Changes

**Requirement:** Free shipping for orders above a certain amount. Orders below this amount will incur a shipping fee.

---

## Let's attempt to solve this by asking pertinent and critical questions that a tester should ask

### 1. Product Rating System

**Vague Requirement:**
Users should be able to rate products with a 5-star system and have the option to add written feedback.

**Questions to be clarified:**

1. Must the user be logged in, or can guests rate?
2. Must the user have bought the product (verified purchase), or can anyone rate any product?
3. Can a user rate the same product more than once? Can they edit or delete their rating or review later?
4. Is the star rating mandatory when the user writes feedback? Can the user submit text without stars, or stars without text?
5. Are whole stars the only option, or are half stars allowed? Is a 0-star rating possible?
6. What are the minimum and maximum lengths of the written feedback?
7. Are emojis, links or HTML allowed in the input field
8. Are there any language restrictions, and is profanity filtered?
9. What is displayed for a product that has no ratings yet?
10. Should users be able to sort or filter by rating, in addition to the existing name and price sorting?
11. In what order are reviews listed, and are they paginated?
12. Are reviews published immediately or approved first? Who moderates, and can users report a review?
13. Is the reviewer’s name shown?
14. What happens to a user’s reviews when their account is deleted?
15. Can the reviews be responded to by the Webstore?
16. Can the reviews be responded to by the other users?
17. Can the reviews be liked (reactions) by other users?
18. What happens to ratings when a product is deactivated or removed?

**Detailed requirements:**
- Logged-in users must be able to rate a product on its product page with 1 to 5 whole stars. Each user can submit one rating per product and can edit or delete it later. Guests who try to rate must be asked to log in first.
- Users may add an optional written review of up to 500 characters together with the star rating. A review cannot be submitted without a star rating. The system must reject empty text, HTML and links, with a clear error message.
- The product page, search results and category lists must show the average rating, rounded to one decimal, and the number of ratings. A product without ratings must show a “no ratings yet” message instead of an average.
- Reviews are published immediately, listed newest first, with 10 reviews per page. Users can report a review for moderation. When a product is removed, its ratings and reviews are no longer displayed.

### 2. Age Verification for Alcoholic Products

**Vague Requirement:**
Alcoholic products require age verification. A modal should appear when navigating to the alcoholic products category asking if the user is 18+. Users must input their age before accessing the alcoholic products.

**Questions to be clarified:**

1. How should the age input field be displayed to the user?
2. Does the user type a number, a date of birth, or just click “I am 18+”?
3. Is it a self-declaration only, or is there a real check (ID, third-party service)?
4. Are alcoholic products visible (blurred or hidden) to unverified users in search results?
5. Does the age check apply only to the category page, or also to search results, favorites, basket, direct product URLs and promotions?
6. How should borderline products such as non-alcoholic beer or alcohol-filled chocolates be handled?
7. What happens to a user under 18: message, redirect, block? Can they retry with a different age?
8. Is there a limit on retries to prevent simply guessing an adult age?
9. What input is invalid, and what happens with it (empty, negative, non-numeric, future date, age 150)?
10. Can the modal be dismissed (close button, ESC, browser back)? What happens then?
11. How should a user who turns exactly 18 today be handled?
12. Is the result remembered for the session, per device (cookie), or in the user account? For how long?
13. When should the age verification be done? At registration or at checkout?
14. What if alcohol is already in the basket or favorites before verification, how should it be handled?
15. Is there a second age check at checkout or at delivery?

**Detailed requirements:**
- When a user navigates to the alcoholic products category, a modal must appear before any product is shown. The modal asks the user to enter their date of birth. Alcoholic products are those flagged as alcoholic in the product data.
- The system must validate that the user is at least 18 years old on the current date. If the user is under 18, an error message is displayed, access to the category is denied, and the user is redirected to the home page. Empty, non-date and future-date input must be rejected with an error message.
- The check must apply to every route to alcoholic products: search results, favorites, basket and direct product URLs. Alcoholic products must not be visible or addable to the basket for unverified users.
- A successful verification is remembered for the current session. The entered date of birth is not stored. Closing the modal (close button, ESC or browser back) must leave alcoholic products inaccessible.


### 3. Shipping Cost Changes

**Vague Requirement:**
Free shipping for orders above a certain amount. Orders below this amount will incur a shipping fee.

**Questions to be clarified:**

1. What is the threshold amount? It needs to be defined. Is it fixed or configurable by an admin?
2. What is the current shipping behavior, and what happens to orders and baskets already in progress at release?
3. Is the shipping cost variable according to the country or currency?
4. Is “above” strictly greater than the threshold, or greater than or equal?
5. Is the threshold applied before or after discounts and vouchers, and including or excluding VAT?
6. Do all products count toward the threshold, or are some excluded?
7. Is the fee below the threshold flat, or does it depend on weight, size, destination, delivery speed or number of items?
8. Where is the shipping cost shown? Is it going to be in the basket, checkout, order summary, confirmation email, and/or invoice?
9. Should the basket show how much more the user needs to spend for free shipping?
10. Is the total recalculated live when items are added, removed or quantities change?
11. What happens if a price changes between the basket and checkout?
12. Is VAT charged on the shipping fee, and how is it displayed?
13. Does free shipping also apply to express or other delivery methods?
14. Does it combine with promo codes and existing discounts? How is it calculated?
15. Are split shipments or multiple parcels possible, and is the threshold per order or per parcel?
16. If a returned item drops an order below the threshold, is the shipping fee charged retroactively?

**Detailed requirements:**
- Orders with a total of or above €200 (for example) must have free shipping, so the shipping cost is 0.00 €. The total is calculated after discounts and vouchers and includes VAT. Orders below this value must be charged a flat shipping fee of 5€ (for example) including VAT.
- The shipping cost must be displayed in the basket, at checkout, in the order summary, in the confirmation email and on the invoice. The total price is calculated as the product total minus discounts plus shipping, and it must update immediately when products or quantities change.
- The basket should show how much more the user needs to spend to get free shipping. When the threshold is reached, the shipping fee must disappear from the total.
- Baskets that are open at the time of release must be recalculated with the new shipping rules at checkout.
