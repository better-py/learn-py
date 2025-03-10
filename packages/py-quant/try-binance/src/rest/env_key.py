import os
from pathlib import Path  # Python 3.6+ only

# Example from https://pypi.org/project/python-dotenv/
from dotenv import load_dotenv

# current directory
cur_dir = os.getcwd()
project_dir = cur_dir.split("/packages/py-quant/try-binance/src/rest")[0]
env_path = Path(project_dir) / ".env"

# load env file
load_dotenv(dotenv_path=env_path)

# api key & secret
api_key = os.environ.get("BINANCE_API_KEY")
api_secret = os.environ.get("BINANCE_API_SECRET")

# print(api_key)
# print(api_secret)
