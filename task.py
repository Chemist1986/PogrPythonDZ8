import os
import json
import csv
import pickle

def save_directory_listing(directory):
    results = []
    
    for root, dirs, files in os.walk(directory):
        # Расчет размера директории с учетом всех вложенных файлов и директорий
        total_size = 0
        
        for file in files:
            file_path = os.path.join(root, file)
            total_size += os.path.getsize(file_path)
        
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            for root_dir, _, files_dir in os.walk(dir_path):
                for file_dir in files_dir:
                    file_path = os.path.join(root_dir, file_dir)
                    total_size += os.path.getsize(file_path)
        
        # Сохранение результатов обхода в список
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            results.append({
                'path': file_path,
                'type': 'file',
                'parent_directory': root,
                'size': file_size
            })
        
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            results.append({
                'path': dir_path,
                'type': 'directory',
                'parent_directory': root,
                'size': total_size
            })
    
    # Сохранение результатов в файлы JSON, CSV и Pickle
    with open('results.json', 'w') as json_file:
        json.dump(results, json_file, indent=4)
    
    with open('results.csv', 'w', newline='') as csv_file:
        fieldnames = ['path', 'type', 'parent_directory', 'size']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)
    
    with open('results.pickle', 'wb') as pickle_file:
        pickle.dump(results, pickle_file)

# Пример использования функции
directory_path = '/path/to/directory'
save_directory_listing(directory_path)