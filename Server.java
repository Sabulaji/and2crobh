import java.io.*;
import java.net.*;

public class Server{
	public static void main(String args[]){
		ServerSocket server = null;
		Socket you = null;
		DataOutputStream out = null;
		DataInputStream in = null;
		
		try{
			server = new ServerSocket(4331);
		}
		catch(IOException e1){
			System.out.println("ERRO:" + e1);
		}
		try{
			you = server.accept();
			in = new DataInputStream(you.getInputStream());
			out = new DataOutputStream(you.getOutputStream());
			while(true){
				int m = 0;
				m = in.readInt();
				out.writeUTF("your output is:" + (char)m);
				System.out.println("Server get:" + m);
				Thread.sleep(500);
			}
		}
		catch(IOException e){
			System.out.println("" + e);
		}
		catch(InterruptedException e){}
	}
}