import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

class PhotoSorterApp(App):
    def build(self):
        self.title = "Photo Sorter"
        self.image_directory = (r"C:\Users\chinarhitesh\OneDrive\Desktop\ChinAR\pipa")  # Replace with your image directory path
        self.image_files = []

        layout = BoxLayout(orientation='vertical')
        
        sort_button = Button(text="Sort by Alphabetical Order", on_press=self.sort_alphabetical)
        layout.add_widget(sort_button)

        sort_button = Button(text="Sort by Numerical Order", on_press=self.sort_numerical)
        layout.add_widget(sort_button)

        self.image_scrollview = ScrollView()
        layout.add_widget(self.image_scrollview)

        self.image_layout = BoxLayout(orientation='horizontal', spacing=10, padding=10)
        self.image_scrollview.add_widget(self.image_layout)

        return layout

    def sort_alphabetical(self, instance):
        self.clear_images()
        self.image_directory = (r"C:\Users\chinarhitesh\OneDrive\Desktop\ChinAR\pipa")  # Replace with your image directory path
        self.image_files = sorted(os.listdir(self.image_directory))
        self.display_images()

    def sort_numerical(self, instance):
        self.clear_images()
        self.image_directory = (r"C:\Users\chinarhitesh\OneDrive\Desktop\ChinAR\pipa\Boom")  # Replace with your image directory path
        self.image_files = sorted(os.listdir(self.image_directory), key=lambda x:3) #Removed this "int(x.split('.')[0])"
        self.display_images()

    def clear_images(self):
        self.image_layout.clear_widgets()

    def display_images(self):
        for image_file in self.image_files:
            image_path = os.path.join(self.image_directory, image_file)
            if os.path.isfile(image_path) and image_file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
                image = Image(source=image_path)
                self.image_layout.add_widget(image)

PhotoSorterApp().run()
