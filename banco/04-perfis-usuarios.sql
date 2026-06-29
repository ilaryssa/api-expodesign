	-- Criação de Usuários e Controle de Acesso

-- Criação dos 3 principais roles
create role administrador;
create role autor;
create role leitor;

-- Provendo as autorizações para cada role
grant select on all tables in schema public
to leitor;

grant select on all tables in schema public to autor;
grant update on projeto, galeria to autor;

grant all privileges on
	usuario, autor, projeto, galeria, disciplina, trabalho_em_equipe, membros_equipe
to administrador;

-- Criação de 3 usuários, um para cada role
create user daniely_admin with password 'senha123';
grant administrador to daniely_admin;

create user lara_autora with password 'senha456';
grant autor to lara_autora;

create user laryssa_leitora with password 'senha789';
grant leitor to laryssa_leitora;
