# Test Environment Setup

- **Application under test:** Grocery Mate Web Shop, <https://grocerymate.masterschool.com/>
- **Environment:** TEST
- **Test devices:** real devices with real browsers and operating systems, as listed below
- **Test data:** user accounts, products and baskets as listed in section 4 of `[Test_Execution.md](https://github.com/olugbemigaojumu/solid-umbrella/blob/main/STLC_Processes/Test%20Execution.md)`
- **Tools:** Postman for API checks, Jira for defect tracking

## Platforms

| Platform | Browser | Version | Used for execution |
|----------|---------|---------|--------------------|
| Windows 11 (PC, laptop) | Chrome | Latest stable | Yes, primary (all test cases) |
| Windows 11 (PC, laptop) | Firefox | Latest stable | Yes (UI test cases) |
| Windows 11 (PC, laptop) | Edge | Latest stable | Yes (smoke test and check-out) |
| macOS 15 (laptop) | Safari | 18 | Yes (UI test cases) |
| macOS 15 (laptop) | Chrome | Latest stable | Not planned |
| Android 15 (smartphone, tablet) | Chrome | Latest stable | Yes (age verification modal, basket and check-out) |
| iOS 18 (smartphone, tablet) | Safari | 18 | Yes (age verification modal, basket and check-out) |
