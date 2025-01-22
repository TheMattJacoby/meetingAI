from PIL import Image, ImageDraw

def create_icon(state="idle"):
    """Creates a system tray icon with different states."""
    size = (64, 64)
    image = Image.new('RGB', size, (255, 255, 255))
    draw = ImageDraw.Draw(image)
    
    if state == "recording":
        draw.ellipse((10, 10, 54, 54), fill=(255, 0, 0))  # Red (Recording)
    elif state == "loading":
        draw.ellipse((10, 10, 54, 54), fill=(128, 128, 128))  # Gray (Loading)
    else:
        draw.ellipse((10, 10, 54, 54), fill=(0, 0, 0))  # Black (Idle)
    
    return image
