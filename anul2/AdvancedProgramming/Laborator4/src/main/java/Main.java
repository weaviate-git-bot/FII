import com.github.javafaker.Faker;

import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.Stream;

public class Main {
    public static void main(String args[]) {
        Faker faker = new Faker();

        // generate the intersections
        var intersections = IntStream.rangeClosed(0,8)
                                            .mapToObj(i -> new Intersection(faker.name().fullName()))
                                            .toArray(Intersection[]::new);

//        var streets = IntStream.rangeClosed(0, intersections.length-2)
//                                    .mapToObj(i -> new Street(faker.name().fullName(), i % 4, intersections[i], intersections[i+1]))
//                                    .sorted()
//                                    .collect(Collectors.toCollection(LinkedList::new));

        /*
            a b c d e f g h i
            0 1 2 3 4 5 6 7 8
         */

        // streets according to the graph
        Street streetsList[] = new Street[] {
                new Street(faker.name().fullName(), 2, intersections[0], intersections[1]), // a -> b
                new Street(faker.name().fullName(), 2, intersections[0], intersections[2]), // a -> c
                new Street(faker.name().fullName(), 2, intersections[0], intersections[3]), // a -> d
                new Street(faker.name().fullName(), 1, intersections[1], intersections[2]), // b -> c
                new Street(faker.name().fullName(), 3, intersections[1], intersections[8]), // b -> i
                new Street(faker.name().fullName(), 2, intersections[2], intersections[3]), // c -> d
                new Street(faker.name().fullName(), 2, intersections[2], intersections[8]), // c -> i
                new Street(faker.name().fullName(), 2, intersections[2], intersections[6]), // c -> g
                new Street(faker.name().fullName(), 3, intersections[3], intersections[4]), // d -> e
                new Street(faker.name().fullName(), 1, intersections[4], intersections[8]), // e -> i
                new Street(faker.name().fullName(), 1, intersections[4], intersections[5]), // e -> f
                new Street(faker.name().fullName(), 2, intersections[4], intersections[7]), // e -> h
                new Street(faker.name().fullName(), 1, intersections[5], intersections[6]), // f -> g
                new Street(faker.name().fullName(), 1, intersections[5], intersections[7]), // f -> h
                new Street(faker.name().fullName(), 3, intersections[7], intersections[8]), // h -> i
        };

        // transformation of streets and intersections
        var streets = Arrays.stream(streetsList).sorted().collect(Collectors.toCollection(LinkedList::new));
        Set<Intersection> intersectionSet = new HashSet<Intersection>(Arrays.stream(intersections).toList());

        // checking if the intersections were unique
        if(intersectionSet.size() < intersections.length) {
            System.out.println("Intersections have duplicates");
            System.exit(1);
        }

        for(Street stre : streets) {
            System.out.format("%s -> %d\n",stre.getName(), stre.getLength());
        }

        City iasi = new City(streets, intersectionSet);
        iasi.displayStreetsWithAtLeast3IntersectionsBiggerThan(3);
        iasi.minimumDataCableLength();
    }
}
