# micropy_launcher/launcher.py
import argparse
import importlib
import sys
from fastapi import FastAPI

def main():
    parser = argparse.ArgumentParser(description="Launch a Micropy microservice.")
    parser.add_argument("module_path", help="The path to the module containing the FastAPI app.")
    parser.add_argument("function_name", help="The function within the module that returns a FastAPI app instance.")
    parser.add_argument("--host", default="0.0.0.0", help="The host the app will run on. Defaults to 0.0.0.0")
    parser.add_argument("--port", type=int, default=8000, help="The port the app will run on. Defaults to 8000")
    
    args = parser.parse_args()
    
    module = importlib.import_module(args.module_path)
    create_app = getattr(module, args.function_name)
    
    if not callable(create_app) or not isinstance(create_app(), FastAPI):
        print(f"The function {args.function_name} must exist in {args.module_path} and return a FastAPI instance.")
        sys.exit(1)
    
    app = create_app()
    # Utilizziamo Uvicorn per eseguire l'applicazione FastAPI
    import uvicorn
    uvicorn.run(app, host=args.host, port=args.port)

if __name__ == "__main__":
    main()
