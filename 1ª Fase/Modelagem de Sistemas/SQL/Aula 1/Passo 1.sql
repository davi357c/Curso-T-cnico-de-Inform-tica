create database exemplo;
create table cursos (
    codigo int(5) not null,
    aluno varchar(50) not null,
    endereco varchar(50),
    primary key (codigo)
);
create table alunos (
    cpf int(11) not null,
    nome varchar(50) not null,
    age int(3) not null,
    telefone_do_responsavel int(10) no null,
    codigo_curso int(5) not null,
    primary key (cpf),
    foreign key (codigo_curso) references cursos (codigo)
);