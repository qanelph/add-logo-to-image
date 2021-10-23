from PIL import Image
from glob import glob


images_paths = glob('./input_data/*')
logo_path = './logo.png'

logo_size = 0.2

for background_path in images_paths:
    background = Image.open(background_path)
    overlay = Image.open(logo_path)

    background = background.convert("RGBA")
    overlay = overlay.convert("RGBA")

    zoom_c = overlay.size[0] / background.size[0] / logo_size
    overlay_width = int(overlay.size[0] / zoom_c)
    overlay_height = int(overlay.size[1] / zoom_c)

    size = (overlay_width, overlay_height)

    overlay = overlay.resize(size)

    x = int((background.size[0] / 2) - (overlay_width / 2))
    y = int((background.size[1] / 2) - (overlay_height / 2))

    background.paste(overlay, box=(x, y), mask=overlay)

    # new_img = Image.blend(background, overlay, 1)

    output_path = background_path.replace('input_data', 'output_data').replace('.png', '.jpg')
    background = background.convert("RGB")
    background.save(output_path)
