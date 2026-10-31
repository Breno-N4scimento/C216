import os

os.environ.setdefault(
    "DATABASE_URL",
    "postgresql+psycopg://postgres:postgres@localhost:5432/backend_db",
)

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, delete
from sqlalchemy.orm import sessionmaker

from app.database.base import Base
from app.database.dependencies import get_db
from app.main import app
from app.models.item import Item

TEST_DATABASE_URL = os.getenv(
    "TEST_DATABASE_URL",
    "postgresql+psycopg://postgres:postgres@localhost:5432/backend_test_db",
)

test_engine = create_engine(
    TEST_DATABASE_URL,
    pool_pre_ping=True,
)

TestingSessionLocal = sessionmaker(
    bind=test_engine,
    autoflush=False,
    autocommit=False,
)


@pytest.fixture(scope="session")
def setup_test_database():
    Base.metadata.create_all(bind=test_engine)

    yield

    test_engine.dispose()


@pytest.fixture
def db_session(setup_test_database):
    with TestingSessionLocal() as db:
        db.execute(delete(Item))
        db.commit()

        yield db

        db.execute(delete(Item))
        db.commit()


@pytest.fixture
def client(db_session):
    def override_get_db():
        yield db_session

    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()
