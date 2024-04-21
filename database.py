import os
from supabase import create_client
import json
import datetime

# Load the environment variables from the .env file

# Get Supabase URL and API key from environment variables
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Create Supabase client
supabase_client = create_client(SUPABASE_URL, SUPABASE_KEY)


def load_jobs_from_db():
  data = supabase_client.table("jobs").select("*").execute()
  return data


def select_jobs_from_db(id):
  data = supabase_client.table("jobs").select("*").eq("id", id).execute()
  return data
