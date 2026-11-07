from aiohttp import ClientSession, ClientError
from async_lru import alru_cache
import logging

logger = logging.getLogger(__name__)


class HTTPClient:
    def __init__(self, base_url: str, api_key: str):
        self._session = ClientSession(
            base_url=base_url,
            headers={
                'X-CMC_PRO_API_KEY': api_key,
            }
        )

    async def close(self):
        await self._session.close()


class CMCHTTPClient(HTTPClient):
    @alru_cache
    async def get_listings(self):
        try:
            async with self._session.get(
                "/v1/cryptocurrency/listings/latest"
            ) as resp:
                if resp.status != 200:
                    logger.error(f"API error: {resp.status} - {await resp.text()}")
                    raise ClientError(f"API request failed with status {resp.status}")
                result = await resp.json()
                return result["data"]
        except Exception as e:
            logger.error(f"Error in get_listings: {e}")
            raise

    @alru_cache
    async def get_currency(self, currency_id: int):
        try:
            async with self._session.get(
                "/v2/cryptocurrency/quotes/latest",
                params={"id": currency_id}
            ) as resp:
                if resp.status != 200:
                    logger.error(f"API error: {resp.status} - {await resp.text()}")
                    raise ClientError(f"API request failed with status {resp.status}")
                result = await resp.json()
                return result["data"][str(currency_id)]
        except Exception as e:
            logger.error(f"Error in get_currency for {currency_id}: {e}")
            raise
