#!/usr/bin/env python2.7

import pygtk
pygtk.require("2.0")
import gtk
import sys
import os
import thread
from time import sleep

from shared import *
# Cryptography libaries
import cryptography
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet

import base64
import os
import subprocess
import sys
import getpass
import uuid

SUCCESSFUL_LOG_IN = 0
FILE_DOES_NOT_EXIST = 1
WRONG_PASSPHRASE = 2

class SecureJournalGui:
		def __init__(self):
				self.successful_login = False
				self.setupLoginGui()
				self.lines = []
				self.main()
		# the main thread
		def main(self):
				try:
					gtk.main()
				except KeyboardInterrupt:
					print("\nBye")

		# initializes the GUI
		def setupLoginGui(self):
				# create a new window
				self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
				self.window.resize(400, 200)
				# set window parameters
				self.window.set_title("SecureJournal Log In")
				self.window.set_border_width(10)

				# connects the exit button to gtk.main_quit
				self.window.connect("delete-event", gtk.main_quit)

				# define and add the vertical box
				self.vbox = gtk.VBox(False, 0)
				self.window.add(self.vbox)

				# create the button and input box
				self.topBox = gtk.HBox(False, 0)

				# create the button and input box
				self.middleBox = gtk.HBox(False, 0)

				# create the button and input box
				self.bottomBox = gtk.HBox(False, 0)

				# pack the boxes
				self.vbox.pack_start(self.topBox, True, True, 0)
				self.vbox.pack_start(self.middleBox, True, True, 0)
				self.vbox.pack_start(self.bottomBox, True, True, 0)

				# label
				self.label = gtk.Label()
				self.label.set_text("Enter decryption key passphrase:")
				self.topBox.pack_start(self.label, True, True, 0)

				# text box
				self.txtInput = gtk.Entry()
				self.txtInput.set_visibility(False)
				self.middleBox.pack_start(self.txtInput, True, True, 0)

				# buttons
				self.btnExit = gtk.Button("Cancel")
				self.btnLogin = gtk.Button("Decrypt")
				self.btnNew = gtk.Button("New Journal")
				self.bottomBox.pack_start(self.btnExit, True, True, 0)
				self.bottomBox.pack_start(self.btnLogin, True, True, 0)
				self.bottomBox.pack_start(self.btnNew, True, True, 0)

				# define handler IDs
				exit_handler_id = 	self.btnExit.connect("clicked", self.btnClick, "btnExit")
				login_handler_id = 	self.btnLogin.connect("clicked", self.btnClick, "btnLogin")
				new_file_handler_id = self.btnExit.connect("clicked", self.btnClick, "btnNew")

				# show everything
				self.window.show_all()

		# initializes the GUI
		def setupJournalGui(self):
				self.window.hide()
				# create a new window
				self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
				self.window.resize(800, 600)
				# set window parameters
				self.window.set_title("SecureJournal")
				self.window.set_border_width(10)

				# connects the exit button to gtk.main_quit
				self.window.connect("delete-event", gtk.main_quit)

				# define and add the vertical box
				self.vbox = gtk.VBox(False, 0)
				self.window.add(self.vbox)

				# create the button and input box
				self.sbox = gtk.HBox(False, 0)

				# create the log viewer
				self.logView = gtk.TextView()
				self.logView.set_editable(False)

				# define the textbuffer
				self.txtBuffer = self.logView.get_buffer()

				# define the scrolled window
				self.winScroll = gtk.ScrolledWindow()
				self.winScroll.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)

				# add the textview to the scrolled window
				self.winScroll.add(self.logView)

				# define the command text box
				self.txtInput = gtk.Entry()
				self.btnSend = gtk.Button("Send")
				self.btnExit = gtk.Button("Encrypt and Exit")

				# pack vbox
				self.vbox.pack_start(self.winScroll, True, True, 0)
				self.vbox.pack_start(self.sbox, True, True, 0)

				# pack sbox (subset of vbox)
				self.sbox.pack_start(self.txtInput, True, True, 0)

				self.sbox.pack_start(self.btnSend, False, False, 0)
				self.sbox.pack_start(self.btnExit, False, False, 0)

				# define handler IDs
				send_handler_id = self.btnSend.connect("clicked", self.btnClick, "btnSend")
				exit_handler_id = self.btnExit.connect("clicked", self.btnClick, "btnExit")


				# show everything
				self.window.show_all()

		# outputs journal entries
		def output(self, msg, to_window_log=True):
				position = self.txtBuffer.get_end_iter()
				self.txtBuffer.insert(position, msg+'\n')
				# write to memory
				self.lines.append(msg)

		# Generates a key derivation function
		# Adds a salt to the input
		def getKeyDerivationFunction(self):
				# Salt the password so it cannot be attacked using rainbow tables
				# It cannot be attacked using precomputed tables because those tables
				# Are unlikely to have the salt added onto the end of the tested messages
				salt = b'\xea\x0cP!\xa4\xd7\xaa{f\xf7\x97\xdd\t\xb29`'

				# KDF - key derivation function
				# Compute the key that is associated with the password
				# Using a CHF (cryptographic hash function)
				kdf = PBKDF2HMAC(
					algorithm = hashes.SHA256(),
					length=32,
					salt=salt,
					iterations=100000,
					backend=default_backend()
				)
				return kdf

		# decrypt the input file and show it in the browser
		def decrypt_and_show(self, passphrase):
				print("Starting...")

				# Salt the passphrase so it cannot be attacked using rainbow tables
				# It cannot be attacked using precomputed tables because those tables
				# Are unlikely to have the salt added onto the end of the tested messages
				salt = b'\xea\x0cP!\xa4\xd7\xaa{f\xf7\x97\xdd\t\xb29`'

				# KDF - key derivation function
				# Compute the key that is associated with the passphrase
				# Using a CHF (cryptographic hash function)
				kdf = PBKDF2HMAC(
					algorithm = hashes.SHA256(),
					length=32,
					salt=salt,
					iterations=100000,
					backend=default_backend()
				)
				# Get the key which encrypts the file
				# And create the decryption function
				key = base64.urlsafe_b64encode(kdf.derive(passphrase))
				decrypt_function = Fernet(key)

				# Open the encrypted file for decryption
				try:
					with open('encrypted', 'rb') as encrypted_data:
						encrypted_lines = encrypted_data.read()
					decrypted_message = decrypt_function.decrypt(encrypted_lines)
					plaintext = decrypted_message.decode('ascii')
					print("Success")
					self.setupJournalGui()
					self.output(plaintext)

				except IOError as e:
					print("Encrypted file does not exist.")
					print("Continuing with blank slate.")
					return FILE_DOES_NOT_EXIST

				except cryptography.fernet.InvalidToken as e:
					print("Invalid passphrase")
					return WRONG_PASSPHRASE

		# encrypt the output and save the ciphertext to a file
		# then exit the program
		def encrypt_and_exit(self, passphrase):
				kdf = getKeyDerivationFunction()

				# Get the key which encrypts the file
				key = base64.urlsafe_b64encode(kdf.derive(passphrase))
				encrypt_function = Fernet(key)

			 	print("Encoding the message")
				# Encode the message from the file in Base64
				message = str('\n'.join(self.lines))

			  	encoded_message = message.encode()

				# Encrypt the message
				encrypted_message = encrypt_function.encrypt(encoded_message)

				# Write the encrypted file
				outputFile = open(os.getcwd() + '/' + 'encrypted', 'wb')
				outputFile.write(encrypted_message)
				print("Wrote to encrypted file")


		# a simple button event handler
		def btnClick(self, widget, args):
				if not args:
					raise ValueError
				if args == "btnSend":
					print("Sending message...")
					self.lines.append(self.txtInput.get_text())
					self.txtInput.set_text("")

				if args == "btnExit":
					# Run the encryption mechanism
					self.encrypt_and_exit(self.passphrase)
					gtk.main_quit()
				if args == "btnLogin":
					self.passphrase = self.txtInput.get_text()
					result = self.decrypt_and_show(self.txtInput.get_text())

					if(result == WRONG_PASSPHRASE):
						print("Bad passphrase")
						self.txtInput.set_text("")

## JournalGui class ##
class JournalGui:
		def __init__(self):
				self.setupGui()
				self.decrypt_and_show()
				self.lines = []
				self.running = True
				thread.start_new_thread (self.main, ())
				self.main()

		# the main thread
		def main(self):
				try:
					gtk.main()
				except KeyboardInterrupt:
					print("\nBye")

## __main__ ##
if __name__ == "__main__":
	login = SecureJournalGui()
	# check if the file exists?
	journal = JournalGui()
	journal.encrypt_and_exit()

