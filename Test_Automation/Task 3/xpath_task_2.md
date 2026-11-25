## Market Mate Web Shop
 
Write stable XPath expressions for elements on the Market Mate shop's header and its sign-in page (`/auth`).

None of the elements below have an `id`, `name` or `data-testid`, so each XPath is anchored on attributes that describe the element's meaning (input `type`, `placeholder`) or on distinctive class names.
 
### Exercise 1: Xpath for User Icon (Home Page)
 
| Target              | XPath                                                                          |
|---------------------|--------------------------------------------------------------------------------|
| User icon (`<svg>`) | `//div[@class='social-icon-cont']/div[@class='headerIcon'][1]/*[name()='svg']` |


---

### Exercise 2: Xpath for Sign-in Page
 
Relevant HTML:
 
```html
<div class="auth-form">
  <form class="form">
    <input type="email" placeholder="Email address" class="form-input" required>
    <input type="password" placeholder="Password" class="form-input" required>
    <button type="submit" class="submit-btn">Sign In</button>
    <a href="#!" class="switch-link">Create a new account</a>
    <a href="#!" class="home-link">Go to Home</a>
  </form>
</div>
```
 
| Target                      | XPath                                                                                 |
|-----------------------------|---------------------------------------------------------------------------------------|
| Email address field         | `//div[@class='auth-form']//input[@type='email' and @placeholder='Email address']`    |
| Password field              | `//div[@class='auth-form']//input[@type='password' and @placeholder='Password']`      |
| Sign In button              | `//div[@class='auth-form']//button[@type='submit' and contains(@class,'submit-btn')]` |
| "Create a new account" link | `//div[@class='auth-form']//a[contains(@class,'switch-link')]`                        |
| "Go to Home" link           | `//div[@class='auth-form']//a[contains(@class,'home-link')]`                          |


---



### Exercise 3: Xpath for Sign-up Page
 
Relevant HTML:
 
```html
<div class="auth-form">
    <div class="auth-form-header">
        <img src="/static/media/Frame2.8640dfde1f04338ac04f.png"
             alt="logo" class="logo">
        <h4 class="header-title">We are MarketMate</h4>
    </div>

    <form class="form">
        <input type="text"
               placeholder="Full Name"
               class="form-input"
               required=""
               value="">

        <input type="email"
               placeholder="Email address"
               class="form-input"
               required=""
               value="">

        <input type="password"
               placeholder="Password"
               class="form-input"
               required=""
               value="">

        <button type="submit" class="submit-btn">Sign Up</button>

        <a href="#!" class="switch-link">
            Already have an account? Login
        </a>

        <a href="#!" class="home-link">Go to Home</a>
    </form>
</div>
```
 
| Target            | XPath                                                                                     |
|-------------------|-------------------------------------------------------------------------------------------|
| Full Name         | `//div[@class='auth-form']//form//input[@type='text' and @placeholder='Full Name']]`      |
| Email Field       | `//div[@class='auth-form']//form//input[@type='email' and @placeholder='Email address']`  |
| Password Field    | `//div[@class='auth-form']//form//input[@type='password' and @placeholder='Password']`    |
| Sign-up button    | `//div[@class='auth-form']//form//button[@type='submit' and normalize-space(.)='Sign Up'` |


---



### Exercise 4: Xpath for Confirm Button in Modal
 
Relevant HTML:
 
```html
<div class="modal-overlay">
    <div class="modal-content">

        <h2>Age Verification</h2>

        <p>
            You need to be +18 to see products.
            Please enter your birth date:
        </p>

        <input
            type="text"
            placeholder="DD-MM-YYYY"
            value=""
        />

        <button type="button">Confirm</button>

    </div>
</div>
```
 
| Target                  | XPath                                                                                               |
|-------------------------|-----------------------------------------------------------------------------------------------------|
| Confirm Button in Modal | `//div[@class='modal-overlay']//div[@class='modal-content']//button[normalize-space(.)='Confirm']`  |



---



### Exercise 5: Xpath for Control Elements in Oranges Product Card
 
Relevant HTML:
 
```html
<div class="product-card">
  <div class="card">
    <div class="card-header"><p class="lead">Oranges</p></div>
    <img src="..." alt="Oranges" class="card-img-top">
    <div class="card-body">
      <div class="content"><p class="category"><a href="#!" class="text-muted">Fresh Vegetables</a></p></div>
      <div class="content"><h5 class="discount-price">0.89€</h5></div>
      <div class="button-area">
        <div class="row">
          <div class="col-3"><input type="number" name="quantity_66b3a57b3fd5048eacb4798f" class="quantity" min="1" value="1"></div>
          <div class="col-7"><button class="btn btn-primary btn-cart">Add to Cart</button></div>
          <div class="col-1"><button class="btn btn-outline-dark ">❤</button></div>
        </div>
      </div>
    </div>
  </div>
</div>
```

 
| Target                               | XPath                                                                                                                         |
|--------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| Quantity input of Oranges            | `//div[@class='product-card'][.//p[@class='lead'][normalize-space()='Oranges']]//input[@class='quantity']`                    |
| "Add to Cart" button for Oranges     | `//div[@class='product-card'][.//p[@class='lead'][normalize-space()='Oranges']]//button[contains(@class,'btn-cart')]`         |
| Wish list (heart) button for Oranges | `//div[@class='product-card'][.//p[@class='lead'][normalize-space()='Oranges']]//button[contains(@class,'btn-outline-dark')]` |