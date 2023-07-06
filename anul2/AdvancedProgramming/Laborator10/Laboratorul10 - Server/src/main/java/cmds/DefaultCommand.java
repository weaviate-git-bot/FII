package cmds;

import io.cmds.OutputCommand;
import server.Player;
import server.SimpleServer;

import java.util.List;

public class DefaultCommand implements ICommand {
    public OutputCommand execute(SimpleServer s, Player p, List<String> args) {
        OutputCommand out = new OutputCommand();
        out.setCommand("display");
        out.setMessage("Command not found");
        return out;
    }
}
