import java.util.Random;

public class Main {
    /**
     * The main entry point of the program. Generates and prints a 128-bit binary sequence.
     *
     * @param args command line arguments.
     */
    public static void main(String[] args) {
        Random rand = new Random();
                int size = 128;
        int[] binarySequence = new int[size];
        for (int i = 0; i < size; ++i) {
            binarySequence[i] = rand.nextInt(2); 
            System.out.print(binarySequence[i]); 
        }
        System.out.println(); 
    }
}