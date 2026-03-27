from fastapi import APIRouter, HTTPException

from app.api.handlers.retrain_handler import retrain_model_service
from app.api.schemas.data_schema import RetrainResponse


router = APIRouter(prefix="/api/v1/model", tags=["model"])


@router.post("/retrain", response_model=RetrainResponse)
def retrain_model():
    try:
        result = retrain_model_service()
        return RetrainResponse(**result)

    except FileNotFoundError as exc:
        raise HTTPException(
            status_code=404,
            detail={
                "status": 404,
                "code": "DATASET_NOT_FOUND",
                "message": "Required dataset file is missing",
                "details": [{"field": "dataset", "message": str(exc)}],
            },
        ) from exc

    except ValueError as exc:
        raise HTTPException(
            status_code=422,
            detail={
                "status": 422,
                "code": "RETRAIN_VALIDATION_ERROR",
                "message": "Retraining data validation failed",
                "details": [{"field": "dataset", "message": str(exc)}],
            },
        ) from exc

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail={
                "status": 500,
                "code": "RETRAIN_FAILED",
                "message": "Model retraining failed",
                "details": [{"field": "server", "message": str(exc)}],
            },
        ) from exc
