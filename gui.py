import tkinter as tk
from tkinter import filedialog, messagebox
import threading
from time import sleep

from read_data import read_data
from process_scores import data_cleaner
from generate_reports import report_generator
from summary_report import generate_summary


# -------------------- UI SETUP --------------------

root = tk.Tk()
root.title("Student Report Generator")
root.geometry("560x260")
root.configure(bg="#2B2B2B")
root.resizable(False, False)

# Style variables
BG = "#2B2B2B"
FG = "#EDEDED"
BTN_BG = "#3A3A3A"
BTN_FG = "#FFFFFF"
HOVER = "#4A90E2"
FRAME_BG = "#333333"


# -------------------- UI FRAMES --------------------

header_frame = tk.Frame(root, bg=BG)
header_frame.pack(fill="x", pady=(10, 5))

file_frame = tk.Frame(root, bg=FRAME_BG, padx=10, pady=10)
file_frame.pack(fill="x", pady=5, padx=10)

output_frame = tk.Frame(root, bg=FRAME_BG, padx=10, pady=10)
output_frame.pack(fill="x", pady=5, padx=10)

action_frame = tk.Frame(root, bg=BG)
action_frame.pack(fill="x", pady=10)

status_frame = tk.Frame(root, bg=BG)
status_frame.pack(fill="x", pady=(0, 10))


# -------------------- HEADER --------------------

header_lbl = tk.Label(
    header_frame,
    text="Student Report Generator",
    bg=BG, fg=FG,
    font=("Arial", 16, "bold")
)
header_lbl.pack()


# -------------------- LABELS --------------------

path_lbl = tk.Label(file_frame, text="No file selected", bg=FRAME_BG, fg=FG, anchor="w")
path_lbl.grid(row=0, column=1, sticky="w", padx=10)

output_lbl = tk.Label(output_frame, text="No output folder selected", bg=FRAME_BG, fg=FG, anchor="w")
output_lbl.grid(row=0, column=1, sticky="w", padx=10)

status_lbl = tk.Label(status_frame, text="Status: Idle", bg=BG, fg=FG, anchor="w")
status_lbl.pack(fill="x")


# -------------------- UI HELPERS --------------------

def disable_ui():
    run_btn.config(state="disabled")
    filebox_btn.config(state="disabled")
    output_btn.config(state="disabled")
    status_lbl.config(text="Status: Running...")


def enable_ui():
    run_btn.config(state="normal")
    filebox_btn.config(state="normal")
    output_btn.config(state="normal")


def on_success():
    status_lbl.config(text="Status: Done")
    enable_ui()
    messagebox.showinfo("Success", "Reports generated successfully.")


def on_error(error_message):
    status_lbl.config(text="Status: Error")
    enable_ui()
    messagebox.showerror("Error", error_message)


def enable_run_if_ready():
    if (path_lbl["text"] != "No file selected" and
            output_lbl["text"] != "No output folder selected"):
        run_btn.config(state="normal")


# -------------------- FILE SELECTION --------------------

selected_path = None
output_path = None


def open_filebox():
    global selected_path

    path = filedialog.askopenfilename(
        title="Choose an Excel file",
        filetypes=[("Excel files", "*.xlsx")]
    )

    if not path:
        messagebox.showerror("Error", "Please select a file")
        return

    selected_path = path
    path_lbl.config(text=path)
    enable_run_if_ready()


def choose_output_folder():
    global output_path

    folder = filedialog.askdirectory(title="Select Output Folder")

    if not folder:
        messagebox.showerror("Error", "Please select an output folder")
        return

    output_path = folder
    output_lbl.config(text=folder)
    enable_run_if_ready()


# -------------------- BUTTON HOVER EFFECT --------------------

def on_enter(event):
    event.widget.config(bg=HOVER)


def on_leave(event):
    event.widget.config(bg=BTN_BG)


# -------------------- THREAD CONTROL --------------------

def run():
    if not selected_path or not output_path:
        messagebox.showerror("Error", "Please select file and output folder")
        return

    disable_ui()

    worker = threading.Thread(
        target=thread_target,
        args=(selected_path, output_path),
        daemon=True
    )
    worker.start()


def thread_target(path, output_folder):
    try:
        backend(path, output_folder)
        root.after(0, on_success)
    except Exception as e:
        root.after(0, on_error, str(e))


# -------------------- BACKEND --------------------

def backend(path, output_folder):
    records = read_data(path)
    cleaned_data = data_cleaner(records)
    report_generator(cleaned_data, output_folder)
    generate_summary(cleaned_data, output_folder)
    sleep(1)


# -------------------- BUTTONS --------------------

filebox_btn = tk.Button(
    file_frame, text="Select File",
    bg=BTN_BG, fg=BTN_FG,
    activebackground=HOVER,
    relief="flat",
    width=14,
    command=open_filebox
)
filebox_btn.grid(row=0, column=0, padx=5)

output_btn = tk.Button(
    output_frame, text="Select Output",
    bg=BTN_BG, fg=BTN_FG,
    activebackground=HOVER,
    relief="flat",
    width=14,
    command=choose_output_folder
)
output_btn.grid(row=0, column=0, padx=5)

run_btn = tk.Button(
    action_frame, text="Run",
    state="disabled",
    bg=BTN_BG, fg=BTN_FG,
    activebackground=HOVER,
    relief="flat",
    width=18,
    command=run
)
run_btn.pack(side="right", padx=10)

# bind hover effect
for btn in [filebox_btn, output_btn, run_btn]:
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

root.mainloop()
