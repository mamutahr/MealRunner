INSERT INTO USERS(username, fullname, email, password, type, address)
    VALUES
    ('MLB', 'Moustafa', 'mlb@umich.edu', 'sha512$a45ffdcc71884853a2cba9e6bc55e812$c739cef1aec45c6e345c8463136dc1ae2fe19963106cf748baf87c7102937aa96928aa1db7fe1d8da6bd343428ff3167f4500c8a61095fb771957b4367868fb8', 'Giver', 'Modern Languages Building, 812 E Washington St #4108, Ann Arbor, MI 48109'),
    ('CC Little', 'James', 'ccl@umich.edu', 'sha512$a45ffdcc71884853a2cba9e6bc55e812$c739cef1aec45c6e345c8463136dc1ae2fe19963106cf748baf87c7102937aa96928aa1db7fe1d8da6bd343428ff3167f4500c8a61095fb771957b4367868fb8', 'Receiver', '1100 N University Ave, Ann Arbor, MI 48109'),
    ('George', 'George', 'george@umich.edu', 'sha512$a45ffdcc71884853a2cba9e6bc55e812$c739cef1aec45c6e345c8463136dc1ae2fe19963106cf748baf87c7102937aa96928aa1db7fe1d8da6bd343428ff3167f4500c8a61095fb771957b4367868fb8', 'Driver', '9922 thirtyone st');

INSERT INTO REQUESTS(description, giverowner, receiveraccept, driveraccept)
    VALUES
    ('150 lb. apples', 'MLB', 0, 0),
    ('200 lb. chocolate', 'MLB', 0, 0),
    ('200 lb. canned food', 'MLB', 0, 0);