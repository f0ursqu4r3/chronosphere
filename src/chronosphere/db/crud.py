from supabase import Client
import bcrypt
from chronosphere.db.models import User
from chronosphere.schema import UserCreate


def user_exists(supabase: Client, key: str | None = "email", value: str | None = None):
    user = supabase.table("users").select("*").eq(key, value).execute()
    return user.data is not None


def create_user(supabase: Client, user: UserCreate) -> User:
    try:
        email = user.email.lower()
        hashed_password = bcrypt.hashpw(
            user.password.encode(), bcrypt.gensalt()
        ).decode()
        if user_exists(supabase, "email", email):
            return {"message": "User already exists"}
        new_user = User(
            name=user.name,
            email=email,
            password=hashed_password,
        )
        if user := supabase.table("users").insert(new_user.model_dump()).execute():
            return {"message": "User created successfully"}
    except Exception as e:
        print(f"Error creating user: {e}")
    return {"message": "User creation failed"}


def get_user(supabase: Client, key: str | None = "email", value: str | None = None):
    user = supabase.table("users").select("*").eq(key, value).execute()
    return user.data
