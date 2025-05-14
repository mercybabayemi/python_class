import segno
from PIL import Image
from pyzbar.pyzbar import decode


def generate_qr_code(menu_text, filename):
    text = segno.make(menu_text)
    text.save(filename)
    print("Qr code generated successfully")


def scan_qr_code(filename):
    img = Image.open(filename)
    decode_text = decode(img)
    for obj in decode_text:
        data = obj.data.decode("utf-8")
        return data


if __name__ == "__main__":
    menu_text = """
    Hey champ,

        You are doing well, keep going.

                Tireni toto, 
                Mercy.
    """

    generate_qr_code(menu_text, "hard_worker.png")
    scan_qr_code("hard_worker.png")