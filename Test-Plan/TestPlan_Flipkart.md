# Test Plan - Flipkart QA Portfolio

## 1. Project Overview
**Application:** Flipkart (E-commerce critical flows)  
**Objective:** Validate core user flows: Search → Product Details → Add to Cart → Checkout to ensure functional correctness, data integrity, and a good user experience.

## 2. Scope
**In Scope**
- Login/Authentication flows
- Product search & filtering
- Product details and add-to-cart
- Cart management
- Checkout: address entry, order summary, payment step (button flow)
- Basic API and DB validation for critical flows

**Out of Scope**
- Seller/vendor admin panels
- Deep performance/load testing
- Internationalization/localization testing beyond default locale

## 3. Test Approach
- **Manual testing:** Execute detailed test cases, exploratory sessions, smoke & regression cycles.
- **Automation:** Selenium + Python for critical happy-path flows (smoke).
- **API checks:** Use Postman for sanity checks (status codes, response schema).
- **DB checks:** Run SQL queries to verify order creation and data integrity.

## 4. Test Environment
- **Browser:** Chrome (latest stable), Windows 10/11
- **Devices:** Desktop (primary)
- **Test Data:** Use test/demo accounts; do not use real payment transactions (use mock or staging)
- **Tools:** Excel, GitHub, Selenium, Postman, sqlite/mysql client

## 5. Entry & Exit Criteria
**Entry**
- Test environment available and stable
- Test accounts created
- Test data seeded (products & addresses)

**Exit**
- All critical and high-severity defects fixed or accepted
- No open critical defects blocking release
- Test coverage for core flows executed

## 6. Risks & Mitigations
- **Risk:** Live payment gateway triggers real transactions  
  **Mitigation:** Use staging environment or mock payment gateway.
- **Risk:** Intermittent network causing flakiness  
  **Mitigation:** Use retries in automation; mark flaky tests and investigate.

## 7. Test Deliverables
- Test Plan (this document)
- Test Cases (Excel)
- Bug Reports (Markdown)
- Automation scripts (Selenium)
- How-to-demo guide
