package com.company;

import java.util.ArrayList;


public class Main {
    private int n, p, alphabetLen;
    private char[] alphabet;

    public static void main(String[] args) {
        Main app = new Main();
        long startTime = System.nanoTime();

        // parsing and validating all the arguments given as input
        app.parseArguments(args);

        String[] words = app.generate();
        //app.displayWords(words);

        boolean[][] neighborsMatrix = new boolean[words.length][words.length];
        ArrayList<ArrayList> neighbours = new ArrayList<ArrayList>();


        for (int idx = 0; idx < words.length; ++idx) {
            int currentNeighbors = 0;
            ArrayList<String> neighboursIdx = new ArrayList<String>();
            for (int possibleNeighbor = 0; possibleNeighbor < words.length; ++possibleNeighbor) {
                // we don't want to have the word to be neighbour to himself
                if (idx == possibleNeighbor) {
                    continue;
                }

                if (Main.compareWords(words[idx], words[possibleNeighbor]) == true) {
                    // building at the same time the boolean matrix and the array of words
                    neighborsMatrix[idx][currentNeighbors] = true;
                    neighboursIdx.add(words[possibleNeighbor]);
                }
            }
            neighbours.add(idx, neighboursIdx);
        }
        long endTime = System.nanoTime();
        System.out.format("The runtime of the application is: %d\n", endTime-startTime);
        if (app.n < 1000) {
            Main.displayNeighbours(neighbours, words);
        }



    }

    /**
     * Displaying the neighbours
     * @param neighbours the array of lists
     * @param words the generated words
     */
    private static void displayNeighbours(ArrayList<ArrayList> neighbours, String[] words) {
        for(int i = 0; i < words.length; ++i) {
            ArrayList<String> neighboursIdx = new ArrayList<String>();
            neighboursIdx = neighbours.get(i);
            System.out.format("Neighbours of '%s' are: \n", words[i]);
            for(int idx = 0; idx < neighboursIdx.size(); ++idx) {
                System.out.print(neighboursIdx.get(idx) + " ");
            }
            System.out.println();
        }
    }
    /**
     * Checking if two words have a common letter
     * This is a static function because it doesn't require any attributes from the class
     *
     * @param firstWord  the base word
     * @param secondWord the word to compare with
     * @return true if the two words have a common letter, false otherwise
     */
    private static boolean compareWords(String firstWord, String secondWord) {

        for (int i = 0; i < firstWord.length(); ++i) {
            for (int j = 0; j < secondWord.length(); ++j) {
                if (firstWord.charAt(i) == secondWord.charAt(j)) {
                    return true;
                }
            }
        }
        return false;
    }

    /**
     * Displaying on the screen the array of words
     *
     * @param words
     */
    private void displayWords(String[] words) {
        System.out.println("Displaying the array of words");
        System.out.println("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=");
        for (int i = 0; i < words.length; ++i) {
            System.out.println(words[i]);
        }
        System.out.println("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=");
    }

    /**
     * Generating an array of n words, each word having exactly p characters from the alphabet
     *
     * @return a list of words with the specified length and size
     */
    private String[] generate() {
        String[] words = new String[this.n];

        for (int i = 0; i < this.n; ++i) {
            StringBuilder sb = new StringBuilder();
            int len = this.p;
            while (len > 0) {
                int pos = (int) (Math.random() * (this.alphabetLen + 1)) - 1;
                if (pos < 0) {
                    continue;
                }
                sb.append(this.alphabet[pos]);
                len = len - 1;
            }
            words[i] = sb.toString();
        }

        return words;
    }

    /**
     * Validate and parse the required arguments given from the input line and set them inside class
     *
     * @param args The list of arguments given from the input line
     */
    private void parseArguments(String[] args) {
        try {
            if (args.length < 3) {
                throw new Exception("You should have at least 3 parameters!");
            }

            this.n = Integer.parseInt(args[0]);
            this.p = Integer.parseInt(args[1]);
            this.alphabetLen = args.length - 2;
            this.alphabet = new char[alphabetLen];

            for (int i = 0; i < alphabetLen; ++i) {
                this.alphabet[i] = args[i + 2].charAt(0);
            }
        } catch (Exception e) {
            System.err.format("Failed to parse the arguments. Errors is: '%s'", e.getMessage());
            System.exit(1);
        }
    }
}
