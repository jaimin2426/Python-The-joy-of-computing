import pyqrcode
import png   # Required for PNG support
from pyqrcode import QRCode

site = "https://www.linkedin.com/feed/"

# Create the QR code
url_qr = pyqrcode.create(site)

# Save as SVG
url_qr.svg("great.svg", scale=8)

# Save as PNG
url_qr.png("great.png", scale=6)
