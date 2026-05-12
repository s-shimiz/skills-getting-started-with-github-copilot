import copy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


_INITIAL_ACTIVITIES = copy.deepcopy(activities)


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities() -> None:
    """Reset in-memory activity data to keep tests isolated."""
    activities.clear()
    activities.update(copy.deepcopy(_INITIAL_ACTIVITIES))
    yield
    activities.clear()
    activities.update(copy.deepcopy(_INITIAL_ACTIVITIES))
