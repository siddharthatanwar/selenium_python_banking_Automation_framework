
# import pytest
# from core.config_reader import ConfigReader
# from core.logger import setup_logger

# def pytest_addoption(parser):
#     parser.addoption("--browser", action="store", default="chrome")
#     parser.addoption("--env", action="store", default=None)

# @pytest.fixture(scope="session", autouse=True)
# def load_config(request):
#     env = request.config.getoption("--env")
#     ConfigReader.load_config(env)
# @pytest.fixture(scope="session", autouse=True)
# def setup_logging():
#     setup_logger()

import pytest
from core.config_reader import ConfigReader
from core.logger import setup_logger

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--env", action="store", default=None)

@pytest.fixture(scope="session", autouse=True)
def session_setup(request):
    # 1️⃣ Load configuration FIRST
    env = request.config.getoption("--env")
    ConfigReader.load_config(env)

    # 2️⃣ Setup logging AFTER config is loaded
    setup_logger()
