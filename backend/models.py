from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum
from sqlalchemy.orm import relationship
from database import Base
import enum

class TipoMaterial(enum.Enum):
    MARMORE = "Mármore"
    GRANITO = "Granito"
    QUARTZO = "Quartzo"
    OUTRO = "Outro"

class Material(Base):
    __tablename__ = "materiais"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False) # Ex: Preto São Gabriel
    tipo = Column(Enum(TipoMaterial), nullable=False)
    cor = Column(String)
    
    chapas = relationship("Chapa", back_populates="material")

class Chapa(Base):
    __tablename__ = "chapas"

    id = Column(Integer, primary_key=True, index=True)
    material_id = Column(Integer, ForeignKey("materiais.id"))
    comprimento = Column(Float) # em cm
    largura = Column(Float)     # em cm
    espessura = Column(Float)   # em mm
    m2_total = Column(Float)
    status = Column(String, default="Disponivel") # Disponivel, Reservado, Vendido
    
    material = relationship("Material", back_populates="chapas")