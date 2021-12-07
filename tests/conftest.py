import os
import tempfile

import pytest

from project.app import app

@pytest.fixture
def test_app():
    """Create and configure a new app instance for each test."""
    # create a temporary file to isolate the database for each test
    db_fd, db_path = tempfile.mkstemp()
    # # create the app with common test config
    # app = create_app()

    yield app

    # close and remove the temporary database
    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def client(test_app):
    """A test client for the app."""
    return test_app.test_client()


@pytest.fixture
def runner(test_app):
    """A test runner for the app's Click commands."""
    return test_app.test_cli_runner()