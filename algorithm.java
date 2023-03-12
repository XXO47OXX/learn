// Online Java Compiler
// Use this editor to write, compile and run your Java code online
import java.util.*;
import java.util.stream.Collectors;
interface listTask{
    public void fizbuz(int lenght);
    public void palindrome(String data);
    public void learnIterator();
    public void learnForEach();
    public void addList();
    public void getOddUsingLambda();
}
class Task implements listTask{
    public void fizbuz(int lenght){
        for (int i=1; i <= lenght; i++){
            if (i%15 == 0){
                System.out.println("fizbuz");
            }
            else if (i%3 == 0){
                System.out.println("fiz");
            }
            else if (i%5 == 0){
                System.out.println("buz");
            }
            else{
                System.out.println(i);
            }
        }
    }
    public void palindrome(String data){
    String reverseStr = "";
    
    int dataLength = data.length();

    for (int i = (dataLength - 1); i >=0; --i) {
      reverseStr = reverseStr + data.charAt(i);
    }

    if (data.toLowerCase().equals(reverseStr.toLowerCase())) {
      System.out.println(data + " is a Palindrome String.");
    }
    else {
      System.out.println(data + " is not a Palindrome String.");
    }
  }
    public void learnIterator(){
    int x = 10;
        String y = x > 5 ? "good":"not good";
        System.out.println(y);
  }
    public void learnForEach(){
    List<Integer> theNumbers = Arrays.asList(1, 2, 3, 4, 5);
        theNumbers.forEach((theNumber) -> System.out.println(theNumber));
  }
    public void addList(){
    String[] array = {"guge", "Android","Yongfa"};
    List<String> list = new ArrayList<>(Arrays.asList(array));
    list.add("lushu");
    array = list.toArray(new String[0]);
        System.out.println(Arrays.toString(array));
  }
    public void getOddUsingLambda(){
        ArrayList<Integer> listNumbers = new ArrayList<>();
        for (int i = 0; i <= 20; i++) {
            listNumbers.add(i);
        }
        // System.out.println(listNumbers);
        List<Integer> getOdd = listNumbers.stream().filter(n -> n % 2 == 1).collect(Collectors.toList());
        System.out.println(getOdd);
  }
}
class Main {
    public static void main(String[] args) {
        Task myTask = new Task();
        myTask.fizbuz(20);
        myTask.palindrome("malam");
        myTask.learnIterator();
        myTask.learnForEach();
        myTask.addList();
        myTask.getOddUsingLambda();
    }
}