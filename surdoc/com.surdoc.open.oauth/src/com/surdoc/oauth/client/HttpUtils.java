package com.surdoc.oauth.client;

import java.io.IOException;
import java.io.OutputStream;
import java.util.ArrayList;
import java.util.List;
import org.apache.commons.httpclient.DefaultHttpMethodRetryHandler;
import org.apache.commons.httpclient.Header;
import org.apache.commons.httpclient.HttpClient;
import org.apache.commons.httpclient.HttpMethod;
import org.apache.commons.httpclient.MultiThreadedHttpConnectionManager;
import org.apache.commons.httpclient.UsernamePasswordCredentials;
import org.apache.commons.httpclient.auth.AuthScope;
import org.apache.commons.httpclient.cookie.CookiePolicy;
import org.apache.commons.httpclient.methods.DeleteMethod;
import org.apache.commons.httpclient.methods.GetMethod;
import org.apache.commons.httpclient.methods.PostMethod;
import org.apache.commons.httpclient.methods.multipart.*;
import org.apache.commons.httpclient.params.HttpClientParams;
import org.apache.commons.httpclient.params.HttpMethodParams;
import org.apache.commons.httpclient.protocol.Protocol;

public class HttpUtils {

    private static final HttpClient client = new HttpClient();
    public final static String DEFAULTCHAESET = "UTF-8";

    /**
     * 初始化httpclient
     */
    static {
        int connectionTimeout = 30000;
        int soTimeout = 30000;
        try {
            connectionTimeout = Integer.parseInt(System.getProperty("sun.net.client.defaultConnectTimeout", "30000"));
        } catch (Exception e) {
        }
        try {
            soTimeout = Integer.parseInt(System.getProperty("sun.net.client.defaultReadTimeout", "30000"));
        } catch (Exception e) {
        }
        MultiThreadedHttpConnectionManager connectionManager = new MultiThreadedHttpConnectionManager();
        connectionManager.getParams().setDefaultMaxConnectionsPerHost(10);
        connectionManager.getParams().setMaxTotalConnections(300);
        connectionManager.getParams().setConnectionTimeout(connectionTimeout);
        connectionManager.getParams().setSoTimeout(soTimeout);
        client.setHttpConnectionManager(connectionManager);
        // 忽略cookie 避免 Cookie rejected 警告
        HttpClientParams clientParams = new HttpClientParams();
        clientParams.setCookiePolicy(CookiePolicy.IGNORE_COOKIES);
        client.setParams(clientParams);
        //支持https
        Protocol myhttps = new Protocol("https", new SSLSocketFactory(), 443);
        Protocol.registerProtocol("https", myhttps);
        //设置代理
        if (ProxyClient.getProxy() != null) {
            client.getHostConfiguration().setProxy(ProxyClient.getHost(), ProxyClient.getPort());
            client.getParams().setAuthenticationPreemptive(true);
            if (ProxyClient.getUsername() != null && !ProxyClient.getUsername().trim().equals("")) {
                client.getState().setProxyCredentials(
                        AuthScope.ANY,
                        new UsernamePasswordCredentials(ProxyClient.getUsername().trim(),
                        ProxyClient.getPassword().trim()));
            }
        }
    }

    /**
     * get
     *
     * @param url
     * @param params
     * @return
     * @throws ApiException
     */
    public static String get(String url, PostParameter[] params, String token) throws IOException {
        if (null != params && params.length > 0) {
            String encodedParams = PostParameter.encodeParameters(params);
            if (-1 == url.indexOf("?")) {
                url += "?" + encodedParams;
            } else {
                url += "&" + encodedParams;
            }
        }
        GetMethod getmethod = new GetMethod(url);
        return httpRequest(getmethod, token);
    }

    /**
     * 处理http deletemethod请求
     */
    public static String delete(String url, PostParameter[] params, String token) throws IOException {
        if (0 != params.length) {
            String encodedParams = PostParameter.encodeParameters(params);
            if (-1 == url.indexOf("?")) {
                url += "?" + encodedParams;
            } else {
                url += "&" + encodedParams;
            }
        }
        DeleteMethod deleteMethod = new DeleteMethod(url);
        return httpRequest(deleteMethod, token);

    }

    /**
     * post
     *
     * @param url
     * @param params
     * @param token
     * @return
     * @throws ApiException
     */
    public static String post(String url, PostParameter[] params, String token) throws IOException {
        PostMethod postMethod = new PostMethod(url);
        for (int i = 0; i < params.length; i++) {
            postMethod.addParameter(params[i].getName(), params[i].getValue());
        }
        HttpMethodParams param = postMethod.getParams();
        param.setContentCharset(DEFAULTCHAESET);
        return httpRequest(postMethod, token);
    }

    /**
     * 支持multipart方式上传
     *
     * @param url
     * @param params
     * @param token
     * @return
     * @throws ApiException
     */
    public static String multPartURL(String url, PostParameter[] params, String token) throws IOException {
        PostMethod postMethod = new PostMethod(url);
        if (params != null) {
            Part[] parts = new Part[params.length];
            int i = 0;
            for (PostParameter entry : params) {
                if (entry.isFile()) {
                    parts[i++] = new ByteArrayPart(entry.getFile().getContent(), entry.getName(), entry.getFile().getMimeType());
                } else {
                    parts[i++] = new StringPart(entry.getName(), entry.getValue(), DEFAULTCHAESET);
                }
            }
            postMethod.setRequestEntity(new MultipartRequestEntity(parts, postMethod.getParams()));
        }
        return httpRequest(postMethod, token);
    }

    /**
     * 提交
     *
     * @param method
     * @param token
     * @return
     * @throws ApiException
     */
    private static String httpRequest(HttpMethod method, String token) throws IOException {
        try {
            List<Header> headers = new ArrayList<Header>();
            if (token != null) {
                headers.add(new Header("Authorization", "Bearer " + token));
                client.getHostConfiguration().getParams().setParameter("http.default-headers", headers);
            }
            method.getParams().setParameter(HttpMethodParams.RETRY_HANDLER, new DefaultHttpMethodRetryHandler(3, false));
            client.executeMethod(method);
            return method.getResponseBodyAsString();
        } catch (IOException ioe) {
            throw ioe;
        } finally {
            method.releaseConnection();
        }
    }

    private static class ByteArrayPart extends PartBase {

        private byte[] mData;
        private String mName;

        public ByteArrayPart(byte[] data, String name, String type)
                throws IOException {
            super(name, type, DEFAULTCHAESET, "binary");
            mName = name;
            mData = data;
        }

        @Override
        protected void sendData(OutputStream out) throws IOException {
            out.write(mData);
        }

        @Override
        protected long lengthOfData() throws IOException {
            return mData.length;
        }

        @Override
        protected void sendDispositionHeader(OutputStream out)
                throws IOException {
            super.sendDispositionHeader(out);
            StringBuilder buf = new StringBuilder();
            buf.append("; filename=\"").append(mName).append("\"");
            out.write(buf.toString().getBytes());
        }
    }
}
