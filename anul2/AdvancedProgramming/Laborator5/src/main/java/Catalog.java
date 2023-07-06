import java.io.Serializable;
import java.util.ArrayList;
import java.util.List;

public class Catalog implements Serializable {
    private String name;
    private List<Item> items = new ArrayList<>();

    /**
     * A catalog constructor that sets the name of the class
     * @param name
     */
    public Catalog(String name) {
        this.name = name;
    }

    /**
     * Default constructor for Catalog class
     */
    public Catalog() {

    }

    /**
     * Add a new item to the catalog
     * @param newItem
     */
    public void add(Item newItem) {
        this.items.add(newItem);
    }

    /**
     * Getting the name of the catalog
     * @return name
     */
    public String getName() {
        return name;
    }

    /**
     * Getting a list of current items from the catalog
     * @return items
     */
    public List<Item> getItems() {
        return items;
    }

    /**
     * Setting the name of the catalog
     * @param name
     */
    public void setName(String name) {
        this.name = name;
    }

    /**
     * Setting a list of items to the current catalog
     * @param items
     */
    public void setItems(List<Item> items) {
        this.items = items;
    }

    /**
     * Displaying the catalog in a text format
     * @return
     */
    @Override
    public String toString() {
        return "Catalog{" +
                "name='" + name + '\'' +
                ", items=" + items +
                '}';
    }
}
