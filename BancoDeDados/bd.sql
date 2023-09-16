create database desafioStemis;

use desafioStemis;

create table produtos(
	id_produto int primary key auto_increment,
    nome varchar(30),
    valor int,
    quantidade int
);

insert into produtos(nome, valor, quantidade) values
	("Coca-Cola", 03, 150),
    ("Queijo", 05, 50),
    ("Nescau", 06, 125),
    ("Arroz", 14, 200),
    ("Barra de Chocolate", 10, 100);

select * from produtos; 
