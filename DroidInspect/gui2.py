
# import tkinter as tk
# from tkinter import filedialog, messagebox
# import subprocess
# import threading
# import os
# import webbrowser

# class ApkRunnerApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("DroidInspect")

#         # Configure the root window
#         self.root.configure(bg="#2c3e50")  # Dark background color
#         self.root.geometry("600x400")  # Set initial size
#         self.root.minsize(600, 400)  # Set minimum size

#         # Centering the grid configuration
#         self.root.grid_rowconfigure(0, weight=1)
#         self.root.grid_rowconfigure(1, weight=1)
#         self.root.grid_rowconfigure(2, weight=1)
#         self.root.grid_rowconfigure(3, weight=1)
#         self.root.grid_rowconfigure(4, weight=1)
#         self.root.grid_rowconfigure(5, weight=1)
#         self.root.grid_columnconfigure(0, weight=1)
#         self.root.grid_columnconfigure(1, weight=1)
#         self.root.grid_columnconfigure(2, weight=1)

#         # Title Label
#         self.title_label = tk.Label(root, text="DroidInspect: Auto UI Inspector", bg="#2c3e50", fg="white", font=("Arial", 16, "bold"))
#         self.title_label.grid(row=0, column=0, columnspan=3, padx=10, pady=20, sticky='n')

#         # Label and Entry for APK Path
#         self.label = tk.Label(root, text="Enter path of APK", bg="#2c3e50", fg="white", font=("Arial", 12))
#         self.label.grid(row=1, column=0, padx=10, pady=10, sticky='e')

#         self.apk_path_entry = tk.Entry(root, width=50)
#         self.apk_path_entry.grid(row=1, column=1, padx=10, pady=10, sticky='we')

#         self.browse_button = tk.Button(root, text="Browse", command=self.browse_file, bg="#1abc9c", fg="white", font=("Arial", 10))
#         self.browse_button.grid(row=1, column=2, padx=10, pady=10, sticky='w')

#         # Submit Button
#         self.submit_button = tk.Button(root, text="Submit", command=self.run_command, bg="#3498db", fg="white", font=("Arial", 12), width=15)
#         self.submit_button.grid(row=2, column=1, padx=5, pady=10, sticky='n')

#         # Loading Label
#         self.loading_label = tk.Label(root, text="", bg="#2c3e50", fg="white", font=("Arial", 12))
#         self.loading_label.grid(row=2, column=2, padx=5, pady=10, sticky='nw')

#         # View Result Button
#         self.view_result_button = tk.Button(root, text="View Result", command=self.view_result, bg="#9b59b6", fg="white", font=("Arial", 12), width=15)
#         self.view_result_button.grid(row=3, column=1, padx=5, pady=10, sticky='n')

#         # View State Button
#         self.view_state_button = tk.Button(root, text="View State", command=self.view_state, bg="#e67e22", fg="white", font=("Arial", 12), width=15)
#         self.view_state_button.grid(row=4, column=1, padx=5, pady=10, sticky='n')

#         self.process = None

#     def browse_file(self):
#         file_path = filedialog.askopenfilename(filetypes=[("APK files", "*.apk")])
#         if file_path:
#             self.apk_path_entry.delete(0, tk.END)
#             self.apk_path_entry.insert(0, file_path)

#     def run_command(self):
#         apk_path = self.apk_path_entry.get()
#         if apk_path and apk_path.endswith(".apk"):
#             command = ["python", "start.py", "-a", apk_path, "-o", "output"]
#             try:
#                 self.show_loading_animation()
#                 self.process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)
#                 # Create a separate thread to read the stdout and stderr
#                 threading.Thread(target=self.read_process_output, daemon=True).start()
#                 # Check the process status periodically
#                 self.root.after(100, self.check_process_status)
#             except Exception as e:
#                 self.hide_loading_animation()
#                 messagebox.showerror("Error", f"Failed to start process: {e}")
#         else:
#             messagebox.showerror("Error", "Please provide a valid APK path.")

#     def check_process_status(self):
#         if self.process and self.process.poll() is None:
#             self.root.after(100, self.check_process_status)
#         else:
#             self.hide_loading_animation()

#     def read_process_output(self):
#         if self.process:
#             try:
#                 for line in self.process.stdout:
#                     print(line.decode(), end='')
#                 for line in self.process.stderr:
#                     print(line.decode(), end='')
#                 self.hide_loading_animation()
#             except Exception as e:
#                 print(f"Error reading process output: {e}")
#                 self.hide_loading_animation()

#     def show_loading_animation(self):
#         self.loading_label.config(text="Processing...")

#     def hide_loading_animation(self):
#         self.loading_label.config(text="Error!Connect ADB device.")

#     def view_result(self):
#         result_path = os.path.join("output", "index.html")
#         if os.path.exists(result_path):
#             webbrowser.open(f"file://{os.path.realpath(result_path)}")
#         else:
#             messagebox.showerror("Error", "Result file does not exist.")

#     def view_state(self):
#         state_path = os.path.join("output", "states")
#         if os.path.exists(state_path):
#             webbrowser.open(f"file://{os.path.realpath(state_path)}")
#         else:
#             messagebox.showerror("Error", "State folder does not exist.")

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = ApkRunnerApp(root)
#     root.mainloop()


import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import threading
import os
import webbrowser

class ApkRunnerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("DroidInspect")

        # Configure the root window
        self.root.configure(bg="#2c3e50")  # Dark background color
        self.root.geometry("600x400")  # Set initial size
        self.root.minsize(600, 400)  # Set minimum size

        # Centering the grid configuration
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_rowconfigure(3, weight=1)
        self.root.grid_rowconfigure(4, weight=1)
        self.root.grid_rowconfigure(5, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)

        # Title Label
        self.title_label = tk.Label(root, text="DroidInspect: Auto UI Inspector", bg="#2c3e50", fg="white", font=("Arial", 16, "bold"))
        self.title_label.grid(row=0, column=0, columnspan=3, padx=10, pady=20, sticky='n')

        # Label and Entry for APK Path
        self.label = tk.Label(root, text="Enter path of APK", bg="#2c3e50", fg="white", font=("Arial", 12))
        self.label.grid(row=1, column=0, padx=10, pady=10, sticky='e')

        self.apk_path_entry = tk.Entry(root, width=50)
        self.apk_path_entry.grid(row=1, column=1, padx=10, pady=10, sticky='we')

        self.browse_button = tk.Button(root, text="Browse", command=self.browse_file, bg="#1abc9c", fg="white", font=("Arial", 10))
        self.browse_button.grid(row=1, column=2, padx=10, pady=10, sticky='w')

        # Submit Button
        self.submit_button = tk.Button(root, text="Submit", command=self.run_command, bg="#3498db", fg="white", font=("Arial", 12), width=15)
        self.submit_button.grid(row=2, column=1, padx=5, pady=10, sticky='n')

        # Loading Label
        self.loading_label = tk.Label(root, text="", bg="#2c3e50", fg="white", font=("Arial", 12))
        self.loading_label.grid(row=2, column=2, padx=5, pady=10, sticky='nw')

        # View Result Button
        self.view_result_button = tk.Button(root, text="View Result", command=self.view_result, bg="#9b59b6", fg="white", font=("Arial", 12), width=15)
        self.view_result_button.grid(row=3, column=1, padx=5, pady=10, sticky='n')

        # View State Button
        self.view_state_button = tk.Button(root, text="View State", command=self.view_state, bg="#e67e22", fg="white", font=("Arial", 12), width=15)
        self.view_state_button.grid(row=4, column=1, padx=5, pady=10, sticky='n')

        # View CSV File Button
        self.view_csv_button = tk.Button(root, text="View CSV File", command=self.view_csv, bg="#5eade6", fg="white", font=("Arial", 12), width=15)
        self.view_csv_button.grid(row=5, column=1, padx=5, pady=10, sticky='n')

        self.process = None

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("APK files", "*.apk")])
        if file_path:
            self.apk_path_entry.delete(0, tk.END)
            self.apk_path_entry.insert(0, file_path)

    def run_command(self):
        apk_path = self.apk_path_entry.get()
        if apk_path and apk_path.endswith(".apk"):
            command = ["python", "start.py", "-a", apk_path, "-o", "output"]
            try:
                self.show_loading_animation()
                self.process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)
                # Create a separate thread to read the stdout and stderr
                threading.Thread(target=self.read_process_output, daemon=True).start()
                # Check the process status periodically
                self.root.after(100, self.check_process_status)
            except Exception as e:
                self.hide_loading_animation()
                messagebox.showerror("Error", f"Failed to start process: {e}")
        else:
            messagebox.showerror("Error", "Please provide a valid APK path.")

    def check_process_status(self):
        if self.process and self.process.poll() is None:
            self.root.after(100, self.check_process_status)
        else:
            self.hide_loading_animation()

    def read_process_output(self):
        if self.process:
            try:
                for line in self.process.stdout:
                    print(line.decode(), end='')
                for line in self.process.stderr:
                    print(line.decode(), end='')
                self.hide_loading_animation()
            except Exception as e:
                print(f"Error reading process output: {e}")
                self.hide_loading_animation()

    def show_loading_animation(self):
        self.loading_label.config(text="Processing...")

    def hide_loading_animation(self):
        self.loading_label.config(text="")

    def view_result(self):
        result_path = os.path.join("output", "index.html")
        if os.path.exists(result_path):
            webbrowser.open(f"file://{os.path.realpath(result_path)}")
        else:
            messagebox.showerror("Error", "Result file does not exist.")

    def view_state(self):
        state_path = os.path.join("output", "states")
        if os.path.exists(state_path):
            webbrowser.open(f"file://{os.path.realpath(state_path)}")
        else:
            messagebox.showerror("Error", "State folder does not exist.")

    def view_csv(self):
        csv_path = os.path.join("output", "summary.csv")
        if os.path.exists(csv_path):
            webbrowser.open(f"file://{os.path.realpath(csv_path)}")
        else:
            messagebox.showerror("Error", "CSV file does not exist.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ApkRunnerApp(root)
    root.mainloop()
