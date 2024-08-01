import math
import hashlib
from PIL import Image, ImageDraw

def draw_shape(shape_type, size, color, sides=0, hollow=False, border_thickness=1, anti_alias=False):
    """
    draw shape
    
    :param shape_type: 'circle' | 'square' | 'polygon'
    :param size: size of the shape (diameter for circle, side length for square and polygon)
    :param color: color of the shape as a tuple (R, G, B)
    :param sides: number of sides for polygon (ignored for circle)
    :param hollow: if True, create a hollow shape
    :param border_thickness: thickness of the border for hollow shapes
    :param anti_alias: if True, apply anti-aliasing
    :return: PIL Image object
    """
    # make image larger if anti-aliasing is enabled
    scale = 4 if anti_alias else 1
    img_size = size * scale
    
    image = Image.new('RGBA', (img_size, img_size), (0, 0, 0, 0))  # transparent bg
    draw = ImageDraw.Draw(image)
    
    if shape_type == 'circle':
        if hollow:
            #outer_radius = img_size // 2
            #inner_radius = outer_radius - (border_thickness * scale)
            draw.ellipse([0, 0, img_size-1, img_size-1], fill=color + (255,))
            draw.ellipse([border_thickness*scale, border_thickness*scale, 
                          img_size-1-border_thickness*scale, img_size-1-border_thickness*scale], 
                         fill=(0, 0, 0, 0))
        else:
            draw.ellipse([0, 0, img_size-1, img_size-1], fill=color + (255,))
    
    elif shape_type == 'square':
        if hollow:
            for i in range(border_thickness):
                draw.rectangle([i, i, size - 1 - i, size - 1 - i], outline=color + (255,))
        else:
            draw.rectangle([0, 0, size - 1, size - 1], fill=color + (255,))
    
    elif shape_type == 'polygon':
        if sides < 3:
            raise ValueError('polygon must have at least 3 sides')
        
        # calculate points for the polygon
        points = []
        for i in range(sides):
            angle = i * (2 * math.pi / sides) - (math.pi / 2)  # from top center
            x = img_size / 2 + (img_size / 2) * math.cos(angle)
            y = img_size / 2 + (img_size / 2) * math.sin(angle)
            points.append((x, y))
        
        if hollow:
            draw.polygon(points, fill=color + (255,))
            inner_points = []
            for x, y in points:
                inner_x = (x - img_size/2) * (1 - 2*border_thickness*scale/img_size) + img_size/2
                inner_y = (y - img_size/2) * (1 - 2*border_thickness*scale/img_size) + img_size/2
                inner_points.append((inner_x, inner_y))
            draw.polygon(inner_points, fill=(0, 0, 0, 0))
        else:
            draw.polygon(points, fill=color + (255,))
    
    if anti_alias:
        image = image.resize((size, size), Image.LANCZOS)
    
    return image

def generate_id(image, length=8):
    '''
    generates a unique hash identifier based on image data so i dont get confused...
    
    :param image: image object
    :param length: length of identifier
    :return: string
    '''
    image_data = image.tobytes()
    full_hash = hashlib.sha1(image_data.hex().encode('utf-8')).hexdigest()
    return full_hash[:length]

def save_shape(image, filename_prefix):
    '''
    save the image
    
    :param image: image object
    :param filename_prefix: Prefix for the filename
    '''
    unique_id = generate_id(image)
    filename = f"{filename_prefix}_{unique_id}.png"
    image.save(filename, format='PNG')

if __name__ == "__main__":
    shape = draw_shape('circle', 40, (255, 255, 255), anti_alias=True)
    save_shape(shape, 'circle_aa')