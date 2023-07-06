/**
 * @class modeling an intersection
 */
public class Intersection implements IIdentifiabble {
    private String name;

    public Intersection(String name) {
        this.name = name;
    }

    /**
     * Getting the name of the intersection
     * @return name
     */
    @Override
    public String getName() {
        return name;
    }

    /**
     * Setting the name of the intersection
     * @param name
     */
    public void setName(String name) {
        this.name = name;
    }

    /**
     * Checks if two intersections are equal
     * @param o
     * @return true if two classes have the same name, false otherwise
     */
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;

        Intersection that = (Intersection) o;

        return getName() != null ? getName().equals(that.getName()) : that.getName() == null;
    }

    /**
     * This function is helpful when we need to check in hashmap
     * @return hashCode of name, 0 otherwise
     */
    @Override
    public int hashCode() {
        return getName() != null ? getName().hashCode() : 0;
    }
}
