msg = b"GURE MEZUA HAU DA"
key = b"GAKO1234567890"
# Se ajusta la longitud de la clave para que coincida con el mensaje
key_padded = (key * (len(msg) // len(key) + 1))[:len(msg)]

# Zifratu 
crypto = bytes(a ^ b for a, b in zip(msg, key_padded))
print("Kriptograma (Hex):", crypto.hex())

# Deskodetu 
decrypted = bytes(a ^ b for a, b in zip(crypto, key_padded))
print("Mezua:", decrypted.decode())
