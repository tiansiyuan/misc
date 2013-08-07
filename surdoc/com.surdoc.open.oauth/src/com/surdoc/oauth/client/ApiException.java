package com.surdoc.oauth.client;

import net.sf.json.JSONObject;

public class ApiException extends Exception {

    private static final long serialVersionUID = -71058500666371407L;
    private String errorCode;
    private String errorMsg;

    public ApiException() {
    }

    public ApiException(String errorMsg) {
        this.errorCode = "";
        this.errorMsg = errorMsg;
    }

    public String getErrorCode() {
        return errorCode;
    }

    public void setErrorCode(String errorCode) {
        this.errorCode = errorCode;
    }

    public String getErrorMsg() {
        return errorMsg;
    }

    public void setErrorMsg(String errorMsg) {
        this.errorMsg = errorMsg;
    }

    @Override
    public String toString() {
        return "ApiException [errorCode=" + errorCode + ", errorMsg=" + errorMsg + "]";
    }

    /**
     * 通过json数据构建BaiduApiException类
     *
     * @param json
     */
    public void formJson(JSONObject obj) {
        Object objErrorCode = obj.get("error_code");
        Object objErrorMsg = obj.get("error_msg");
        if (objErrorCode != null) {
            this.setErrorCode(objErrorCode.toString());
        }
        if (objErrorMsg != null) {
            this.setErrorMsg(objErrorMsg.toString());
        }
    }
}
