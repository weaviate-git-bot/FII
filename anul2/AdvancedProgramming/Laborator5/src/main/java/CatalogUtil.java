import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.SerializationFeature;

import java.io.File;
import java.io.IOException;

/**
 * A class for handling all the actions for Catalog
 *
 * @deprecated This will remain here only for "backwards compatibility"
 */
public class CatalogUtil {
    /**
     * Saving a catalog in a JSON format
     * @param catalog
     * @param path
     * @throws IOException
     */
    public static void save(Catalog catalog, String path) throws IOException {
        ObjectMapper mapper = new ObjectMapper();
        mapper.enable(SerializationFeature.INDENT_OUTPUT);
        mapper.writeValue(new File(path), catalog);
    }

    /**
     * Loading the catalog class
     * @param path the path to the file
     * @return a new catalog class loaded from the file
     * @throws InvalidCatalogException
     * @throws IOException
     */
    public static Catalog load(String path) throws InvalidCatalogException, IOException {
        ObjectMapper mapper = new ObjectMapper();
        Catalog catalog = mapper.readValue(new File(path), Catalog.class);
        return catalog;
    }
}
