package com.surdoc.oauth.client;

import net.sf.json.JSONObject;

public final class OAuthToken {

    /**
     * 过期时间
     */
    private int expiresIn;
    /**
     * 刷新token的令牌
     */
    private String refreshToken;
    /**
     * accessToken信息
     */
    private String accessToken;
    /**
     * 资源服务
     */
    private String resourceServer;

    public OAuthToken() {
    }

    /**
     * 通过json数据创建AccessToken对象
     *
     * @param json json数据
     */
    public OAuthToken(JSONObject obj) {
        Object objExpire = obj.get("expires_in");
        Object objRefresh = obj.get("refresh_token");
        Object objAccess = obj.get("access_token");
        Object objResourceServer = obj.get("resource_server");
        if (objAccess != null) {
            this.setAccessToken(objAccess.toString());
        }
        if (objExpire != null) {
            this.setExpiresIn(Integer.valueOf(objExpire.toString()));
        }
        if (objRefresh != null) {
            this.setRefreshToken(objRefresh.toString());
        }
        if (objResourceServer != null) {
            this.setResourceServer(objResourceServer.toString());
        }
    }

    public int getExpiresIn() {
        return expiresIn;
    }

    public void setExpiresIn(int expiresIn) {
        this.expiresIn = expiresIn;
    }

    public String getRefreshToken() {
        return refreshToken;
    }

    public void setRefreshToken(String refreshToken) {
        this.refreshToken = refreshToken;
    }

    public String getAccessToken() {
        return accessToken;
    }

    public void setAccessToken(String accessToken) {
        this.accessToken = accessToken;
    }

    @SuppressWarnings("unchecked")
    public void putToJSONObject(JSONObject obj) {
        if (obj != null) {
            obj.put("expires_in", getExpiresIn());
            obj.put("refresh_token", getRefreshToken());
            obj.put("access_token", getAccessToken());
            obj.put("resource_server", getResourceServer());
        }
    }

    @Override
    public String toString() {
        JSONObject obj = new JSONObject();
        putToJSONObject(obj);
        return obj.toString();
    }

    /**
     * @return the resourceServer
     */
    public String getResourceServer() {
        return resourceServer;
    }

    /**
     * @param resourceServer the resourceServer to set
     */
    public void setResourceServer(String resourceServer) {
        this.resourceServer = resourceServer;
    }
}
