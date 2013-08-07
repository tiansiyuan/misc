package com.surdoc.oauth.client;

import java.net.Authenticator;
import java.net.InetSocketAddress;
import java.net.PasswordAuthentication;
import java.net.Proxy;

public class ProxyClient {

    private static String username = null;//账号
    private static String password = null;//密码
    private static String host = null;//主机
    private static int port = 1080;//端口
    private static int proxytype = -1;

    /**
     * 设置http代理
     *
     * @param ausername
     * @param apassword
     * @param ahost
     * @param aport
     */
    public static void setHttpProxy(String ausername, String apassword, String ahost, int aport) {
        init(ausername, apassword, ahost, aport);
        proxytype = 0;
    }

    /**
     * 设置socks代理
     *
     * @param ausername
     * @param apassword
     * @param ahost
     * @param aport
     */
    public static void setSocksProxy(String ausername, String apassword, String ahost, int aport) {
        init(ausername, apassword, ahost, aport);
        proxytype = 1;
    }

    /**
     * 初始化
     *
     * @param ausername
     * @param apassword
     * @param ahost
     * @param aport
     */
    private static void init(String ausername, String apassword, String ahost, int aport) {
        username = ausername;
        password = apassword;
        host = ahost;
        port = aport;
        Authenticator.setDefault(new Authenticator() {

            @Override
            protected PasswordAuthentication getPasswordAuthentication() {
                return new PasswordAuthentication(username, password.toCharArray());
            }
        });
    }

    /**
     * @return the proxy
     */
    public static Proxy getProxy() {
        if (proxytype == 0) {
            return new Proxy(Proxy.Type.HTTP, new InetSocketAddress(host, port));
        } else if (proxytype == 1) {
            return new Proxy(Proxy.Type.SOCKS, new InetSocketAddress(host, port));
        } else {
            return null;
        }
    }

    /**
     * @return the username
     */
    public static String getUsername() {
        return username;
    }

    /**
     * @return the password
     */
    public static String getPassword() {
        return password;
    }

    /**
     * @return the host
     */
    public static String getHost() {
        return host;
    }

    /**
     * @return the port
     */
    public static int getPort() {
        return port;
    }
}
