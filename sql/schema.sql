CREATE TABLE USERS (
    username VARCHAR2(50) PRIMARY KEY,
    fullname VARCHAR2(50) NOT NULL,
    email VARCHAR2(50) NOT NULL,
    password VARCHAR2(256) NOT NULL,
    type INTEGER NOT NULL
);

CREATE TABLE REQUESTS (
    requestid INTEGER PRIMARY KEY,
    giverowner VARCHAR2(50) NOT NULL,
    recieverowner VARCHAR2(50),
    recieveraccept INTEGER NOT NULL,
    driveraccept INTEGER NOT NULL,
    CONSTRAINT giver_owner 
        FOREIGN KEY (giverowner) REFERENCES USERS(USERNAME) ON DELETE CASCADE ON UPDATE CASCADE
);