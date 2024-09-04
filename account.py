def get_customers(account_customer):
    acc_cus = dict()
    cus_acc = dict()
    res = []

    for i in range(len(account_customer)):
        acc_cus[account_customer[i][1]] = account_customer[i][0]

    for k, v in acc_cus.items():
        if v not in cus_acc:
            cus_acc[v] = [k]
        else:
            cus_acc[v].append(k)

    for k, v in cus_acc.items():
        if len(v) >= 2:
            res.append(v)

    print(res)

if __name__ == "__main__":
    account_customer = [(1, "a"), 
                        (2, "b"), 
                        (1, "c"), 
                        (3, "d"), 
                        (2, "e"), 
                        (4, "f"), 
                        (5, "y"), 
                        (2, "a"), 
                        (3, "e")]
    get_customers(account_customer)
            
    
