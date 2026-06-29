	-- Criação de Usuários e Controle de Acesso

--Aqui eu crio os três roles principais
create role administrador
create role autor
create role leitor

--Dou as autorizações descritas acima para cada role
grant select on all tables in schema public
to leitor;

grant select on all tables in schema public to autor;
grant update on projeto, galeria to autor;

grant all privileges on
	usuario, autor, projeto, galeria, disciplina, trabalho_em_equipe, membros_equipe
to administrador;

--Aqui eu crio 3 usuários, cada um com um role diferente.
create user daniely_admin with password 'senhai123'
grant administrador to daniely_admin;

create user lara_autora with password 'senha456'
grant autor to lara_autora;

create user laryssa_leitora with password 'senha789'
grant leitor to laryssa_leitora