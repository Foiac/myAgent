from fastapi import APIRouter, Depends
from app.application.use_cases.generate_response import GenerateResponseUseCase
from app.config.container import get_generate_response_use_case
from app.adapters.input.request_model import GenerateRequest
from app.adapters.output.response_model import GenerateResponse

router = APIRouter()

@router.post("/generate", response_model=GenerateResponse)
def generate_endpoint(
    request: GenerateRequest,
    use_case: GenerateResponseUseCase = Depends(get_generate_response_use_case)):  

    response_text = use_case.execute(user_input=request.user_input, context=request.context)
    return GenerateResponse(response=response_text)
