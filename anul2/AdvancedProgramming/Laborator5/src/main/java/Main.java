import java.io.IOException;
import java.net.URISyntaxException;

public class Main {
    public static void main(String[] args) {
        Main app = new Main();
        try{
            app.testCreateSave();
            app.testLoadView();
//            app.testViewCommand();
            app.testReportCommand();
        }catch (Exception e) {
            System.err.println("Error found."+e.getMessage());
        }

    }

    private Catalog mockCatalog() throws IOException {
        Catalog catalog = new Catalog("Bogdan's Biography");
        AddCommand addItem = new AddCommand();
        var book = new Book("The Art of Computer Programming", "d:/books/programming/tacp.ps", 1967, "Donald E. Knuth", "book");
        var article = new Article("The Java Language Specification", "https://docs.oracle.com/javase/specs/jls/se17/html/index.html", 2021,"James Gosling & others");

        addItem.setItem(book).execute(catalog);
        addItem.setItem(article).execute(catalog);
        return catalog;
    }

    private void testReportCommand() throws IOException {
        Catalog catalog = this.mockCatalog();
        ReportCommand cmd = new ReportCommand();
        cmd.setPath("D:\\Work\\Facultate\\ProgramareAvansata\\Laborator5\\Report.html")
                .execute(catalog);
    }

    private void testViewCommand() throws IOException{
        var book = new Book("The Art of Computer Programming", "https://pground.io", 1967, "Donald E. Knuth", "book");

        ViewCommand view = new ViewCommand();
        view.execute(book);
    }

    private void testCreateSave() throws IOException {
        Catalog catalog = this.mockCatalog();

        SaveCommand save = new SaveCommand();
        save.setPath("D:\\Work\\Facultate\\ProgramareAvansata\\Laborator5\\test.json")
                .execute(catalog);
    }

    private void testLoadView() throws IOException, InvalidCatalogException {
        Catalog catalog = new Catalog();
        LoadCommand cmd = new LoadCommand();
        cmd.setPath("D:\\Work\\Facultate\\ProgramareAvansata\\Laborator5\\test.json").execute(catalog);
        ListCommand ls = new ListCommand();
        ls.execute(catalog);
    }

}
