from chronosphere.config import config
from supabase import Client, create_client

api_url: str = config.supabase.url
key: str = config.supabase.key


def create_supabase_client() -> Client:
    supabase: Client = create_client(api_url, key)
    return supabase
