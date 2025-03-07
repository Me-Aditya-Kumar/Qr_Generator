import qrcode
import os
import time
import csv
from PIL import Image
from pyzbar.pyzbar import decode

QR_FOLDER = "qr_codes"
LOG_FILE = "qrcode_log.txt"
DATA_FILE = "qrcode_data.txt"
CSV_FILE = "qrcode_records.csv"

if not os.path.exists(QR_FOLDER):
    os.makedirs(QR_FOLDER)

def generate_qr(data, color="black", bg_color="white"):
    custom_name = input("Enter a name for the QR code file (without extension): ").strip()
    if custom_name:
        qr_filename = os.path.join(QR_FOLDER, f"{custom_name}.png")
    else:
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        qr_filename = os.path.join(QR_FOLDER, f"qr_{timestamp}.png")

    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)

    qr_img = qr.make_image(fill_color=color, back_color=bg_color)
    qr_img.save(qr_filename)

    with open(DATA_FILE, "a") as file:
        file.write(data + "\n")

    with open(LOG_FILE, "a") as log_file:
        log_file.write(f"{qr_filename}\n")

    with open(CSV_FILE, "a", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([custom_name if custom_name else "qr_" + time.strftime("%Y%m%d_%H%M%S"), data, qr_filename])

    qr_img.show()
    print(f"QR Code saved as {qr_filename}")

def list_qr_codes():
    if not os.path.exists(LOG_FILE):
        print("No QR codes generated yet.")
        return

    print("\nSaved QR Codes:")
    with open(LOG_FILE, "r") as log_file:
        for line in log_file:
            print(line.strip())

def search_qr_by_name(qr_name):
    if not os.path.exists(LOG_FILE):
        print("Cannot Find Specified QR")
        return

    found = False
    with open(LOG_FILE, "r") as log_file:
        for line in log_file:
            if qr_name in line:
                print(line.strip())  # Print only the file path
                found = True
                break

    if not found:
        print("Cannot Find Specified QR")

def decode_qr(image_path):
    try:
        img = Image.open(image_path)
        decoded_data = decode(img)

        if decoded_data:
            for obj in decoded_data:
                print(f"Decoded QR Code Data: {obj.data.decode('utf-8')}")
        else:
            print("No QR code found in the image.")
    except Exception as e:
        print(f"Error: {e}")

while True:
    print("\nQR Code Generator Menu:")
    print("1. Generate a new QR Code")
    print("2. List all QR Codes")
    print("3. Search for a QR Code by Name")
    print("4. Decode a QR Code from an Image")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        input_data = input("Enter the text to generate QR code: ")
        color = input("Enter QR code color (default: black): ") or "black"
        bg_color = input("Enter background color (default: white): ") or "white"
        generate_qr(input_data, color, bg_color)
    elif choice == "2":
        list_qr_codes()
    elif choice == "3":
        qr_name = input("Enter the QR code name to search for (without extension): ").strip()
        search_qr_by_name(qr_name)
    elif choice == "4":
        img_path = input("Enter the path of the QR code image: ")
        decode_qr(img_path)
    elif choice == "5":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number between 1-5.")
