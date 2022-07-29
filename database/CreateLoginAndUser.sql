USE [TheFacialDataBase]
GO
CREATE LOGIN [facial] WITH PASSWORD=N'facial', DEFAULT_DATABASE=[TheFacialDataBase], CHECK_EXPIRATION=OFF, CHECK_POLICY=OFF
GO

USE [TheFacialDataBase]
GO
CREATE USER [facial] FOR LOGIN [facial]
GO
USE [TheFacialDataBase]
GO
ALTER ROLE [db_owner] ADD MEMBER [facial]
