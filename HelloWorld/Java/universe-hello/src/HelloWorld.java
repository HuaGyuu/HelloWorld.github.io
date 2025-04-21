import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

/**
 * @author universe
 */
public class HelloWorld {

    public static void main(String[] args) {
        try {
            // Read the contents of the hello.txt file
            List<String> lines = Files.readAllLines(Paths.get("../banner/hello.txt"));
            // Combine the content into a single string
            String banner = String.join(System.lineSeparator(), lines);
            // Print the banner to the console
            System.out.println(banner);
        } catch (IOException e) {
            // Handle file reading exceptions
            System.err.println("Unable to read the file: " + e.getMessage());
        }
    }
}