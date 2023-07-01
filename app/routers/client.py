from fastapi import APIRouter
from app.db.session import session
from app.models.client import Client
from app.schemas.client import ClientModel

router = APIRouter()


@router.get("/client")
async def get_clients():
    return session.query(Client).all()


@router.post("/client")
async def add_client(client_model: ClientModel):
    client = Client(
        id=client_model.id,
        created_at=client_model.created_at,
        first_name=client_model.first_name,
        last_name=client_model.last_name,
        street_address=client_model.street_address,
        phone_number=client_model.phone_number,
        post_number=client_model.post_number,
        town=client_model.town
    )

    session.add(client)
    session.commit()
    return "Client has been added."


@router.get("/client/{client_id}")
async def get_client_by_id(client_id: int):
    return session.query(Client).filter(Client.id == client_id).first()


@router.put("/client/{client_id}")
async def update_client(client_id: int, client_update: ClientModel):
    client = session.query(Client).filter(Client.id == client_id).first()
    if client is None:
        return "Client with provided id does not exist."

    client.created_at = client_update.created_at if client_update.created_at else client.created_at
    client.first_name = client_update.first_name if client_update.first_name else client.first_name
    client.last_name = client_update.last_name if client_update.last_name else client.last_name
    client.street_address = client_update.street_address if client_update.street_address else client.street_address
    client.phone_number = client_update.phone_number if client_update.phone_number else client.phone_number
    client.post_number = client_update.post_number if client_update.post_number else client.post_number
    client.town = client_update.town if client_update.town else client.town

    session.commit()
    return "Client has been updated."


@router.delete("/client/{client_id}")
async def delete_client_by_id(client_id: int):
    client = session.query(Client).filter(Client.id == client_id).first()
    if client is None:
        return f"Client with id {client_id} does not exist."

    session.delete(client)
    session.commit()
    return "Client has been deleted."
