#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    gui.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: macarval <macarval@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/05 11:27:03 by macarval          #+#    #+#              #
#    Updated: 2026/02/05 11:27:08 by macarval         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import tkinter as tk
import ft_otp
import time
import os
import pyperclip

from tkinter import messagebox, ttk
from PIL import Image, ImageTk

# --- COLOR PALETTE ---
COLOR_BG = "#FFF0F5" # Lavender Blush (Window background)
COLOR_ACCENT = "#D81B60" # Dark Pink (Main buttons)
COLOR_TEXT = "#4A148C" # Dark Purple (Text)
COLOR_TOKEN = "#C2185B" # Hot Pink (Token)
COLOR_FRAME_BG = "#FFFFFF" # White (Frame background)

class OtpApp:
	def __init__(self, root):
		self.root = root
		self.main_screen()
		self.define_style()

		self.registration_area()
		self.token_area()

		# self.copy_button()
		self.update_token_loop()

	def main_screen(self):
		self.main_frame = tk.Frame(root, bg=COLOR_BG)
		self.main_frame.pack(fill="both", expand=True)

		self.root.title("ft_otp Authenticator")
		self.root.geometry("420x600")
		self.root.resizable(False, False)
		self.root.configure(bg=COLOR_BG)

	def define_style(self):
		self.style = ttk.Style()
		self.style.theme_use("clam")

		self.style.configure("TButton", padding=6, relief="flat",
					background="#ccc")

		self.style.configure("TLabelframe", background="white",
					relief="flat")
		self.style.configure("TLabelframe.Label", background="white",
					foreground=COLOR_TEXT, font=("Verdana", 10, "bold"))

		self.style.configure("TLabel", background="white",
					foreground="#333", font=("Verdana", 10))
		self.style.configure("Header.TLabel", background=COLOR_BG,
					foreground=COLOR_TEXT, font=("Verdana", 16, "bold"))

		self.style.configure("Horizontal.TProgressbar", background=COLOR_ACCENT,
					troughcolor="#E1E1E1", bordercolor="white",
					lightcolor=COLOR_ACCENT, darkcolor=COLOR_ACCENT)

	def registration_area(self):
		'''Area to register a new OTP key.'''
		lbl_title = ttk.Label(self.main_frame, text="OTP Manager",
						style="Header.TLabel")
		lbl_title.pack(pady=(20, 10))

		frame = ttk.LabelFrame(self.main_frame, text=" Register New Key ",
						 padding=15)
		frame.pack(fill="x", padx=20, pady=10)

		ttk.Label(frame, text="Paste Hex key below:").pack(anchor="w",
													pady=(0, 5))
		self.entry_key = ttk.Entry(frame, width=40, font=("Courier", 10))
		self.entry_key.pack(fill="x", pady=5, ipady=3)

		btn_frame = tk.Frame(frame, bg="white")
		btn_frame.pack(fill="x", pady=10)

		btn_save = self.create_custom_button(btn_frame, "Save & Generate",
									self.register_key, COLOR_ACCENT)
		btn_save.pack(side="left", fill="x", expand=True, padx=(0, 5))

		btn_qr = self.create_custom_button(btn_frame, "View QR",
									self.show_qr_popup, "#8E24AA")
		btn_qr.pack(side="right", fill="x", expand=True, padx=(5, 0))

	def create_custom_button(self, parent, text, command, bg_color):
		'''Cria um botão Tkinter padrão (não ttk) para ter controle total da cor'''
		btn = tk.Button(parent, text=text, command=command,
						bg=bg_color, fg="white",
						font=("Verdana", 9, "bold"),
						relief="flat", cursor="hand2",
						activebackground="#AD1457", activeforeground="white",
						padx=10, pady=5)
		return btn

	def register_key(self):
		'''Register a new OTP key from user input.'''
		hex_key = self.entry_key.get().strip()

		try:
			ft_otp.validate_key(hex_key)
			ft_otp.make_qr(hex_key)
			ft_otp.store_key(hex_key)

			messagebox.showinfo("Success",
					"Key saved and QR code generated (ft_otp_qr.png)!")
			self.entry_key.delete(0, tk.END)

		except Exception as e:
			messagebox.showerror("Oops!", f"Validation Error:\n{str(e)}")

	def show_qr_popup(self):
		'''Show the generated QR code in a popup window.'''
		if not os.path.exists("ft_otp_qr.png"):
			messagebox.showwarning("Not Found",
			"No QR Code.\nPlease register a key first to generate the QR code.")
			return

		popup = tk.Toplevel(self.root)
		popup.title("Scan Me")
		popup.geometry("300x350")
		popup.configure(bg="white")
		popup.resizable(False, False)

		try:
			load = Image.open("ft_otp_qr.png")
			load = load.resize((250, 250))
			render = ImageTk.PhotoImage(load)

			img_label = tk.Label(popup, image=render, bg="white")
			img_label.image = render
			img_label.pack(pady=20)

			tk.Label(popup, text="Scan with Google Authenticator", bg="white",
				fg="#555", font=("Verdana", 8)).pack()

		except Exception as e:
			messagebox.showerror("Error",
						f"Could not load QR code image:\n{str(e)}")
			popup.destroy()

	def token_area(self):
		self.frame_token = ttk.LabelFrame(self.main_frame,
									text=" Active Token ", padding=20)
		self.frame_token.pack(fill="both", expand=True, padx=20, pady=10)

		self.lbl_token = tk.Label(self.frame_token, text="--- ---",
							font=("Courier New", 35, "bold"),
							bg=COLOR_FRAME_BG, fg="#CCC")
		self.lbl_token.pack(pady=15, anchor="center")

		self.create_progress_bar()

		self.btn_copy = tk.Button(self.frame_token, text="Copy Token",
						command=self.copy_to_clipboard,
						relief="groove", bg="#F5F5F5", fg="#333",
						font=("Verdana", 9))
		self.btn_copy.pack(pady=15, ipadx=10)

	def create_progress_bar(self):
		self.progress = ttk.Progressbar(self.frame_token, orient="horizontal",
								length=300, mode="determinate")
		self.progress.pack(pady=(10, 5), fill="x")

		self.lbl_timer = ttk.Label(self.frame_token, text="Waiting...",
							font=("Verdana", 9), foreground="#888")
		self.lbl_timer.pack()

	def copy_to_clipboard(self):
		token = self.lbl_token.cget("text").replace(" ", "")

		if token and token.isdigit():
			try:
				pyperclip.copy(token)

				self.btn_copy.configure(text="Copied!", bg="#E8F5E9")
				self.root.after(1500,
					lambda: self.btn_copy.configure(text="Copy Token",
															bg="#F5F5F5"))

			except Exception as e:
				print(f"Pyperclip error: {str(e)}. Trying native...")
				self.root.clipboard_clear()
				self.root.clipboard_append(token)
				self.root.update()

		else:
			messagebox.showwarning("Wait",
						"No active token to copy.\nPlease register a key first.")

	def update_token_loop(self):
		'''Update the OTP token and progress bar every second.'''
		try:
			if os.path.exists("ft_otp.key"):
				with open("ft_otp.key", "r", encoding="utf-8") as f:
					encrypted_key = f.read().strip()

				otp = ft_otp.generate_otp(encrypted_key)
				formatted_otp = f"{otp[:3]} {otp[3:]}"

				self.lbl_token.config(text=formatted_otp, fg=COLOR_TOKEN)
				self.update_progress_bar()

			else:
				self.lbl_token.config(text="NO KEY", fg="#DDD")
				self.progress['value'] = 0
				self.lbl_timer.config(text="Please register a key above.")

		except Exception as e:
			self.lbl_token.config(text="Error", fg="red")
			self.lbl_timer.config(text=f"Error: {str(e)}")

		self.root.after(1000, self.update_token_loop)

	def update_progress_bar(self):
		passed = time.time() % 30
		remaining = 30 - passed

		self.progress["value"] = (remaining / 30) * 100
		self.lbl_timer.config(text=f"Refreshes in {int(remaining)}s")

		if remaining < 5:
			self.lbl_timer.config(foreground="red")
		else:
			self.lbl_timer.config(foreground="#888")

if __name__ == "__main__":
	root = tk.Tk()
	app = OtpApp(root)
	root.mainloop()

