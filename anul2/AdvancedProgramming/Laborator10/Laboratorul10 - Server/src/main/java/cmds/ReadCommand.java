package cmds;

import io.cmds.OutputCommand;
import server.Player;
import server.SimpleServer;

import java.util.ArrayList;
import java.util.List;

public class ReadCommand implements ICommand {

    public OutputCommand execute(SimpleServer s, Player p, List<String> args) {
        OutputCommand out = new OutputCommand();
        if(p == null) {
            out.setCommand("error");
            out.setMessage("You are not logged in");
            return out;
        }
        List<String> messages = new ArrayList<>();
        for(var msg : p.getMessagesToRead()) {
            synchronized (p) {
                messages.add(msg);
            }
        }
        p.setMessagesToRead(new ArrayList<>());
        out.setCommand("display");
        out.setMessage("Successfully read all messages to all your friends");
        out.setArgs(messages);
        return out;
    }
}
