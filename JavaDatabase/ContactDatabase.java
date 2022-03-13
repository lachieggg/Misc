import java.util.ArrayList;
import java.util.Scanner;
import java.io.ObjectOutputStream;
import java.io.EOFException;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.File;

public class ContactDatabase {
	private static ArrayList<Contact> contacts;
	private static Scanner keyboard = new Scanner(System.in);
	// Current directory
	private static String currentDir;
	// Storage file
	private static File file;
	private static FileInputStream fileInputStream;
	private static FileOutputStream fileOutputStream;
	private static ObjectOutputStream outputStream = null;
	private static ObjectInputStream inputStream = null;
	private static boolean loadFile = true;
	// Debug
	private static boolean debug = false;

	public static ArrayList<Contact> search(String sT) {
		ArrayList<Contact> listOfFoundContacts = new ArrayList<Contact>();
		for(Contact c : contacts) {
			Boolean firstNameMatch = c.getFirstName().contains(sT);
			Boolean lastNameMatch = c.getLastName().contains(sT);
			Boolean phoneNumberMatch = c.getPhoneNumber().contains(sT);
			Boolean emailMatch = c.getEmail().contains(sT);

			if(firstNameMatch || lastNameMatch || phoneNumberMatch || emailMatch) {
				listOfFoundContacts.add(c);
			}
		}
		return listOfFoundContacts;
	}
	
	public static void main(String[] args) {
		String fName, lName, ph, email, delete, sT;
		contacts = new ArrayList<Contact>();
		
		String username = System.getProperty("user.name");

		// create the input stream
		try {
			currentDir = System.getProperty("user.dir");
			file = new File(currentDir + "/contacts.txt");
			if(!file.exists() && !file.isDirectory()) {
				file.createNewFile();
			}
			fileInputStream = new FileInputStream(currentDir + "/contacts.txt");
			inputStream = new ObjectInputStream(fileInputStream);
		} catch (FileNotFoundException e) {
			loadFile = false;
			System.out.println("File not found");
		} catch (EOFException e) {
			System.out.println("New file. Not loading anything.");
			loadFile = false;
		} catch (IOException e) {
			loadFile = false;
			e.printStackTrace();
		} 
		
		
		if(loadFile) {
			// Import the file
			while(true) {
				try {
					if(debug) {
						System.out.println("Loading contact from file");
					}
					fName = inputStream.readUTF();
					lName = inputStream.readUTF();
					ph = inputStream.readUTF();
					email = inputStream.readUTF();
					contacts.add(new Contact(fName, lName, ph, email));
					
				} catch (EOFException e) {
					if(debug) {
						System.out.println("EOF");
					}
 					break;
				} catch (NullPointerException e) {
					System.out.println("Not reading the file since it does not exist yet.");
					break;
				} catch (IOException e) {
					System.out.print(e.getMessage());
					System.exit(0);
				}
			}

			// Close the file
			try {
				inputStream.close();
			} catch (IOException e) {
				e.printStackTrace();
			} catch (NullPointerException e) {
				System.out.println("File " + currentDir + "/contacts.txt doesn't exist");
			}
		}
		
		// Main loop
		while(true) {
			System.out.print("add / show / search / delete / exit: ");
			String input = keyboard.next();
			System.out.println();
			
			switch(input) {
				case "add":
					System.out.print("First Name: ");
					keyboard.nextLine();
					fName = keyboard.nextLine();
					System.out.println();

					System.out.print("Last Name: ");
					lName = keyboard.nextLine();
					System.out.println();
					
					System.out.print("Phone: ");
					ph = keyboard.nextLine();
					System.out.println();
					
					System.out.print("Email: ");
					email = keyboard.nextLine();
					System.out.println();
					
					contacts.add(new Contact(fName, lName, ph, email));

					break;
				case "show":
					for(Contact c : contacts) {
						System.out.println(c.toString());
					}
					break;
				case "search":
					System.out.print("Enter a string to search for: ");
					keyboard.nextLine();
					sT = keyboard.nextLine(); // search term 
					System.out.println();
					for(Contact c : search(sT)) {
						System.out.println(c.toString());
					}
					break;
				case "delete":
					System.out.print("Enter a string to search for: ");
					keyboard.nextLine();
					sT = keyboard.nextLine();
					System.out.println();
					
					for(Contact c : search(sT)) {
						System.out.println(c.toString());
						System.out.print("Delete?: (y/n) ");
						delete = keyboard.next();
						if(delete.equals("y") || delete.equals("yes")) {
							contacts.remove(c);
							System.out.println("Contact deleted");
						}
					}
					break;
				case "exit":
					try {
						fileOutputStream = new FileOutputStream(currentDir + "/contacts.txt");
						outputStream = new ObjectOutputStream(fileOutputStream);
						if(debug) {
							System.out.println(fileOutputStream);
							System.out.println(outputStream);
						}
						System.out.println("Exiting...");
						for(Contact c : contacts) {
							if(debug) {
								System.out.println("Writing contact to file");
							}
							c.writeToFile(outputStream);
						}
						outputStream.close();
					} catch (IOException e) {
						System.out.println("Critical error writing or closing file");
						e.printStackTrace();
					}
					System.exit(0);
				default:

					break;
			}
		}
	}
}