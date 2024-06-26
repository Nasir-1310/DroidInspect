# import tkinter as tk
# from tkinter import messagebox, filedialog
# import subprocess
# import threading
# import sys
# import trace
# import threading
# import time
# class thread_with_trace(threading.Thread):
#   def __init__(self, *args, **keywords):
#     threading.Thread.__init__(self, *args, **keywords)
#     self.killed = False
 
#   def start(self):
#     self.__run_backup = self.run
#     self.run = self.__run      
#     threading.Thread.start(self)
 
#   def __run(self):
#     sys.settrace(self.globaltrace)
#     self.__run_backup()
#     self.run = self.__run_backup
 
#   def globaltrace(self, frame, event, arg):
#     if event == 'call':
#       return self.localtrace
#     else:
#       return None
 
#   def localtrace(self, frame, event, arg):
#     if self.killed:
#       if event == 'line':
#         raise SystemExit()
#     return self.localtrace
 
#   def kill(self):
#     self.killed = True
 
# def func():
#   while True:
#     print('thread running')
 
# # t1 = thread_with_trace(target = func)
# # t1.start()
# # time.sleep(2)
# # t1.kill()
# # t1.join()
# # if not t1.isAlive():
# #   print('thread killed')
# # Global variable to store the subprocess reference
# process = None

# def browse_file():
#     file_path = filedialog.askopenfilename(filetypes=[("APK files", "*.apk")])
#     if file_path:
#         entry1.delete(0, tk.END)
#         entry1.insert(0, file_path)

# def submit_action():
#     global process
#     # Get the value from the input field
#     input1 = entry1.get()
    
#     if not input1:
#         messagebox.showwarning("Warning", "Please select an APK file.")
#         return
    
#     command = f"python start.py -a \"{input1}\" -o output"
#     print(command)
    
#     def run_command():
#         global process
#         try:
#             # Start the subprocess
#             process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            
#             stdout_lines = []
#             stderr_lines = []
#             # Read the output line by line
#             while True:
#                 output = process.stdout.readline()
#                 if output == '' and process.poll() is not None:
#                     break
#                 if output:
#                     stdout_lines.append(output.strip())
#                     print(output.strip())
#             # Capture any remaining stderr
#             stderr = process.stderr.read()
#             stderr_lines.append(stderr.strip())
            
#             if process.returncode == 0:
#                 messagebox.showinfo("Submitted", f"Input 1: {input1}\n\nCommand Output:\n{'\n'.join(stdout_lines)}")
#             else:
#                 messagebox.showerror("Error", f"Command failed with error:\n{'\n'.join(stderr_lines)}")
#         except Exception as e:
#             messagebox.showerror("Error", f"Failed to start the process:\n{str(e)}")
#         finally:
#             process = None
    
#     # Run the command in a separate thread to avoid blocking the main thread
#     thread = threading.Thread(target=run_command)
#     thread.start()

# def stop_action():
#     global process

#     if process:
#         print("Process exist")
#         process.terminate()
#         try:
#             process.wait(timeout=5)  # Ensure the process has terminated
#         except subprocess.TimeoutExpired:
#             process.kill()  # Kill the process if it does not terminate in time
#         process = None
#         messagebox.showinfo("Stopped", "The subprocess has been terminated.")
#     else:
#         messagebox.showwarning("Warning", "No process is running.")

# # Create the main window
# root = tk.Tk()
# root.title("Simple GUI")

# # Create and place the first input field
# label1 = tk.Label(root, text="APK File Path:")
# label1.pack(padx=10, pady=5)
# entry1 = tk.Entry(root, width=50)
# entry1.pack(padx=10, pady=5)

# # Create and place the browse button
# browse_button = tk.Button(root, text="Browse", command=browse_file)
# browse_button.pack(padx=10, pady=5)

# # Create and place the submit button
# submit_button = tk.Button(root, text="Submit", command=submit_action)
# submit_button.pack(padx=10, pady=20)

# # Create and place the stop button
# stop_button = tk.Button(root, text="Stop", command=stop_action)
# stop_button.pack(padx=10, pady=20)

# # Run the application
# root.mainloop()






# import tkinter as tk
# from tkinter import filedialog
# import subprocess
# import threading
# import os
# import ctypes
# process_ids = []

# class ApkRunnerApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("APK Runner")

#         # Label and Entry for APK Path
#         self.label = tk.Label(root, text="APK Path:")
#         self.label.pack(padx=20, pady=5)

#         self.apk_path_entry = tk.Entry(root, width=50)
#         self.apk_path_entry.pack(padx=20, pady=5)

#         self.browse_button = tk.Button(root, text="Browse", command=self.browse_file)
#         self.browse_button.pack(padx=20, pady=5)

#         # Submit Button
#         self.submit_button = tk.Button(root, text="Submit", command=self.run_command)
#         self.submit_button.pack(padx=20, pady=5)

#         # Stop Button
#         self.stop_button = tk.Button(root, text="Stop", command=self.stop_command)
#         self.stop_button.pack(padx=20, pady=5)

#         self.process = None
#         self.stop_thread_flag = threading.Event()

#     def browse_file(self):
#         file_path = filedialog.askopenfilename(filetypes=[("APK files", "*.apk")])
#         if file_path:
#             self.apk_path_entry.delete(0, tk.END)
#             self.apk_path_entry.insert(0, file_path)

#     def run_command(self):
#         apk_path = self.apk_path_entry.get()
#         if apk_path:
#             command = ["python", "start.py", "-a", apk_path, "-o", "output"]
#             self.process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)
#             self.stop_thread_flag.clear()
#             process_ids.append(self.process.pid)
#             # Create a separate thread to read the stdout and stderr
#             threading.Thread(target=self.read_process_output, daemon=True).start()

#     def read_process_output(self):
#         if self.process:
#             while not self.stop_thread_flag.is_set():
#                 output = self.process.stdout.readline()
#                 if output == b"" and self.process.poll() is not None:
#                     break
#                 if output:
#                     print(output.decode(), end='')
#             self.process.stdout.close()
#             self.process.stderr.close()

#     def stop_command(self):
#         print("stop called")
#         if self.process:
#             print("Process exists")
#             self.stop_thread_flag.set()  # Signal the thread to stop reading output
#             for process_id in process_ids:
#                 os.system(f"taskkill /F /T /PID {process_id}")
#             self.process = None

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = ApkRunnerApp(root)
#     root.mainloop()