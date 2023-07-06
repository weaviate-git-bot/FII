import java.util.*;

public class CityDAO extends GenericDAO {
    final private static String tableName = "city";
    final private static List<String> fields = new ArrayList<>(Arrays.asList(
            "id", "country", "name", "capital", "latitude", "longitude"
    ));
    final private Map<String, Object> values = new HashMap<>();

    public CityDAO() {
        super();
    }

    public Object getValue(String key) {
        return this.values.get(key);
    }

    public static double distanceBetweenCities(String firstCityName, String secondCityName) throws Exception{
        CityDAO c1 = new CityDAO();
        CityDAO c2 = new CityDAO();
        if(!c1.findBy("name", firstCityName) || !c2.findBy("name", secondCityName)){
            throw new Exception("Invalid city name!");
        }

        double c1Lat = (double) c1.getValue("latitude");
        double c1Long = (double) c1.getValue("longitude");

        double c2Lat = (double) c2.getValue("latitude");
        double c2Long = (double) c2.getValue("longitude");

        return CityDAO.calculateDistance(c1Lat, c1Long, c2Lat, c2Long);
    }

    private static double calculateDistance(double  lat1, double long1, double lat2, double long2) {
        long1 = Math.toRadians(long1);
        long2 = Math.toRadians(long2);
        lat1 = Math.toRadians(lat1);
        lat2 = Math.toRadians(lat2);

        // Haversine formula
        double dLon = long2 - long1;
        double dLat = lat2 - lat1;
        double a = Math.pow(Math.sin(dLat / 2), 2)
                + Math.cos(lat1) * Math.cos(lat2)
                * Math.pow(Math.sin(dLon / 2),2);
        double c = 2 * Math.asin(Math.sqrt(a));

        // Radius of earth in kilometers.
        double r = 6371;

        return(c * r);
    }

    protected void setValue(String key, Object value) {
        this.values.put(key, value);
    }

    protected String getTableName() {
        return this.tableName;
    }

    protected List<String> getFields() {
        return this.fields;
    }


}
