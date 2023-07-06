package cmds;

import io.cmds.OutputCommand;

public class DisplayCommand implements ICommand{
    public String execute(OutputCommand data) {
        StringBuilder sb = new StringBuilder();

        if(data.getMessage() != null) {
            sb.append("Message: "+data.getMessage()+"\n");
        }
        if(data.getArgs().size() > 0) {
            sb.append("Data: \n");
            for(var msg : data.getArgs()) {
                sb.append("\t-> " + msg + "\n");
            }
        }
        return sb.toString();
    }
}
