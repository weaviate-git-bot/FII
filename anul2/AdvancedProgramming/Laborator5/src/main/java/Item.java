import com.aventrix.jnanoid.jnanoid.NanoIdUtils;
import com.fasterxml.jackson.annotation.JsonSubTypes;
import com.fasterxml.jackson.annotation.JsonTypeInfo;

import java.io.Serializable;

/**
 * @Class Item
 *
 * An abstract class that models the Items found inside a catalog
 * Adding the decorators such that we know to which object we should map the objects
 */
@JsonTypeInfo(use = JsonTypeInfo.Id.NAME,
        property = "type")
@JsonSubTypes({
        @JsonSubTypes.Type(value = Book.class, name = "Book"),
        @JsonSubTypes.Type(value = Article.class, name = "Article"),
})
public abstract class Item implements Serializable {
    private String id;
    private String title;
    private String location;


    /**
     * The constructor of the class that takes in two parameters and generates a unique identifier
     * @param title the title of the Item
     * @param location the location of the item
     */
    public Item(String title, String location) {
        this.id = NanoIdUtils.randomNanoId();
        this.title = title;
        this.location = location;
    }

    /**
     * A default constructor for the class
     */
    public Item() {
    }


    /**
     * Getting the unique identifier of the item
     * @return id
     */
    public String getId() {
        return id;
    }


    /**
     * Setting the unique identifier of the item
     * @param id
     */
    public void setId(String id) {
        this.id = id;
    }

    /**
     * Getting the title of the item
     * @return title
     */
    public String getTitle() {
        return title;
    }

    /**
     * Setting the title of the item
     * @param title
     */
    public void setTitle(String title) {
        this.title = title;
    }

    /**
     * Getting the location of the item
     * @return location
    */
    public String getLocation() {
        return location;
    }

    /**
     * Setting the location of the item
     * @param location
     */
    public void setLocation(String location) {
        this.location = location;
    }

    @Override
    public String toString() {
        return "Item{" +
                "id='" + id + '\'' +
                ", title='" + title + '\'' +
                ", location='" + location + '\'' +
                '}';
    }
}
