from PIL import Image, ImageDraw
import numpy as np
from pathlib import Path

# Папки для картинок
real_dir = Path("data/images/real")
fake_dir = Path("data/images/fake")
real_dir.mkdir(parents=True, exist_ok=True)
fake_dir.mkdir(parents=True, exist_ok=True)

def create_image(path, color, text):
    img = Image.new("RGB", (128, 128), color=color)
    draw = ImageDraw.Draw(img)
    draw.text((10, 50), text, fill=(255, 255, 255))
    img.save(path)

# Эталонные изображения
create_image(real_dir / "real1.jpg", (0, 128, 255), "Cat")
create_image(real_dir / "real2.jpg", (0, 255, 128), "Dog")

# "Сгенерированные"
create_image(fake_dir / "fake1.jpg", (0, 100, 200), "Cat*")
create_image(fake_dir / "fake2.jpg", (0, 200, 100), "Dog*")

print(f"Картинки сохранены в {real_dir.parent.resolve()}")

