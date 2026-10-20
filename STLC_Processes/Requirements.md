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

### 2. Age Verification for Alcoholic Products

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

### 3. Shipping Cost Changes

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
