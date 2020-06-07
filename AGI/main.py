import importlib
modules = ["compute", "generator", "GUI", "input_scrapper", "memory", "network",
"output_scrapper", "output", "read", "stack", "threads"]

for i in range(len(modules)):
    importlib.import_module(modules[i])