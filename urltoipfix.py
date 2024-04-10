import customtkinter
import socket

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light")
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("URL to IP Checker")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="URL to IP Checker", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # create main entry and button
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Enter URL")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), text="Check URL to IP", command=self.check_url_to_ip)
        self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # create text widget to display result
        self.result_text = customtkinter.CTkTextbox(self, height=300, width=40)
        self.result_text.grid(row=4, column=1, columnspan=3, padx=(20, 0), pady=(0, 20), sticky="nsew")

    def check_url_to_ip(self):
        url_input = self.entry.get()
        ip_address = self.resolve_ip_from_url(url_input)
        if ip_address:
            self.result_text.delete(1.0, customtkinter.END)
            self.result_text.insert(customtkinter.END, f"The IP address of {url_input} is: {ip_address}")
        else:
            self.result_text.delete(1.0, customtkinter.END)
            self.result_text.insert(customtkinter.END, "Invalid URL")

    def resolve_ip_from_url(self, url):
        try:
            if url.startswith("https://"):
                url = url[8:]  # Remove "https://"
            elif url.startswith("http://"):
                url = url[7:]  # Remove "http://"
            ip_address = socket.gethostbyname(url)
            return ip_address
        except socket.gaierror:
            return None

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

if __name__ == "__main__":
    app = App()
    app.mainloop()
