package org.example.emailservice;

import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;

import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;
import java.security.NoSuchAlgorithmException;
import java.util.Base64;

@SpringBootTest
class EmailServiceApplicationTests {

    @Test
    void contextLoads() throws NoSuchAlgorithmException {
        KeyGenerator keyGenerator = KeyGenerator.getInstance("HmacSHA256");
        keyGenerator.init(256);
        SecretKey secretKey = keyGenerator.generateKey();
        String key = Base64.getEncoder().encodeToString(secretKey.getEncoded());
        System.out.println(key);
    }

}
