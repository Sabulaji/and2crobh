import java.io.*;
import java.net.*;

public class Client{
	public static void main(String arg[]){
		String s = null;
		Socket mysocket;
		DataInputStream in = null;
		DataOutputStream out = null;
		int i = 1;
		try{
			mysocket = new Socket("localhost",4331);
			in = new DataInputStream(mysocket.getInputStream());
			out = new DataOutputStream(mysocket.getOutputStream());
			out.writeInt(i);
			while(true){
				i = (i+1)%128;
				s = in.readUTF();
				out.writeInt(i);
				System.out.println("Client get:" + s);
				Thread.sleep(500);
			}
		}
		catch(IOException e){
			System.out.println("no link.");
		}
		catch(InterruptedException e){}
	}
}