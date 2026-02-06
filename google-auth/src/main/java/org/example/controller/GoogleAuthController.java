package org.example.controller;

import com.google.zxing.BarcodeFormat;
import com.google.zxing.WriterException;
import com.google.zxing.client.j2se.MatrixToImageWriter;
import com.google.zxing.common.BitMatrix;
import com.google.zxing.qrcode.QRCodeWriter;
import org.example.service.GoogleAuthService;
import org.example.service.impl.GoogleAuthServiceImpl;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.util.Base64;

@RestController
public class GoogleAuthController {

    @Autowired
    private GoogleAuthService googleAuthService;

    @GetMapping("/generateKey")
    public Object getGenerateKey(){
        // 首次使用-需要扫描二维码
        // 首次生成二维码图片
        GoogleAuthServiceImpl.GoogleAuthResult result= googleAuthService.generateKey("test", "test");
        System.out.println(result.getSecretKey());
        return result;
    }

    /**
     * 用户验证接口
     * @param secretKey 秘钥
     * @param code 编码
     * @return
     */
    @GetMapping("/verifyCode")
    public Object verifyCode(String secretKey, int code){
        // 验证用户输入的验证码
        // secretKey 从数据库获取
        return googleAuthService.verifyCode(secretKey, code);
    }

    @GetMapping("/getQRImage")
    public ResponseEntity<String> getQRImage() throws WriterException, IOException {
        GoogleAuthServiceImpl.GoogleAuthResult result= googleAuthService.generateKey("test", "test");
        System.out.println(result.getSecretKey());
        return this.generateQRImage(result.getQrCodeUrl());
    }

    // 使用ZXing库生成二维码图片
    @GetMapping("/qrcode-image")
    public ResponseEntity<String> generateQRImage(String url) throws WriterException, IOException {
    // String url = "otpauth://totp/test:test?secret="+secret+"&issuer=test";
        BitMatrix matrix = new QRCodeWriter().encode(
                url, BarcodeFormat.QR_CODE, 200, 200);

        ByteArrayOutputStream os = new ByteArrayOutputStream();
        MatrixToImageWriter.writeToStream(matrix, "PNG", os);

        String base64 = "data:image/png;base64," +
                Base64.getEncoder().encodeToString(os.toByteArray());
        return ResponseEntity.ok(base64);
    }


}
