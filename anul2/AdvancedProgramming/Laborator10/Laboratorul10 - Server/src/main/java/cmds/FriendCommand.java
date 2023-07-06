package cmds;

import io.cmds.OutputCommand;
import server.Player;
import server.SimpleServer;

import java.util.List;

public class FriendCommand implements ICommand {

    public OutputCommand execute(SimpleServer s, Player p, List<String> args) {
        OutputCommand out = new OutputCommand();
        if(p == null) {
            out.setCommand("error");
            out.setMessage("You are not logged in");
            return out;
        }

        for(String user: args) {
            synchronized (s) {
                Player friend = s.getDb().getPlayerByName(user);
                if(friend == null) {
                    out.setCommand("error");
                    out.setMessage("Friend "+user+" doesn't exist on our database");
                    return out;
                }
                if(p.getFriends().contains(friend)) {
                    out.setCommand("error");
                    out.setMessage("You are already friend with "+ user + "!");
                    return out;
                }
                if(friend.getName().compareTo(p.getName()) == 0) {
                    out.setCommand("error");
                    out.setMessage("You can't be friend with yourself");
                    return out;
                }
                p.addFriend(friend);
                friend.addFriend(p);
            }
        }

        out.setCommand("display");
        out.setMessage("Your current friend list is: "+p.getFriends().toString());

        return out;
    }
}
