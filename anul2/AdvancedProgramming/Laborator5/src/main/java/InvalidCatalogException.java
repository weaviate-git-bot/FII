import java.io.InvalidClassException;

/**
 * A custom exception to be thrown when the loading is invalid
 */
public class InvalidCatalogException extends InvalidClassException {
    public InvalidCatalogException(String message) {
        super(message);
    }
}
