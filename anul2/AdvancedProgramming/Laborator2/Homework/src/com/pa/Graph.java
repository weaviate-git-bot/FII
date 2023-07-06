package com.pa;

/**
 * @Class class that represens a graph data structure using a matrix
 */
public class Graph {
    private int vertex;
    private boolean adj[][];

    /**
     * The construction
     * @param vertex maximum number of vertexes
     */
    public Graph(int vertex) {
        this.vertex = vertex;
        this.adj = new boolean[vertex][vertex];
    }

    /**
     * Add a new edge in an undirected graph
     * @param v first vertex
     * @param w second vertex
     */
    public void addEdge(int v, int w){
        adj[v][w] = true;
        adj[w][v] = true;
    }

    /**
     * Get a row from the graph
     * @param v representing the vertex for witch you  want the adjency vector
     * @return adjency vector for v
     */
    public boolean[] getRow(int v) {
        return adj[v];
    }

    /**
     * Display the entire graph data structure.
     */
    public void print() {
        for(int height = 0; height < this.vertex; ++height) {
            for(int width = 0; width < this.vertex; ++width) {
                System.out.format("%d ", this.adj[height][width] ? 1 : 0);
            }
            System.out.println();
        }
    }
}
