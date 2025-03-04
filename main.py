import os
import importlib

def load_and_run_games(games_folder):
    for root, _, files in os.walk(games_folder):
        for file in files:
            if file.endswith(".py") and not file.startswith("__") and not file.startswith("win_"):
                # Get the full path of the file
                full_path = os.path.join(root, file)
                # Compute the module name by getting the relative path from the current directory
                relative_path = os.path.relpath(full_path, '.')  # relative to project root
                # Replace path separators with dots and strip the .py extension
                module_name = relative_path.replace(os.sep, '.')[:-3]
                
                try:
                    module = importlib.import_module(module_name)
                except Exception as e:
                    print(f"Failed to import module {module_name}: {e}")
                    continue

                # Check for a callable entry point, e.g., 'main'
                if hasattr(module, "main") and callable(module.main):
                    print(f"Running {file[:-3]}...")
                    module.main()
                else:
                    print(f"No callable main() in {module_name}")

if __name__ == "__main__":
    load_and_run_games("Games")

