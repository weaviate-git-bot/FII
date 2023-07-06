package cmds;

import io.cmds.OutputCommand;
import server.Player;
import server.SimpleServer;

import java.util.ArrayList;
import java.util.List;

public class ListCommand implements ICommand {

    public OutputCommand execute(SimpleServer s, Player p, List<String> args) {
        OutputCommand out = new OutputCommand();
        if(p == null) {
            out.setCommand("error");
            out.setMessage("You are not logged in");
            return out;
        }

        switch(args.get(0)) {
            case "friends":
                out.setArgs(this.getFriends(s, p.getName()));
                out.setCommand("display");
                out.setMessage("Successfully fetched friends");
                break;
            default:
                out.setCommand("error");
                out.setMessage("Invalid list command");
        }
        return out;
    }

    private List<String> getFriends(SimpleServer s, String name) {
        synchronized (s) {
            var player = s.getDb().getPlayerByName(name);
            List<String> friendList = new ArrayList<>();
            for(var friend : player.getFriends()) {
                friendList.add(friend.getName());
            }
            return friendList;
        }
    }
}
