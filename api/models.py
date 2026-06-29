from pydantic import BaseModel
from typing import Optional
# from datetime import date

# crud Projeto Expodesign
# puxar no get
class Projeto(BaseModel):
    codigo_proj: int #gerado automaticamente no bd
    titulo: str
    descricao: Optional[str] = None #pode ser nulo tmabem
    ano: int
    matricula:Optional[str] = None #quando em equipe vira nulo
    codigo_disc: str

# puxar no put // tudo opcional pra permitir que o usuário mude so o que ele quer
class ProjetoUpdate(BaseModel): 
    titulo: Optional[str] = None
    descricao: Optional[str] = None
    ano: Optional[int] = None
    matricula: Optional[str] = None
    codigo_disc: Optional[str] = None

# puxar no post
class ProjetoCreate(BaseModel):
    titulo: str
    descricao: Optional[str] = None
    ano: int
    matricula: Optional[str] = None
    codigo_disc: str