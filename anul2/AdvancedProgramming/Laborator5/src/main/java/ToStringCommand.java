/**
 * @class ToStringCommand
 * Prints a textual representation of the catalog
 */
public class ToStringCommand implements ICommand{
    /**
     * Outputs a textual representation of the catalog
     * @param o
     */
    @Override
    public void execute(Object o) {
        if(o == null) throw new NullPointerException();
        if(!(o instanceof Catalog)) throw new IllegalArgumentException("Commands should receive only Catalog objects");

        System.out.println((Catalog) o);
    }
}
