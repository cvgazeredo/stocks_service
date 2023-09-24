from pydantic import BaseModel


class SearchStockSchema(BaseModel):
    symbol: str


class StockSchema(BaseModel):
    symbol: str
    price: float


class ErrorSchema(BaseModel):
    message: str




def list_stock(stock: StockSchema):
    return {
        "stock": stock.symbol,
        "price": stock.price
    }
