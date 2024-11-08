import os
import sys
from src.config import ServerFastapi

app = ServerFastapi()

sys.path.append(os.path.abspath("./src"))