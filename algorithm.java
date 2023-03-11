// Online Java Compiler
// Use this editor to write, compile and run your Java code online
interface listTask{
    public void fizbuz(int lenght);
    public void palindrome(String data);
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
}
class Main {
    public static void main(String[] args) {
        Task myTask = new Task();
        myTask.fizbuz(20);
        myTask.palindrome("malam");
    }
}