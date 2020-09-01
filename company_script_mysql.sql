create database company;
use company;

CREATE USER 'goku'@'localhost' IDENTIFIED BY 'shenlong';
GRANT ALL PRIVILEGES ON company.* TO 'goku'@'localhost';

CREATE TABLE `funcionarios` (
  `idfunc` int NOT NULL AUTO_INCREMENT,
  `fname` varchar(15) NOT NULL,
  `lname` varchar(15) NOT NULL,
  `cargo` varchar(30) NOT NULL,
  `salario` float NOT NULL,
  PRIMARY KEY (`idfunc`)
);

CREATE TABLE `usuarios` (
  `idusuarios` int NOT NULL AUTO_INCREMENT,
  `user` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  PRIMARY KEY (`idusuarios`)
  );