package com.surdoc.oauth.examples;

import com.surdoc.oauth.client.OAuthClient;
import com.surdoc.oauth.client.OAuthToken;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * <p>Title: 向授权服务器获取令牌测试</p>
 *
 * <p>Description: 向授权服务器获取令牌测试</p>
 *
 * <p>Copyright: Sursen Copyright (c) 2011</p>
 *
 * <p>Company: Sursen </p>
 *
 * @author 刘社朋
 * @version 1.0
 */
public class OauthTest {

    public static void main(String[] args) throws IOException {
        //设置授权服务器地址
        //Authorize Endpoint
        //System.setProperty("com.surdoc.oauth.authorize", "https://cn.surdoc.com:10229/oauth/authorize");
        //Token Endpoint
        //System.setProperty("com.surdoc.oauth.token", "https://cn.surdoc.com:10229/oauth/token");
 
        OAuthClient oauthClient = new OAuthClient("51c3fe421999", "31e730213ee56950292c2fa2122c42bb");
        oauthClient.setRedirectUri("https://cn.surdoc.com:10229/oauth/authinfo");

        authorization_Code(oauthClient);
        //implicit(oauthClient);
        //client_Credentials(oauthClient);
        //password_Credentials(oauthClient);
        //refreshToken(oauthClient);    
    }

    /**
     * code授权测试
     */
    private static void authorization_Code(OAuthClient oauthClient) {
        String ss = oauthClient.getAuthorizeUrl();
        System.out.println(ss);
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        OAuthToken accessToken = null;
        while (null == accessToken) {
            System.out.print("Hit enter when it's done.[Enter]:");
            try {
                String pin = br.readLine();
                System.out.println("pin: " + pin);
                accessToken = oauthClient.getAccessTokenByAuthorizationCode(pin);
                System.out.println("Access token: " + accessToken.toString());
            } catch (Exception te) {
                te.printStackTrace();
            }
        }
    }

    /**
     * 隐式授权测试
     */
    private static void implicit(OAuthClient oauthClient) {
        String ss = oauthClient.getImplicitUrl();
        System.out.println(ss);
        //一般是移动设备调用webkit，并最终从地址栏截取到accessToken
    }

    /**
     * 应用凭证授权测试
     */
    private static void client_Credentials(OAuthClient oauthClient) {
        try {
            OAuthToken accessToken = oauthClient.getAccessTokenByClientCredentials();
            System.out.println("Access token: " + accessToken.toString());
        } catch (Exception te) {
            te.printStackTrace();
        }
    }

    /**
     * password授权测试
     */
    private static void password_Credentials(OAuthClient oauthClient) {
        try {
            OAuthToken accessToken = oauthClient.getAccessTokenByPasswordCredentials("baoguohao555@555.com", "Aa111111");
            System.out.println("Access token: " + accessToken.toString());
        } catch (Exception te) {
            te.printStackTrace();
        }
    }

    /**
     * RefreshToken测试
     */
    private static void refreshToken(OAuthClient oauthClient) {
        try {
            OAuthToken accessToken = oauthClient.getAccessTokenByRefreshToken("fee3ac99960625c594dedae24fe7f37f");
            System.out.println("Access token: " + accessToken.toString());
        } catch (Exception te) {
            te.printStackTrace();
        }
    }
}
