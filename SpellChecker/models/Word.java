package spellchecker.models;

public class Word extends CheckableText {

  // constructor
  public Word(String text) {
    this.text = text;
  }

  // check the word
  public boolean check(Database database) {
    if(database.checkWord(this.text)) {
      return true;
    }
    return false;
  }

  // return the length
  public int length() {
    return this.text.length();
  }
}
