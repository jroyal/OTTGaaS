from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from name_generator import get_random_name

FONT_SIZE = 14
FONT = ImageFont.truetype("appletext.ttf", FONT_SIZE)

def generate_new_tombstone(name, inscription):
    img = Image.open("base_tombstone.png")
    draw = ImageDraw.Draw(img)
    add_name(draw, name)
    add_inscription(draw, inscription)
    out_file_name = get_random_name()
    img.save("created_tombstones/{}.png".format(out_file_name))
    return out_file_name

def add_name(draw, name):
    draw.text((330, 160), "Here Lies", (0,0,0), font=FONT)
    draw.text((center(len(name)), 160 + FONT_SIZE + 10), name, (0,0,0), font=FONT)

def add_inscription(draw, inscription):
    n = 26
    split_list = split_inscription(inscription)
    for i, insc in enumerate(split_list):
        distance = 210 + ((i + 1) * (FONT_SIZE + 10))
        draw.text((center(len(insc)), distance), insc, (0,0,0), font=FONT)

def center(text_len):
    mid = text_len / 2
    if text_len % 2 == 0:
        start_loc = 330 + ((4-mid) * FONT_SIZE) + (FONT_SIZE / 2)
    else:
        start_loc = 330 + ((4-mid) * FONT_SIZE)
    return start_loc

def split_inscription(inscription):
    n = 26
    words = inscription.split()
    result = []
    current = ""
    for word in words:
        current = "{} {}".format(current, word)
        if len(current) > n:
            result.append(current)
            current = ""
    if current:
        result.append(current)
    return result

if __name__ == '__main__':
    generate_new_tombstone("Aaron Montana", "Ate corndog with no mustard. Tried putting it in gravy. Died.")
