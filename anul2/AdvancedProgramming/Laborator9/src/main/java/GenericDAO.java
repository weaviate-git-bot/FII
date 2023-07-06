import com.mysql.cj.result.Field;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public abstract class GenericDAO {
    final protected static String tableName = "";
    final protected static List<String> fields = new ArrayList<>();

    protected abstract String getTableName();
    protected abstract List<String> getFields();
    protected abstract void setValue(String key, Object value);
    public void addValue(String key, Object value) {
        this.setValue(key, value);
    }
    public abstract Object getValue(String key);

    public boolean findBy(String key, String value) {
        Connection con = Database.getConnection();
        try (Statement stmt = con.createStatement();
             ResultSet rs = stmt.executeQuery(
                     "select * from "+ this.getTableName() +" where "+ key +"='" + value + "'")) {

            var metaData = rs.getMetaData();
            if(!rs.next())
                return false;

            for (int idx = 1; idx <= metaData.getColumnCount(); ++idx) {
                this.addValue(metaData.getColumnName(idx), rs.getObject(idx));
            }

            return true;
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return true;
    }

    public void create() {
        Connection con = Database.getConnection();
        StringBuilder sb =  new StringBuilder("insert  into `");
        sb.append(this.getTableName());
        sb.append("` (");

        boolean hasId = false;
        for(String row: this.getFields()) {
            if(row.equals("id")) {
                hasId = true;
                continue;
            }
            sb.append("`"+row+"`,");
        }
        sb.deleteCharAt(sb.length()-1);
        sb.append(") values (");

        int size = this.getFields().size();
        if(hasId) --size;

        for(int idx = 0; idx < size; ++idx) {
            sb.append("?,");
        }
        sb.deleteCharAt(sb.length()-1);
        sb.append(")");


        try (PreparedStatement pstmt = con.prepareStatement(sb.toString())) {
            int counter = 1;
            for(int idx = 1; idx <= size; ++idx) {
                String field = this.getFields().get(idx - 1);
                if(field.equals("id")) {
                    ++size;
                    continue;
                }
                pstmt.setObject(counter, this.getValue(field));
                ++counter;
            }
            pstmt.executeUpdate();
            System.out.println("added");
        }catch (Exception e) {
            e.printStackTrace();
        }
    }

}
