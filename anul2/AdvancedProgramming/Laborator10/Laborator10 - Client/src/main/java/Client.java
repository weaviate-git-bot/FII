
import cmds.DisplayCommand;
import cmds.ErrorCommand;
import cmds.ShutdownCommand;
import com.fasterxml.jackson.databind.ObjectMapper;
import io.cmds.InputCommand;
import io.cmds.OutputCommand;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ConnectException;
import java.net.Socket;
import java.net.UnknownHostException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class Client {
    private Map<String,Object> payload = new HashMap<>();
    private ObjectMapper mapper = new ObjectMapper();

    public static void main(String[] args) throws IOException {
        String serverAddress = "127.0.0.1"; // The server's IP address
        int PORT = 8100; // The server's port
        Client client = new Client();

        try (Socket socket = new Socket(serverAddress, PORT);
             PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
             BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()))) {

            while (!socket.isClosed()) {
                String request = "";
                BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

                System.out.print("[>] In: ");
                InputCommand cmd = new InputCommand();
                try {
                    request = reader.readLine();
                    cmd = new InputCommand(request);
                } catch (IOException e) {
                    e.printStackTrace();
                }
                ObjectMapper mapper = new ObjectMapper();
                request = mapper.writeValueAsString(cmd);

                out.println(request);

                // Wait the response from the server ("Hello World!")
                String response = in.readLine();
                // Send a request to the server
                OutputCommand outCmd = mapper.readValue(response, OutputCommand.class);

                switch (outCmd.getCommand()) {
                    case "display":
                        response = (new DisplayCommand()).execute(outCmd);
                        break;
                    case "error":
                        response = (new ErrorCommand()).execute(outCmd);
                        break;
                    case "set-user":
                        response = ""; //TODO: To be added
                        break;
                    case "shutdown":
                        response = (new ShutdownCommand()).setSocket(socket).execute(outCmd);
                        break;
                    default:
                        response = "Unknown command: " + outCmd.getCommand();
                }
                System.out.format("[<] %s",response);
                if(response == null) {
                    break;
                }
            }
        } catch (UnknownHostException e) {
            System.err.println("No server listening... " + e);
        } catch(ConnectException e) {
            System.err.println("Server might be closed. " + e.getMessage());
        } catch (Exception e) {
            System.err.println(e.getMessage());
        } finally {
            System.out.println("Client connection to server is closed");
        }
    }
//display
//error
//display-args
//shutdown

    private String parseInput(String req) {
        String[] parts = req.split(" ");

        this.payload.put("command", parts[0]);
        if(parts.length == 1) {
            this.payload.put("args", new ArrayList<String>());
        } else {
            this.payload.put("args", Arrays.asList(parts).subList(1, parts.length));
        }

        try {
            ObjectMapper mapper = new ObjectMapper();
            String json = mapper.writeValueAsString(payload);
            return json;
        } catch(Exception e) {
            System.out.println(e.getMessage());
            return null;
        }
    }
}
