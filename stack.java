import java.io.*;
import java.util.*;

/**
Implements a stack as a linked list.
**/
class stack{
	private Node top;
	
	public stack(Node n){
		this.top = n;
	}
	
	public stack(){
		
	}
	
	public static void main(String[] args){
		stack s = new stack();
		ArrayList<String[]> valuesList = s.getData(args[0]);
		for(String[] values : valuesList){
			s.fill(values);
			String[] everyOtherValue = s.everyOtherValue(values.length);
			s.printValues(everyOtherValue);
		}
	}

	String[] everyOtherValue(int cardinality){
		int capacity = cardinality % 2 != 0 ? (cardinality+1)/2 : cardinality/2;
		String[] everyOtherValue = new String[capacity];
		int arrayIndex = 0;
		for(int i = 0; i < cardinality; i++){
			String value = pop().value();
			if(i % 2 == 0)  everyOtherValue[arrayIndex++] = value;
		}
		return everyOtherValue;
	}
	
	void printValues(String[] values){
		for(int i = 0; i < values.length; i++){
			System.out.print(values[i]);
			if(i < values.length-1) System.out.print(" ");
		}
		System.out.print("\n");
	}
	
	ArrayList<String[]> getData(String path){
		ArrayList<String[]> values = new ArrayList<String[]>();
		try{
			Scanner scan = new Scanner(new File(path));
			while(scan.hasNextLine()){
				String s = scan.nextLine();
				if (s.length() > 0) values.add(s.split(" "));
			}
		} catch(Exception e) {
			
		}
		return values;
	}
	
	void fill(String[] values){
		for(String value : values){
			push(value);
		}
	}
	
	void push(String value){
		Node n = new Node(value);
		if(this.top == null){
			this.top = n;
		} else {
			this.top.setNext(n);
			n.setPrev(this.top);
			this.top = n;
		}
	}
	
	Node pop() {
		if(this.top == null){
			return this.top;
		} else {
			Node top = this.top;
			Node prev = top.getPrev();
			this.top = prev;
			top.detach();
			if(prev != null){
				prev.detachNext();
			}
			return top;
		}
	}
	
	Node peek() {
		return this.top;
	}
	
	private class Node {
		private String value;
		private Node next;
		private Node prev;
		
		Node(String value){
			this.value = value;
		}
		String value(){
			return this.value;
		}
		void setNext(Node n){
			this.next = n;
		}
		void setPrev(Node n){
			this.prev = n;
		}
		Node getPrev(){
			return this.prev;
		}
		Node getNext(){
			return this.next;
		}
		void detach(){
			this.next = null;
			this.prev = null;
		}
		void detachNext(){
			this.next = null;
		}
	}	
}