from fastapi import APIRouter, HTTPException, status
from typing import Optional
import logging

from src.init import cmc_client

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/cryptocurrencies")


@router.get("")
async def get_cryptocurrencies():
    try:
        result = await cmc_client.get_listings()
        return result
    except Exception as e:
        logger.error(f"Error fetching cryptocurrencies: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch cryptocurrency data"
        )


@router.get("/{currency_id}")
async def get_cryptocurrency(currency_id: int):
    try:
        result = await cmc_client.get_currency(currency_id)
        return result
    except Exception as e:
        logger.error(f"Error fetching cryptocurrency {currency_id}: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to fetch cryptocurrency data for ID {currency_id}"
        )
