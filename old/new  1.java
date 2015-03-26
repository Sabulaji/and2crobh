public class BogoclientActivity extends Activity
{
  /* 服务器地址 */
  private final String SERVER_HOST_IP = "192.168.1.2";

  /* 服务器端口 */
  private final int SERVER_HOST_PORT = 9400;
  
  private Button btnConnect;
  private Button btnSend;
  private EditText editSend;
  private Socket socket;
  private PrintStream output;


  public void toastText(String message)
  {
    Toast.makeText(this, message, Toast.LENGTH_LONG).show();
  }

  public void handleException(Exception e, String prefix)
  {
    e.printStackTrace();
    toastText(prefix + e.toString());
  }

  /** Called when the activity is first created. */
  @Override
  public void onCreate(Bundle savedInstanceState)
  {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.main);

    initView();

    btnConnect.setOnClickListener(new Button.OnClickListener()
    {
      @Override
      public void onClick(View v)
      {
        initClientSocket();
      }
    });
    
    btnSend.setOnClickListener(new Button.OnClickListener()
    {
      @Override
      public void onClick(View v)
      {
        sendMessage(editSend.getText().toString());
      }
    });
  }
  
  public void initView()
  {
    btnConnect = (Button)findViewById(R.id.btnConnect);
    btnSend = (Button)findViewById(R.id.btnSend);
    editSend = (EditText)findViewById(R.id.sendMsg);

    btnSend.setEnabled(false);
    editSend.setEnabled(false);
  }

  public void closeSocket()
  {
    try
    {
      output.close();
      socket.close();
	}
    catch (IOException e)
    {
      handleException(e, "close exception: ");
	}
  }
  
  private void initClientSocket()
  {
    try
    {
      /* 连接服务器 */
      socket = new Socket(SERVER_HOST_IP, SERVER_HOST_PORT);

      /* 获取输出流 */
      output = new PrintStream(socket.getOutputStream(), true, "utf-8");
      
      btnConnect.setEnabled(false);
      editSend.setEnabled(true);
      btnSend.setEnabled(true);
    }
    catch (UnknownHostException e)
    {
      handleException(e, "unknown host exception: " + e.toString());
    }
    catch (IOException e)
    {
      handleException(e, "io exception: " + e.toString());
    }
  }
  
  private void sendMessage(String msg)
  {
    output.print(msg);
  }
}