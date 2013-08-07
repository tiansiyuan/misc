package com.surdoc.oauth.client;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.net.URLEncoder;

public class PostParameter implements java.io.Serializable {

    private String name = null;//参数名
    private String value = null;//参数值
    private FileItem file = null;
    private boolean encode = false;//当提交multipart/form-data数据时
    private static final long serialVersionUID = -8708108746980739212L;

    public PostParameter(String name, String value, boolean encode) {
        this.encode = encode;
        this.name = name;
        this.value = value;
    }

    public PostParameter(String name, String value) {
        this.name = name;
        this.value = value;
    }

    public PostParameter(String name, double value) {
        this.name = name;
        this.value = String.valueOf(value);
    }

    public PostParameter(String name, int value) {
        this.name = name;
        this.value = String.valueOf(value);
    }

    public PostParameter(String name, FileItem file) {
        this.name = name;
        this.file = file;
    }

    /**
     * 参数名
     *
     * @return
     */
    public String getName() {
        return name;
    }

    /**
     * 参数值
     *
     * @return
     */
    public String getValue() {
        return value;
    }

    /**
     * 参数值,当提交multipart/form-data数据时，有时需要加码Signature.encode(value)
     *
     * @return
     */
    public String getPostValue() {
        if (encode) {
            return encode(value);
        } else {
            return value;
        }
    }

    /**
     * 文件
     *
     * @return
     */
    public FileItem getFile() {
        return file;
    }

    /**
     * 是否为上传文件
     *
     * @return
     */
    public boolean isFile() {
        return null != file;
    }

    /**
     * 参数是否包含文件
     *
     * @param params
     * @return
     */
    public static boolean containsFile(PostParameter[] params) {
        boolean containsFile = false;
        if (null == params) {
            return false;
        }
        for (PostParameter param : params) {
            if (param.isFile()) {
                containsFile = true;
                break;
            }
        }
        return containsFile;
    }

    @Override
    public String toString() {
        if (this.isFile()) {
            try {
                return "PostParameter{name='" + name + "', ContentType='" + file.getMimeType() + "'}";
            } catch (IOException ex) {
                return "PostParameter{name='" + name + "'}";
            }
        } else {
            return "PostParameter{name='" + name + "', value='" + value + "'}";
        }
    }

    /**
     * 对参数名参数值加码
     *
     * @param value
     * @return
     */
    public static String encode(String value) {
        String encoded = null;
        try {
            encoded = URLEncoder.encode(value, HttpUtils.DEFAULTCHAESET);
        } catch (UnsupportedEncodingException ignore) {
        }
        StringBuilder buf = new StringBuilder(encoded.length());
        char focus;
        for (int i = 0; i < encoded.length(); i++) {
            focus = encoded.charAt(i);
            if (focus == '*') {
                buf.append("%2A");
            } else if (focus == '+') {
                buf.append("%20");
            } else if (focus == '%' && (i + 1) < encoded.length() && encoded.charAt(i + 1) == '7' && encoded.charAt(i + 2) == 'E') {
                buf.append('~');
                i += 2;
            } else {
                buf.append(focus);
            }
        }
        return buf.toString();
    }

    /**
     * 将各个参数连接为字符串准备提交,不包含file
     *
     * @param httpParams
     * @return
     */
    public static String encodeParameters(PostParameter[] httpParams) {
        if (null == httpParams) {
            return "";
        }
        StringBuilder buf = new StringBuilder();
        for (int j = 0, count = httpParams.length; j < count; j++) {
            if (httpParams[j].isFile()) {
                continue;//throw new IllegalArgumentException("parameter [" + httpParams[j].name + "]should be text");
            }
            if (j != 0) {
                buf.append("&");
            }
            buf.append(encode(httpParams[j].name));
            buf.append("=");
            buf.append(encode(httpParams[j].value));
        }
        return buf.toString();
    }
    private static String boundary = "---------------------------37531613912423";

    public static String getMultiContentType() {
        return "multipart/form-data; boundary=" + boundary;
    }

    /**
     * 生成multipart/form-data格式数据
     *
     * @param httpParams
     * @return
     * @throws IOException
     */
    public static byte[] makeMultipart(PostParameter[] httpParams) throws IOException {
        ByteArrayOutputStream bo = null;
        for (PostParameter p : httpParams) {
            if (bo == null) {
                bo = new ByteArrayOutputStream();
            } else {
                bo.write("\r\n".getBytes());
            }
            if (p.isFile()) {
                String bound = "--" + boundary + "\r\nContent-Disposition: form-data; name=\"" + p.name + "\"; filename=\"image.jpg\"\r\nContent-Type: " + p.getFile().getMimeType() + "\r\n\r\n";
                bo.write(bound.getBytes());
                bo.write(p.getFile().getContent());
            } else {
                String bound = "--" + boundary + "\r\nContent-Disposition: form-data; name=\"" + p.getName() + "\"\r\n\r\n";
                bo.write(bound.getBytes());
                bo.write(p.getPostValue().getBytes(HttpUtils.DEFAULTCHAESET));
            }
        }
        bo.write(("\r\n--" + boundary + "--\r\n").getBytes());
        return bo.toByteArray();
    }
}
