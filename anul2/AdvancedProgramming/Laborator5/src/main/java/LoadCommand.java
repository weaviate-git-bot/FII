import com.fasterxml.jackson.databind.ObjectMapper;

import java.io.File;
import java.io.IOException;

/**
 * @class LoadCommand
 * Loads the catalog from an external file
 */
public class LoadCommand implements ICommand {
    private String path;

    /**
     * Setting the path from which to load the object
     * @param path
     * @return
     */
    public LoadCommand setPath(String path) {
        this.path = path;
        return this;
    }
    /**
     * Loading the catalog class
     * @param path the path to the file
     * @return a new catalog class loaded from the file
     * @throws InvalidCatalogException
     * @throws IOException
     */
    @Override
    public void execute(Object o) throws IOException {
        if (o == null) throw new NullPointerException();
        if (!(o instanceof Catalog)) throw new IllegalArgumentException("Commands should receive only Catalog objects");
        ObjectMapper mapper = new ObjectMapper();
        Catalog catalog = mapper.readValue(new File(this.path), Catalog.class);
        ((Catalog) o).setItems(catalog.getItems());
        ((Catalog) o).setName(catalog.getName());
    }
}
