def find_unique_users(transactions):
    
    unique_users = set()  
    for transaction in transactions:
        unique_users.add(transaction[1])  
    return len(unique_users)

def highest_transaction(transactions):
    highest=transactions[0]
    for transcation in transactions:
        if transcation[2]>highest[2]:
            highest=transcation
    return highest
        

def separate_ids(transactions):
   
    transaction_ids = []
    user_ids = []
    
    for transaction in transactions:
        if len(transaction) != 4:
            raise ValueError(f"Inconsistent tuple size: {transaction}")
        transaction_ids.append(transaction[0])  
        user_ids.append(transaction[1])  
    
    return transaction_ids, user_ids

transactions_data = [
    (201, 'user1', 130.45, '2024-10-02 10:23:55'),
    (202, 'user2', 750.87, '2024-10-09 11:12:34'),
    (203, 'user3', 33.09, '2024-10-06 09:50:23'),
    (204, 'user2', 650.00, '2024-10-05 14:15:13'),
    (205, 'user1', 190.00, '2024-10-08 08:05:17')
]
unique_user_count = find_unique_users(transactions_data)
print("Total Unique Users:", unique_user_count)
highest_tx = highest_transaction(transactions_data)
print("Transaction with the Highest Amount:", highest_tx)
transaction_ids, user_ids = separate_ids(transactions_data)
print("Transaction IDs:", transaction_ids)
print("User IDs:", user_ids)
