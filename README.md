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
  - main.py
  - db.py
  - models.py
  - crud_projeto.py
- banco/
  - 01-criacao-tabelas.sql
  - 02-povoamento.sql
  - 03-visoes.sql
  - 04-perfis-usuarios.sql
- requirements.txt
- .env.example
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

# 2. Instale as dependências
pip install -r requirements.txt

# 3. Configure o .env
cp .env.example .env
# Edite com sua senha do PostgreSQL

# 4. Execute os scripts SQL no pgAdmin
# (criação de tabelas, povoamento, views e perfis)

# 5. Rode a API
python -m uvicorn main:app --reload (ou opções parecidas)

# 6. Acesse a documentação
# http://localhost:8000/docs
```
## 🧪 Testando
Acesse o Swagger em http://localhost:8000/docs para testar todos os endpoints interativamente.

## ⚠️ Aviso
Este projeto foi desenvolvido exclusivamente para fins acadêmicos na disciplina de Fundamentos de Banco de Dados. Não é um sistema pronto para produção.

## 👩‍💻 Autores
#### Daniely Maia — Estudante de Engenharia de Software na Universidade Federal do Ceará (UFC)
#### Lara Gurgel — Estudante de Design Digital na Universidade Federal do Ceará (UFC)
#### Laryssa Santos — Estudante de Design Digital na Universidade Federal do Ceará (UFC)
#### Natan Oliveira — Estudante de Design Digital na Universidade Federal do Ceará (UFC)

## 📚 Disciplina
Fundamentos de Banco de Dados (FBD) — Curso de Design Digital — UFC — 2026
