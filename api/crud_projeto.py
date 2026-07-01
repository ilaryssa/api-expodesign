from fastapi import APIRouter, HTTPException
from db import get_connection
from models import Projeto, ProjetoCreate, ProjetoUpdate
from typing import List, Optional

router = APIRouter()

@router.post("/projeto")
async def criar_projeto(projeto: ProjetoCreate):

    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute(
            "SELECT 1 FROM disciplina WHERE codigo_disc = %s", (projeto.codigo_disc,)) #verificar se a disicplina existe
        if cur.fetchone() is None:
            raise HTTPException(400, "Disciplina não encontrada")
        
        cur.execute("SELECT 1 FROM autor WHERE matricula = %s", (projeto.matricula, ))
        if cur.fetchone() is None:
            raise HTTPException(400, "Autor não encontrado")
            
        cur.execute(
            "INSERT INTO projeto (titulo, descricao, ano, matricula, codigo_disc) VALUES (%s, %s, %s, %s, %s)", (projeto.titulo, projeto.descricao, projeto.ano, projeto.matricula, projeto.codigo_disc)
        )
        
        conn.commit() #avisar que deu certo e salvar no banco de dados

    except HTTPException:
        raise

    except Exception as e:
        conn.rollback() #se der erro, desfaz a operação
        raise HTTPException(400, f"Erro ao criar projeto: {str(e)}") #retorna o erro; esse str(e) indica mais especificamente

    finally:
        cur.close() #fechar o cursor
        conn.close() #fechar a conexão

    return {"msg": "Projeto criado com sucesso!"} 

@router.get("/projetos", response_model=List[Projeto])
async def listar_projetos():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT codigo_proj, titulo, descricao, ano, matricula, codigo_disc FROM projeto ORDER BY codigo_proj")
    rows = cur.fetchall() #fetchall retorna todas as linhas da consulta

    cur.close()
    conn.close()

    return [
        Projeto(
            codigo_proj=p[0],
            titulo=p[1],
            descricao=p[2],
            ano=p[3],
            matricula=p[4],
            codigo_disc=p[5],
        ) for p in rows
    ]

@router.get("/projeto/{codigo_proj}", response_model=Projeto)
async def get_projeto(codigo_proj: int):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT codigo_proj, titulo, descricao, ano, matricula, codigo_disc FROM projeto WHERE codigo_proj = %s", (codigo_proj, ))
    p = cur.fetchone() #fetchone pra pegar um so

    cur.close()
    conn.close()

    if p is None:
        raise HTTPException(404, "Projeto não encontrado")

    return Projeto(
            codigo_proj=p[0],
            titulo=p[1],
            descricao=p[2],
            ano=p[3],
            matricula=p[4],
            codigo_disc=p[5],
        )
    

@router.put("/projeto/{codigo_proj}") #put atualiza recursos existentes
async def atualizar_projeto(codigo_proj: int, projeto_update: ProjetoUpdate): #pega o dnumero do departamento que vai ser atualizado e o objeto com os novos dados do departamentoUpdate
    conn = get_connection() #conexão com o db.py
    cur = conn.cursor() #cursor para executar comandos sql

    # esse tanto de if refere-se à verificação das FKs dessa entidade 
    try:
        cur.execute("SELECT 1 FROM projeto WHERE codigo_proj = %s", (codigo_proj, )) #verfifica se o projeto existe
        if cur.fetchone() is None:
            raise HTTPException(400, "Projeto não encontrado")
        
        #verifica se cada campo do json veio e se não é "string"
        if projeto_update.titulo is not None and projeto_update.titulo != "string":
            cur.execute("UPDATE projeto SET titulo = %s WHERE codigo_proj = %s", (projeto_update.titulo, codigo_proj,))
        if projeto_update.descricao is not None and projeto_update.descricao != "string":
            cur.execute("UPDATE projeto SET descricao = %s WHERE codigo_proj = %s", (projeto_update.descricao, codigo_proj,))
        if projeto_update.ano is not None and projeto_update.ano > 2015:
            if projeto_update.ano < 2015:
                raise HTTPException(400, "Ano válido somente a partir de 2015")
            cur.execute("UPDATE projeto SET ano = %s WHERE codigo_proj = %s", (projeto_update.ano, codigo_proj,))
        if projeto_update.matricula is not None and projeto_update.matricula != "string":
            cur.execute("UPDATE projeto SET matricula = %s WHERE codigo_proj = %s", (projeto_update.matricula, codigo_proj,))
        if projeto_update.codigo_disc is not None and projeto_update.codigo_disc != "string":
            cur.execute("UPDATE projeto SET codigo_disc = %s WHERE codigo_proj = %s", (projeto_update.codigo_disc, codigo_proj,))
        
        conn.commit() #avisar que deu bom
    
    except HTTPException: #roda as mensagens de erro antes da mensagem genérica
        raise

    except Exception as e: 
        conn.rollback()
        raise HTTPException(400, f"Erro ao atualizar o projeto {str(e)}") #se der erro, desfaz a operação e retorna o erro

    finally:
        cur.close()
        conn.close() #aqui, quando da tudo certo, fecha o cursor e a conexão com o banco de dados

    return {"msg": "Projeto atualizado com sucesso!"} 

@router.delete("/projeto/{codigo_proj}")
async def deletar_projeto(codigo_proj: int):
    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute("SELECT 1 FROM projeto WHERE codigo_proj = %s", (codigo_proj, )) #o projeto existe?
        if cur.fetchone() is None:
            raise HTTPException(404, "Projeto não encontrado")
        
        #precisa deletar coisa por coisa quando é FK
        cur.execute("DELETE FROM trabalho_em_equipe WHERE codigo_proj = %s", (codigo_proj,)) #apagar da tabela trabalho em equipe quando apagar de projeto
        cur.execute("DELETE FROM ferr_proj WHERE codigo_proj = %s", (codigo_proj,))

        cur.execute("SELECT codigo_galeria FROM galeria WHERE codigo_proj = %s", (codigo_proj,))
        galerias = cur.fetchall()
        for galeria in galerias:
            cur.execute("DELETE FROM imagem_galeria WHERE codigo_galeria = %s", (galeria[0],))
        
        cur.execute("DELETE FROM galeria WHERE codigo_proj = %s", (codigo_proj,))
        cur.execute("DELETE FROM projeto WHERE codigo_proj = %s", (codigo_proj,))
    
        conn.commit()
    
    except Exception as e:
        conn.rollback()
        raise HTTPException(400, f"Erro ao deletar o projeto: {str(e)}")

    finally:
        cur.close()
        conn.close()

    return {"msg": "Projeto deletado com sucesso!"}