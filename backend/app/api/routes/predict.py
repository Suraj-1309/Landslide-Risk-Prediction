from fastapi import APIRouter, HTTPException
from app.api.handlers.predict_handler import predict_landslide_service
from app.api.schemas.data_schema import PredictRequest, PredictResponse

router = APIRouter(prefix="/api/v1", tags=["predict"])

@router.post("/predict", response_model=PredictResponse)
def predict(payload: PredictRequest):
    try: 
        result = predict_landslide_service(payload)
        return PredictResponse(**result)
    
    except FileNotFoundError as exc:
        raise HTTPException(
            status_code=503,
            detail={
                "status": 503,
                "code": "MODEL_UNAVAILABLE",
                "message": "Model artifacts are not available",
                "details": [{"field" : "model", "message" : str(exc)}]
            },
        ) from exc
    
    except ValueError as exc:
        raise HTTPException(
            status_code=422,
            detail={
                "status": 422,
                "code": "VALIDATION_ERROR",
                "message": "Request validation failed",
                "details" : [{"field" : "request", "message" : str(exc)}],
            }
        ) from exc
    
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail={
                "status" : 500,
                "code" : "INTERNAL_SERVER_ERROR",
                "message" : "Unexpected server error",
                "details" : [{"field": "server", "message": str(exc)}],
            }
        ) from exc