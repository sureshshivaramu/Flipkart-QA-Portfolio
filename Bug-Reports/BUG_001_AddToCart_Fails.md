# BUG_001_AddToCart_Fails

**ID:** BUG_001  
**Title:** Add to Cart button not working on product page for selected variant  
**Reported By:** SNR  
**Date:** 2025-09-25  
**Environment:** Chrome 117, Staging (staging.flipkart.example)  
**Priority:** High  
**Severity:** Major

## Steps to Reproduce
1. Open product: Product ABC (product id: 1234)  
2. Select variant: Color - Blue, Storage - 128GB  
3. Click 'Add to Cart'  
4. Observe no item added and no error message

## Actual Result
Clicking 'Add to Cart' does not add the item to the cart. No message is shown.

## Expected Result
Product should be added to cart and cart count should update.

## Attachments
- screenshots/annotated_add_to_cart.png

## Notes
Occurs intermittently. Appears on specific variants only.
