package cmds;

import io.cmds.OutputCommand;
import server.Player;
import server.SimpleServer;

import java.util.List;

public class RegisterCommand implements ICommand {

    public OutputCommand execute(SimpleServer s, Player p, List<String> args) {
        OutputCommand out = new OutputCommand();

        synchronized (s) {
            if(s.getDb().getPlayerByName(args.get(0)) == null) {
                s.getDb().addPlayer(new Player(args.get(0)));
                out.setCommand("display");
                out.setMessage("Successfully added "+ args.get(0) + " player to database");
            } else {
                out.setCommand("error");
                out.setMessage("Player is already registered");
            }
        }

        return out;
    }
}
