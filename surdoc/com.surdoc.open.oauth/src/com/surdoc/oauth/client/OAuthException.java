package com.surdoc.oauth.client;

import net.sf.json.JSONObject;

public class OAuthException extends Exception {

    private static final long serialVersionUID = -1603706048276355225L;
    private String error;
    private String errorDesp;

    public OAuthException() {
    }

    public OAuthException(String error) {
        this.error = error;
    }

    public OAuthException(String error, String errorDesp) {
        this.error = error;
        this.errorDesp = errorDesp;
    }

    public String getError() {
        return error;
    }

    public void setError(String error) {
        this.error = error;
    }

    public String getErrorDesp() {
        return errorDesp;
    }

    public void setErrorDesp(String errorDesp) {
        this.errorDesp = errorDesp;
    }

    @Override
    public String toString() {
        return "OAuthException [error=" + error + ", errorDesp=" + errorDesp + "]";
    }

    /**
     * 通过json信息构造 异常类对象
     *
     * @param json
     */
    public void formJson(JSONObject obj) {
        if (obj != null) {
            Object objError = obj.get("error");
            Object objErrorDesp = obj.get("error_description");
            if (objError != null) {
                String error1 = objError.toString();
                this.setError(error1);
            }
            if (objErrorDesp != null) {
                String errorDesp1 = objErrorDesp.toString();
                this.setErrorDesp(errorDesp1);
            }
        }
    }
}
