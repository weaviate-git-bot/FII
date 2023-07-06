import static java.lang.Thread.sleep;

/**
 * @class Timekeeper
 */
public class Timekeeper implements Runnable {
    private final int timeToSleep = 1337; // time in seconds

    @Override
    public void run() {
        try {
            sleep(timeToSleep * 1000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
