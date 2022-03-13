package spellchecker;

import java.util.ArrayList;
import java.lang.Thread;
import java.io.EOFException;
import java.io.IOException;

import javax.swing.*;

import spellchecker.models.*;

public class Launcher {

	public static void main(String[] args) {
    UserInterface ui = new UserInterface();
		Database database = new Database();
		CheckableText checkableText;

		String previousText = "";
		String currentText = "";

		// initialize the database
		database.run();

		// create the user interface (thread)
		ui.start();

		while(true) {
			currentText = ui.getTextInput();

			if(previousText == null || currentText == null) {
				continue;
			}

			// update if text has changed
			if(!currentText.equals(previousText)) {
				previousText = currentText;
				currentText = ui.getTextInput();
				if(currentText.contains(" ")) {
					// contains a space
					checkableText = new Text(currentText);
				} else {
					// no spaces, treat as a word
					checkableText = new Word(currentText);
				}
				boolean result = checkableText.check(database);
				ui.updateResultLabel(result);
			}
		}

  }
}
