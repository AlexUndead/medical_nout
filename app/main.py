from uuid import uuid4, UUID
from fastapi import FastAPI
from db import Loan

app = FastAPI()


@app.post('/loans')
def create_loan(product_name: str):
    '''Метод создания кредита'''
    id = uuid4()
    Loan.create(id=id, productName=product_name)
    return {'id': id}


@app.get('/loans/{id}')
def get_loan(id: UUID):
    '''Метод просмотра кредита'''
    loan = Loan.get(Loan.id == id)
    return {'product_name': loan.productName}
