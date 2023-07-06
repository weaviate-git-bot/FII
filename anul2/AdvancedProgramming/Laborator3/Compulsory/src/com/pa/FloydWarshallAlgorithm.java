package com.pa;

import java.util.ArrayList;
import java.util.List;

/**
 * @Class  An extension of Algorithm class that solves the Network Routing Problem using Floyd-Warshall algorithm
 */
public class FloydWarshallAlgorithm extends Algorithm{
    private Graph graph;

    public FloydWarshallAlgorithm(Network network) {
        this.network = network;
        this.graph = network.getNetworkMap();
    }

    public Solution solve() {
      Solution sol = new Solution();
      System.out.println("Started to solve the problem");

      this.graph.FloydWarshall();

      List<Node> identifiableNodes = this.network.getIdentifiableNodes();

      for (int idx = 0; idx < identifiableNodes.size() - 1; ++idx) {
          for (int second = idx+1; second < identifiableNodes.size(); ++second) {
              Node n1 = identifiableNodes.get(idx);
              Node n2 = identifiableNodes.get(second);
              int cost = this.graph.getValueAt(idx, second);

              n1.setCost(n2, cost);
              n2.setCost(n1, cost);

              // adding to the solution
              sol.addSolution(n1);
              sol.addSolution(n2);
          }
      }

      return sol;
    };


}
