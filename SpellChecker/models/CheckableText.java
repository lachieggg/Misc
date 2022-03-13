package spellchecker.models;

public abstract class CheckableText {
  public String text;

  public abstract boolean check(Database database);

  public abstract int length();
}
