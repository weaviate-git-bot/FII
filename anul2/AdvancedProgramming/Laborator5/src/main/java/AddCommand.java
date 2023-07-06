import java.io.IOException;

/**
 * @class AddCommand
 *  adds a new entry into the catalog;
 */
public class AddCommand implements ICommand{
    private Item item;

    /**
     * Set the item to be added on the catalog
     * @param item
     * @return AddCommand for function chaining
     */
    public AddCommand setItem(Item item) {
        this.item = item;
        return this;
    }


    /**
     * Adds a new entry into the catalog;
     * @param o a catalog object
     * @throws IOException
     */
    @Override
    public void execute(Object o) throws IOException {
        if (o == null) throw new NullPointerException();
        if (!(o instanceof Catalog)) throw new IllegalArgumentException("Commands should receive only Catalog objects");

        ((Catalog) o).add(this.item);
    }
}
