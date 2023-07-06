import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.Persistence;
import java.sql.Connection;

public class Main {
    public static void main(String[] args) {
        // importing the data from a real world source
        EntityManagerFactory emf =
                Persistence.createEntityManagerFactory("zaPU");
        EntityManager em = emf.createEntityManager();

        em.getTransaction().begin();

        Continent continent = new Continent("ZaEurope");
        em.persist(continent);


        em.close();
        emf.close();

//        ImportController.importFromFile("./concap.csv");
//        try {
////            System.out.println(CityDAO.distanceBetweenCities("Hargeisa", "Vienna"));
//        } catch(Exception e) {
//            System.err.println(e.getMessage());
//        }


    }
}
