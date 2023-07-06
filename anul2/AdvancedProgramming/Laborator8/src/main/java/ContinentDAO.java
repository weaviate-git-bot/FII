import java.sql.*;
import java.util.*;

public class ContinentDAO extends GenericDAO {
    final private static String tableName = "continents";
    final private static List<String> fields = new ArrayList<>(Arrays.asList(
            "id", "name"
    ));
    final private Map<String, Object> values = new HashMap<>();

    public ContinentDAO() {
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
