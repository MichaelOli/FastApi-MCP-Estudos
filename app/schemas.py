from pydantic import BaseModel, Field


class ItemCreate(BaseModel):
    name: str = Field(..., title="Nome do item", min_length=1, max_length=100)
    price: float = Field(
        gt=0, title="Preço do item", description="O preço deve ser maior que zero"
    )
    description: str | None = None


class Item(ItemCreate):
    id: int = Field(
        ...,
        title="ID do item",
        description="O ID do item é gerado automaticamente pelo banco de dados",
    )
