import javax.swing.*;
import java.awt.*;
import java.io.File;
import java.io.IOException;
import java.net.URI;

/**
 * @class ViewCommand
 * Opens an item using the native operating system application
 */
public class ViewCommand implements ICommand {
    /**
     * Opens an item using the native operating system application
     * @param o
     * @throws IOException
     */
    @Override
    public void execute(Object o) throws IOException {
        if (o == null) throw new NullPointerException();
        if (!(o instanceof Item)) throw new IllegalArgumentException("Commands should receive only Items objects");
        String location = ((Item) o).getLocation();
        if(location.startsWith("http")) {
            if (Desktop.isDesktopSupported() && Desktop.getDesktop().isSupported(Desktop.Action.BROWSE)) {
                try {
                    Desktop.getDesktop().browse(new URI(location));
                } catch (Exception e) {
                    System.err.println(e.getMessage());
                }
            }
        } else {
            if (Desktop.isDesktopSupported()) {
                Desktop.getDesktop().open(new File(location));
            }
        }

        System.out.println();

    }
}
