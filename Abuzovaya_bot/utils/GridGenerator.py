from PIL import Image, ImageDraw
import random
import os


class GridGenerator:
    def __init__(self, star_count):
        self.star_count = star_count
        self.grid_size = 5  # 5x5 grid
        self.cell_size = 114  # Size of each cell in pixels (will adjust based on the images)

        # Load images
        self.background = Image.open(os.path.join("../src/image/fragments", 'background.png')).convert("RGBA")
        self.frame = Image.open(os.path.join("../src/image/fragments", 'frame.png')).convert("RGBA")

    def generate_grid(self):
        # Create a new image for the grid
        grid_img = Image.new('RGBA', self.background.size)
        grid_img.paste(self.background, (0, 0))

        # Create a list of grid positions
        positions = [(x, y) for x in range(self.grid_size) for y in range(self.grid_size)]
        star_positions = random.sample(positions, self.star_count)

        for i in range(self.grid_size):
            for j in range(self.grid_size):
                x = i * self.cell_size + 21
                y = j * self.cell_size + 21
                if (i, j) in star_positions:
                    star = Image.open(os.path.join("../src/image/fragments",
                                                   f'звезды_{0 if i * 5 + j + 1 < 10 else ""}{i * 5 + j + 1}.jpg')).convert(
                        "RGBA")
                    grid_img.paste(star, (x, y), star)  # No mask needed for star
                else:
                    square = Image.open(os.path.join("../src/image/fragments",
                                                     f'Квадрат_{0 if i * 5 + j + 1 < 10 else ""}{i * 5 + j + 1}.jpg')).convert(
                        "RGBA")
                    grid_img.paste(square, (x, y), square)  # No mask needed for square
        grid_img.paste(self.frame, (0, 0), self.frame)

        return grid_img.convert("RGB")
