/**
 * @class modeling a Street
 */
public class Street implements IIdentifiabble, Comparable<Street> {
    private String name;
    private int length;
    private Intersection leftIntersection, rightIntersection;

    public Street(String name, int length, Intersection left, Intersection right) {
        this.name = name;
        this.length = length;
        this.leftIntersection = left;
        this.rightIntersection = right;
    }

    /**
     * Getting the intersection from the left of the street
     * @return leftIntersection
     */
    public Intersection getLeftIntersection() {
        return leftIntersection;
    }

    /**
     * Setting the intersection from the left of the street
     * @param leftIntersection
     */
    public void setLeftIntersection(Intersection leftIntersection) {
        this.leftIntersection = leftIntersection;
    }

    /**
     * Getting the intersection from the right of the street
     * @return rightIntersection
     */
    public Intersection getRightIntersection() {
        return rightIntersection;
    }

    /**
     * Setting the intersection from the right of the street
     * @param rightIntersection
     */
    public void setRightIntersection(Intersection rightIntersection) {
        this.rightIntersection = rightIntersection;
    }

    /**
     * Getting the name of the street
     *
     * @return name
     */
    @Override
    public String getName() {
        return name;
    }

    /**
     * Setting the name of the street
     *
     * @param name
     */
    public void setName(String name) {
        this.name = name;
    }

    /**
     * Getting the length of the street
     *
     * @return
     */
    public int getLength() {
        return length;
    }

    /**
     * Setting the length of the street
     *
     * @param length
     */
    public void setLength(int length) {
        this.length = length;
    }

    /**
     * Comparing two streets by length
     * @param other the street that we want to compare with
     * @return 0 if they have the same name, positive number if the current node is bigger, negative number if o is bigger
     */
    @Override
    public int compareTo(Street o) {
        return (this.length - o.length);
    }

    @Override
    public String toString() {
        return "Street{" +
                "name='" + name + '\'' +
                ", length=" + length +
                ", leftIntersection=" + leftIntersection +
                ", rightIntersection=" + rightIntersection +
                '}';
    }
}


