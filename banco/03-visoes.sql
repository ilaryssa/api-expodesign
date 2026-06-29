	-- Criação e Uso das Visões

-- 1. Pódio de autores com mais projetos publicados
-- (contando solo ou em equipe)
create view podio_autores as
select 
    a.username,
    u.nome_usuario,
    count(distinct p1.codigo_proj) as projetos_solo,
    count(distinct p2.codigo_proj) as projetos_em_equipe,
    count(distinct p1.codigo_proj) + count(distinct p2.codigo_proj) as total_projetos
from usuario u
join autor a on u.username = a.username
join projeto p1 on a.matricula = p1.matricula
join trabalho_em_equipe t on a.matricula in (
	select matricula from membros_equipe where codigo_equipe = t.codigo_equipe
)
join projeto p2 on t.codigo_proj = p2.codigo_proj
group by a.username, u.nome_usuario
order by total_projetos desc
limit 3;

-- Usando apenas 3 das 5 colunas da visão
select username, nome_usuario, total_projetos
from podio_autores;

-- 2. Pegar informação de contato de autores que
-- tenham projetos publicados, 
-- e filtrar na visão pelo nome da disciplina,
-- mostrando também tais projeto
create view contatos_por_projetos as
select 
    a.email,
    u.username,
    u.nome_usuario,
    d.nome_disc,
    p.titulo as nome_projeto,
	g.url_capa as capa
from autor a
join usuario u on a.username = u.username
join projeto p on a.matricula = p.matricula
join disciplina d on p.codigo_disc = d.codigo_disc
join galeria g on p.codigo_proj = g.codigo_proj;

-- Como a visão vai conter todos os projetos publicados,
-- a filtragem da disciplina acontece na visão
-- (no exemplo, utilizando a disciplina de Modelagem)

select * from contatos_por_projetos
where nome_disc like '%Modelagem%';