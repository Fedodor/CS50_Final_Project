from src.config import settings
from src.http_client import CMCHTTPClient
import atexit


cmc_client = CMCHTTPClient(
    base_url="https://pro-api.coinmarketcap.com",
    api_key=settings.CMC_API_KEY
)

# Ensure the client is closed when the application exits
atexit.register(lambda: cmc_client.close())
