import java.sql.*;
import java.util.*;

public class CountryDAO extends  GenericDAO {
    final private static String tableName = "countries";
    final private static List<String> fields = new ArrayList<>(Arrays.asList(
            "id","name", "code", "continent"
    ));
    final private Map<String, Object> values = new HashMap<>();


    public CountryDAO() {
        super();
    }

    public Object getValue(String key) {
        return this.values.get(key);
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
