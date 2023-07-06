package com.pa;

/**
 * @Class class that represens a graph data structure using a matrix
 */
public class Graph {
    private int vertex;
    private int adj[][];
    private int INF = 99999;

    /**
     * The construction
     * @param vertex maximum number of vertexes
     */
    public Graph(int vertex) {
        this.vertex = vertex;
        this.adj = new int[vertex][vertex];

        // initialize the matrix
        for (int height = 0; height < vertex; ++height) {
            for (int width = 0; width < vertex; ++width) {
                this.adj[height][width] = INF;
            }
        }
    }

    /**
     * Add a new edge in an undirected graph
     * @param v first vertex
     * @param w second vertex
     */
    public void addEdge(int v, int w, int cost){
        adj[v][w] = cost;
        adj[w][v] = cost;
    }

    /**
     * Get the value from line v column w
     * @param v the line
     * @param w the column
     * @return adj[v][w]
     */
    public int getValueAt(int v, int w) {
        return this.adj[v][w];
    }

    /**
     * Run Floyd Warshall algorithm on the graph
     */
    public void FloydWarshall() {
        for(int k = 0; k < this.vertex; ++k) {
            for(int i = 0; i < this.vertex; ++i) {
                for(int j = 0; j < this.vertex; ++j) {
                    if(this.adj[i][k] + this.adj[k][j] < this.adj[i][j]) {
                        this.adj[i][j] = this.adj[i][k] + this.adj[k][j];
                    }
                }
            }
        }
    }

    /**
     * Display the entire graph data structure.
     */
    public void print() {
        for(int height = 0; height < this.vertex; ++height) {
            for(int width = 0; width < this.vertex; ++width) {
                System.out.format("%d ", this.adj[height][width]);
            }
            System.out.println();
        }
    }

    public void printWithCosts() {
        for(int height = 0; height < this.vertex; ++height) {
            for(int width = 0; width < this.vertex; ++width) {
                if(this.adj[height][width] != INF) {
                    System.out.format("%d ---> %d : %d\n", height + 1, width + 1, this.adj[height][width]);
                }
            }
        }
    }
}
