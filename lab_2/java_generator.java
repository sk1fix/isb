import java.util.Random;

public class Main {
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