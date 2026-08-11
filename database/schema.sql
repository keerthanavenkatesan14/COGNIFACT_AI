USE cognifact_ai;
CREATE TABLE Roles (
    RoleID INT IDENTITY(1,1) PRIMARY KEY,
    RoleName VARCHAR(50) NOT NULL UNIQUE,
    Description VARCHAR(255),
    CreatedAt DATETIME2 DEFAULT GETDATE()
);
GO

CREATE TABLE Users (
    UserID INT IDENTITY(1,1) PRIMARY KEY,

    FullName VARCHAR(150) NOT NULL,

    Email VARCHAR(255) NOT NULL UNIQUE,

    PasswordHash VARCHAR(255) NOT NULL,

    Phone VARCHAR(20),

    EmailVerified BIT NOT NULL DEFAULT 0,

    IsActive BIT NOT NULL DEFAULT 1,

    LastLoginAt DATETIME2 NULL,

    CreatedAt DATETIME2 DEFAULT GETDATE(),

    UpdatedAt DATETIME2 DEFAULT GETDATE()
);
GO

CREATE TABLE Factories (
    FactoryID INT IDENTITY(1,1) PRIMARY KEY,
    FactoryName VARCHAR(200) NOT NULL,
    Industry VARCHAR(150),
    RegistrationNumber VARCHAR(100),
    Address VARCHAR(500),
    City VARCHAR(100),
    State VARCHAR(100),
    Country VARCHAR(100) DEFAULT 'India',
    Pincode VARCHAR(20),
    ContactPhone VARCHAR(20),
    TimeZone VARCHAR(100) DEFAULT 'Asia/Kolkata',
    IsActive BIT NOT NULL DEFAULT 1,
    CreatedAt DATETIME2 DEFAULT GETDATE(),

    UpdatedAt DATETIME2 DEFAULT GETDATE()
);
GO

CREATE TABLE UserFactory (
    UserFactoryID INT IDENTITY(1,1) PRIMARY KEY,

    UserID INT NOT NULL,

    FactoryID INT NOT NULL,

    RoleID INT NOT NULL,

    IsPrimary BIT NOT NULL DEFAULT 1,

    JoinedAt DATETIME2 DEFAULT GETDATE(),

    CONSTRAINT FK_UserFactory_User
        FOREIGN KEY (UserID)
        REFERENCES Users(UserID),

    CONSTRAINT FK_UserFactory_Factory
        FOREIGN KEY (FactoryID)
        REFERENCES Factories(FactoryID),

    CONSTRAINT FK_UserFactory_Role
        FOREIGN KEY (RoleID)
        REFERENCES Roles(RoleID),

    CONSTRAINT UQ_UserFactory
        UNIQUE (UserID, FactoryID)
);
GO


CREATE TABLE Machines (
    MachineID INT IDENTITY(1,1) PRIMARY KEY,

    FactoryID INT NOT NULL,

    MachineCode VARCHAR(100) NOT NULL,

    MachineName VARCHAR(200) NOT NULL,

    MachineType VARCHAR(150),

    Manufacturer VARCHAR(150),

    Model VARCHAR(150),

    SerialNumber VARCHAR(150),

    InstallationDate DATE,

    OperatingHours DECIMAL(12,2) DEFAULT 0,

    MachineStatus VARCHAR(30) DEFAULT 'HEALTHY',

    LastMaintenanceDate DATE,

    NextMaintenanceDate DATE,
     IsActive BIT NOT NULL DEFAULT 1,

    CreatedAt DATETIME2 DEFAULT GETDATE(),

    UpdatedAt DATETIME2 DEFAULT GETDATE(),

    CONSTRAINT FK_Machines_Factory
        FOREIGN KEY (FactoryID)
        REFERENCES Factories(FactoryID),

    CONSTRAINT UQ_MachineCode_Factory
        UNIQUE (FactoryID, MachineCode)
);
GO


CREATE TABLE SensorData (
    SensorDataID BIGINT IDENTITY(1,1) PRIMARY KEY,

    FactoryID INT NOT NULL,

    MachineID INT NOT NULL,

    RecordedAt DATETIME2 NOT NULL,

    Temperature DECIMAL(10,2),

    Vibration DECIMAL(10,3),

    RPM DECIMAL(10,2),

    PowerConsumption DECIMAL(10,3),

    OperatingHours DECIMAL(12,2),

    CreatedAt DATETIME2 DEFAULT GETDATE(),

    CONSTRAINT FK_SensorData_Factory
        FOREIGN KEY (FactoryID)
        REFERENCES Factories(FactoryID),

    CONSTRAINT FK_SensorData_Machine
            FOREIGN KEY (MachineID)
        REFERENCES Machines(MachineID)
);
GO

CREATE TABLE MaintenanceRecords (
    MaintenanceID INT IDENTITY(1,1) PRIMARY KEY,

    FactoryID INT NOT NULL,

    MachineID INT NOT NULL,

    PerformedBy INT NULL,

    MaintenanceType VARCHAR(100) NOT NULL,

    Description VARCHAR(MAX),

    MaintenanceDate DATETIME2 NOT NULL,

    DowntimeHours DECIMAL(10,2) DEFAULT 0,

    Cost DECIMAL(12,2) DEFAULT 0,

    PartsReplaced VARCHAR(MAX),

    MaintenanceStatus VARCHAR(50) DEFAULT 'COMPLETED',

    CreatedAt DATETIME2 DEFAULT GETDATE(),

    CONSTRAINT FK_Maintenance_Factory
        FOREIGN KEY (FactoryID)
        REFERENCES Factories(FactoryID),

    CONSTRAINT FK_Maintenance_Machine
        FOREIGN KEY (MachineID)
        REFERENCES Machines(MachineID),

    CONSTRAINT FK_Maintenance_User
        FOREIGN KEY (PerformedBy)
        REFERENCES Users(UserID)
);
GO

CREATE TABLE Predictions (
    PredictionID INT IDENTITY(1,1) PRIMARY KEY,

    FactoryID INT NOT NULL,

    MachineID INT NOT NULL,

    PredictionTime DATETIME2 DEFAULT GETDATE(),

    FailureProbability DECIMAL(5,2) NOT NULL,

    RiskLevel VARCHAR(30) NOT NULL,

    PredictedFailureType VARCHAR(150),

    ModelName VARCHAR(100),

    ModelVersion VARCHAR(50),

    InputData VARCHAR(MAX),

    CreatedAt DATETIME2 DEFAULT GETDATE(),

    CONSTRAINT FK_Predictions_Factory
        FOREIGN KEY (FactoryID)
        REFERENCES Factories(FactoryID),
        CONSTRAINT FK_Predictions_Machine
        FOREIGN KEY (MachineID)
        REFERENCES Machines(MachineID)
);
GO

CREATE TABLE Recommendations (
    RecommendationID INT IDENTITY(1,1) PRIMARY KEY,

    FactoryID INT NOT NULL,

    MachineID INT NOT NULL,

    PredictionID INT NULL,

    Recommendation VARCHAR(MAX) NOT NULL,

    Reason VARCHAR(MAX),

    Priority VARCHAR(30) DEFAULT 'MEDIUM',

    RecommendationStatus VARCHAR(30) DEFAULT 'PENDING',

    RecommendedAction VARCHAR(255),

    DueDate DATETIME2 NULL,

    CompletedAt DATETIME2 NULL,
    CreatedAt DATETIME2 DEFAULT GETDATE(),

    CONSTRAINT FK_Recommendations_Factory
        FOREIGN KEY (FactoryID)
        REFERENCES Factories(FactoryID),

    CONSTRAINT FK_Recommendations_Machine
        FOREIGN KEY (MachineID)
        REFERENCES Machines(MachineID),

    CONSTRAINT FK_Recommendations_Prediction
        FOREIGN KEY (PredictionID)
        REFERENCES Predictions(PredictionID)
);
GO

CREATE TABLE AuditLogs (
    AuditLogID BIGINT IDENTITY(1,1) PRIMARY KEY,

    UserID INT NULL,

    FactoryID INT NULL,

    Action VARCHAR(100) NOT NULL,

    EntityType VARCHAR(100),

    EntityID INT,

    Details VARCHAR(MAX),

    IPAddress VARCHAR(45),

    CreatedAt DATETIME2 DEFAULT GETDATE(),

    CONSTRAINT FK_AuditLogs_User
        FOREIGN KEY (UserID)
        REFERENCES Users(UserID),

    CONSTRAINT FK_AuditLogs_Factory
        FOREIGN KEY (FactoryID)
        REFERENCES Factories(FactoryID)
);
GO

INSERT INTO Roles (RoleName, Description)
VALUES
('ADMIN', 'Factory administrator'),
('MANAGER', 'Factory manager'),
('OPERATOR', 'Machine operator');
GO

SELECT * FROM Roles;