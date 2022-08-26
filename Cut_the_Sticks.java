import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {

    /*
     * Complete the 'cutTheSticks' function below.
     *
     * The function is expected to return an INTEGER_ARRAY.
     * The function accepts INTEGER_ARRAY arr as parameter.
     */

    public static List<Integer> cutTheSticks(List<Integer> S, int n) {
    // Write your code here
        LinkedList <Integer> Length = new LinkedList<>();
        LinkedList <Integer> temp = new LinkedList<>();
        Length.add(n);
    
        Collections.sort(S);
        while (S.size() > 1){
            Collections.sort(S);
            int t = S.get(0);
            temp.clear();
            for(int j = 0; j< S.size(); j++){
                if(S.get(j) == t){
                    continue;
                }
                temp.add(S.get(j) - t);
            }
           S.clear();
            for(int k = 0; k<temp.size(); k++){
                S.add(temp.get(k));
            }
            if(S.size() == 0){
                break;
            }
            Length.add(S.size());
        }
        return(Length);

    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int n = Integer.parseInt(bufferedReader.readLine().trim());

        List<Integer> S= Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
            .map(Integer::parseInt)
            .collect(toList());

        List<Integer> result = Result.cutTheSticks(S, n);

        bufferedWriter.write(
            result.stream()
                .map(Object::toString)
                .collect(joining("\n"))
            + "\n"
        );

        bufferedReader.close();
        bufferedWriter.close();
    }
}
