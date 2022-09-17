import os
from supabase.client import create_client, Client

url: str = os.environ.get("SUPABASE_URL") or ""
key: str = os.environ.get("SUPABASE_KEY") or ""

db: Client = create_client(url, key)
