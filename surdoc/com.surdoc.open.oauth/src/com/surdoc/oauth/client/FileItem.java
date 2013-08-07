package com.surdoc.oauth.client;

import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;

public class FileItem {

    /**
     * 文件名
     */
    private String fileName;
    /**
     * 媒体类型
     */
    private String mimeType;
    /**
     * 文件字节流
     */
    private byte[] content;
    /**
     * File 文件
     */
    private File file;

    /**
     * 基于本地的File对象构造对象
     *
     * @param file file对象
     */
    public FileItem(File file) {
        this.file = file;
    }

    /**
     * 基于本地的文件路径地址构建对象
     *
     * @param filePath 文件路径地址
     */
    public FileItem(String filePath) {
        this(new File(filePath));
    }

    /**
     * 基于文件名称、字节流构建对象
     *
     * @param fileName 文件名称
     * @param content 文件字节流
     */
    public FileItem(String fileName, byte[] content) {
        this.fileName = fileName;
        this.content = content;
    }

    /**
     * 基于文件名、字节流和媒体类型的构造器。
     *
     * @param fileName 文件名
     * @param content 文件字节流
     * @param mimeType 媒体类型
     */
    public FileItem(String fileName, byte[] content, String mimeType) {
        this(fileName, content);
        this.mimeType = mimeType;
    }

    /**
     * 获取文件名称
     *
     * @return 文件名称
     */
    public String getFileName() {
        if (this.fileName == null && this.file != null && this.file.exists()) {
            this.fileName = this.file.getName();
        }
        return this.fileName;
    }

    /**
     * 获取文件的字节流信息
     *
     * @return 文件的字节流信息
     * @throws IOException
     */
    public byte[] getContent() throws IOException {
        if (this.content == null && this.file != null && this.file.exists()) {
            InputStream in = null;
            byte[] readBuffer = new byte[1024 * 1024];
            ByteArrayOutputStream out = null;
            try {
                in = new FileInputStream(file);
                out = new ByteArrayOutputStream();
                int ch;
                while ((ch = in.read(readBuffer)) > 0) {
                    out.write(readBuffer, 0, ch);
                }
                this.content = out.toByteArray();
            } finally {
                if (in != null) {
                    try {
                        in.close();
                    } catch (IOException e) {
                    }
                }
                if (out != null) {
                    try {
                        out.close();
                    } catch (IOException e) {
                    }
                }
            }
        }
        return this.content;
    }

    /**
     * 获取文件的媒体类型
     *
     * @return 文件的媒体类型
     * @throws IOException
     */
    public String getMimeType() throws IOException {
        if (this.mimeType == null && this.file != null && this.file.exists()) {
            this.mimeType = getMimeType(getContent());
        }
        return this.mimeType;
    }

    /**
     * 获取文件的真实媒体类型。目前只支持JPG, GIF, PNG, BMP四种图片文件。
     *
     * @param bytes 文件字节流
     * @return 媒体类型(MEME-TYPE)
     */
    public static String getMimeType(byte[] bytes) {
        String suffix = getFileSuffix(bytes);
        String mimeType;

        if ("JPG".equals(suffix)) {
            mimeType = "image/jpeg";
        } else if ("GIF".equals(suffix)) {
            mimeType = "image/gif";
        } else if ("PNG".equals(suffix)) {
            mimeType = "image/png";
        } else if ("BMP".equals(suffix)) {
            mimeType = "image/bmp";
        } else {
            mimeType = "application/octet-stream";
        }

        return mimeType;
    }

    /**
     * 获取文件的真实后缀名。目前只支持JPG, GIF, PNG, BMP四种图片文件。
     *
     * @param bytes 文件字节流
     * @return JPG, GIF, PNG or null
     */
    private static String getFileSuffix(byte[] bytes) {
        if (bytes == null || bytes.length < 10) {
            return null;
        }
        if (bytes[0] == 'G' && bytes[1] == 'I' && bytes[2] == 'F') {
            return "GIF";
        } else if (bytes[1] == 'P' && bytes[2] == 'N' && bytes[3] == 'G') {
            return "PNG";
        } else if (bytes[6] == 'J' && bytes[7] == 'F' && bytes[8] == 'I' && bytes[9] == 'F') {
            return "JPG";
        } else if (bytes[0] == 'B' && bytes[1] == 'M') {
            return "BMP";
        } else {
            return null;
        }
    }
}
