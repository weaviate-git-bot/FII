package cmds;

import io.cmds.OutputCommand;
import server.Player;
import server.SimpleServer;

import java.util.ArrayList;
import java.util.List;

public class SelfCommand implements ICommand {

    public OutputCommand execute(SimpleServer s, Player p, List<String> args) {
        OutputCommand out = new OutputCommand();
        if(p == null) {
            out.setCommand("error");
            out.setMessage("You are not logged in");
        } else {
            out.setCommand("set-user");
            out.setMessage("You are currently logged as "+p.getName());
            //TODO: Add user data here
//            out.setArgs((new ArrayList<>()).);
        }

        return out;
    }
}
