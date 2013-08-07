package com.surdoc.oauth.client;

import java.io.IOException;
import net.sf.json.JSONObject;

public class OAuthClient {

    private static String AUTHORIZE = null;//授权地址
    private static String TOKEN = null;
    private String clientId;
    private String clientSecret;
    private String redirectUri;

    static {
        AUTHORIZE = System.getProperty("com.surdoc.oauth.authorize", "https://open.surdoc.com/oauth/oauth/authorize");
        TOKEN = System.getProperty("com.surdoc.oauth.token", "https://open.surdoc.com/oauth/oauth/token");
    }

    /**
     * 通过应用的基本信息构建OAuth客户端类
     *
     * @param clientId 应用注册的id
     * @param clientSecret 应用注册的密钥
     */
    public OAuthClient(String clientId, String clientSecret) {
        this.clientId = clientId;
        this.clientSecret = clientSecret;
    }

    /**
     * 获得申请授权码Authorization_Code的URL
     *
     * @return 申请获取Authorization Code的URL地址
     */
    public String getAuthorizeUrl() {
        PostParameter[] httpParams = new PostParameter[3];
        httpParams[0] = new PostParameter("client_id", clientId);
        httpParams[1] = new PostParameter("response_type", "code");
        httpParams[2] = new PostParameter("redirect_uri", redirectUri);
        return AUTHORIZE + "?" + PostParameter.encodeParameters(httpParams);
    }

    /**
     * 获得申请授权码Implicit的URL
     *
     * @return 申请获取Implicit的URL地址
     */
    public String getImplicitUrl() {
        PostParameter[] httpParams = new PostParameter[3];
        httpParams[0] = new PostParameter("client_id", clientId);
        httpParams[1] = new PostParameter("response_type", "token");
        httpParams[2] = new PostParameter("redirect_uri", redirectUri);
        return AUTHORIZE + "?" + PostParameter.encodeParameters(httpParams);
    }

    /**
     * 使用Authorization_code来获取Access Token。
     *
     * @param code 授权码Authorization Code
     * @return AccessToken对象的封装。
     * @throws OAuthException异常类
     */
    public OAuthToken getAccessTokenByAuthorizationCode(String code) throws OAuthException {
        PostParameter[] httpParams = new PostParameter[5];
        httpParams[0] = new PostParameter("client_id", clientId);
        httpParams[1] = new PostParameter("client_secret", clientSecret);
        httpParams[2] = new PostParameter("grant_type", "authorization_code");
        httpParams[3] = new PostParameter("redirect_uri", redirectUri);
        httpParams[4] = new PostParameter("code", code);
        try {
            String res = HttpUtils.post(TOKEN, httpParams, null);
            JSONObject obj = JSONObject.fromObject(res);
            checkOAuthResponse(obj);
            return new OAuthToken(obj);
        } catch (IOException ex) {
            throw new OAuthException(ex.getMessage());
        } 
    }

    /**
     * 使用应用公钥、密钥获取Access Token(只能用于访问与用户无关的Open API)
     *
     * @return AccessToken对象的封装
     * @throws OAuthException异常类
     */
    public OAuthToken getAccessTokenByClientCredentials() throws OAuthException {
        PostParameter[] httpParams = new PostParameter[3];
        httpParams[0] = new PostParameter("client_id", clientId);
        httpParams[1] = new PostParameter("client_secret", clientSecret);
        httpParams[2] = new PostParameter("grant_type", "client_credentials");
        try {
            String res = HttpUtils.post(TOKEN, httpParams, null);
            JSONObject obj = JSONObject.fromObject(res);
            checkOAuthResponse(obj);
            return new OAuthToken(obj);
        } catch (IOException ex) {
            throw new OAuthException(ex.getMessage());
        } 
    }

    /**
     * 使用Refresh Token来获取Access Token
     *
     * @param refreshToken 用于涮新Access Token用的Refresh Token
     * @return AccessToken对象的封装信息。
     * @throws OAuthException异常类
     */
    public OAuthToken getAccessTokenByRefreshToken(String refreshToken) throws OAuthException {
        PostParameter[] httpParams = new PostParameter[4];
        httpParams[0] = new PostParameter("client_id", clientId);
        httpParams[1] = new PostParameter("client_secret", clientSecret);
        httpParams[2] = new PostParameter("grant_type", "refresh_token");
        httpParams[3] = new PostParameter("refresh_token", refreshToken);
        try {
            String res = HttpUtils.post(TOKEN, httpParams, null);
            JSONObject obj = JSONObject.fromObject(res);
            checkOAuthResponse(obj);
            return new OAuthToken(obj);
        } catch (IOException ex) {
            throw new OAuthException(ex.getMessage());
        } 
    }

    /**
     * 使用用户名和密码获得AccessToken对象
     *
     * @param username 用户名
     * @param password 密码
     * @return OAuthToken 对象，封装了token的具体信息
     * @throws OAuthException
     */
    public OAuthToken getAccessTokenByPasswordCredentials(String username, String password) throws OAuthException {
        PostParameter[] httpParams = new PostParameter[5];
        httpParams[0] = new PostParameter("client_id", clientId);
        httpParams[1] = new PostParameter("client_secret", clientSecret);
        httpParams[2] = new PostParameter("grant_type", "password");
        httpParams[3] = new PostParameter("username", username);
        httpParams[4] = new PostParameter("password", password);
        try {
            String res = HttpUtils.post(TOKEN, httpParams, null);
            JSONObject obj = JSONObject.fromObject(res);
            checkOAuthResponse(obj);
            return new OAuthToken(obj);
        } catch (IOException ex) {
            throw new OAuthException(ex.getMessage());
        }
    }

    /**
     * 判断授权回应
     *
     * @param json
     * @throws OAuthException
     */
    public static void checkOAuthResponse(JSONObject json) throws OAuthException {
        if (json.has("error")) {
            OAuthException oauthException = new OAuthException();
            oauthException.formJson(json);
            throw oauthException;
        }

    }

    public void setRedirectUri(String redirectUri) {
        this.redirectUri = redirectUri;
    }
}
