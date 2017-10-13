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
  `Password` VARCHAR(55) NOT NULL,
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

INSERT INTO `JohmpsonClothing`.`Customer` (`CustomerID`,`Password`,`LastName`,`FirstName`,`Address`,`City`,`State`,`Zip`,`Phone`,`Email`) VALUES
(1,"Default1","Dudley","Ignacia","7298 Ligula. Ave","Mobile","AL","39596","(356) 713-3877","aliquam.eu@vulputatelacusCras.com"),
(2,"Default2","Ortega","Howard","568-4385 Tellus Ave","Columbus","OH","47159","(658) 167-4958","elit.dictum@vitae.com"),
(3,"Default3","Burgess","Gillian","P.O. Box 792, 5220 Pede, Av.","Nashville","TN","35476","(730) 463-6803","amet@et.edu"),
(4,"Default4","Doyle","Benjamin","199-7144 Et St.","Helena","MT","21566","(949) 548-7116","orci@aliquetodio.org"),
(5,"Default5","Mullins","Judah","972-7983 Felis Rd.","Saint Paul","MN","83104","(625) 824-9438","ipsum@non.net"),
(6,"Default6","Kim","Margaret","Ap #171-6913 Lacinia Avenue","Montgomery","AL","95478","(955) 105-7481","ultrices@nonluctus.edu"),
(7,"Default7","Chapman","Deirdre","P.O. Box 106, 1265 Nunc St.","Wichita","KS","56877","(588) 884-5124","porttitor.scelerisque@tempus.com"),
(8,"Default8","Cervantes","Kimberley","Ap #429-4117 Sapien. Rd.","Erie","PA","94040","(885) 290-7969","libero.dui@loremlorem.edu"),
(9,"Default9","Oneill","Haviva","Ap #722-8330 Cras St.","Sioux City","IA","12461","(235) 669-2731","nonummy.ac@idmollis.co.uk"),
(10,"Default10","Massey","Cullen","P.O. Box 425, 2389 Varius. Ave","Gillette","WY","94974","(422) 340-3785","lacus.Quisque@nec.org"),
(11,"Default11","Taylor","Drake","335-8309 Cursus. St.","Lincoln","NE","40305","(708) 259-1979","nisl@sitamet.co.uk"),
(12,"Default12","Dennis","Edan","882-7758 Et Av.","Mobile","AL","14070","(824) 893-7711","Sed.congue.elit@et.co.uk"),
(13,"Default13","Pena","Imogene","Ap #348-2489 Nulla St.","Salt Lake City","UT","98110","(300) 964-6316","a.odio@quispedeSuspendisse.org"),
(14,"Default14","Duffy","Stephanie","1401 In Rd.","Augusta","GA","92503","(778) 901-2976","Vivamus@ornareegestas.net"),
(15,"Default15","Meyer","Evelyn","478-131 Erat, Street","Cleveland","OH","51789","(450) 986-9072","ipsum@etnunc.co.uk"),
(16,"Default16","Sutton","Ila","900-4752 Auctor Av.","West Valley City","UT","32228","(250) 615-1005","adipiscing.fringilla.porttitor@Crasvehiculaaliquet.ca"),
(17,"Default17","Hopper","Cassady","930-8233 Morbi Av.","Houston","TX","11813","(819) 843-6065","ac@atlacus.net"),
(18,"Default18","Cantu","Unity","4336 Mauris St.","Jackson","MS","76645","(906) 496-9548","hendrerit.consectetuer.cursus@Integerinmagna.ca"),
(19,"Default19","Carr","Amity","Ap #938-7068 Urna. Av.","Casper","WY","35942","(745) 217-3361","pharetra.ut.pharetra@pharetraut.edu"),
(20,"Default20","Durham","Salvador","Ap #444-5136 Nibh Av.","Stamford","CT","08115","(272) 863-8721","mattis@primis.ca"),
(21,"Default21","Lloyd","Lara","Ap #726-9230 Nibh Road","Sacramento","CA","50835","(192) 487-7131","Nullam.feugiat.placerat@fermentummetusAenean.org"),
(22,"Default22","Hatfield","Melvin","P.O. Box 131, 2910 Id, Avenue","Las Vegas","NV","73838","(885) 178-2158","aliquam@lobortismaurisSuspendisse.org"),
(23,"Default23","Carson","Porter","1500 Molestie St.","Lexington","KY","98480","(213) 359-2666","orci@necdiam.edu"),
(24,"Default24","Madden","Madison","Ap #431-6638 Nibh St.","Salt Lake City","UT","06250","(681) 155-3445","magna@magnaSed.net"),
(25,"Default25","Hurley","Tyler","P.O. Box 406, 7374 Risus. Rd.","Memphis","TN","37528","(497) 685-8647","pharetra.sed.hendrerit@mattisornare.net");

INSERT INTO `JohmpsonClothing`.`CreditCards` (`CardNumber`,`SecurityCode`,`Customer`,`ExpirationDate`) VALUES 
("559667 9314846726","926",1,"07/2017"),
("5418 1663 8357 8816","650",2,"01/2017"),
("545 08716 20773 687","596",3,"02/2017"),
("532 88545 12843 214","751",4,"03/2017"),
("557 03029 10223 493","186",5,"04/2017"),
("514297 009014 6475","441",6,"05/2017"),
("555370 833445 6587","440",7,"06/2017"),
("519205 422411 4300","979",8,"07/2017"),
("5444 1242 4327 8802","316",9,"08/2017"),
("559207 869059 5342","271",10,"09/2017"),
("554089 778268 8993","590",11,"10/2017"),
("556 76991 74488 661","350",12,"11/2017"),
("5412561409706076","264",13,"12/2017"),
("5433 3873 7764 8321","191",14,"01/2017"),
("558545 8519494050","521",15,"02/2017"),
("519247 624078 9452","340",16,"03/2017"),
("5305463878463414","197",17,"04/2017"),
("5387033358358227","632",18,"05/2017"),
("555802 3370678895","284",19,"06/2017"),
("531 04862 43807 448","730",20,"07/2017"),
("542938 903063 1278","918",21,"08/2017"),
("526 86907 30433 467","616",22,"09/2017"),
("5576514780739879","345",23,"10/2017"),
("538 21277 31289 052","423",24,"11/2017"),
("5526981119566805","614",25,"12/2017");

INSERT INTO `JohmpsonClothing`.`Invoice` (`InvoiceID`,`CustomerID`,`BillingAddress`,`BillingCity`,`BillingState`,`BillingZip`,`DateOfInvoice`) VALUES
(1,1,"P.O. Box 339, 8698 Gravida St.","Flint","MI","89122","2015-09-09"),
(2,2,"Ap #430-7708 Id, Rd.","Colchester","VT","89801","2014-08-26"),
(3,3,"Ap #926-7166 Sit St.","Olathe","KS","78219","2015-10-30"),
(4,4,"322-8990 Et Road","Tuscaloosa","AL","50883","2015-04-20"),
(5,5,"814-3198 Non Rd.","Burlington","VT","92052","2015-04-17"),
(6,6,"7240 Pulvinar St.","Cheyenne","WY","17321","2015-06-20"),
(7,7,"2052 Aenean Av.","Cleveland","OH","25967","2014-01-26"),
(8,8,"232-6041 Ut, Avenue","Jonesboro","AR","31560","2014-06-02"),
(9,9,"P.O. Box 840, 5052 Mi. Rd.","Fayetteville","AR","35561","2015-06-24"),
(10,10,"Ap #338-4613 Leo. Rd.","Cambridge","MA","29827","2014-07-06"),
(11,11,"447-4666 Risus, Ave","Waterbury","CT","26255","2015-10-25"),
(12,12,"5409 Ut Road","Oklahoma City","OK","37591","2015-01-16"),
(13,13,"Ap #513-7404 Integer St.","Gaithersburg","MD","20700","2015-11-03"),
(14,14,"P.O. Box 538, 5184 Bibendum Street","Austin","TX","73050","2014-05-29"),
(15,15,"Ap #940-6755 Tincidunt Av.","Lansing","MI","10089","2014-01-04"),
(16,16,"P.O. Box 759, 6257 In, Av.","Rutland","VT","46039","2014-11-27"),
(17,17,"5538 Tempor St.","Cedar Rapids","IA","50401","2014-07-07"),
(18,18,"P.O. Box 194, 7610 Vulputate Street","Hattiesburg","MS","42853","2014-10-27"),
(19,19,"216-8173 Dui Rd.","Sandy","UT","25785","2015-09-21"),
(20,20,"P.O. Box 230, 2781 At Av.","Little Rock","AR","69484","2014-02-26"),
(21,21,"Ap #118-5773 Cras St.","Huntsville","AL","31566","2014-09-30"),
(22,22,"4692 Mi Road","Jefferson City","MO","57433","2014-05-02"),
(23,23,"681-9454 Commodo Av.","Sioux City","IA","56234","2014-04-18"),
(24,24,"556-8219 Et St.","Missoula","MT","75185","2014-06-25"),
(25,25,"P.O. Box 455, 635 Malesuada. Road","Anchorage","AK","74858","2014-01-14");

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

INSERT INTO `JohmpsonClothing`.`InvoiceLine` (`InvoiceLineID`,`InvoiceID`,`ClothingID`,`Quantity`,`SoldFor`,`Credit`) VALUES 
(1,1,9,1,100.00,"559667 9314846726"),
(2,2,2,1,40.00,"5418 1663 8357 8816"),
(3,3,3,1,50.00,"545 08716 20773 687"),
(4,4,1,1,20.00,"532 88545 12843 214"),
(5,5,4,1,20.00,"557 03029 10223 493"),
(6,6,11,1,30.00,"514297 009014 6475"),
(7,7,16,1,50.00,"555370 833445 6587"),
(8,8,3,1,50.00,"519205 422411 4300"),
(9,9,1,1,20.00,"5444 1242 4327 8802"),
(10,10,12,1,40.00,"559207 869059 5342"),
(11,11,16,1,50.00,"554089 778268 8993"),
(12,12,12,1,40.00,"556 76991 74488 661"),
(13,13,9,1,100.00,"5412561409706076"),
(14,14,5,1,5.00,"5433 3873 7764 8321"),
(15,15,4,1,20.00,"558545 8519494050"),
(16,16,11,1,30.00,"519247 624078 9452"),
(17,17,4,1,20.00,"5305463878463414"),
(18,18,1,1,20.00,"5387033358358227"),
(19,19,1,1,20.00,"555802 3370678895"),
(20,20,3,1,50.00,"531 04862 43807 448"),
(21,21,9,1,100.00,"542938 903063 1278"),
(22,22,2,1,40.0,"526 86907 30433 467"),
(23,23,2,1,40.00,"5576514780739879"),
(24,24,16,1,50.00,"538 21277 31289 052"),
(25,25,15,1,100.00,"5526981119566805");

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
