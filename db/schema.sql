SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
DROP DATABASE IF EXISTS `JohmpsonClothing`;
CREATE DATABASE `JohmpsonClothing`;

USE `JohmpsonClothing` ;

-- -----------------------------------------------------
-- Table `mydb`.`Employee`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `JohmpsonClothing`.`Employee`;
CREATE TABLE `JohmpsonClothing`.`Employee`(
  `EmpID` INT NOT NULL AUTO_INCREMENT,
  `LastName` VARCHAR(45) NOT NULL,
  `FirstName` VARCHAR(45) NOT NULL,
  `Title` VARCHAR(45) NOT NULL,
  `ReportsTo` INT NULL,
  `Phone` VARCHAR(15) NOT NULL,
  `Email` VARCHAR(255) NULL,
  `Address` VARCHAR(55) NOT NULL,
  `City` VARCHAR(45) NOT NULL,
  `State` VARCHAR(45) NOT NULL,
  `Zip` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`EmpID`),
  INDEX `ReportsTo_idx` (`ReportsTo` ASC),
  CONSTRAINT `ReportsTo`
    FOREIGN KEY (`ReportsTo`)
    REFERENCES `JohmpsonClothing`.`Employee` (`EmpID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Customer`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `JohmpsonClothing`.`Customer`;
CREATE TABLE `JohmpsonClothing`.`Customer` (
  `CustomerID` INT NOT NULL AUTO_INCREMENT,
  `Password` VARCHAR(255) NOT NULL,
  `LastName` VARCHAR(45) NOT NULL,
  `FirstName` VARCHAR(45) NOT NULL,
  `Address` VARCHAR(55) NOT NULL,
  `City` VARCHAR(45) NOT NULL,
  `State` VARCHAR(45) NOT NULL,
  `Zip` VARCHAR(45) NOT NULL,
  `Phone` VARCHAR(255) NOT NULL,
  `Email` VARCHAR(255) NULL,
  PRIMARY KEY (`CustomerID`))
ENGINE = InnoDB;

DROP TABLE IF EXISTS `JohmpsonClothing`.`CreditCards`;
CREATE TABLE `JohmpsonClothing`.`CreditCards` (
  `CardNumber` varchar(32) NOT NULL,
  `SecurityCode` varchar(3) NOT NULL,
  `Customer` int NOT NULL,
  `ExpirationDate` varchar(7) NOT NULL,
  PRIMARY KEY (`CardNumber`),
  INDEX `Customer_idx` (`Customer` ASC),
  CONSTRAINT `Customer`
    FOREIGN KEY (`Customer`)
    REFERENCES `JohmpsonClothing`.`Customer` (`CustomerID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `mydb`.`Invoice`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `JohmpsonClothing`.`Invoice`;
CREATE TABLE `JohmpsonClothing`.`Invoice` (
  `InvoiceID` INT NOT NULL AUTO_INCREMENT,
  `CustomerID` INT NOT NULL,
  `BillingAddress` VARCHAR(55) NOT NULL,
  `BillingCity` VARCHAR(45) NOT NULL,
  `BillingState` VARCHAR(45) NOT NULL,
  `BillingZip` VARCHAR(45) NOT NULL,
  `DateOfInvoice` DATE NOT NULL,
  PRIMARY KEY (`InvoiceID`),
  INDEX `CustomerID_idx` (`CustomerID` ASC),
  CONSTRAINT `CustomerID`
    FOREIGN KEY (`CustomerID`)
    REFERENCES `JohmpsonClothing`.`Customer` (`CustomerID`)
    ON DELETE Cascade
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Stores`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `JohmpsonClothing`.`Stores`;
CREATE TABLE `JohmpsonClothing`.`Stores` (
  `StoreID` INT NOT NULL AUTO_INCREMENT,
  `Address` VARCHAR(55) NOT NULL,
  `City` VARCHAR(45) NOT NULL,
  `State` VARCHAR(45) NOT NULL,
  `Zip` VARCHAR(45) NOT NULL,
  `ManagedBy` INT NOT NULL,
  PRIMARY KEY (`StoreID`),
  INDEX `ManagedBy_idx` (`ManagedBy` ASC),
  CONSTRAINT `ManagedBy`
    FOREIGN KEY (`ManagedBy`)
    REFERENCES `JohmpsonClothing`.`Employee` (`EmpID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Clothing`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `JohmpsonClothing`.`Clothing`;
CREATE TABLE `JohmpsonClothing`.`Clothing` (
  `ClothingID` INT NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(55) NOT NULL,
  `Type` VARCHAR(55) NOT NULL,
  `Season` VARCHAR(6) NULL,
  `Price` DECIMAL(10,2) NOT NULL,
  `Material` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`ClothingID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`StoresClothing`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `JohmpsonClothing`.`StoresClothing`;
CREATE TABLE `JohmpsonClothing`.`StoresClothing` (
  `StoreID` INT NOT NULL,
  `ClothingID` INT NOT NULL,
  `Inventory` INT NOT NULL,
  PRIMARY KEY (`StoreID`, `ClothingID`),
  INDEX `ClothingID_idx` (`ClothingID` ASC),
  CONSTRAINT `StoreID`
    FOREIGN KEY (`StoreID`)
    REFERENCES `JohmpsonClothing`.`Stores` (`StoreID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `ClothingID`
    FOREIGN KEY (`ClothingID`)
    REFERENCES `JohmpsonClothing`.`Clothing` (`ClothingID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`InvoiceLine`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `JohmpsonClothing`.`InvoiceLine`;
CREATE TABLE `JohmpsonClothing`.`InvoiceLine` (
  `InvoiceLineID` INT NOT NULL AUTO_INCREMENT,
  `InvoiceID` INT NOT NULL,
  `ClothingID` INT NOT NULL,
  `Quantity` INT NOT NULL,
  `SoldFor` DECIMAL(10,2) NOT NULL,
  `Credit` varchar(32) NOT NULL,
  PRIMARY KEY (`InvoiceLineID`),
    FOREIGN KEY (`InvoiceID`)
    REFERENCES `JohmpsonClothing`.`Invoice` (`InvoiceID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    FOREIGN KEY (`ClothingID`)
    REFERENCES `JohmpsonClothing`.`Clothing` (`ClothingID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
	FOREIGN KEY (`Credit`)
    REFERENCES `JohmpsonClothing`.`CreditCards` (`CardNumber`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

INSERT INTO `JohmpsonClothing`.`Employee` (`EmpID`,`LastName`,`FirstName`,`Title`,`ReportsTo`,`Phone`,`Email`,`Address`,`City`,`State`,`Zip`) VALUES
(1,"Sears","Ciaran","CEO",NULL,"(114) 605-6055","fringilla.ornare.placerat@Duis.edu","Ap #442-4429 Curabitur Ave","Dover","DE","04329"),
(2,"Lynch","Tyrone","CIO",1,"(417) 942-8861","In.faucibus@ornareFusce.co.uk","835-3713 Id Rd.","Kenosha","WI","00954"),
(3,"Lindsay","Shaeleigh","CFO,",1,"(914) 161-2704","Ut@ullamcorpervelitin.co.uk","8357 Lectus Av.","Cheyenne","WY","40087"),
(4,"Salazar","Lillian","General Managaer",1,"(930) 556-4317","tincidunt@estcongue.net","P.O. Box 296, 640 Egestas. Rd.","Orlando","FL","50581"),
(5,"Mueller","Gil","Store Manager",4,"(826) 357-1010","erat@nonlorem.edu","P.O. Box 692, 4222 Est, St.","Grand Island","NE","64566"),
(6,"Chang","Shelley","Store Manager",4,"(267) 206-7475","vel.lectus.Cum@velitQuisque.ca","P.O. Box 986, 724 Laoreet St.","Idaho Falls","ID","08475"),
(7,"Spears","Phillip","Store Manager",4,"(208) 421-1981","diam.Sed@mi.com","Ap #375-3394 Curabitur Rd.","Tucson","AZ","76751"),
(8,"Vang","Deborah","Store Manager",4,"(599) 123-0262","dui@aaliquet.ca","216-4760 Vulputate Street","New Haven","CT","19173"),
(9,"Dotson","Daria","Store Manager",4,"(572) 628-1505","nisi@vulputateposuere.co.uk","Ap #741-1478 Enim Road","Topeka","KS","59302"),
(10,"Palmer","Wanda","Clerk",5,"(414) 996-1146","luctus.felis@liberomaurisaliquam.co.uk","124-4898 Sagittis Av.","Fort Wayne","IN","85970"),
(11,"Mcmahon","Chanda","Clerk",6,"(985) 425-4561","massa@Suspendissetristiqueneque.edu","7043 Odio. Rd.","Cleveland","OH","91829"),
(12,"Summers","Jolie","Clerk",7,"(775) 788-6037","quam@penatibus.ca","P.O. Box 261, 9169 Gravida. St.","Gresham","OR","59911"),
(13,"Fox","Patricia","Clerk",8,"(517) 531-5767","sociis.natoque.penatibus@nuncnulla.com","Ap #326-7180 Egestas. St.","Frederick","MD","97073"),
(14,"Jennings","Demetrius","Clerk",9,"(468) 278-8835","lectus.ante@nislQuisquefringilla.ca","P.O. Box 489, 686 Magna. Avenue","Chesapeake","VA","67583"),
(15,"Trevino","Elliott","Clerk",5,"(417) 987-1450","in@Nullaaliquet.co.uk","5396 Libero. Road","Kansas City","MO","30893"),
(16,"Cabrera","Ross","Developer",2,"(977) 355-4127","Donec@vitaenibhDonec.co.uk","5821 Donec Ave","Pocatello","ID","48576"),
(17,"Preston","Aladdin","Developer",2,"(702) 649-2332","malesuada@sagittisNullam.com","Ap #932-1629 Vivamus Rd.","Wichita","KS","73289"),
(18,"Tucker","Molly","Accountant",3,"(781) 910-0157","vel.est@placerateget.org","219-3247 Sed Avenue","Toledo","OH","41967"),
(19,"Villarreal","Shaine","Accountant",3,"(212) 992-2482","dolor.sit.amet@bibendumsed.ca","611-2195 Velit. Ave","Milwaukee","WI","27795"),
(20,"Nichols","Jessica","DB Admin",2,"(669) 574-8138","quam.Pellentesque@dignissimmagna.ca","6120 Faucibus. Street","Springfield","IL","17193");

insert into `JohmpsonClothing`.`Clothing` (ClothingID, Name, Type, Season, Price, Material) values (1, 'Mr. Dope', 'Shorts', 'Summer', 20.00, 'Cotton');
insert into `JohmpsonClothing`.`Clothing` (ClothingID, Name, Type, Season, Price, Material) values (2, 'The Antonio', 'Button-Down Shirt', 'Spring', 40.00, 'Cotton');
insert into `JohmpsonClothing`.`Clothing` (ClothingID, Name, Type, Season, Price, Material) values (3, 'Hipster Jeans', 'Pants', 'Yearly', 50.00, 'Denim');
insert into `JohmpsonClothing`.`Clothing` (ClothingID, Name, Type, Season, Price, Material) values (4, 'La Maria', 'T-Shirt', 'Summer', 20.00, 'Cotton');
insert into `JohmpsonClothing`.`Clothing` (ClothingID, Name, Type, Season, Price, Material) values (5, 'Henries', 'Socks', 'Yearly', 5.00, 'Cotton');
insert into `JohmpsonClothing`.`Clothing` (ClothingID, Name, Type, Season, Price, Material) values (6, 'Mens No-Shows', 'Underwear', 'Yearly', 5.00, 'Cotton');
insert into `JohmpsonClothing`.`Clothing` (ClothingID, Name, Type, Season, Price, Material) values (7, 'Womens No-Shows', 'Underwear', 'Yearly', 5.00, 'Cotton');
insert into `JohmpsonClothing`.`Clothing` (ClothingID, Name, Type, Season, Price, Material) values (8, 'Royale', 'Sweater', 'Fall', 35.00, 'Wool');
insert into `JohmpsonClothing`.`Clothing` (ClothingID, Name, Type, Season, Price, Material) values (9, 'The Revolution', 'Jacket', 'Winter', 100.00, 'Leather');
insert into `JohmpsonClothing`.`Clothing` (ClothingID, Name, Type, Season, Price, Material) values (10, 'The Lumber Jack', 'Button-Down Shirt', 'Fall', 50.00, 'Flanel');
insert into `JohmpsonClothing`.`Clothing` (ClothingID, Name, Type, Season, Price, Material) values (11, 'Swag Rag', 'Scarf', 'Winter', 30.00, 'Wool');
insert into `JohmpsonClothing`.`Clothing` (ClothingID, Name, Type, Season, Price, Material) values (12, 'Los Chinos', 'Pants', 'Spring', 40.00, 'Chino');
insert into `JohmpsonClothing`.`Clothing` (ClothingID, Name, Type, Season, Price, Material) values (13, 'Sun Dress', 'Dress', 'Summer', 40.00, 'Cotton');
insert into `JohmpsonClothing`.`Clothing` (ClothingID, Name, Type, Season, Price, Material) values (14, 'Flower Dress', 'Dress', 'Spring', 40.00, 'Cotton');
insert into `JohmpsonClothing`.`Clothing` (ClothingID, Name, Type, Season, Price, Material) values (15, 'Ice Queen', 'Coat', 'Winter', 100.00, 'Wool');
insert into `JohmpsonClothing`.`Clothing` (ClothingID, Name, Type, Season, Price, Material) values (16, 'Apple-Bottom Jeans', 'Pants', 'Yearly', 50.00, 'Denim');
insert into `JohmpsonClothing`.`Clothing` (ClothingID, Name, Type, Season, Price, Material) values (17, 'Cut-Off Jorts', 'Shorts', 'Summer', 30.00, 'Denim');
insert into `JohmpsonClothing`.`Clothing` (ClothingID, Name, Type, Season, Price, Material) values (18, 'Croissant', 'T-Shirt', 'Spring', 25.00, 'Cotton');
insert into `JohmpsonClothing`.`Clothing` (ClothingID, Name, Type, Season, Price, Material) values (19, 'Monalisa', 'T-Shirt', 'Spring', 25.00, 'Cotton');
insert into `JohmpsonClothing`.`Clothing` (ClothingID, Name, Type, Season, Price, Material) values (20, 'Thugnificent', 'T-Shirt', 'Summer', 20.00, 'Cotton');

insert into `JohmpsonClothing`.`Stores` (StoreID, Address, City, State, Zip, ManagedBy) values (1, '6 Emmet Plaza', 'West Palm Beach', 'FL', '33416', 5);
insert into `JohmpsonClothing`.`Stores` (StoreID, Address, City, State, Zip, ManagedBy) values (2, '9008 8th Trail', 'Washington', 'DC', '20397', 6);
insert into `JohmpsonClothing`.`Stores` (StoreID, Address, City, State, Zip, ManagedBy) values (3, '946 Badeau Lane', 'New York City', 'NY', '10045', 7);
insert into `JohmpsonClothing`.`Stores` (StoreID, Address, City, State, Zip, ManagedBy) values (4, '061 Golf View Alley', 'Toledo', 'OH', '43635', 8);
insert into `JohmpsonClothing`.`Stores` (StoreID, Address, City, State, Zip, ManagedBy) values (5, '407 Packers Circle', 'Tulsa', 'OK', '74156', 9);

insert into `JohmpsonClothing`.`StoresClothing` (StoreID,ClothingID,Inventory) values
(1,1,86),
(1,2,7),
(1,3,50),
(1,4,81),
(1,5,32),
(1,6,74),
(1,7,69),
(1,8,95),
(1,9,29),
(1,10,58),
(1,11,31),
(1,12,38),
(1,13,14),
(1,14,39),
(1,15,48),
(1,16,12),
(1,17,43),
(1,18,76),
(1,19,23),
(1,20,31),
(2,1,74),
(2,2,7),
(2,3,40),
(2,4,27),
(2,5,99),
(2,6,44),
(2,7,13),
(2,8,16),
(2,9,2),
(2,10,39),
(2,11,26),
(2,12,29),
(2,13,17),
(2,14,30),
(2,15,77),
(2,16,47),
(2,17,36),
(2,18,38),
(2,19,73),
(2,20,66),
(3,1,12),
(3,2,63),
(3,3,61),
(3,4,75),
(3,5,63),
(3,6,15),
(3,7,82),
(3,8,47),
(3,9,7),
(3,10,50),
(3,11,20),
(3,12,32),
(3,13,87),
(3,14,9),
(3,15,37),
(3,16,81),
(3,17,40),
(3,18,29),
(3,19,63),
(3,20,60),
(4,1,50),
(4,2,16),
(4,3,83),
(4,4,11),
(4,5,35),
(4,6,30),
(4,7,71),
(4,8,3),
(4,9,10),
(4,10,94),
(4,11,20),
(4,12,13),
(4,13,52),
(4,14,16),
(4,15,55),
(4,16,2),
(4,17,71),
(4,18,72),
(4,19,32),
(4,20,11),
(5,1,58),
(5,2,47),
(5,3,56),
(5,4,56),
(5,5,38),
(5,6,21),
(5,7,20),
(5,8,66),
(5,9,79),
(5,10,49),
(5,11,93),
(5,12,47),
(5,13,41),
(5,14,22),
(5,15,65),
(5,16,48),
(5,17,65),
(5,18,72),
(5,19,1),
(5,20,41);
