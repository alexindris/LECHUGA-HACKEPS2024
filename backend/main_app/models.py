from django.db import models
import os
import importlib

for root, dirs, files in os.walk("main_app"):
    if "models.py" in files:
        module_name = os.path.relpath(os.path.join(root, "models")).replace(os.sep, ".")
        importlib.import_module(module_name)
