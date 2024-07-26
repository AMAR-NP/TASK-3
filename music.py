import customtkinter as ctk
import lyricsgenius
from tkinter import messagebox

# Initialize Genius API
genius = lyricsgenius.Genius("LvBUbHXUEbCt0boym4MxdFmhH2t4prhvFvSLcYO44X_QGm9ZTsRGSotrNkLPHTbT")

def get_lyrics():
    song_title = song_title_entry.get()
    artist_name = artist_name_entry.get()

    if not song_title:
        messagebox.showerror("Input Error", "Song title is required.")
        return

    try:
        if artist_name:
            song = genius.search_song(song_title, artist_name)
        else:
            song = genius.search_song(song_title)
        
        if song:
            show_lyrics(song)
        else:
            messagebox.showinfo("Lyrics Not Found", "Lyrics not found. Please check the title and try again.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def show_lyrics(song):
    lyrics_window = ctk.CTkToplevel(root)
    lyrics_window.title(f"Lyrics for '{song.title}' by {song.artist}")
    
    lyrics_text = ctk.CTkTextbox(lyrics_window, wrap='word')
    lyrics_text.pack(expand=True, fill='both')
    
    lyrics_text.insert('end', song.lyrics)
    lyrics_text.configure(state='disabled')

# Set the appearance to dark mode
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Main window setup
root = ctk.CTk()
root.title("Lyrics Finder")

# Song title label and entry
ctk.CTkLabel(root, text="Song Title:").grid(row=0, column=0, padx=10, pady=10)
song_title_entry = ctk.CTkEntry(root, width=300)
song_title_entry.grid(row=0, column=1, padx=10, pady=10)

# Artist name label and entry
ctk.CTkLabel(root, text="Artist Name (optional):").grid(row=1, column=0, padx=10, pady=10)
artist_name_entry = ctk.CTkEntry(root, width=300)
artist_name_entry.grid(row=1, column=1, padx=10, pady=10)

# Search button
search_button = ctk.CTkButton(root, text="Search Lyrics", command=get_lyrics, corner_radius=10)
search_button.grid(row=2, columnspan=2, pady=10)

# Run the application
root.mainloop()
