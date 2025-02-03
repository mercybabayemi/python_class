public class PrimeNumber{
	public static void main(String[] args){
	
	System.out.print(get_count(7));
	}

	public static int get_count(int integer){
		int count = 0
		for(int i = 1; i < integer; i++){
			count++;
		}
		return count;
	}
}
