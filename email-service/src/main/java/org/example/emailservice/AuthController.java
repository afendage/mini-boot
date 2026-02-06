package org.example.emailservice;

import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.responses.ApiResponse;
import io.swagger.v3.oas.annotations.tags.Tag;
import jakarta.servlet.http.HttpServletRequest;
import lombok.RequiredArgsConstructor;
import org.example.emailservice.service.EmailVerifyCodeService;
import org.springframework.web.bind.annotation.*;

@Tag(name = "邮件服务", description = "邮件发送相关接口")
@RestController
@RequestMapping("/api/auth")
@RequiredArgsConstructor
public class AuthController {

    private final EmailVerifyCodeService emailVerifyCodeService;

    /**
     * 发送邮箱验证码
     */
    @Operation(summary = "发送邮件", description = "发送普通文本邮件")
    @ApiResponse(responseCode = "200", description = "发送成功")
    @ApiResponse(responseCode = "400", description = "请求参数错误")
    @GetMapping("/send-verify-code")
    public String sendVerifyCode(@RequestParam String email, HttpServletRequest request) {
        try {
            String ip = request.getRemoteAddr();// 获取客户端IP（hutool工具类）
            emailVerifyCodeService.sendEmailVerifyCode(email, ip);
            return "验证码已发送，请查收邮件";
        } catch (Exception e) {
            return "发送失败：" + e.getMessage();
        }
    }

    /**
     * 验证邮箱验证码（注册/登录场景调用）
     */
    @Operation(summary = "邮箱验证", description = "验证邮箱验证码")
    @ApiResponse(responseCode = "200", description = "验证成功")
    @ApiResponse(responseCode = "400", description = "请求参数错误")
    @ApiResponse(responseCode = "401", description = "验证码无效或已过期")
    @GetMapping("/validate-code")
    public String validateCode(@RequestParam String email, @RequestParam String code) {
        boolean isValid = emailVerifyCodeService.validateEmailVerifyCode(email, code);
        return isValid ? "验证码验证通过" : "验证码无效或已过期";
    }
}
