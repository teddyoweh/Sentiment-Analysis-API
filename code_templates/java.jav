
import java.net.*;
import java.io.*;
import org.json.*;

public class GetRequest {

    public static void main(String[] args) throws Exception {
        URL url = new URL("https://sentiment-analytics-api.herokuapp.com/?text=$word"+);
        HttpURLConnection con = (HttpURLConnection) url.openConnection();
        con.setRequestMethod("GET");

        int status = con.getResponseCode();

        BufferedReader in = new BufferedReader(
                new InputStreamReader(con.getInputStream()));
        String inputLine;
        StringBuffer content = new StringBuffer();
        while ((inputLine = in.readLine()) != null) {
            content.append(inputLine);
        }
        in.close();

        //print in string format
        System.out.println(content);

        //print in dict format
        JSONObject myresponse = new JSONObject(content.toString());
        System.out.println("print in dict format");
        for (String key: myresponse.keySet())
        
        
}
}