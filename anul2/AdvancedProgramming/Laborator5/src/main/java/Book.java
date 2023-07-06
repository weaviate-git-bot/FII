/**
 * @Class Book
 * A class that simulates a book extending an item
 */
public class Book extends Item{
    private int year;
    private String author;
    private String type;

    /**
     * Creating a new book with all required fields
     * @param title
     * @param location
     * @param year
     * @param author
     * @param type
     */
    public Book(String title, String location, int year, String author, String type) {
        super(title, location);
        this.year = year;
        this.author = author;
        this.type = type;
    }

    /**
     * Default constructor of the Book
     */
    public Book() {

    }

    /**
     * Getting the year
     * @return year
     */
    public int getYear() {
        return year;
    }

    /**
     * Setting the year
     * @param year
     */
    public void setYear(int year) {
        this.year = year;
    }

    /**
     * Getting the author
     * @return author
     */
    public String getAuthor() {
        return author;
    }

    /**
     * Setting the author
     * @param author
     */
    public void setAuthor(String author) {
        this.author = author;
    }

    /**
     * Getting the type
     * @return type
     */
    public String getType() {
        return type;
    }

    /**
     * Setting the type
     * @param type
     */
    public void setType(String type) {
        this.type = type;
    }

    @Override
    public String toString() {
        return "Book{" +
                "id='" + this.getId() + '\'' +
                ", title='" + this.getTitle() + '\'' +
                ", location='" + this.getLocation() + '\'' +
                ", year=" + year +
                ", author='" + author + '\'' +
                ", type='" + type + '\'' +
                '}';
    }
}
