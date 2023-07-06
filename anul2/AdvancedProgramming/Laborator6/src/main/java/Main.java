public class Main {
    public static final String GAME_PATH = Main.class.getProtectionDomain().getCodeSource().getLocation().getPath();

    public static void main(String[] args) {
        MainFrame game = new MainFrame();
        game.setVisible(true);
    }
}
