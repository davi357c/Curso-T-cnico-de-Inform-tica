create database escola;
create table estado (
    codigo int(5) not null,
    nome varchar(50) not null,
    primary key (codigo)
);
create table cidade (
    codigo int(5) not null,
    nome varchar(50) not null,
    codigoEstado int(5) not null,
    primary key (codigo),
    foreign key (codigoEstado) references estado(codigo)
);
create table aluno (
    codigo int(5) not null,
    nome varchar(50) not null,
    endereco varchar(50) not null,
    bairro varchar (50) not null,
    telefone int(10) not null,
    nomePai varchar(50) not null,
    nomeMae varchar(50) not null,
    fonePai int(10) not null,
    foneMae int(10) not null,
    rg int(12) not null,
    cpf int(11) not null,
    email varchar(50) not null,
    dataNascimento date not null,
    codigoCidade int(5) not null,
    codigoCurso int(5) not null,
    primary key (codigo),
    foreign key (codigoCidade) references cidade(codigo),
    foreign key (codigoCurso) references curso(codigo)
);
create table curso (
    codigo int(5) not null,
    nome varchar(50) not null,
    primary key (codigo)
)