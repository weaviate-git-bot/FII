import com.opencsv.CSVReader;

import java.io.FileReader;
import java.sql.Connection;

public class ImportController {
    public static void importFromFile(String path) {
        Connection conn = Database.getConnection();

        try (CSVReader reader = new CSVReader(new FileReader(path))) {
            String[] lineInArray;
            boolean firstLine = false;
            while ((lineInArray = reader.readNext()) != null) {
                if(firstLine == false) {
                    firstLine = !firstLine;
                    continue;
                }
                return;
//                ContinentDAO continent = new ContinentDAO();
//                CountryDAO country = new CountryDAO();
//                CityDAO city = new CityDAO();

//                if(!continent.findBy("name", lineInArray[5])){
//                    System.out.println("Continent doesn't exist: "+ lineInArray[5]);
//                    continent.addValue("name", lineInArray[5]);
//                    continent.create();
//                    conn.commit();
//                    continent.findBy("name", lineInArray[5]);
//                }

//                if(!country.findBy("name", lineInArray[0])) {
//                    System.out.println("Country doesn't exist: "+ lineInArray[0]);
//                    country.addValue("name", lineInArray[0]);
//                    country.addValue("code", lineInArray[4]);
////                    country.addValue("continent", continent.getValue("id"));
//                    country.create();
//                    conn.commit();
//                    country.findBy("name", lineInArray[0]);
//                }
//
//                if(!city.findBy("name", lineInArray[1])) {
//                    System.out.println("City doesn't exist: "+ lineInArray[1]);
//                    city.addValue("name", lineInArray[1]);
//                    city.addValue("capital", true);
//                    city.addValue("country", country.getValue("id"));
//                    city.addValue("latitude", Double.parseDouble(lineInArray[2]));
//                    city.addValue("longitude", Double.parseDouble(lineInArray[3]));
//                    city.create();
//                    conn.commit();
//                }


            }
        } catch(Exception e) {
            System.err.println(e.getMessage());
        }

    }
}
