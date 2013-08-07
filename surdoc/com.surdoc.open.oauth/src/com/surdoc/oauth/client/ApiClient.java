package com.surdoc.oauth.client;

import java.io.IOException;
import net.sf.json.JSONObject;

public class ApiClient {

    private String accessToken;
    private String baseUrl = null;

    /**
     * 创建openapi的调用实例，使用Https的方法访问api
     *
     * @param accessToken 基于https调用Open API时所需要的访问授权码
     */
    public ApiClient(String accessToken, String baseUrl) {
        this.accessToken = accessToken;
        this.baseUrl = baseUrl;
    }

    /**
     * 上传文件
     *
     * @param httpParams
     * @return
     */
    public String postMultPart(String uri, PostParameter[] httpParams) throws ApiException, OAuthException {
        try {
            String res = HttpUtils.multPartURL(baseUrl + uri, httpParams, accessToken);
            JSONObject obj = JSONObject.fromObject(res);
            OAuthClient.checkOAuthResponse(obj);
            checkApiResponse(obj);
            return obj.toString();
        } catch (IOException ex) {
            throw new ApiException(ex.getMessage());
        }
    }

    /**
     * get
     *
     * @return
     */
    public String get(String uri, PostParameter[] httpParams) throws ApiException, OAuthException {
        try {
            String res = HttpUtils.get(baseUrl + uri, httpParams, accessToken);
            JSONObject obj = JSONObject.fromObject(res);
            OAuthClient.checkOAuthResponse(obj);
            checkApiResponse(obj);
            return obj.toString();
        } catch (IOException ex) {
            throw new ApiException(ex.getMessage());
        }
    }

    /**
     * post
     *
     * @return
     */
    public String post(String uri, PostParameter[] httpParams) throws ApiException, OAuthException {
        try {
            String res = HttpUtils.post(baseUrl + uri, httpParams, accessToken);
            JSONObject obj = JSONObject.fromObject(res);
            OAuthClient.checkOAuthResponse(obj);
            checkApiResponse(obj);
            return obj.toString();
        } catch (IOException ex) {
            throw new ApiException(ex.getMessage());
        }
    }

    /**
     * delete
     *
     * @return
     */
    public String delete(String uri, PostParameter[] httpParams) throws ApiException, OAuthException {
        try {
            String res = HttpUtils.delete(baseUrl + uri, httpParams, accessToken);
            JSONObject obj = JSONObject.fromObject(res);
            OAuthClient.checkOAuthResponse(obj);
            checkApiResponse(obj);
            return obj.toString();
        } catch (IOException ex) {
            throw new ApiException(ex.getMessage());
        }
    }

    /**
     * 判断授权回应
     *
     * @param json
     * @throws OAuthException
     */
    public static void checkApiResponse(JSONObject json) throws ApiException {
        if (json.has("error_code")) {
            ApiException oauthException = new ApiException();
            oauthException.formJson(json);
            throw oauthException;
        }
    }
}
