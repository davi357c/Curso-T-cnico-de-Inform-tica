create database clinicaMedica;
create table paciente (
    codigo int(5) not null,
    nome varchar(50) not null,
    endereco varchar(50) not null,
    telefone int(8) not null,
    cidade varchar(50) not null,
    estado char(2) not null,
    sexo char(1) not null,
    dataNascimento date not null,
    estadoCivil varchar(50) not null,
    rg int(8) not null,
    cpf int(10) not null,
    carteira int(8) not null,
    primary key (codigo)
)
create table convenio (
    codigo int(5) not null,
    descricao varchar(50) not null,
    tipo varchar(50) not null,
    primary key (codigo)
)
create table medico (
    crm int(5) not null,
    endereco varchar(50) not null,
    telefone int(8) not null,
    cidade varchar(50) not null,
    estado varchar(50) not null,
    especialidade varchar(50) not null,
    primary key (crm)
)
create table consulta (
    codigo int(5) not null,
    dataConsulta data not null,
    hora time not null,
    tipo varchar(50) not null,
    codigoPaciente int(5) not null,
    codigoConvenio int(5) not null,
    codigoMedico int(5) not null,
    foreign key (codigoPaciente) references paciente(codigo),
    foreign key (codigoConvenio) references convenio(codigo),
    foreign key (codigoMedico) references medico(crm)
)
create table exame (
    codigo int(5) not null,
    descricao varchar(50) not null,
    tipo varchar(50) not null,
    dataExame data not null,
    resultado varchar(100) not null,
    codigoConsulta int(5) not null,
    foreign key (codigoConsulta) references consulta(codigo)
)

insert into paciente(codigo, nome, endereco, telefone, cidade, estado, sexo, dataNascimento, estadoCivil, rg, cpf, carteira) values (1, 'Ana Silva', 'Rua A, 123', 11122233, 'São Paulo', 'SP', 'F', '15/06/1985', 'Casada', 12345678, 1234567890, 12345678);
insert into paciente(codigo, nome, endereco, telefone, cidade, estado, sexo, dataNascimento, estadoCivil, rg, cpf, carteira) values (2, 'Carlos Oliveira', 'Avenida B, 456', 22223333, 'Rio de Janeiro', 'RJ', 'M', '22/03/2001', 'Solteiro', 23456789, 2345678901, 87654321);
insert into paciente(codigo, nome, endereco, telefone, cidade, estado, sexo, dataNascimento, estadoCivil, rg, cpf, carteira) values (3, 'Maria Santos', 'Praça C, 789', 89234793, 'Belo Horizonte', 'MG', 'F', '05/12/1978', 'Divorciada', 34567890, 3456789012, 61534734);

insert into convenio(codigo, descricao, tipo) values (1, 'Unimed Criciúma', 'Oq é tipo');
insert into convenio(codigo, descricao, tipo) values (2, 'São José Criciúma', 'sla');
insert into convenio(codigo, descricao, tipo) values (3, 'Hospital inclusivo para pessoas com problemas de saúde', 'aaaa');

insert into medico(crm, endereco, telefone, cidade, estado, especialidade) values (12345, 'Rua Carlos', 12345678, 'São Paulo', 'SP', 'Cardiologista');
insert into medico(crm, endereco, telefone, cidade, estado, especialidade) values (54321, 'Avenida Carlos', 87654321, 'Rio de Janeiro', 'RJ', 'Dermatologista');
insert into medico(crm, endereco, telefone, cidade, estado, especialidade) values (11223, 'Rua Alberto', 76543210, 'Belo Horizonte', 'MG', 'Ortopedista');

insert into consulta(codigo, dataConsulta,hora, tipo, codigoPaciente, codigoConvenio, codigoMedico) values (1, '15/08/2024', '09:00', 'Rotina', 1, 1, 12345);
insert into consulta(codigo, dataConsulta,hora, tipo, codigoPaciente, codigoConvenio, codigoMedico) values (2, '24/08/2024', '10:00', 'Emergência', 2, 2, 54321);
insert into consulta(codigo, dataConsulta,hora, tipo, codigoPaciente, codigoConvenio, codigoMedico) values (3, '02/09/2024', '14:00', 'Rotina', 3, 3, 11223);

insert into exame(codigo, descricao, tipo, dataExame, resultado, codigoConsulta) values (1, 'Exame de Sangue', 'Coleta de sangue', '15/08/2024', 'Normal', 1);
insert into exame(codigo, descricao, tipo, dataExame, resultado, codigoConsulta) values (2, 'Radiografia de Tórax', 'Laboratório', '24/08/2024', 'Melhor', 2);
insert into exame(codigo, descricao, tipo, dataExame, resultado, codigoConsulta) values (3, 'Ultrassonografia Abdominal', 'Endoscopia', '02/09/2024', 'Anormal', 3);