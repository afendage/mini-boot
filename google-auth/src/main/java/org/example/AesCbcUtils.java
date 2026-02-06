package org.example;

import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;
import javax.crypto.SecretKeyFactory;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.PBEKeySpec;
import javax.crypto.spec.SecretKeySpec;
import java.nio.charset.StandardCharsets;
import java.security.NoSuchAlgorithmException;
import java.security.SecureRandom;
import java.security.spec.KeySpec;
import java.util.Base64;

public class AesCbcUtils {

    public AesCbcUtils() throws Exception {
    }

    public static SecretKey generateKey256Static() throws Exception {
        // 固定密码和盐（实际应用中需安全存储）
        String password = "asdfghjkl!@#$%^&*&^%$#@$%^&*(*&^%$";
        byte[] salt = "12345@#$%^dfgh".getBytes(StandardCharsets.UTF_8);
        // 使用PBKDF2派生密钥
        SecretKeyFactory factory = SecretKeyFactory.getInstance("PBKDF2WithHmacSHA256");
        // 迭代次数65536，密钥长度256位
        KeySpec spec = new PBEKeySpec(password.toCharArray(), salt, 65536, 256);
        return new SecretKeySpec(factory.generateSecret(spec).getEncoded(), "AES");
    }

    // 生成 256 位密钥（在实际应用中应使用安全的密钥管理系统）
    public static SecretKey generateKey256() throws NoSuchAlgorithmException {
        KeyGenerator keyGen = KeyGenerator.getInstance("AES");
        // 256 位
        keyGen.init(256);
        return keyGen.generateKey();
    }

    // 生成随机 IV
    public static byte[] generateIv(int size) {
        byte[] iv = new byte[size];
        new SecureRandom().nextBytes(iv);
        return iv;
    }

    // 加密：CBC 模式，PKCS5Padding
    public static String encryptCBC(String plaintext, SecretKey key) throws Exception {
        byte[] ivBytes = generateIv(16); // 16 字节 IV
        IvParameterSpec ivSpec = new IvParameterSpec(ivBytes);

        Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
        cipher.init(Cipher.ENCRYPT_MODE, key, ivSpec);

        byte[] plaintextBytes = plaintext.getBytes(StandardCharsets.UTF_8);
        byte[] ciphertextBytes = cipher.doFinal(plaintextBytes);

        // 将 IV 与密文拼接后进行 Base64 编码，便于传输
        byte[] payload = new byte[ivBytes.length + ciphertextBytes.length];
        System.arraycopy(ivBytes, 0, payload, 0, ivBytes.length);
        System.arraycopy(ciphertextBytes, 0, payload, ivBytes.length, ciphertextBytes.length);

        return Base64.getEncoder().encodeToString(payload);
    }

    // 解密：CBC 模式，PKCS5Padding
    public static String decryptCBC(String payloadBase64, SecretKey key) throws Exception {
        byte[] payload = Base64.getDecoder().decode(payloadBase64);

        // 先提取 IV（前 16 字节），再剩余为密文
        byte[] ivBytes = new byte[16];
        byte[] ciphertext = new byte[payload.length - 16];
        System.arraycopy(payload, 0, ivBytes, 0, 16);
        System.arraycopy(payload, 16, ciphertext, 0, payload.length - 16);

        IvParameterSpec ivSpec = new IvParameterSpec(ivBytes);
        Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
        cipher.init(Cipher.DECRYPT_MODE, key, ivSpec);

        byte[] plaintextBytes = cipher.doFinal(ciphertext);
        return new String(plaintextBytes, StandardCharsets.UTF_8);
    }

    private final static SecretKey key;

    static {
        try {
            key = AesCbcUtils.generateKey256Static();
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    // 示例使用
    public static void main(String[] args) {
        try {
            // 1) 生成密钥（示例；实际场景请从安全的密钥管理系统获取）
//            SecretKey key = generateKey256Static();

            String originalText = "这是一个AES-CBC 加密解密的示例文本。";

            // 2) 加密
            String encrypted = encryptCBC(originalText, key);
            System.out.println("Encrypted (base64): " + encrypted);

            // 3) 解密
            String decrypted = decryptCBC(encrypted, key);
            System.out.println("Decrypted: " + decrypted);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }

}
