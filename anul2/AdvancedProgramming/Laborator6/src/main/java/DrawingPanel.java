import javax.imageio.ImageIO;
import javax.swing.*;
import java.awt.*;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.util.List;
import java.util.Map;

/**
 * @class DrawingPanel
 * A class that's responsible with drawing the actual game
 */
public class DrawingPanel extends JPanel {
    private final MainFrame frame;
    int rows, cols;
    int canvasWidth = 400, canvasHeight = 400;
    int boardWidth, boardHeight;
    int cellWidth, cellHeight;
    int padX, padY;
    int stoneSize = 20;
    BufferedImage image;
    Graphics2D offscreen;

    /**
     * Constructor of the class that renders the first image
     * @param frame
     */
    public DrawingPanel(MainFrame frame) {
        this.frame = frame;
        createOffscreenImage();
        init(frame.configPanel.getRows(), frame.configPanel.getCols());
    }

    /**
     * When some events occur we should redraw the game board, setting again some values  and doing some calculations
     */
    public void redraw() {
        this.canvasHeight = this.frame.getHeight() - 100;
        this.canvasWidth = this.frame.getWidth();
        init(frame.configPanel.getRows(), frame.configPanel.getCols());
        createOffscreenImage();
    }

    /**
     * Calculating the values used later for offsets and drawing
     * @param rows
     * @param cols
     */
    final void init(int rows, int cols) {
        this.cols = cols;
        this.rows = rows;
        this.padX = this.stoneSize + 10;
        this.padY = this.stoneSize + 10;
        this.cellWidth = (canvasWidth - 2 * padX) / (cols - 1);
        this.cellHeight = (canvasHeight - 2 * padY) / (rows -1);
        this.boardWidth = (cols - 1) * cellWidth;
        this.boardHeight = (rows - 1) * cellHeight;
        this.addMouseListener(new MouseAdapter() {
            @Override
            public void mousePressed(MouseEvent e) {
        if(frame.configPanel.game.validate(e.getX(), e.getY()) == true) {
//                    canvas.drawStone(e.getX(), e.getY());
                    System.out.format("Mouse: %d, %d\n",e.getX(), e.getY());

                }
                repaint();
            }
        });
        setPreferredSize(new Dimension(canvasWidth, canvasHeight));
    }

    /**
     * A retained mode drawer of the board
     */
    private void createOffscreenImage() {
        image = new BufferedImage(canvasWidth, canvasHeight, BufferedImage.TYPE_INT_ARGB);
        offscreen =  image.createGraphics();
        offscreen.setColor(Color.WHITE);
        offscreen.fillRect(0,0,canvasWidth, canvasHeight);
        paintGrid(offscreen);
        paintSticks(offscreen);
        paintStones(offscreen);
    }

    /**
     * Painting the actual game on the screen
     * @param graphics
     */
    @Override
    protected void paintComponent(Graphics graphics) {
        this.redraw();
        graphics.drawImage(image, 0, 0, this);
    }

    /**
     * Painting the stones
     * @param g
     */
    private void paintStones(Graphics2D g) {
        g.setColor(Color.BLUE);
        g.fillOval(stoneSize * 3, (stoneSize - 1) * 3, stoneSize, stoneSize);
    }

    /**
     * Drawing the lines representing the sticks
     * @param g
     */
    private void paintSticks(Graphics2D g) {
        if (rows <= 0) {
            return;
        }

        Map<Integer, List<Integer>> sticks = this.frame.configPanel.getGame().getSticksMap().getAdjacency();
        Stroke stroke = new BasicStroke(4f);
        g.setColor(Color.BLACK);
        g.setStroke(stroke);

        System.out.println("Drawing sticks now!");
        for(Integer vertex : sticks.keySet()) {
            for(Integer neighbour : sticks.get(vertex)) {

                int column = vertex % this.rows;
                int line = vertex / this.rows;

                int x1 = padX + (column) * cellWidth;
                int y1 = padY + (line) * cellHeight;


                column = neighbour % this.rows;
                  line = neighbour / this.rows;
                int x2 = padX + (column) * cellWidth;
                int y2 = padY + (line) * cellHeight;


                if(x1 >= canvasHeight - padX || x2 >= canvasHeight - padX || y1 >= canvasWidth - padY || y2 >= canvasWidth - padY)
                    continue;
//                System.out.println("--------------------------------------------\n");
//                System.out.format("Vertex: %d at coords: (%d, %d)\n", vertex,x1,y1);
//                System.out.format("Vertex: %d at coords: (%d, %d)\n", neighbour,x2,y2);
//                System.out.println("--------------------------------------------\n");
                g.drawLine(x1, y1, x2, y2);
            }
        }
    }

    /**
     * Drawing the grid
     * @param g
     */
    private void paintGrid(Graphics2D g) {
        g.setColor(Color.DARK_GRAY);
        //horizontal lines
        System.out.format("Row: %d, Col: %d\n", this.rows, this.cols);
        for (int row = 0; row < this.rows; row++) {
            int x1 = padX;
            int y1 = padY + row * cellHeight;
            int x2 = padX + boardWidth;
            int y2 = y1;
            g.drawLine(x1, y1, x2, y2);
        }
        for (int col = 0; col < this.cols; col++) {
            int x1 = padX + col * cellWidth;
            int y1 = padY;
            int x2 = x1;
            int y2 = padY + boardHeight;
            g.drawLine(x1, y1, x2, y2);
        }

        //intersections
        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                int x = padX + col * cellWidth;
                int y = padY + row * cellHeight;
                g.setColor(Color.LIGHT_GRAY);
                g.drawOval(x - stoneSize / 2, y - stoneSize / 2, stoneSize, stoneSize);
            }
        }
    }


    /**
     * Saving the game in a screenshot mode
     */
    public void saveBoard() {
        try {
            File outputFile = new File(Main.GAME_PATH + "/board.png");
            ImageIO.write(image, "png", outputFile);
            System.out.println("Board saved");
        }catch (IOException e) {
            System.err.println(e.getMessage());
        }
    }
}
