import qrcode

# Dictionary mapping plant names to their page URLs
plant_pages = {
    "Hoya Obovata": "https://ticibi.github.io/plant_care/plants/hoya-obovata.html",
    "Peperomia Obtusifolia": "https://ticibi.github.io/plant_care/plants/peperomia-obtusifolia.html",
    "Variegated English Ivy": "https://ticibi.github.io/plant_care/plants/english-ivy.html",
    "Variegated Creeping Fig": "https://ticibi.github.io/plant_care/plants/ficus-pumila.html",
    "Croton": "https://ticibi.github.io/plant_care/plants/croton.html",
    "Tradescantia Zebrina": "https://ticibi.github.io/plant_care/plants/tradescantia-zebrina.html"
}

# Generate QR codes for each page
for plant, url in plant_pages.items():
    qr = qrcode.QRCode(
        version=1,  # version 1 is a 21x21 matrix; adjust if needed
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Create a filename using the plant name (lowercase, underscores)
    filename = plant.lower().replace(" ", "_") + ".png"
    img.save(filename)
    print(f"QR code for '{plant}' saved as {filename}")
