1. Write the XPath to locate the main **h1** element.
2. Write the XPath to select the **About Us** navigational link.
3. Write the XPath to select the **Graphic Design** dropdown link.
4. Write the XPath to select the team member’s name **Jane Smith**.
5. Write the XPath to select the description (which is inside the paragraph) of **SEO Services**. 
6. Write an XPath expression to select all service items in the "**Our Services**" section.
7. What is the XPath to select the **email input field** in the contact form?
8. How would you write an XPath to select the **entire contact form**?
9. Provide the XPath to select the **footer paragraph element**.
10. What is the XPath to select the **first team member**'s (`<h4>`) name?
11. How can you select the description of the **second service** item using XPath?
12. What is the XPath to select the "Contact Us" section header (`<h2>` element)?
13. Write an XPath expression to select all links within the dropdown under the "Services" navigation item.
14. What is the XPath to select the first `<li>` under the "Our Team" section?
15. Provide the XPath to locate the "Send Message" button in the contact form.


---

# XPath Practice on a Nested HTML Document

This document contains XPath expressions which are answers to the above questions for locating elements in a sample HTML page (a company site with a header, navigation, three sections and a footer).

## Page under test

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nested Complex HTML Document</title>
</head>
<body>
    <header>
        <h1 id="mainTitle">Welcome to Our Company</h1>
        <nav>
            <ul>
                <li><a href="#home" class="nav-link">Home</a></li>
                <li><a href="#about" class="nav-link">About Us</a></li>
                <li>
                    <a href="#services" class="nav-link">Services</a>
                    <ul class="dropdown">
                        <li><a href="#webdev">Web Development</a></li>
                        <li><a href="#graphicdesign">Graphic Design</a></li>
                        <li><a href="#seo">SEO Services</a></li>
                    </ul>
                </li>
                <li><a href="#contact" class="nav-link">Contact</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section id="about">
            <h2 class="sectionTitle">About Us</h2>
            <div class="content">
                <p>We are a leading company in the industry.</p>
                <div class="team">
                    <h3>Our Team</h3>
                    <ul>
                        <li>
                            <h4>John Doe</h4>
                            <p>CEO</p>
                        </li>
                        <li>
                            <h4>Jane Smith</h4>
                            <p>CTO</p>
                        </li>
                    </ul>
                </div>
            </div>
        </section>
        <section id="services">
            <h2 class="sectionTitle">Our Services</h2>
            <div class="service-list">
                <div class="service-item">
                    <h3>Web Development</h3>
                    <p>Creating stunning websites.</p>
                </div>
                <div class="service-item">
                    <h3>Graphic Design</h3>
                    <p>Designing visual content.</p>
                </div>
                <div class="service-item">
                    <h3>SEO Services</h3>
                    <p>Improving search engine rankings.</p>
                </div>
            </div>
        </section>
        <section id="contact">
            <h2 class="sectionTitle">Contact Us</h2>
            <form id="contactForm">
                <label for="name">Name:</label>
                <input type="text" id="name" required>
                <label for="email">Email:</label>
                <input type="email" id="email" required>
                <label for="message">Message:</label>
                <textarea id="message" placeholder="Your Message"></textarea>
                <input type="submit" value="Send Message">
            </form>
        </section>
    </main>
    <footer>
        <p>&copy; 2023 Company Name. All rights reserved.</p>
    </footer>
</body>
</html>
```

## The XPath Expressions

|    | Target | XPath |
|----|--------|-------|
| 1  | Main `<h1>` element | `//h1[@id='mainTitle']` |
| 2  | "About Us" navigation link | `//nav//a[normalize-space()='About Us']` |
| 3  | "Graphic Design" dropdown link | `//ul[@class='dropdown']//a[normalize-space()='Graphic Design']` |
| 4  | Team member "Jane Smith" | `//div[@class='team']//h4[normalize-space()='Jane Smith']` |
| 5  | Description of "SEO Services" | `//h3[normalize-space()='SEO Services']/following-sibling::p` |
| 6  | All service items in "Our Services" | `//section[@id='services']//div[@class='service-item']` |
| 7  | Email input field | `//input[@id='email']` |
| 8  | Entire contact form | `//form[@id='contactForm']` |
| 9  | Footer paragraph | `//footer/p` |
| 10 | First team member's name (`<h4>`) | `//div[@class='team']/ul/li[1]/h4` |
| 11 | Description of the second service item | `(//div[@class='service-item'])[2]/p` |
| 12 | "Contact Us" section header (`<h2>`) | `//section[@id='contact']/h2` |
| 13 | All links in the "Services" dropdown | `//ul[@class='dropdown']//a` |
| 14 | First `<li>` under "Our Team" | `//div[@class='team']/ul/li[1]` |
| 15 | "Send Message" button | `//input[@type='submit' and @value='Send Message']` |
