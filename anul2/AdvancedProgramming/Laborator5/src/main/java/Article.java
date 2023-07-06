/**
 * @Class Article
 * A class that simulates
 */
public class Article extends Item {
    private int year;
    private String author;


    /**
     * The default constructor of the article
     * @param title
     * @param location
     * @param year
     * @param author
     */
    public Article(String title, String location, int year, String author) {
        // populating the data from Item using the super keyword
        super(title, location);
        this.year = year;
        this.author = author;
    }

    /**
     * Default constructor for Article class
     */
    public Article() {
        super();
    }

    /**
     * Getting the year of the article
     * @return year
     */
    public int getYear() {
        return year;
    }

    /**
     * Setting the year of the article
     * @param year
     */
    public void setYear(int year) {
        this.year = year;
    }

    /**
     * Getting the author of the article
     * @return author
     */
    public String getAuthor() {
        return author;
    }

    /**
     * Setting the author of the article
     * @param author
     */
    public void setAuthor(String author) {
        this.author = author;
    }

    @Override
    public String toString() {
        return "Article{" +
                "id='" + this.getId() + '\'' +
                ", title='" + this.getTitle() + '\'' +
                ", location='" + this.getLocation() + '\'' +
                ", year=" + year +
                ", author='" + author + '\'' +
                '}';
    }
}
