INSERT INTO USERS(username, fullname, email, password, type, address)
    VALUES
    ('User1', 'Moustafa', 'mamutahr@umich.edu', 'sha512$a45ffdcc71884853a2cba9e6bc55e812$c739cef1aec45c6e345c8463136dc1ae2fe19963106cf748baf87c7102937aa96928aa1db7fe1d8da6bd343428ff3167f4500c8a61095fb771957b4367868fb8', 'Giver', '123 sesame st'),
    ('User2', 'James', 'james@umich.edu', 'sha512$a45ffdcc71884853a2cba9e6bc55e812$c739cef1aec45c6e345c8463136dc1ae2fe19963106cf748baf87c7102937aa96928aa1db7fe1d8da6bd343428ff3167f4500c8a61095fb771957b4367868fb8', 'Giver', '77 johnathan ave'),
    ('User3', 'George', 'george@umich.edu', 'sha512$a45ffdcc71884853a2cba9e6bc55e812$c739cef1aec45c6e345c8463136dc1ae2fe19963106cf748baf87c7102937aa96928aa1db7fe1d8da6bd343428ff3167f4500c8a61095fb771957b4367868fb8', 'Receiver', '9922 thirtyone st'),
    ('User4', 'Alex', 'alex@umich.edu', 'sha512$a45ffdcc71884853a2cba9e6bc55e812$c739cef1aec45c6e345c8463136dc1ae2fe19963106cf748baf87c7102937aa96928aa1db7fe1d8da6bd343428ff3167f4500c8a61095fb771957b4367868fb8', 'Driver', '0927 tenth st');

INSERT INTO REQUESTS(description, giverowner, receiveraccept, driveraccept)
    VALUES
    ('Chocolate', 'User1', 0, 0),
    ('Cookies', 'User1', 0, 0),
    ('Chips', 'User2', 0, 0),
    ('Fruit Please', 'User2', 0, 0);

INSERT INTO REQUESTS(description, giverowner, receiverowner, receiveraccept, driveraccept)
    VALUES
    ('Veggies', 'User1', 'User3', 1, 0),
    ('Cups', 'User2', 'User3', 1, 0),
    ('Plates', 'User2', 'User3', 1, 0),
    ('Spoons', 'User2', 'User3', 1, 0);

INSERT INTO REQUESTS(description, giverowner, receiverowner, driverowner, receiveraccept, driveraccept)
    VALUES
    ('paper', 'User1', 'User3', 'User4', 1, 1),
    ('tables', 'User1', 'User3', 'User4', 1, 1),
    ('books', 'User2', 'User3', 'User4', 1, 1),
    ('news', 'User2', 'User3', 'User4', 1, 1);