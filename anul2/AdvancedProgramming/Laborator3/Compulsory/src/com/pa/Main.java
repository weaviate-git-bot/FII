package com.pa;

import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) {
        Node v1 = new Computer("Computer A", "6B-E4-AC-BB-C9-E9", "v1", "172.0.0.32",1024);
        Node v2 = new Router("Router A", "D6-55-43-12-A5-B4", "v2", "238.432.23.2");
        Node v3 = new Switch("Switch A", "20-20-0E-D9-05-CE", "v3");
        Node v4 = new Switch("Switch B", "5C-00-99-15-6D-1D", "v4");
        Node v5 = new Router("Router B", "CC-39-31-C0-07-48", "v5", "124.32.423.01");
        Node v6 = new Computer("Computer B", "C5-AF-40-50-72-DE", "v6", "423.21.43.23", 2048);
        Network network = new Network();

        network.addNode(v1);
        network.addNode(v2);
        network.addNode(v3);
        network.addNode(v4);
        network.addNode(v5);
        network.addNode(v6);
//        System.out.println(network.toString());

        v1.setCost(v2, 10);
        v1.setCost(v3, 50);
        v2.setCost(v3, 20);
        v2.setCost(v4,20);
        v2.setCost(v5,20);
        v3.setCost(v4,10);
        v4.setCost(v5, 30);
        v4.setCost(v6, 10);
        v5.setCost(v6, 20);

        System.out.println("Entire network with costs:");
        Graph networkGraph = network.getNetworkMap();
        networkGraph.printWithCosts();
        System.out.println("---------------------");

        List<Node> identifiableNodes = new ArrayList<Node>();
        identifiableNodes = network.getIdentifiableNodes();
        System.out.println("Identifiable nodes are:");
        for(Node node: identifiableNodes) {
            System.out.println(node);
        }
        System.out.println("---------------------");

        Algorithm floydWarshall = new FloydWarshallAlgorithm(network);

        try {
//            Solution sol = floydWarshall.solve();
        } catch(Exception e) {
            System.err.println("Couldn't find a valid solution!");
        }
        Solution sol = floydWarshall.solve();
        System.out.println(sol.toString());

    }
}
