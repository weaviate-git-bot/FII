package cmds;

import io.cmds.OutputCommand;

public class ErrorCommand implements ICommand{
    public String execute(OutputCommand data) {
        StringBuilder sb = new StringBuilder();

        if(data.getMessage() != null) {
            sb.append("Error: "+data.getMessage()+"\n");
        }
        return sb.toString();
    }
}
