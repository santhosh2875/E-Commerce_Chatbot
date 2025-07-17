
import semantic_router
import os

print(f"semantic-router version: {semantic_router.__version__}")
print(f"Installation path: {semantic_router.__file__}")
print(f"Available in semantic_router: {dir(semantic_router)}")
print("=" * 60)

# Check the __init__.py file content
init_file = semantic_router.__file__
print(f"Reading {init_file}:")
try:
    with open(init_file, 'r') as f:
        content = f.read()
    print(content[:1000])  # First 1000 characters
    print("..." if len(content) > 1000 else "")
except Exception as e:
    print(f"Error reading file: {e}")

print("\n" + "=" * 60)

# Try to find available modules
semantic_router_dir = os.path.dirname(semantic_router.__file__)
print(f"semantic_router directory: {semantic_router_dir}")
print(f"Files in directory: {os.listdir(semantic_router_dir)}")

print("\n" + "=" * 60)

# Test individual imports
imports_to_test = [
    "from semantic_router import Route",
    "from semantic_router.layer import RouteLayer",
    "from semantic_router.router import Router", 
    "from semantic_router.encoders import HuggingFaceEncoder",
    "from semantic_router.encoders import OpenAIEncoder",
    "import semantic_router.layer",
    "import semantic_router.router",
    "import semantic_router.encoders"
]

for import_stmt in imports_to_test:
    try:
        exec(import_stmt)
        print(f"✓ {import_stmt}")
    except Exception as e:
        print(f"✗ {import_stmt} - {e}")