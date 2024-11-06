import tkinter as tk
from tkinter import messagebox
import webbrowser

# List of sites and URLs
sites = [
    "OWASP ZAP", "Shodan", "Metasploit", "Exploit DB", "CVE Details",
    "Nmap", "VirusTotal", "Pentest-Tools", "Burp Suite", "Nessus",
    "SSL Labs", "Netcraft", "Cobalt Strike", "Intruder", "Qualys",
    "Snyk", "Rapid7", "Acunetix", "Detectify", "CyberChef"
]

urls = [
    "https://www.zaproxy.org/", "https://www.shodan.io/", "https://docs.rapid7.com/metasploit/",
    "https://www.exploit-db.com/", "https://www.cvedetails.com/", "https://nmap.org/",
    "https://www.virustotal.com/", "https://pentest-tools.com/", "https://portswigger.net/burp",
    "https://www.tenable.com/products/nessus", "https://www.ssllabs.com/", "https://sitereport.netcraft.com/",
    "https://www.cobaltstrike.com/", "https://www.intruder.io/", "https://www.qualys.com/",
    "https://snyk.io/", "https://www.rapid7.com/", "https://www.acunetix.com/",
    "https://detectify.com/", "https://gchq.github.io/CyberChef/"
]

# Variable to select the browser
selected_browser = None  # Default value (no browser selected)

# Function to open a site in the selected browser
def open_site(index):
    if selected_browser == "chrome":
        webbrowser.get("chrome").open(urls[index])
    elif selected_browser == "firefox":
        webbrowser.get("firefox").open(urls[index])
    else:
        messagebox.showerror("Error", "Please choose a browser to open the links.")

# Function to display an animated typewriter message
def show_credit():
    credit_text = "This program is made for fun. Usage:\nhttps://github.com/ml0ck"
    credit_window = tk.Toplevel(root)
    credit_window.title("Credits")
    credit_window.geometry("500x200")
    credit_window.config(bg="#1A1A2E")

    text_widget = tk.Label(credit_window, text="", font=("Courier", 12), bg="#1A1A2E", fg="#8A2BE2")
    text_widget.pack(pady=20)

    def type_writer_effect(index=0):
        if index < len(credit_text):
            text_widget.config(text=text_widget.cget("text") + credit_text[index])
            credit_window.after(50, type_writer_effect, index + 1)

    type_writer_effect()

# Function to highlight the selected browser button
def highlight_browser_button(button, browser):
    global selected_browser
    # Remove highlight from the other button
    chrome_button.config(bg="#8A2BE2")
    firefox_button.config(bg="#8A2BE2")

    # Apply highlight
    if browser == "chrome":
        selected_browser = "chrome"
        button.config(bg="#FF5733")  # Highlight color (orange)
    elif browser == "firefox":
        selected_browser = "firefox"
        button.config(bg="#FF5733")  # Highlight color (orange)

# Main function to create the interface
def create_gui():
    global root, chrome_button, firefox_button

    # Create main window
    root = tk.Tk()
    root.title("Bookmarx")
    root.geometry("660x700")  # Width increased by 10%
    root.config(bg="#1A1A2E")  # Dark purple background

    # Canvas and Scrollbar to make the window scrollable
    canvas = tk.Canvas(root, bg="#1A1A2E", highlightthickness=0)  # Remove border around the canvas
    canvas.pack(side="left", fill="both", expand=True)

    # Stylish scrollbar
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview, bg="#8A2BE2", troughcolor="#1A1A2E")
    scrollbar.pack(side="right", fill="y", padx=5)
    canvas.config(yscrollcommand=scrollbar.set)

    # Frame to contain the elements and allow scrolling
    scrollable_frame = tk.Frame(canvas, bg="#1A1A2E")
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    # Title of the window with a sleek font
    title = tk.Label(root, text="Bookmarx", font=("Fira Sans", 28, "bold"), bg="#1A1A2E", fg="#8A2BE2")
    title.place(relx=0.5, rely=0.05, anchor="center")

    # Browser selection buttons
    chrome_button = tk.Button(scrollable_frame, text="Chrome", font=("Arial", 12), width=12, height=2,
                            bg="#8A2BE2", fg="white", activebackground="#5A2D9A", activeforeground="white",
                            relief="flat", bd=0, command=lambda: highlight_browser_button(chrome_button, "chrome"))
    chrome_button.grid(row=0, column=0, padx=10, pady=10)

    firefox_button = tk.Button(scrollable_frame, text="Firefox", font=("Arial", 12), width=12, height=2,
                              bg="#8A2BE2", fg="white", activebackground="#5A2D9A", activeforeground="white",
                              relief="flat", bd=0, command=lambda: highlight_browser_button(firefox_button, "firefox"))
    firefox_button.grid(row=0, column=1, padx=10, pady=10)

    # Displaying site buttons in a 2x2 grid
    for idx, site in enumerate(sites):
        row = (idx // 2) + 1  # Row number
        col = idx % 2  # Column number (0 or 1)

        button = tk.Button(scrollable_frame, text=site, font=("Arial", 12), width=30, height=2,
                           bg="#8A2BE2", fg="white", activebackground="#5A2D9A", activeforeground="white",
                           relief="flat", bd=0, command=lambda idx=idx: open_site(idx))

        # Add hover effect on buttons
        button.bind("<Enter>", lambda event, b=button: b.config(bg="#5A2D9A"))
        button.bind("<Leave>", lambda event, b=button: b.config(bg="#8A2BE2"))

        button.grid(row=row, column=col, padx=10, pady=10)

    # Credits button
    credit_button = tk.Button(scrollable_frame, text="Credits", font=("Arial", 14), width=30, height=2,
                              bg="#4B0082", fg="white", activebackground="#5A2D9A", activeforeground="white",
                              relief="flat", bd=0, command=show_credit)
    credit_button.grid(row=(len(sites) // 2) + 1, columnspan=2, pady=10)

    # Quit button
    quit_button = tk.Button(scrollable_frame, text="Quit", font=("Arial", 14), width=30, height=2,
                            bg="#FF6347", fg="white", activebackground="#FF4500", activeforeground="white",
                            relief="flat", bd=0, command=root.quit)
    quit_button.grid(row=(len(sites) // 2) + 2, columnspan=2, pady=10)

    # Update the canvas size to fit the content
    scrollable_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    # Main loop
    root.mainloop()

# Run the GUI
if __name__ == "__main__":
    create_gui()
