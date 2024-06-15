import customtkinter as ctk
from tkinter import messagebox
import subprocess
import os

def download_playlist(playlist_url, playlist_name):
    try:
        os.makedirs(playlist_name, exist_ok=True)
        if not os.listdir(playlist_name):
            messagebox.showinfo("Info", f"Creating folder: {playlist_name}")

            # Execute spotdl with proper escaping for security
            subprocess.run(
                ["spotdl", "download", playlist_url],
                cwd=playlist_name,
                check=True
            )
            messagebox.showinfo("Info", f"Downloaded songs from playlist: {playlist_name}")
        else:
            messagebox.showwarning("Warning", f"Folder '{playlist_name}' already exists and is not empty.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Error downloading playlist: {e}")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

def on_download_clicked():
    playlist_url = playlist_url_entry.get()
    folder_name = folder_name_entry.get()

    if playlist_url and folder_name:
        download_playlist(playlist_url, folder_name)
    else:
        messagebox.showwarning("Warning", "Please enter both playlist URL and folder name.")

# Set customtkinter appearance mode and theme
ctk.set_appearance_mode("dark")  # Modes: "dark", "light"
ctk.set_default_color_theme("green")  # Themes: "blue", "dark-blue", "green"

# Spotify-inspired color scheme for the download button
spotify_green = "#1DB954"
text_color = "#FFFFFF"

# Create customtkinter window
window = ctk.CTk()
window.title("Spotify Playlist Downloader")

# Create a frame to hold the content
content_frame = ctk.CTkFrame(window)
content_frame.pack(padx=20, pady=20, fill="both", expand=True)

# Playlist URL Label and Entry
playlist_url_label = ctk.CTkLabel(content_frame, text="Spotify Playlist URL:")
playlist_url_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
playlist_url_entry = ctk.CTkEntry(content_frame)
playlist_url_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

# Folder Name Label and Entry
folder_name_label = ctk.CTkLabel(content_frame, text="Folder Name:")
folder_name_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
folder_name_entry = ctk.CTkEntry(content_frame)
folder_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

# Download Button with Spotify-inspired color
download_button = ctk.CTkButton(content_frame, text="Download", command=on_download_clicked, fg_color=spotify_green, text_color=text_color)
download_button.grid(row=2, column=0, columnspan=2, padx=5, pady=10, sticky="ew")

# Set padding and resizing properties for all widgets in the content frame
for child in content_frame.winfo_children():
    child.grid_configure(padx=10, pady=5, sticky="ew")

window.mainloop()
