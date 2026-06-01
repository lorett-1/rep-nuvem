create database db_locadora;
 
CREATE TABLE db_locadora.Veiculos (
    VeiculoID INT PRIMARY KEY AUTO_INCREMENT,
    Modelo VARCHAR(100),
    Marca VARCHAR(100),
    Ano INT,
    Status VARCHAR(20),
    PrecoDiaria DECIMAL(10, 2)
);
 
CREATE TABLE db_locadora.Clientes (
    ClienteID INT PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR(100),
    Email VARCHAR(100),  
    Cidade VARCHAR(50),  
    Idade INT,  
    CategoriaCliente VARCHAR(20)
);
 
insert into db_locadora.Veiculos(Modelo, Marca, Ano, Status, PrecoDiaria)
    values("Nivus","Volks",2026,"novo",550.5),
    ("Uno","Fiat",2025,"Usado",300.5),
    ("Civic","Honda",2020,"Usado",370.5),
    ("Toyota","Corolla",2022,"Novo",350.5),
    ("Chevrolet","Onix",2020,"novo",330.5
);
 
 
insert into db_locadora.clientes(Nome,Email,Cidade,Idade,CategoriaCliente)
    values("Fagner","Fagner@exemplo.com","Sao paulo",29,"ouro"),
    ("Luan","Luan@exemplo.com","Sao paulo",32,"prata"),
    ("Alexandre","Alexandre@exemplo.com","Sao paulo",25,"prata"
);
 
select * from db_locadora.clientes;
select * from db_locadora.Veiculos;
 
delete from db_locadora.Veiculos where VeiculoID =10;
 