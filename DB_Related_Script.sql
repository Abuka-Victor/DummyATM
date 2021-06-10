-- Database Creation Script For DummyATM
CREATE DATABASE DummyATM 
ON
(
NAME = DummyATM,
FILENAME = 'C:\Program Files\Microsoft SQL Server\MSSQL11.MSSQLSERVER\MSSQL\DATA\DummyATM.mdf',
SIZE = 100MB,
MAXSIZE = UNLIMITED,
FILEGROWTH = 10MB
)
LOG ON 
(
NAME = DummyATM_log,
FILENAME = 'C:\Program Files\Microsoft SQL Server\MSSQL11.MSSQLSERVER\MSSQL\DATA\DummyATM.ldf',
SIZE = 40MB,
MAXSIZE = 200MB,
FILEGROWTH = 4MB 
)
GO

-- Table Creation Script
USE DummyATM
CREATE TABLE Atm (
					Email varchar(100) unique,
					First_Name varchar(100),
					Last_Name varchar(100),
					BVN numeric not null,
					Acc_No numeric primary key,
					Acc_Bal money,
)
GO

-- Table Insertion Script
USE DummyATM
INSERT INTO Atm (Email,First_Name,Last_Name,BVN,Acc_No,Acc_Bal)
VALUES('dyna156@gmail.com','Diana','Wolfskin',251378971,2289132456,250000)

INSERT INTO Atm (Email,First_Name,Last_Name,BVN,Acc_No,Acc_Bal)
VALUES('lyma@xyz.com','Lionel','Amar',255318991,2286842456,31000)

INSERT INTO Atm (Email,First_Name,Last_Name,BVN,Acc_No,Acc_Bal)
VALUES('tutsi888@yahoo.com','Adetutu','Olaniyi',228568311,9289142776,1000000)

INSERT INTO Atm (Email,First_Name,Last_Name,BVN,Acc_No,Acc_Bal)
VALUES('clinton@gmail.com','Clinton','Abosede',291318276,7289188856,1000)

INSERT INTO Atm (Email,First_Name,Last_Name,BVN,Acc_No,Acc_Bal)
VALUES('zandeke@hotmail.com','Ndarni','Musa',181678171,2436712456,560000)
GO
