QR Code Manager
A Python-based QR Code Management System that allows users to generate, store, search, and decode QR codes efficiently. The system supports custom names, colors, structured data storage, and easy retrieval through a user-friendly command-line interface.

Features
✔ Generate QR Codes with custom names and colors.
✔ Store QR data in TXT, CSV, and log files.
✔ Search QR codes by name and retrieve file paths.
✔ List all generated QR codes for easy access.
✔ Decode QR codes from images to extract stored content.
✔ User-friendly CLI for seamless interaction.

Installation
Clone the repository

//bash//
git clone https://github.com/your-username/qr-code-manager.git
cd qr-code-manager
Install dependencies

//bash//
pip install qrcode[pil] pillow pyzbar
Run the program

//bash//
python qr_manager.py

Usage
Main Menu Options
1️⃣ Generate a new QR Code → Enter text, set a name, choose colors.
2️⃣ List all QR Codes → View stored QR codes.
3️⃣ Search QR Code by Name → Find QR by filename.
4️⃣ Decode a QR Code → Extract content from an image.
5️⃣ Exit → Quit the program.

File Structure
📂 qr_codes/ → Stores all generated QR images.
📄 qrcode_log.txt → Saves paths of generated QR codes.
📄 qrcode_data.txt → Stores QR content for reference.
📄 qrcode_records.csv → Maintains structured records (name, content, path).

Example Usage
Generate a QR Code


Enter the text to generate QR code: https://github.com
Enter a name for the QR code file (without extension): github_qr
Enter QR code color (default: black): blue
Enter background color (default: white): white
QR Code saved as qr_codes/github_qr.png
Search for a QR Code by Name


Enter the QR code name to search for (without extension): github_qr
qr_codes/github_qr.png
Decode a QR Code from an Image


Enter the path of the QR code image: qr_codes/github_qr.png
Decoded QR Code Data: https://github.com

Technologies Used
🔹 Python
🔹 qrcode
🔹 PIL (Pillow)
🔹 pyzbar
🔹 CSV & File Handling

Contributions
Feel free to fork this repository, create issues, and submit pull requests to enhance the project! 🚀

Let me know if you want any modifications! 😊
