import java.io.IOException;

/**
 * An interface that will mock a command execution
 */
public interface ICommand {
    void execute(Object o) throws IOException;
}
