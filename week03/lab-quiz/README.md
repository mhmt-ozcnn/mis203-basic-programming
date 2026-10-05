-AI Tool Used: Codex
-Promt Used: Ask for order amount, available stock, requested quantity and whether the customer is a member. Reject invalid quantities or insufficient stock. Give members a 10% discount on approved orders of at least 500 TRY.
-I changed variable names. added comment how these codes work.
Test1:    
    Order amount (TRY): 490
    Available stock: 2
    Requested quantity: 1
    Is the customer a member? (yes/no): yes
    Order approved: stock is available.
    Final price: 490.00 TRY
Test2:    
    Order amount (TRY): 690
    Available stock: 2
    Requested quantity: 1
    Is the customer a member? (yes/no): yes
    Order approved: member discount applied.
    Final price: 621.00 TRY
Test3:
    Order amount (TRY): 750
    Available stock: 2
    Requested quantity: 1
    Is the customer a member? (yes/no): yes
    Order approved: member discount applied.
    Final price: 675.00 TRY