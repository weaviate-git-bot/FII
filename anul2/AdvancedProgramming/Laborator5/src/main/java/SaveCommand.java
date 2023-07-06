import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.SerializationFeature;

import java.io.File;
import java.io.IOException;

/**
 * @class SaveCommand
 * Saves the catalog to an external file using JSON format
 */
public class SaveCommand implements ICommand {
    private String path;

    /**
     * Adding path to the command and allow function chaining
     * @param path path
     * @return this
     */
    public SaveCommand setPath(String path) {
        this.path = path;
        return this;
    }

    /**
     * Saving a catalog in a JSON format
     * @param catalog
     * @param path
     * @throws IOException
     */
    @Override
    public void execute(Object o) throws IOException {
        if (o == null) throw new NullPointerException();
        if (!(o instanceof Catalog)) throw new IllegalArgumentException("Commands should receive only Catalog objects");
        ObjectMapper mapper = new ObjectMapper();
        mapper.enable(SerializationFeature.INDENT_OUTPUT);
        mapper.writeValue(new File(this.path), ((Catalog) o));
    }
}