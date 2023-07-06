package server;

import database.*;

import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import java.net.SocketException;
import java.util.ArrayList;
import java.util.List;

public class SimpleServer {
    public static final int PORT = 8100;
    public static final int CLIENT_CONNECTION_TIMEOUT = 5 * 60_000; // 5 minute timeout
    public static boolean running = false;
    private static boolean shutdownProcedureInit = false;
    public static List<Thread> clientList = new ArrayList<>();
    private static ServerSocket serverSocket = null;
    private static IDatabase db = new MockDatabase();

    public SimpleServer() throws IOException {
        running = true;
        serverSocket = new ServerSocket(PORT);

        while (running) {
            try {
                Socket s = this.gotConnection();
                if(s != null) {
                    acceptClient(s);
                }
            } catch(IOException e) {
                if(running == false) handleShutdown();
            }
        }

        System.out.println("Trying to stop the server from main thread");
        this.handleShutdown();
    }

    private Socket gotConnection() throws IOException{
        try {
            serverSocket.setSoTimeout(1000);
            Socket socket = serverSocket.accept();
            return socket;
        } catch(SocketException e) {
            System.out.println("Timeout");
            if(running == false) {
                handleShutdown();
            }
        }
        return null;
    }

    private void handleShutdown() throws IOException{
        if(isShutdownProcedureInit()){
            return;
        }
        setRunning(false);
        setShutdownProcedureInit(true);


        System.out.println("Starting shutdown procedure");
        for(var client : clientList) {
            try {
                client.join(1_000);
            } catch (Exception e) {

            }
        }
        System.out.println("Stopping now");

        serverSocket.close();
    }

    private void acceptClient(Socket socket) {
        // Execute the client's request in a new thread
        var t = new Thread(new ClientThread(socket, this));
        clientList.add(t);
        t.start();
    }

    public static boolean isShutdownProcedureInit() {
        return shutdownProcedureInit;
    }

    public static void setShutdownProcedureInit(boolean shutdownProcedureInit) {
        SimpleServer.shutdownProcedureInit = shutdownProcedureInit;
    }

    public static boolean isRunning() {
        return SimpleServer.running;
    }

    public static void setRunning(boolean running) {
        SimpleServer.running = running;
    }

    public static IDatabase getDb() {
        return SimpleServer.db;
    }
}
