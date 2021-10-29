import os
from ctypes import windll


class Setup:
    def __init__(self):
        self.DIR = os.path.abspath(os.path.dirname(__file__))
        self.screen_resolution = self.get_screen_size()
        self.set_img_paths()
        self.set_regions()

    def set_img_paths(self) -> None:
        """Sets image paths to 1080 or 1440 accordingly"""
        if self.screen_resolution[1] == 1440:
            self.f3_img = os.path.join(
                self.DIR, "external_resources", "image_references", "f3_1440.PNG"
            )
            self.bobber_img = os.path.join(
                self.DIR, "external_resources", "image_references", "bobber_1440.PNG"
            )
            self.green_tension_img = os.path.join(
                self.DIR,
                "external_resources",
                "image_references",
                "green_tension_1440.PNG",
            )
            self.slacked_tension_img = os.path.join(
                self.DIR,
                "external_resources",
                "image_references",
                "slacked_tension_1440.PNG",
            )
            self.repair_img = os.path.join(
                self.DIR, "external_resources", "image_references", "repair_1440.PNG"
            )
        else:
            self.f3_img = os.path.join(
                self.DIR, "external_resources", "image_references", "f3.PNG"
            )
            self.bobber_img = os.path.join(
                self.DIR, "external_resources", "image_references", "bobber.PNG"
            )
            self.green_tension_img = os.path.join(
                self.DIR, "external_resources", "image_references", "green_tension.PNG"
            )
            self.slacked_tension_img = os.path.join(
                self.DIR,
                "external_resources",
                "image_references",
                "slacked_tension.PNG",
            )
            self.repair_img = os.path.join(
                self.DIR, "external_resources", "image_references", "repair.PNG"
            )

    def get_screen_size(self) -> tuple:
        """Returns users monitor resolution"""
        user32 = windll.user32
        screen_size = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        return screen_size

    def get_center_of_screen(self) -> tuple:
        """Returns center pixel coordinates"""
        screen_size = self.get_screen_size()
        center_screen = (int(screen_size[0] / 2), int(screen_size[1] / 2))
        return center_screen

    def set_regions(self) -> None:
        """Sets regions for image scanning"""
        number_of_columns = 12
        number_of_rows = 12

        column_width = self.screen_resolution[0] / number_of_columns
        column_height = self.screen_resolution[1] / number_of_rows

        self.repair_fishing_pole_region = [
            int(column_width * 10),  # X1
            int(column_height * 11),  # Y1
            int(column_width * 12),  # X2
            int(column_height * 12),  # Y2
        ]
        self.hold_text_region = [
            int(column_width * 6),  # X1
            int(column_height * 6),  # Y1
            int(column_width * 8),  # X2
            int(column_height * 10),  # Y2
        ]
        self.bobber_region = [
            int(column_width * 4),  # X1
            int(column_height * 1),  # Y1
            int(column_width * 8),  # X2
            int(column_height * 12),  # Y2
        ]
        self.failed_fishing_message_region = [
            int(column_width * 2),  # X1
            int(column_height * 8),  # Y1
            int(column_width * 8),  # X2
            int(column_height * 12),  # Y2
        ]


if __name__ == "__main__":
    setup = Setup()
    print(setup.bobber_icon_region)
