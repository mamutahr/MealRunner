CREATE TABLE users (
    username VARCHAR2(50) PRIMARY KEY,
    fullname VARCHAR2(50) NOT NULL,
    email VARCHAR2(50) NOT NULL,
    password VARCHAR2(256) NOT NULL,
    type VARCHAR2(50) NOT NULL,
    address VARCHAR2(50) NOT NULL
);

CREATE TABLE requests (
    requestid INTEGER PRIMARY KEY,
    description VARCHAR2(100) NOT NULL,
    giverowner VARCHAR2(50) NOT NULL,
    receiverowner VARCHAR2(50),
    driverrowner VARCHAR2(50),
    receiveraccept INTEGER NOT NULL,
    driveraccept INTEGER NOT NULL,
    CONSTRAINT giver_owner 
        FOREIGN KEY (giverowner) REFERENCES USERS(USERNAME) ON DELETE CASCADE ON UPDATE CASCADE
);