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
);
create table professor (
    codigo int(5) not null,
    nome varchar(50) not null,
    salario float(15, 2) not null,
    endereco varchar(50) not null,
    bairro varchar(50) not null,
    telefone int(10) not null,
    rg int(12) not null,
    cpf int(12) not null,
    email varchar(50) not null,
    dataNascimento date not null,
    codigoCidade int(5) not null,
    codigoDisciplina int(5) not null,
    codigoCurso int(5) not null,
    primary key (codigo),
    foreign key (codigoCidade) references cidade(codigo),
    foreign key (codigoCurso) references curso(codigo),
    foreign key (codigoDisciplina) references disciplina(codigo),
);
create table disciplina (
    codigo int(5) not null,
    nome varchar(50) not null,
    ementa varchar(100) not null,
    numeroAulas int(2) not null,
    periodo varchar(50) not null,
    codigoProfessor int(5) not null,
    codigoCurso int(5) not null,
    primary key (codigo),
    foreign key (codigoCurso) references curso(codigo),
    foreign key (codigoProfessor) references professor(codigo),
);
insert into estado(codigo, nome) values (1, "Santa Catarina");
insert into estado(codigo, nome) values (2, "Paraná");
insert into estado(codigo, nome) values (3, "Rio Grande do Sul");

insert into cidade(codigo, nome, codigoEstado) values (1, "Criciúma", 1);
insert into cidade(codigo, nome, codigoEstado) values (2, "Curitiba", 2);
insert into cidade(codigo, nome, codigoEstado) values (3, "Porto Alegre", 3);

insert into curso(codigo, nome) values (1, "Informática");
insert into curso(codigo, nome) values (2, "Mecânica");
insert into curso(codigo, nome) values (3, "Design Gráfico");

insert into aluno(codigo, nome, endereco, bairro, telefone, nomePai, nomeMae, fonePai, foneMae, rg, cpf, email, dataNascimento, codigoCidade, codigoCurso) values (1, "Augusto Custódio Silva Sauro", "Avenida Paulista", "Ipatueraba", 132799413, "Claudio Ramos", "Carla Ramos", 12345, 54321, 17436, 73264882, "augustoguma@gmail.com", "21/04/2008", 1, 1);
insert into aluno(codigo, nome, endereco, bairro, telefone, nomePai, nomeMae, fonePai, foneMae, rg, cpf, email, dataNascimento, codigoCidade, codigoCurso) values (2, "Sofia Carla", "Rua Paulo Ramos", "Pinheirinho", 1437268, "Oswaldo Cria", "Maria Descria", 1523345, 54523321, 1731436, 736543882, "sofiagames@gmail.com", "11/09/2009", 2, 3);
insert into aluno(codigo, nome, endereco, bairro, telefone, nomePai, nomeMae, fonePai, foneMae, rg, cpf, email, dataNascimento, codigoCidade, codigoCurso) values (3, "Alberto Bitencourt", "Rua Gilio Burigo", "Jardim Maristela", 1234468, "Edurdo 5 Noites", "Edurda Sem Noites", 1834845, 54874321, 17843736, 73547882, "manuelgomes123@gmail.com", "30/07/2011", 3, 2);

insert into professor(codigo, nome, salario, endereco, bairro, telefone, rg, cpf, email, dataNascimento, codigoCidade, codigoCurso, codigoDisciplina) values (1, "Charles Puto", 16969, "Rua Quinto dos Inferno", "La na Puta Que Pariu", 743864, 6969696969, 6666666, "invocacaodocapeta@gmail.com", "69/00/1735", 2, 3, 3);
insert into professor(codigo, nome, salario, endereco, bairro, telefone, rg, cpf, email, dataNascimento, codigoCidade, codigoCurso, codigoDisciplina) values (2, "João Paulo o Melhor", 100000099, "Rua Paraíso", "Seu pai", 487236, 5438583, 467868, "joaopaulosigma@gmail.com", "06/02/1990", 1, 1, 2);
insert into professor(codigo, nome, salario, endereco, bairro, telefone, rg, cpf, email, dataNascimento, codigoCidade, codigoCurso, codigoDisciplina) values (3, "Mari", 99999999, "Rua Perfeito", "Seu pai", 34574, 5743744, 4747447, "mariane@gmail.com", "04/07/1995", 1, 1, 1);

insert into disciplina(codigo, nome, ementa, numeroAulas, periodo, codigoProfessor, codigoCurso) values (1, "Jogos Digitais", "Disciplina voltada na criação de jogos digitais", 3, "2° semestre inteiro", 3, 1);
insert into disciplina(codigo, nome, ementa, numeroAulas, periodo, codigoProfessor, codigoCurso) values (2, "Produção Sexual", "Disciplina voltada na traumatização de crianças", 78, "Desde os primórdios da existencia", 1, 3);
insert into disciplina(codigo, nome, ementa, numeroAulas, periodo, codigoProfessor, codigoCurso) values (3, "História", "Disciplina voltada no ensino da história", 2, "Ano inteiro", 2, 2);
