import qrcode


def generate_qr_code():
    print("\n========== QR Code Generator ==========")

    website_link = input("\nEnter a URL: ").strip()

    if not website_link:
        print("Error: URL cannot be empty.")
        return

    file_name = input("Enter output file name (without .png): ").strip()

    if not file_name:
        file_name = "qr_code"

    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4
    )

    qr.add_data(website_link)
    qr.make(fit=True)

    img = qr.make_image(
        fill_color="black",
        back_color="white"
    )

    img.save(f"{file_name}.png")

    print(f"\nQR Code generated successfully!")
    print(f"Saved as: {file_name}.png")


if __name__ == "__main__":
    generate_qr_code()