package com.pa;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public class Solution {
    List<Node> solution;

    public Solution() {
        this.solution = new ArrayList<Node>();
    }

    public void addSolution(Node n) {
        this.solution.add(n);
    }

    @Override
    public String toString() {
        Node n = this.solution.get(0);
        StringBuilder sb = new StringBuilder("Solution is: \n");
        for (Map.Entry<Node, Integer> entry : n.getCost().entrySet()) {
            if(entry.getKey() instanceof IIdentifiable) {
                sb.append(((IIdentifiable) n).getAddress());
                sb.append(" -> ");
                sb.append(((IIdentifiable) entry.getKey()).getAddress());
                sb.append(" : ");
                sb.append(entry.getValue());
                sb.append("\n");
            }
        }
        return sb.toString();
    }
}
