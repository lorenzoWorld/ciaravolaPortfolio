import qrcode

def create_qr_code(link):
    # Crea un oggetto QRCode
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    # Aggiunge i dati (il link) all'oggetto QRCode
    qr.add_data(link)
    qr.make(fit=True)

    # Crea un'immagine QR code utilizzando la libreria Pillow
    img = qr.make_image(fill_color="black", back_color="white")

    # Salva l'immagine QR code
    qr_filename = "qr_code.png"
    img.save(qr_filename)
    return qr_filename

# Esempio di utilizzo
link = "https://github.com/thezarathustra01/ciaravolaPortfolio"
qr_code_file = create_qr_code(link)
print(f"QR code generato e salvato nel file: {qr_code_file}")
