from fastapi import APIRouter, Body, HTTPException, status, Depends
from fastapi.encoders import jsonable_encoder


from server.database import (
    add_socie,
    delete_socie,
    retrieve_socie,
    retrieve_socies,
    update_socie,
)
from server.models.socie import (
    ErrorResponseModel,
    ResponseModel,
    SchemaDeSocie,
    UpdateSocieModel,
)

router = APIRouter()

# Función de dependencia para validar la existencia de un socio
async def get_socie_or_404(id: str):
    socie_found = await retrieve_socie(id)
    if not socie_found:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Socio con id {id} no existe",
        )
    return socie_found

# Add a new Socie
@router.post("/", response_description="Datos de socie agregados ala base de datos")
async def add_socie_data(socie: SchemaDeSocie = Body(...)):
    socie = jsonable_encoder(socie)
    new_socie = await add_socie(socie)
    return ResponseModel(new_socie, "Socie agregado.")

# Retrieve all Socies
@router.get("/", response_description="Socies retrieved")
async def get_socies():
    socies = await retrieve_socies()
    if socies:
        return ResponseModel(socies, "Se consiguieron los datos de les Socies")
    return ResponseModel(socies, "Vuelvión una lista vacía")

# Retrieve a socie with a matching ID
@router.get("/{id}", response_description="Dato se socieo recuperado")
async def get_socie_data(socie: dict = Depends(get_socie_or_404)):
    return ResponseModel(socie, "Se consiguieron los datos del Socie")

# Update a socie with a matching ID
@router.put("/{id}")
async def update_socie_data(
    id: str,
    req: UpdateSocieModel = Body(...),
    socie_found: dict = Depends(get_socie_or_404),
):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_socie = await update_socie(id, req)
    if updated_socie:
        return ResponseModel(
            f"Se pudo actualizar el Socie con el ID: {id} ", "Socio Actualizado correctamente"
        )
    return ErrorResponseModel(
        "Ocurrió un error",
        404,
        "Hubo una falla actualizando los datos del Socie",
    )

# Delete a socie with a matching ID
@router.delete("/{id}", response_description="Socie data deleted from the database")
async def delete_socie_data(
    id: str,
    socie_found: dict = Depends(get_socie_or_404),
):
    deleted_socie = await delete_socie(id)
    if deleted_socie:
        return ResponseModel(
            f"Socie ID: {id} borrado", "Socio Borrado exitosamente"
        )
    return ErrorResponseModel(
        "Hubo un error", 404, f"Socio con id {id} no existe"
    )