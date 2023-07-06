package cmds;

import io.cmds.OutputCommand;
import server.Player;
import server.SimpleServer;

import java.util.List;

/**
 * An interface that will mock a command execution
 */
public interface ICommand {

    OutputCommand execute(SimpleServer s, Player p, List<String> args);
}