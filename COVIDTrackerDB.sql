CREATE TABLE IF NOT EXISTS Person(
    email VARCHAR(32),
    password CHAR(64), 
    firstName VARCHAR(16),
    lastName VARCHAR(16),
    phoneNumber VARCHAR(11),
    country VARCHAR(36),
    state VARCHAR(3),
    PRIMARY KEY (email)
);

CREATE TABLE IF NOT EXISTS History(
    email VARCHAR(32),
    requestID INT NOT NULL AUTO_INCREMENT,
    timeRequest Timestamp,
    locCountry VARCHAR(4),
    casesCountry INT,
    deathsCountry INT,
    locState VARCHAR(4),
    casesState INT,
    deathsState INT,
    locCounty VARCHAR(20),
    casesCounty INT,
    deathsCounty INT,
    PRIMARY KEY(requestID, email),
    FOREIGN KEY(email) REFERENCES Person(email)
);
