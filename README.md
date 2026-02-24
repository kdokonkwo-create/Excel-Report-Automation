# Excel Report Automation Tool

## 📌 Overview

The Excel Report Automation Tool is a Python-based desktop application that processes a predefined Excel file containing structured student records and automatically generates:

- Individual student performance reports (one per row of data)
- A consolidated summary report

The application includes a simple graphical user interface (GUI) that allows users to select an input file and choose a destination folder for generated reports.

---

## 🚀 Problem It Solves

Manually generating structured reports from spreadsheet data is repetitive and inefficient.

This tool automates the process by:

- Reading structured Excel data
- Processing each row programmatically
- Generating formatted reports automatically
- Organizing output files in a user-selected directory

This reduces manual effort and improves reporting consistency.

---

## 📊 Sample Use Case

The sample dataset used in this project contains student records with the following fields:

- student ID
- full name 
- Course  
- CA1  
- CA2  
- CA3  

### Output Generated

1. **Individual Student Reports**
   - One report per student
   - Displays all CA scores
   - Structured and formatted output

2. **Summary Report**
   - Consolidated overview of all students
   - Structured for quick review and analysis

---

## 🖥 How to Use

1. Launch the application.
2. Click **"Select Excel File"** and choose the predefined Excel file containing student records.
3. Click **"Select Destination Folder"** and choose where you want the generated reports to be saved.
4. Click **"Generate Reports"**.
5. The program will:
   - Read the Excel file
   - Process each row of student data
   - Generate individual reports
   - Generate a summary report
   - Save all reports in the selected folder

No manual editing or formatting is required.

---

## 🛠 Technologies Used

- Python    
- OpenPyXL  
- Tkinter (for GUI)

---


