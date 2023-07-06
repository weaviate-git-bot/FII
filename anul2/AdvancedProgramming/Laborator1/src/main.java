class HelloWorld {
    public static void main(String[] args) {
        // 1. Display on the screen the message "Hello World!". Run the application. If it works, go to step 2 :)
        System.out.println("Hello, World!");

        //2. Define an array of strings languages, containing {"C", "C++", "C#", "Python", "Go", "Rust", "JavaScript", "PHP", "Swift", "Java"}
        String[] languages =  {"C", "C++", "C#", "Python", "Go", "Rust", "JavaScript", "PHP", "Swift", "Java"};

        // 3. Generate a random integer n: int n = (int) (Math.random() * 1_000_000);
        int n = (int)(Math.random() * 1000000);
        System.out.format("Number before formatting is: %d\n", n);
        // 4. Compute the result obtained after performing the following calculations:
        n = n * 3;
        n += 0b10101;
        n += 0xFF;
        n = n * 6;
        System.out.format("Number after formatting is: %d\n", n);
        // 5. Compute the sum of the digits in the result obtained in the previous step. This is the new result. While the new result has more than one digit, continue to sum the digits of the result.
//        int result = n;
//        do {
//            result = 0;
//            while(n != 0) {
//                result += n % 10;
//                n /= 10;
//            }
//            n = result;
//        } while(result > 9);
        // a more efficient approach
        int result = -1;
        if (n % 9 == 0 ) {
            result = 9;
        } else {
            result %= 9;
        }
        System.out.format("Sum of the digits is: %d\n", result);
        // 6. Display on the screen the message: "Willy-nilly, this semester I will learn " + languages[result].
        System.out.format("Willy-nilly, this semester I will learn " + languages[result]);
    }
}