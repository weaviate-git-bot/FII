import java.io.IOException;
import java.util.List;

/**
 * @class ListCommand
 * Prints the list of items on the screen;
 */
public class ListCommand implements ICommand {
    /**
     * Prints the list of items on the screen;
     * @param o
     * @throws IOException
     */
    @Override
    public void execute(Object o) throws IOException {
        if (o == null) throw new NullPointerException();
        if (!(o instanceof Catalog)) throw new IllegalArgumentException("Commands should receive only Catalog objects");
        List<Item> items = ((Catalog) o).getItems();
        for(Item item : items) {
            System.out.println(item);
        }
    }
}