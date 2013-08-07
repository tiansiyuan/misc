package com.surdoc.oauth.examples;

import com.surdoc.oauth.client.ApiClient;
import com.surdoc.oauth.client.ApiException;
import com.surdoc.oauth.client.FileItem;
import com.surdoc.oauth.client.OAuthException;
import com.surdoc.oauth.client.PostParameter;
import java.io.File;

/**
 * <p>Title: 访问资源服务测试</p>
 *
 * <p>Description: 访问资源服务测试</p>
 *
 * <p>Copyright: Sursen Copyright (c) 2011</p>
 *
 * <p>Company: Sursen </p>
 *
 * @author 刘社朋
 * @version 1.0
 */
public class ApiClientTest {

    static String baseUrl = "https://cn.surdoc.com:10229";

    public static void main(String[] args) throws ApiException, OAuthException {
        ApiClient api = new ApiClient("9901ec57e9e5f90e8db122c0cd4dcf98", baseUrl);
        PostParameter[] ps = new PostParameter[2];
        ps[0] = new PostParameter("fileid", "fileid value");
        ps[1] = new PostParameter("file", new FileItem(new File("d:\\aa.txt")));
        ///String ss = api.postMultPart("/api/demoapi", ps);
        String ss = api.get("/api/demoapi.do", ps);
         System.out.println(ss);
    }
}
