
import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
from PIL import Image, ImageTk
import base64
import os

try:
    from OpenAI import OpenAI
except ModuleNotFoundError as exc:
    OpenAI = None
    OPENAI_IMPORT_ERROR = exc
else:
    OPENAI_IMPORT_ERROR = None

# API KEY
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) if OpenAI is not None else None


def ensure_client():
    if client is None:
        messagebox.showerror(
            "Missing dependency",
            "The 'openai' package is not installed. Run: pip install openai"
        )
        return False
    return True

root = tk.Tk()
root.title("JY CHT AI")
root.geometry("950x700")
root.configure(bg="#101321")

chat_history = []
uploaded_image = None

# COLORS
BG = "#101321"
PANEL = "#1b2135"
BLUE = "#1688e8"
WHITE = "#ffffff"

# HEADER
header = tk.Label(
    root,
    text="🤖 JY CHT AI",
    font=("Arial", 28, "bold"),
    bg=BG,
    fg="#65d6ff"
)
header.pack(pady=15)

subtitle = tk.Label(
    root,
    text="Your Personal Artificial Intelligence",
    bg=BG,
    fg=WHITE,
    font=("Arial", 12)
)
subtitle.pack()

# CHAT AREA
chat = scrolledtext.ScrolledText(
    root,
    bg=PANEL,
    fg=WHITE,
    font=("Arial", 12),
    wrap=tk.WORD,
    state="disabled"
)
chat.pack(fill="both", expand=True, padx=20, pady=15)

def display_message(sender, message):
    chat.config(state="normal")
    chat.insert(tk.END, f"\n{sender}:\n{message}\n")
    chat.config(state="disabled")
    chat.see(tk.END)

# IMAGE UPLOAD
def upload_photo():
    global uploaded_image

    path = filedialog.askopenfilename(
        filetypes=[
            ("Images", "*.png *.jpg *.jpeg")
        ]
    )

    if path:
        with open(path, "rb") as f:
            uploaded_image = (
                base64.b64encode(f.read()).decode("utf-8"),
                "image/jpeg" if path.lower().endswith((".jpg", ".jpeg"))
                else "image/png"
            )

        display_message("SYSTEM", "Photo uploaded successfully!")

# SEND MESSAGE
def send_message():
    global uploaded_image

    prompt = input_box.get().strip()

    if not prompt and not uploaded_image:
        return

    input_box.delete(0, tk.END)

    display_message("YOU", prompt or "Please analyze this photo.")

    content = [
        {
            "type": "input_text",
            "text": prompt or "Describe this image."
        }
    ]

    if uploaded_image:
        image_data, mime = uploaded_image

        content.append({
            "type": "input_image",
            "image_url": f"data:{mime};base64,{image_data}"
        })

        uploaded_image = None

    chat_history.append({
        "role": "user",
        "content": content
    })

    root.config(cursor="watch")
    send_button.config(state="disabled")

    def ask_ai():
        try:
            response = client.responses.create(
                model="gpt-5.5",
                instructions=(
                    "You are JY CHT AI. "
                    "Solve questions from beginner to "
                    "extremely advanced level. "
                    "Explain answers clearly, step by step."
                ),
                input=chat_history
            )

            answer = response.output_text

            chat_history.append({
                "role": "assistant",
                "content": answer
            })

            root.after(
                0,
                lambda: display_message("JY CHT", answer)
            )

        except Exception as e:
            root.after(
                0,
                lambda: messagebox.showerror("AI Error", str(e))
            )

        finally:
            root.after(0, finish_request)

    import threading
    threading.Thread(target=ask_ai, daemon=True).start()

def finish_request():
    root.config(cursor="")
    send_button.config(state="normal")

# GENERATE IMAGE
def generate_image():
    prompt = input_box.get().strip()

    if not prompt:
        messagebox.showwarning(
            "JY CHT",
            "Enter an image description first."
        )
        return

    try:
        root.config(cursor="watch")
        root.update()

        result = client.images.generate(
            model="gpt-image-2",
            prompt=prompt,
            size="1024x1024"
        )

        image_data = base64.b64decode(
            result.data[0].b64_json
        )

        filename = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG Image", "*.png")]
        )

        if filename:
            with open(filename, "wb") as f:
                f.write(image_data)

            display_message(
                "JY CHT",
                "Your image has been generated and saved!"
            )

    except Exception as e:
        messagebox.showerror("Image Error", str(e))

    finally:
        root.config(cursor="")

# CLEAR CHAT
def clear_chat():
    chat_history.clear()
    chat.config(state="normal")
    chat.delete("1.0", tk.END)
    chat.config(state="disabled")

# INPUT
bottom = tk.Frame(root, bg=BG)
bottom.pack(fill="x", padx=20, pady=15)

input_box = tk.Entry(
    bottom,
    bg=PANEL,
    fg=WHITE,
    insertbackground=WHITE,
    font=("Arial", 13)
)
input_box.pack(
    side="left",
    fill="x",
    expand=True,
    ipady=12,
    padx=5
)

input_box.bind("<Return>", lambda event: send_message())

send_button = tk.Button(
    bottom,
    text="SEND",
    bg=BLUE,
    fg=WHITE,
    command=send_message
)
send_button.pack(side="left", padx=4)

# BUTTONS
buttons = tk.Frame(root, bg=BG)
buttons.pack(pady=10)

tk.Button(
    buttons,
    text="📷 Upload Photo",
    command=upload_photo,
    bg=PANEL,
    fg=WHITE
).pack(side="left", padx=5)

tk.Button(
    buttons,
    text="🎨 Generate Image",
    command=generate_image,
    bg=PANEL,
    fg=WHITE
).pack(side="left", padx=5)

tk.Button(
    buttons,
    text="🗑️ Clear Chat",
    command=clear_chat,
    bg=PANEL,
    fg=WHITE
).pack(side="left", padx=5)

# FOOTER
tk.Label(
    root,
    text="Powered by JY CHT AI",
    bg=BG,
    fg="#65d6ff"
).pack(pady=10)

root.mainloop()
