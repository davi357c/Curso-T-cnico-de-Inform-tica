create database construtora_Oswald_Builds;
create table escritorio (
    cnpj int(14) not null,
    nome varchar(100) not null,
    telefone int(10) not null,
    endereco varchar(50) not null,
    rua varchar(50) not null,
    bairro varchar(50) not null,
    cidade varchar(50) not null,
    pais varchar(50),
    idade int(3),
    primary key (cnpj)
);
create table setor (
    codigo int(5) not null,
    nome varchar(50) not null,
    telefone int(10) not null,
    max_funcionarios int(4),
    primary key (codigo),
    foreign key (codigo_escritorio) references escritorio (cnpj),
    foreign key (codigo_engenheiro) references engenheiro (cpf)
);
create table engenheiro (
    cpf int(11) not null,
    nome varchar(50) not null,   
    telefone int(10) not null,
    cargo varchar(50) not null,
    idade int(3) not null,
    altura float(3,2),
    peso float(5, 2),
    sexualidade varchar(15),
    genero varchar(15),
    quantia_filhos int(2) not null,
    raca varchar(10),
    endereco varchar(50) not null,
    rua varchar(50) not null,
    bairro varchar(50) not null,
    cidade varchar(50) not null,
    pais varchar(50),
    nacionalidade varchar(50),
    linguajares varchar(50) not null,
    primary key (cpf)
);
create table projeto (
    codigo int(5) not null,
    nome varchar(50) not null,   
    data_inicio int(10) not null,
    data_final int(10) not null,
    valor_estimado int(15) not null,
    valor_final int(15),
    informacoes varchar(500) not null,
    primary key (codigo),
    foreign key (codigo_engenheiro) references engenheiro (cpf)
);
create table cliente (
    cpf int(11) not null,
    nome varchar(50) not null,   
    telefone int(10) not null,
    idade int(3) not null,
    sexualidade varchar(15),
    endereco varchar(50) not null,
    rua varchar(50) not null,
    bairro varchar(50) not null,
    cidade varchar(50) not null,
    pais varchar(50),
    primary key (cpf),
    foreign key (codigo_projeto) references projeto (codigo)
);