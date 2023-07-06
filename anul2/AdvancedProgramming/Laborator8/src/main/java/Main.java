import java.sql.Connection;

public class Main {
    public static void main(String[] args) {
        // importing the data from a real world source
//        ImportController.importFromFile("./concap.csv");
        try {
            System.out.println(CityDAO.distanceBetweenCities("Paris", "Bucharest"));
        } catch(Exception e) {
            System.err.println(e.getMessage());
        }


    }
}
