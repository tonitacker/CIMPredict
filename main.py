import os
from cryptography.fernet import Fernet

import tkinter as tk
from tkinter import messagebox

# Entschlüsselungsfunktion für Modell und Abfrage-R-Skript
def decrypt_file(encrypted_file_path, decrypted_file_path, cipher_suite):
    with open(encrypted_file_path, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    with open(decrypted_file_path, 'wb') as file:
        file.write(decrypted_data)
    

def setup(currentwd):
    #Entschlüsseln der Dateien
    key = b'uTBlD3qSs77uAh5Cm7ANxuFbC-M6yelbiPt-3J1u228='
    
    cipher_suite = Fernet(key)
    
    
    currentwd = os.path.normpath(os.path.join(currentwd, "R-Skripte"))
    
    
    
    # Dateipfade definieren
    encrypted_r_script_path = os.path.join(currentwd, 'RiskAssessmentModule.encrypted')
    decrypted_r_script_path = os.path.join(currentwd, 'RiskAssessmentModule.R')
    encrypted_data_path = os.path.join(currentwd, 'modelCIMAge.encrypted')
    decrypted_data_path = os.path.join(currentwd, 'modelCIMAge.RData')
    
    # Entschlüsseln der R-Skripte und .RData-Datei
    decrypt_file(encrypted_r_script_path, decrypted_r_script_path, cipher_suite)
    decrypt_file(encrypted_data_path, decrypted_data_path, cipher_suite)

    
    ro.globalenv['currentwd_R'] = currentwd

    ro.r('setwd(currentwd_R)')
    
    # Ich hol mir die Funktion ( und die Daten ) 
    ro.r('source("RiskAssessmentModule.R")')

    #Löschen der temporär entschlüsselten Dateien
    os.remove(decrypted_r_script_path)
    os.remove(decrypted_data_path)

    
def calculate():
    CIM_input = float(cim_entry.get())
    Age_input = int(age_entry.get())
    # Überprüfen, ob das Alter im gültigen Bereich liegt
    if not (51 <= Age_input <= 90):
        raise ValueError("Das Alter muss zwischen 51 und 90 liegen.")
    ro.globalenv['CIM_input_R'] = CIM_input
    ro.globalenv['Age_input_R'] = Age_input


    result = ro.r('round(riskAssessment(CIM_input_R,Age_input_R),3)')

    result_num = result[0]
    result_perc = result_num * 100
    result_perc_format = f"{result_perc:.1f} %"
    result_label.config(text=f"Ergebnis für eine Fraktur \n innerhalb der nächsten zwei Jahre: {result_perc_format}")
def validate_inputs(*args):
    cim_value = cim_var.get()
    age_value = age_var.get()
    
    # Überprüfen, ob beide Eingabefelder nicht leer sind
    if cim_value and age_value:
        try:
            # Überprüfen, ob CIM ein float ist und das Alter im Bereich 51 bis 90 liegt
            float(cim_value)
            age = float(age_value)
            if 51 <= age <= 90:
                calculate_button.config(state="normal")
                status_label.config(text="")  # Statushinweis zurücksetzen
            else:
                calculate_button.config(state="disabled")
                status_label.config(text="Das Alter muss zwischen 51 und 90 liegen.")
        except ValueError:
            calculate_button.config(state="disabled")
            status_label.config(text="Bitte geben Sie gültige numerische Werte ein.")
    else:
        calculate_button.config(state="disabled")
        status_label.config(text="Bitte füllen Sie alle Felder aus.")

##############################################################################
currentwd = os.getcwd()
dll_dir = os.path.normpath(os.path.join(currentwd, "portableR","bin", "x64"))

os.add_dll_directory(dll_dir)
r_dir = os.path.normpath(os.path.join(currentwd, "portableR"))
print(r_dir)
os.environ['R_HOME'] = r_dir
import rpy2.robjects as ro        
setup(currentwd)

# Hauptfenster tkinter
script_dir = os.path.dirname(__file__)
#print(script_dir)
root = tk.Tk()
root.title("CIMPredict")

# todo: rel. Pfad für Distribution
root.iconbitmap(os.path.normpath(os.path.join(script_dir, "favicon.ico")))



# StringVar-Objekte erstellen
cim_var = tk.StringVar()
age_var = tk.StringVar()

# Eingabefelder für CIM_input
cim_label = tk.Label(root, text="CIM-Wert:")
cim_label.grid(row=0, column=0)
cim_entry = tk.Entry(root, textvariable = cim_var)
cim_entry.grid(row=0, column=1, padx  =10 , pady = 20)

# Eingabefelder für Age_input
age_label = tk.Label(root, text="Alter des Patienten:")
age_label.grid(row=1, column=0)
age_entry = tk.Entry(root, textvariable = age_var)
age_entry.grid(row=1, column=1, padx  =10 , pady = 20)

# Überwachung der Eingabefelder, um den Button zu aktivieren/deaktivieren
cim_var.trace_add("write", validate_inputs)
age_var.trace_add("write", validate_inputs)

# Button zum Berechnen des Prozentsatzes
calculate_button = tk.Button(root, text="Berechnen", command=calculate)
calculate_button.grid(row=3, column=0, padx  =10 , pady = 10)
calculate_button.config(state="disabled")

# Label, um das Ergebnis anzuzeigen
result_label = tk.Label(root, text="Ergebnis für eine Fraktur \n innerhalb der nächsten zwei Jahre:")
result_label.grid(row=3, column  =1 , padx  =10 , pady = 10)
# Statuslabel für Hinweise
status_label = tk.Label(root, text="", fg="red")
status_label.grid(row=4, columnspan=2)

# Label für Versionsdaten und Copyright
version = "CIMPredict 1.1.1"
copyright = "© 2024 Stryker Trauma GmbH - Stryker confidential for internal use only"
version_label = tk.Label(root, text=version, anchor='e')
version_label.grid(row=4, column=3, padx=10, pady=5, sticky='e')

copyright_label = tk.Label(root, text=copyright, anchor='e')
copyright_label.grid(row=5, column=0, columnspan=3, padx=10, pady=5, sticky='e')

# Hauptloop starten
root.mainloop()

