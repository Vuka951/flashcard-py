from tkinter import ttk, Tk
from ttkthemes import ThemedStyle
from PIL import Image, ImageTk
import json
import base64
from io import BytesIO

class FlashcardApp:
    def __init__(self, master):
        self.master = master # docs: https://docs.python.org/3/library/tkinter.html#tkinter.Tk.master
        # Needed for keys to work for app use/navigation
        self.bind_key_events() # example: https://tkinterexamples.com/events/keyboard/
        self.current_card = 0
        
        with open('./cards.json', encoding='utf-8') as f:
            self.cards = json.load(f)
        
        # Frame for the card
        self.card_frame = ttk.Frame(master, width=500, height=500)
        self.card_frame.pack(padx=10, pady=10)
        
        self.front_label = ttk.Label(self.card_frame, text="", font=("Helvetica", 18), wraplength=380)
        self.front_label.pack(pady=20)
        
        self.back_label = ttk.Label(self.card_frame, text="", font=("Helvetica", 18), wraplength=380)
        
        self.image_label = ttk.Label(self.card_frame)

        self.show_button = ttk.Button(self.card_frame, text="Show", command=self.show_back)
        self.show_button.pack(pady=20)
        
        # Frame for next and previous buttons, needed so they can be on the same horizonatal line
        self.button_frame = ttk.Frame(self.card_frame)
        self.button_frame.pack(pady=10)
        
        self.prev_button = ttk.Button(self.button_frame, text="Previous Card", command=self.previous_card)
        self.prev_button.pack(side="left", padx=5)

        self.next_button = ttk.Button(self.button_frame, text="Next Card", command=self.next_card)
        self.next_button.pack(side="left", padx=5)

        # Label to display current card number
        self.card_counter_label = ttk.Label(master, text="", font=("Helvetica", 14, "bold"))
        self.card_counter_label.place(relx=0.01, rely=0.01, anchor="nw")

        style = ThemedStyle(self.master)
        style.set_theme("arc")
        
        self.show_front()

        # Credit label at the bottom
        self.credit_label = ttk.Label(master, text="Simple Flashcard by Vuka", font=("Helvetica", 10, "italic"), foreground="gray")
        self.credit_label.place(relx=0.5, rely=1.0, anchor="s")

    def show_front(self):
        self.show_button.config(state="enabled")
        card = self.cards[self.current_card]
        self.front_label.config(text=card["front_text"])
        self.front_label.pack()
        self.show_placeholders()  # Display placeholder
        self.update_card_counter()  # Update card counter
        
    def show_back(self):
        self.show_button.config(state="disabled")
        card = self.cards[self.current_card]
        self.back_label.config(text=card["back_text"])
        self.back_label.pack()

        # Check if "image" key exists
        if "image" in card:
            # If key exists, show the image
            self.show_image(f'./images/{card["image"]}')
        
    def next_card(self):
        self.current_card = (self.current_card + 1) % len(self.cards)
        self.show_front()

    def previous_card(self):
        self.current_card = (self.current_card - 1) % len(self.cards)
        self.show_front()
        
    def show_image(self, image_data):
        try:
            # Try decoding image_data assuming it's a Base64 string
            image_bytes = base64.b64decode(image_data)
            image = Image.open(BytesIO(image_bytes))
        except:
            # If decoding as Base64 fails, assume it's a file path
            image = Image.open(image_data)
        
        image = image.resize((400, 400))
        photo = ImageTk.PhotoImage(image)
        self.image_label.configure(image=photo)
        self.image_label.image = photo
        self.image_label.pack(pady=20)
        
    def show_placeholders(self):
        # Show placeholder image
        placeholder_image = Image.new("RGB", (400, 400), "lightgray")  # Creating a blank image as a placeholder
        placeholder_photo = ImageTk.PhotoImage(placeholder_image)
        self.image_label.configure(image=placeholder_photo)
        self.image_label.image = placeholder_photo
        self.image_label.pack(pady=20)
        
        # Placeholder for the back label
        self.back_label.config(text="")
        self.back_label.pack()

    def update_card_counter(self):
        # Update the card counter label
        total_cards = len(self.cards)
        current_card_number = self.current_card + 1
        self.card_counter_label.config(text=f"{current_card_number}/{total_cards}")

    def bind_key_events(self):
        self.master.bind('w', lambda _: self.show_back())
        self.master.bind('a', lambda _: self.previous_card())
        self.master.bind('d', lambda _: self.next_card())

def main():
    root = Tk()

    root.title("Simple Flashcard")  # Set the window title
    root.geometry("750x750")  # Set default window size
    root.resizable(False, False)  # Disable window resizing

    icon_path = "flashcard.ico"
    root.iconbitmap(icon_path) # Set custom icon

    FlashcardApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
