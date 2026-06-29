# 🎨 ExpoDesign API

API RESTful desenvolvida como projeto final para a disciplina de **Fundamentos de Banco de Dados** (FBD) do curso de Design Digital da UFC.

---

## 📦 O que tem aqui?

- ✅ **API completa** com FastAPI para gerenciar projetos de design
- ✅ **CRUD** de projetos (criar, listar, atualizar e deletar)
- ✅ **Banco de dados PostgreSQL** com modelo relacional completo
- ✅ **Scripts SQL** com:
  - DDL (criação de tabelas)
  - DML (povoamento com dados reais)
  - Views (pódio de autores e contatos por projeto)
  - Perfis de acesso (leitor, autor, administrador)
- ✅ **Controle de permissões** por nível de usuário
- ✅ **Documentação automática** gerada pelo Swagger

---

## 🗂️ Estrutura do Projeto
- expodesign/
- api/
  - crud_projeto.py
  - db.py
  - main.py
  - models.py
  - requirements.txt
- banco/
  - 01-criacao-tabelas.sql
  - 02-povoamento.sql
  - 03-visoes.sql
  - 04-perfis-usuarios.sql
- .gitignore
- LICENSE
- README.md

---

## 🛠️ Tecnologias

- **Python 3.14**
- **FastAPI** (framework web)
- **PostgreSQL** (banco de dados)
- **psycopg2** (conector Python-PostgreSQL)
- **Uvicorn** (servidor ASGI)

---

## 👥 Perfis de Usuário

| Perfil | Permissões |
|--------|------------|
| **Leitor** | Visualizar projetos (SELECT) |
| **Autor** | Criar, editar e deletar **próprios** projetos |
| **Administrador** | Controle total sobre o sistema |

---

## 📊 Modelo de Dados

O banco contempla as entidades:

- `disciplina`, `ferramenta`, `usuario`, `autor`
- `links`, `equipe`, `membros_equipe`
- `projeto`, `ferr_proj`, `trabalho_em_equipe`
- `imagem`, `galeria`, `imagem_galeria`

E as views:
- `podio_autores` (top 3 autores com mais projetos)
- `contatos_por_projetos` (informações de contato dos autores)

---

## 🚀 Como rodar

```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/api-expodesign.git

# 2. Acesse a pasta do projeto
cd api-expodesign

# 3. Execute os scripts SQL na ordem (pasta banco/)
# Nomeeie o banco como "expodesign" (caso queira usar outro nome, é preciso modificar o atributo dbname no arquivo api/db.py)
# No pgAdmin, execute os arquivos na seguinte ordem:
#    01-criacao-tabelas.sql
#    02-povoamento.sql
#    03-visoes.sql
#    04-perfis-usuarios.sql
# (copie e cole cada um, ou use o "Query Tool" para rodar cada arquivo)

# 4. Entre na pasta da API
cd api

# 5. Instale as dependências (tendo o Python 3.14 já instalado)
pip install -r requirements.txt
# Ou, se não funcionar
python -m pip install -r requirements.txt

# 6. Configure o .env
crie um arquivo .env e adicione lá DB_PASSWORD = sua_senha_linda_do_postgres

# 7. Rode a API
python -m uvicorn main:app --reload

# 8. Acesse a documentação
# http://localhost:8000/docs
```
## 🧪 Testando a API

Com a API rodando, acesse o Swagger em `http://localhost:8000/docs`.

Por lá, é possível testar o fluxo completo do CRUD:

- **Adicionar** um novo projeto via `POST /projeto`
- **Consultar** a lista completa de projetos com `GET /projetos`
- **Consultar** um projeto específico com `GET /projeto/{codigo_proj}`
- **Modificar** o projeto usando `PUT /projeto/{codigo_proj}`
- **Deletar** o projeto ao final com `DELETE /projeto/{codigo_proj}`

Além disso, é possível consultar os dados diretamente no **pgAdmin** (ou no terminal do PostgreSQL) para verificar se as alterações foram refletidas no banco de dados.

Exemplo de consulta SQL no pgAdmin:

```sql
-- Consultar todos os projetos
SELECT * FROM projeto;

-- Consultar projetos com filtros
SELECT * FROM projeto 
WHERE ano >= 2020 
ORDER BY titulo;

-- Consultar projetos de um autor específico
SELECT * FROM projeto 
WHERE matricula = '202401';
```

## ⚠️ Aviso
Este projeto foi desenvolvido exclusivamente para fins acadêmicos na disciplina de Fundamentos de Banco de Dados. Não é um sistema pronto para produção.

## 👩‍💻 Autores
#### Daniely Maia — Estudante de Engenharia de Software na Universidade Federal do Ceará (UFC)
#### Lara Gurgel — Estudante de Design Digital na Universidade Federal do Ceará (UFC)
#### Laryssa Santos — Estudante de Design Digital na Universidade Federal do Ceará (UFC)
#### Natan Oliveira — Estudante de Design Digital na Universidade Federal do Ceará (UFC)

## 📚 Disciplina
Fundamentos de Banco de Dados (FBD) — Curso de Design Digital — UFC — 2026

## 📝 Licença
Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
