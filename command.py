import os
import argparse


def create_structing_folder(folder_name):
    api_folder = os.path.join(os.getcwd(), 'api')
    
    control_folder = os.path.join(api_folder, 'controllers')
    folder_path = os.path.join(control_folder, f"{folder_name.capitalize()}Controller.py")
    if os.path.exists(folder_path):
        raise FileExistsError(f"The folder '{folder_path}' already exists in the 'api' directory.")
    # Create multiple files inside the folder
    with open(os.path.join(folder_path, f"{folder_name.capitalize()}Controller.py"), 'w') as file:
        file.write("# This is a sample {} file".format(f"{folder_name.capitalize()}Controller.py"))
    
    model_folder = os.path.join(api_folder, 'models')
    folder_path = os.path.join(model_folder, f"{folder_name.capitalize()}Model.py")
    if os.path.exists(folder_path):
        raise FileExistsError(f"The folder '{folder_path}' already exists in the 'api' directory.")
    # Create multiple files inside the folder
    with open(os.path.join(folder_path, f"{folder_name.capitalize()}Model.py"), 'w') as file:
        file.write("# This is a sample {} file".format(f"{folder_name.capitalize()}Model.py"))
    
    service_folder = os.path.join(api_folder, 'services')
    folder_path = os.path.join(service_folder, f"{folder_name.capitalize()}Service.py")
    if os.path.exists(folder_path):
        raise FileExistsError(f"The folder '{folder_path}' already exists in the 'api' directory.")
    # Create multiple files inside the folder
    with open(os.path.join(folder_path, f"{folder_name.capitalize()}Service.py"), 'w') as file:
        file.write("# This is a sample {} file".format(f"{folder_name.capitalize()}Service.py"))
    
    schema_folder = os.path.join(api_folder, 'schemas')
    folder_path = os.path.join(schema_folder, f"{folder_name.capitalize()}Schema.py")
    if os.path.exists(folder_path):
        raise FileExistsError(f"The folder '{folder_path}' already exists in the 'api' directory.")
    # Create multiple files inside the folder
    with open(os.path.join(folder_path, f"{folder_name.capitalize()}Schema.py"), 'w') as file:
        file.write("# This is a sample {} file".format(f"{folder_name.capitalize()}Schema.py"))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Create a Project folder and files inside the '/api' directory.")
    parser.add_argument("folder_name", type=str, help="Name of the folder to create inside '/api'")

    args = parser.parse_args()

    folder_name = args.folder_name

    try:
        create_structing_folder(folder_name.lower())
        print(f"{folder_name}' and files created successfully inside the '/api' directory!")
    except FileExistsError as e:
        print(e)
