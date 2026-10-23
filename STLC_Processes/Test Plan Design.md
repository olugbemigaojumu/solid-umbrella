> This doc prepares a very detailed test plan that includes all the resources, schedules, roles, resources and criteria to execute our tests and ensure nothing is left out or missing.


## Testplan design

### **1. Analyze the Product**

**Objective**

**What is the objective?**

**User Base**

**Who will the product be used by? Who are your user stakeholders?**

**Hardware and Software Specifications**

- **Hardware Requirements:**
    - Devices: PCs, laptops, smartphones, tablets
    - Specifications: Standard configurations for Android and iOS devices, desktops with minimum 4GB RAM, 2GHz processor
- **Software Requirements:**
    - Operating Systems: Windows, macOS, Android, iOS
    - Browsers: Chrome, Firefox, Safari, Edge
    - Dependencies: Backend services, third-party ad services, payment gateways

**Product Functionality**

**What is the functionality of the product? Existing and to be added functionality.**

### **2. Design the Test Strategy**

**Scope of Testing**

- **In Scope: Which functionalities are in scope of testing?**
- **Out of Scope: What is out of scope for testing?**

**Type of Testing**

**What types of testing is necessary for the new functionalities?**

**Risks and Issues**

- **Delays in development**
    - Mitigation: Implement a buffer period in the schedule.
- **Lack of test data**
    - Mitigation: Create mock data sets for testing purposes.
- **Resource unavailability**
    - Mitigation: Identify backup resources.

**Test Logistics**

- **Jane Smith** - Test Manager
- **John Doe** - QA Engineer (Functional and Regression Testing)
- **Alice Johnson** - QA Engineer (Performance and Security Testing)
- **Robert Brown** - QA Engineer (Usability Testing)
- **Maria Garcia** - End User for UAT

### **3. Define Test Objectives**

**Objectives**

- **Functionality:** Ensure new features and existing functionalities work as intended.
- **GUI:** Verify the graphical user interface for usability and consistency.
- **Performance:** Confirm the system's performance under expected load conditions.
- **Security:** Identify and mitigate potential security vulnerabilities.
- **Usability:** Assess the user-friendliness of the platform.

**Expected Outcomes**

- **Functionality:** All features perform correctly according to specifications.
- **GUI:** The interface is intuitive, responsive, and free of defects.
- **Performance:** The platform meets performance benchmarks under load.
- **Security:** No significant vulnerabilities are detected.
- **Usability:** Users can navigate and use the platform easily.

### **4. Define Test Criteria**

**Suspension Criteria**

- Testing will be suspended if critical defects are found that block further testing.
- Lack of necessary resources or test environment failures.

**Exit Criteria**

- All planned tests have been executed.
- Run Rate: At least 95% of all test cases have been executed.
- Pass Rate: At least 90% of executed test cases have passed.
- All critical and high-priority defects have been resolved and closed.
- No severity 1 or severity 2 defects are open.
- Performance metrics meet the defined standards.
- Security vulnerabilities have been identified and addressed.
- User acceptance testing has been completed, and sign-off has been obtained.

### **5. Resource Planning**

- **Human Resources:** QA team, development team, end users for UAT
- **Hardware:** PCs, laptops, smartphones, tablets
- **Software:** Browsers (Chrome, Firefox, Safari, Edge), operating systems (Windows, macOS, Android, iOS)
- **Infrastructure:** Test environments, automation tools, performance testing tools

### **6. Plan Test Environment**

- **Test Environments:** Real devices installed with real browsers and operating systems to simulate user conditions.
- **Environments:** Development (DEV), Testing (TEST), Acceptance (ACC), Production (PROD)

### **7. Schedule and Estimation**

| Activity | Start Date | End Date | Environment | Responsible Person | Estimated Effort |
| --- | --- | --- | --- | --- | --- |
| Test Planning | 01/08/2024 | 05/08/2024 | All | Test Manager | 20 hours |
| Test Case Design | 06/08/2024 | 15/08/2024 | All | QA Team | 40 hours |
| Unit Testing | 16/08/2024 | 25/08/2024 | DEV | Development Team | 60 hours |
| Integration Testing | 26/08/2024 | 30/08/2024 | TEST | QA Team | 30 hours |
| System Testing | 01/09/2024 | 10/09/2024 | TEST | QA Team | 80 hours |
| Regression Testing | 11/09/2024 | 15/09/2024 | TEST | QA Team | 40 hours |
| Performance Testing | 16/09/2024 | 18/09/2024 | TEST | QA Team | 20 hours |
| Security Testing | 19/09/2024 | 21/09/2024 | TEST | QA Team | 20 hours |
| UAT | 22/09/2024 | 30/09/2024 | ACC | End Users | 50 hours |
| Production Release | 01/10/2024 | 01/10/2024 | PROD | DevOps Team | 10 hours |

### **8. Determine Test Deliverables**

Documents/tools that must be created to support testing activities in the project:

- **Test Plan Document**
- **Test Cases and Test Scripts**
- **Test Data**
- **Test Reports**
- **Defect Reports**
- **UAT Sign-off Document**





---
---
---
---
---
---




# Test Plan: Grocery Mate Web Shop, New Features

| | |
|---|---|
| **Product** | Grocery Mate Web Shop, <https://grocerymate.masterschool.com/> |
| **Scope** | Product Rating System, Age Verification for Alcoholic Products, Shipping Cost Changes |
| **Based on** | Requirements document and critical tester questions (README) |
| **Status** | Draft. Assumed values: free shipping above 50 €, flat shipping fee of 4.95 €, review text of 10 to 500 characters. |

---

## 1. Analyze the Product

### Objective

Grocery Mate is an existing web shop where customers register, search and sort products, save favorites, fill a basket and check out. Three new features are being developed. The objective of testing is to verify that the new features meet their requirements, that they work together with the existing shop, and that the existing functionality has not been broken.

### User Base

**Users of the product**
- Shoppers who are registered and logged in
- Guests who browse without an account
- Adult shoppers and users under 18 who must be blocked from alcoholic products
- Shop staff who moderate reviews and manage product data

**User stakeholders**
- Product Owner (owns the requirements)
- Development team
- Test Manager and QA team
- Shop owner and customer support
- Legal and compliance (age verification and data protection)
- End users who take part in user acceptance testing (UAT)

### Hardware and Software Specifications

- **Hardware Requirements:**
    - Devices: PCs, laptops, smartphones, tablets
    - Specifications: Standard configurations for Android and iOS devices, desktops with minimum 4GB RAM, 2GHz processor
- **Software Requirements:**
    - Operating Systems: Windows, macOS, Android, iOS
    - Browsers: Chrome, Firefox, Safari, Edge
    - Dependencies: Backend services, payment gateways, email service for order confirmations

### Product Functionality

**Existing functionality**
1. Register and login
2. Searching for products, sorting on price, product categories
3. Add products to favorites
4. Add products to basket
5. Check-out: billing and sending information form, payment method, calculation of costs (total price)

**New functionality**

| ID | Feature | Summary of the detailed requirement |
|----|---------|-------------------------------------|
| F1 | Product Rating System | Logged-in users rate a product with 1 to 5 whole stars and can add optional written feedback of 10 to 500 characters. One rating per user and product, which the user can edit or delete. The product page, search results and category lists show the average and the number of ratings. A product without ratings shows a "no ratings yet" message. |
| F2 | Age Verification for Alcoholic Products | When a user opens the alcoholic products category, a modal asks for the date of birth before any product is shown. Users of 18 or older get access for the session. Under 18, invalid or dismissed input must keep alcoholic products inaccessible, also through search, favorites, basket and direct URLs. |
| F3 | Shipping Cost Changes | Orders above 50 € have free shipping. Orders of 50 € or less pay a flat shipping fee of 4.95 € including VAT. The cost is shown in the basket, at checkout, in the order summary, in the confirmation email and on the invoice. The total updates immediately when the basket changes. |

**Areas of the existing shop affected by the new features**

| Existing functionality | Affected by |
|------------------------|-------------|
| Register and login | F1 (only logged-in users can rate) |
| Search, sort and categories | F1 (average rating, optional sorting by rating), F2 (alcoholic products in search results) |
| Favorites | F2 (alcoholic products in favorites) |
| Basket | F2 (alcoholic products in the basket), F3 (shipping cost and total) |
| Check-out and total price calculation | F3 (shipping cost, discounts, VAT) |

---

## 2. Design the Test Strategy

### Scope of Testing

- **In Scope:**
    - F1: rating input, validation, editing and deleting, average calculation, display, moderation and reporting
    - F2: modal behavior, age validation, access control across all routes to alcoholic products, session handling
    - F3: threshold logic, shipping fee, total price calculation, display in all places, interaction with discounts and vouchers
    - Integration points: login, search, sort, favorites, basket and checkout
    - Regression of the existing functionality listed in section 1
- **Out of Scope:**
    - Internal behavior of the payment gateway and other third-party services
    - Real identity checks (ID or third-party age verification), because the requirement is a self-declaration of the age
    - Carrier and delivery integration
    - Legal approval of the age verification method (handled by compliance)
    - Load tests beyond the expected load

### Type of Testing

| Feature | Test types and techniques |
|---------|---------------------------|
| F1 Product Rating | Functional testing, equivalence partitioning and boundary value analysis (stars 0 to 6, review length 0, 9, 10, 500, 501), average calculation tests, negative tests (HTML, links, empty input), usability testing |
| F2 Age Verification | State transition testing (unverified, verified, blocked, modal dismissed), boundary value analysis (age 17 and 18, born exactly 18 years ago), invalid input tests, access tests for every route (search, favorites, basket, direct URL), security tests (bypass of the check) |
| F3 Shipping Costs | Boundary value analysis around 50 € (49.99 €, 50.00 €, 50.01 €), decision table testing (threshold, discount, voucher, VAT), calculation checks of the total price, API tests with Postman, regression of checkout |
| All | Smoke test on every new build, regression testing, GUI and cross-browser testing, accessibility checks, performance testing, security testing (XSS in review text, tampering with shipping cost through the API), exploratory testing, user acceptance testing (UAT) |

**Automation:** Stable regression and API checks are automated (Python, Selenium, Pytest, Postman). New features are tested manually first and automated once they are stable.

### Risks and Issues

| Risk | Impact | Mitigation |
|------|--------|------------|
| Incomplete requirements (for example no threshold amount for shipping, unclear age input) | Tests cannot be designed or results cannot be judged | Clarify the open questions with the product owner before test design and confirm the assumed values (50 € threshold, 4.95 € fee). Keep a requirements Q&A log. |
| Delays in development | Less time for testing | Implement a buffer period in the schedule. |
| Lack of test data | Scenarios cannot be executed | Create mock data sets: products with 0, 1 and many ratings, alcoholic and non-alcoholic products, baskets around the shipping threshold, users of different ages. |
| Resource unavailability | Schedule slips | Identify backup resources. |
| Errors in the total price or shipping calculation | Direct financial impact | Treat F3 as high priority, with boundary and decision table tests and API-level checks. |
| Age check can be bypassed | Legal and reputational risk | Test every route to alcoholic products and test on server side as well. Involve compliance. |
| Unsafe review input (XSS, links) | Security vulnerability | Include injection tests in security testing. |
| Test environment is unstable or differs from production | Unreliable results | Smoke test every deployment. Keep ACC as close to PROD as possible. |

### Test Logistics

| Role | Name | Responsibility |
|------|------|----------------|
| Test Manager | Jane Smith | Test planning, requirements clarification with the product owner, coordination, reporting |
| QA Engineer (Functional and Regression Testing) | John Doe | F1 to F3 functional tests, regression |
| QA Engineer (Performance and Security Testing) | Alice Johnson | Performance and security tests, API checks |
| QA Engineer (Usability Testing) | Robert Brown | GUI, usability, accessibility, cross-browser |
| End User for UAT | Maria Garcia | User acceptance testing |

---

## 3. Define Test Objectives

| Objective | Expected Outcome |
|-----------|------------------|
| **Functionality:** Ensure the new features and the existing functionalities work as intended. | Ratings and reviews are saved, validated and displayed correctly. Only users aged 18 or older can access alcoholic products. Shipping costs and totals are calculated correctly. Existing functions show no regression. |
| **GUI:** Verify the graphical user interface for usability and consistency. | The rating stars, review form, age modal and shipping cost lines are consistent with the shop design, responsive on all devices and free of defects. |
| **Performance:** Confirm the system's performance under expected load conditions. | Product pages with many reviews, the modal and the basket and checkout total calculation respond in under 3 seconds for 95% of requests with 100 concurrent users. |
| **Security:** Identify and mitigate potential security vulnerabilities. | Review input cannot inject scripts. The age check cannot be bypassed by direct URLs, the API or the browser. Shipping cost cannot be manipulated by the client. |
| **Usability:** Assess the user-friendliness of the platform. | Users can rate a product, pass the age check and understand the shipping cost and the amount missing for free shipping without help. |

---

## 4. Define Test Criteria

### Entry Criteria

- The requirements are approved and the open questions are answered and documented in the Requirements Q&A Log, including the values 50 € (free shipping threshold), 4.95 € (shipping fee) and 10 to 500 characters (review text).
- The test plan is approved by the Test Manager (Jane Smith).
- Test cases are designed and reviewed, and the test data is prepared.
- The new features are developed and unit testing has been completed with no open critical defects.
- The build is deployed to the TEST environment and passes the smoke test.
- The test environment, devices, browsers, tools (Selenium, Pytest, Postman, Jira) and user accounts are available to the QA team.

### Suspension Criteria

- Testing will be suspended if critical defects are found that block further testing.
- Lack of necessary resources or test environment failures.
- The build fails the smoke test.
- Requirements that are needed to continue testing change or remain unconfirmed, for example the shipping threshold.

### Exit Criteria

- All planned tests have been executed.
- Run Rate: At least 95% of all test cases have been executed.
- Pass Rate: At least 90% of executed test cases have passed.
- All critical and high-priority defects have been resolved and closed.
- No severity 1 or severity 2 defects are open.
- All test cases for the age check (F2) and for the shipping and total price calculation (F3) have been executed and passed.
- Performance metrics meet the defined standards (95% of requests under 3 seconds with 100 concurrent users).
- Security vulnerabilities have been identified and addressed.
- User acceptance testing has been completed, and sign-off has been obtained.

---

## 5. Resource Planning

- **Human Resources:** Test Manager, QA team, development team, DevOps team, product owner, end users for UAT
- **Hardware:** PCs, laptops, smartphones, tablets
- **Software:** Browsers (Chrome, Firefox, Safari, Edge), operating systems (Windows, macOS, Android, iOS)
- **Infrastructure:** Test environments, automation tools (Python with Selenium and Pytest, Postman for API tests), performance testing tool (for example Locust or JMeter), security scanner (for example OWASP ZAP), Jira for test and defect tracking, Git and a CI/CD pipeline for automated runs

---

## 6. Plan Test Environment

- **Test Environments:** Real devices installed with real browsers and operating systems to simulate user conditions.
- **Environments:**

| Environment | Purpose |
|-------------|---------|
| Development (DEV) | Unit testing by developers |
| Testing (TEST) | Integration, system, regression, performance, security and usability testing by the QA team |
| Acceptance (ACC) | User acceptance testing with end users |
| Production (PROD) | Release and smoke test after release |

**Test matrix**

| Platform | Browsers |
|----------|----------|
| Windows (PC, laptop) | Chrome, Firefox, Edge |
| macOS (laptop) | Safari, Chrome |
| Android (smartphone, tablet) | Chrome |
| iOS (smartphone, tablet) | Safari |

**Test data**
- Users: guest, registered user, user aged 17, user aged 18, user who just turned 18, moderator or admin
- Products: with no, one and many ratings, alcoholic, non-alcoholic and borderline (for example non-alcoholic beer)
- Baskets: totals of 49.99 €, 50.00 € and 50.01 €, with and without discounts and vouchers

---

## 7. Schedule and Estimation

| Activity | Start Date | End Date | Environment | Responsible Person | Estimated Effort |
| --- | --- | --- | --- | --- | --- |
| Requirements Review and Clarification | 02/11/2026 | 03/11/2026 | All | Test Manager, QA Team | 12 hours |
| Test Planning | 04/11/2026 | 05/11/2026 | All | Test Manager | 12 hours |
| Test Case Design | 06/11/2026 | 13/11/2026 | All | QA Team | 40 hours |
| Unit Testing | 16/11/2026 | 20/11/2026 | DEV | Development Team | 40 hours |
| Integration Testing | 23/11/2026 | 25/11/2026 | TEST | QA Team | 24 hours |
| System Testing | 26/11/2026 | 04/12/2026 | TEST | QA Team | 60 hours |
| Regression Testing | 07/12/2026 | 09/12/2026 | TEST | QA Team | 24 hours |
| Performance Testing | 10/12/2026 | 11/12/2026 | TEST | QA Team | 16 hours |
| Security Testing | 14/12/2026 | 15/12/2026 | TEST | QA Team | 16 hours |
| Usability and Compatibility Testing | 16/12/2026 | 17/12/2026 | TEST | QA Team | 16 hours |
| UAT | 18/12/2026 | 23/12/2026 | ACC | End Users | 30 hours |
| Production Release | 11/01/2027 | 11/01/2027 | PROD | DevOps Team | 8 hours |
| **Total** | | | | | **298 hours** |

The dates assume that the builds are delivered on time. The schedule contains a buffer for delays in development and for retesting after defect fixes.

---

## 8. Determine Test Deliverables

Documents/tools that must be created to support testing activities in the project:

- **Test Plan Document**
- **Requirements Q&A Log** (answers to the critical questions)
- **Test Cases and Test Scripts** (manual and automated)
- **Requirements Traceability Matrix** (F1 to F3 linked to test cases)
- **Test Data**
- **Test Reports** (progress reports and a final test summary report)
- **Defect Reports**
- **UAT Sign-off Document**
