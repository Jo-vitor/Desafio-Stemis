create database desafioStemis;

use desafioStemis;

create table produtos(
	id_produto int primary key auto_increment,
    nome varchar(30),
    valor decimal(4,2),
    quantidade int
);

insert into produtos(nome, valor, quantidade) values
	("Coca-Cola", 03.99, 150),
    ("Queijo", 05.50, 50),
    ("Nescau", 06.75, 125),
    ("Arroz", 14.25, 200),
    ("Barra de Chocolate", 10.00, 100);
