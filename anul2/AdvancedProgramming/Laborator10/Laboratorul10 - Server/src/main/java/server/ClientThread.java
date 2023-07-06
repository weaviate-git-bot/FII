package server;

import cmds.*;
import com.fasterxml.jackson.databind.ObjectMapper;
import io.cmds.InputCommand;
import io.cmds.OutputCommand;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;

public class ClientThread implements Runnable {
    private Socket socket = null;
    private SimpleServer server = null;
    private Player currentPlayer = null;

    public ClientThread(Socket socket, SimpleServer s) {
        this.socket = socket;
        this.server = s;
    }

    public synchronized void run() {
        try {
            System.out.println("Server created a new client thread");
            String req = "continue", res = "";
            var lastCommandReceived = System.currentTimeMillis();
            while (server.isRunning()) {
                // Get the request from the input stream: client → server
                req = this.gotText();

                if(req == null) {
                    if(System.currentTimeMillis() - lastCommandReceived > server.CLIENT_CONNECTION_TIMEOUT) {
                        System.out.println("Closed connection with client");
                        this.socket.close();
                        break;
                    } else {
                        continue;
                    }
                }
                // here we got a valid command
                lastCommandReceived = System.currentTimeMillis();
                // Send the response to the output stream: server → client
                res = this.parseRequest(req);
                PrintWriter out = new PrintWriter(socket.getOutputStream());

                out.println(res);
                out.flush();
            }
        } catch (IOException e) {
            System.err.println(e.getStackTrace().toString());
        }
    }

    private String gotText() {
        try {
            socket.setSoTimeout(2000);
            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            return in.readLine();
        } catch(Exception e) {
        }
        return null;
    }

    private String parseRequest(String req) throws com.fasterxml.jackson.core.JsonProcessingException {
        ObjectMapper mapper = new ObjectMapper();
        OutputCommand response;
        try {
            var json = mapper.readValue(req, InputCommand.class);
            switch(json.getCommand()) {
                case "register":
                    response = (new RegisterCommand()).execute(server, currentPlayer, json.getArgs());
                    break;
                case "login":
                    LoginCommand cmd = new LoginCommand();
                    response = cmd.execute(server, currentPlayer, json.getArgs());
                    this.currentPlayer = cmd.getPlayer();
                    break;
                case "friend":
                    response = (new FriendCommand()).execute(server, currentPlayer, json.getArgs());
                    break;
                case "self":
                    response = (new SelfCommand()).execute(server, currentPlayer, json.getArgs());
                    break;
                case "list":
                    response = (new ListCommand()).execute(server, currentPlayer, json.getArgs());
                    break;
                case "send":
                    response = (new SendCommand()).execute(server, currentPlayer, json.getArgs());
                    break;
                case "read":
                    response = (new ReadCommand()).execute(server, currentPlayer, json.getArgs());
                    break;
                case "stop":
                    response = (new StopCommand()).setSocket(socket).execute(server, currentPlayer, json.getArgs());
                    break;
                default:
                    response = (new DefaultCommand()).execute(server, currentPlayer, json.getArgs());
            }
        } catch(Exception e) {
            System.out.println(e.getMessage());
            response = new OutputCommand(e.getMessage());
        }
        return mapper.writeValueAsString(response);
    }

}
