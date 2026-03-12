import os
import shutil
import tkinter as tk
from tkinter import messagebox
import webbrowser

def copy_and_rename_html_file():
    main_folder = r"C:\Users\szhur\Documents\Избранное\мои игры и программы"
    specific_folder = r"C:\Users\szhur\Documents\Избранное\мои игры и программы\управление гф-8 - сайт"
    
    source_file = os.path.join(main_folder, "управление гф-8.html")
    file_to_delete = os.path.join(specific_folder, "index.html")
    target_file = os.path.join(specific_folder, "index.html")
    
    try:
        if not os.path.exists(source_file):
            messagebox.showerror("Ошибка", f"Исходный файл не найден:\n{source_file}")
            return
        
        if not os.path.exists(specific_folder):
            messagebox.showerror("Ошибка", f"Целевая папка не найдена:\n{specific_folder}")
            return
        
        if os.path.exists(file_to_delete):
            os.remove(file_to_delete)
        
        shutil.copy2(source_file, target_file)
        
        root = tk.Tk()
        root.withdraw()
        result = messagebox.showinfo("Успешно", "Операция успешно завершена!\n\nНажмите ОК, чтобы открыть сайт загрузки.")
        
        if result == "ok":
            webbrowser.open("https://github.com/UGF-master/ugf-8/upload/main")
        
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка:\n{e}")

if __name__ == "__main__":
    copy_and_rename_html_file()
