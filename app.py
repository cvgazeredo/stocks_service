
from flask import redirect, request
from flask_openapi3 import OpenAPI, Info, Tag
from flask_cors import CORS
from flask_session import Session
from flask import Flask
from helpers import lookup
from schema import StockSchema, SearchStockSchema, list_stock, ErrorSchema

# Application config
info = Info(title="Project Home Broker -  Stocks Microservice", version="1.0.0")
app = OpenAPI(__name__, info=info)
app.run(debug=True)

# CORS(app)
# Session(app)

# Make sure api key is set
# if not os.environ.get("API KEY"):
#     raise RuntimeError("API_KEY not set")

# Tags for documentation
home_tag = Tag(name="Documentation - Stock Microservice", description="Select doc: Swagger, Redoc")
stock_tag = Tag(name="Stock", description="Details of stock")


# Home
@app.get('/', tags=[home_tag])
def home():
    return redirect('/openapi')


# Stock's details
@app.get("/stock", tags=[stock_tag],
         responses={"200": StockSchema, "404": ErrorSchema})
def get_stock(query: SearchStockSchema):

    symbol = query.symbol
    stock = lookup(symbol)

    if not stock or not stock.get("Global Quote"):
        return {"error": "Stock information not available"}, 404

    stock_symbol = stock.get("Global Quote").get("01. symbol")
    stock_price = float(stock.get("Global Quote").get("05. price"))

    if stock:
        stock_data = {
            "symbol": stock_symbol.upper(),
            "price": stock_price
        }

        return list_stock(StockSchema(**stock_data)), 200



# List most popular stocks and it's prices


