import java.awt.*;
import java.io.*;
import java.net.URI;
import java.util.HashMap;
import java.util.Map;

import freemarker.template.Configuration;
import freemarker.template.Template;
import freemarker.template.Version;

/**
 * @Class ReportCommand
 * Creates (and opens) an HTML report representing the content of the catalog.
 */
public class ReportCommand implements ICommand {
    private String reportPath = "C:\\Users\\Public\CatalogReport.html";

    public ReportCommand setPath(String path) {
        this.reportPath = path;
        return this;
    }

    /**
     * Creates (and opens) an HTML report representing the content of the catalog.
     * See the template at resources/templates/catalog.ftl
     * @param o
     * @throws IOException
     */
    @Override
    public void execute(Object o) throws IOException {
        if (o == null) throw new NullPointerException();
        if (!(o instanceof Catalog)) throw new IllegalArgumentException("Commands should receive only Catalog objects");
        Configuration cfg = new Configuration(Configuration.VERSION_2_3_29);
        cfg.setClassForTemplateLoading(ReportCommand.class, "/");
        cfg.setDefaultEncoding("UTF-8");
        Template template = cfg.getTemplate("templates/catalog.ftl");
        Map<String, Object> templateData = new HashMap<>();

        templateData.put("items", ((Catalog) o).getItems());
        templateData.put("title", ((Catalog) o).getName());

        Writer file = new FileWriter(new File(this.reportPath));
        try{
            template.process(templateData, file);
        } catch (Exception e) {
            System.err.println(e.getMessage());
            System.exit(1);
        }
        file.flush();
        file.close();
        if (Desktop.isDesktopSupported() && Desktop.getDesktop().isSupported(Desktop.Action.BROWSE)) {
            try {
                File htmlFile = new File(this.reportPath);
                Desktop.getDesktop().browse(htmlFile.toURI());
            } catch (Exception e) {
                System.err.println(e.getMessage());
            }
        }

    }
}
