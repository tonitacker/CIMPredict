from cryptography.fernet import Fernet

# Generiere einen Schlüssel für die Verschlüsselung
key = b'uTBlD3qSs77uAh5Cm7ANxuFbC-M6yelbiPt-3J1u228='
cipher_suite = Fernet(key)

# Verschlüssel die R-Skripte
def encrypt_file(file_path, encrypted_file_path, cipher_suite):
    with open(file_path, 'rb') as file:
        file_data = file.read()
    encrypted_data = cipher_suite.encrypt(file_data)
    with open(encrypted_file_path, 'wb') as file:
        file.write(encrypted_data)

encrypt_file('RiskAssessmentModule.R', 'RiskAssessmentModule.encrypted', cipher_suite)
encrypt_file('modelCIMAge.RData', 'modelCIMAge.encrypted', cipher_suite)
# Speichere den Schlüssel sicher
with open('key.key', 'wb') as key_file:
    key_file.write(key)
print("success")
